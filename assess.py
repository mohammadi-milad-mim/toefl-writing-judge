#!/usr/bin/env python3
"""Assess every run in one TOEFL question directory."""

from __future__ import annotations

import argparse
import asyncio
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from dotenv import load_dotenv
from openai import AsyncOpenAI
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)

from prompts import build_user_prompt, split_discussion_task


TaskType = Literal["write_an_email", "academic_discussion"]
QUESTION_FILENAMES = (
    "prompt.md",
    "prompt.txt",
    "question.md",
    "question.txt",
    "task.md",
    "task.txt",
)
ANSWER_FILENAMES = ("response.md", "response.txt", "answer.md", "answer.txt")
console = Console(stderr=True)


@dataclass(frozen=True)
class ModelConfig:
    name: str
    input_usd_per_million: float
    cached_input_usd_per_million: float
    output_usd_per_million: float


@dataclass(frozen=True)
class Settings:
    api_key: str
    base_url: str
    models: tuple[ModelConfig, ModelConfig, ModelConfig]
    max_output_tokens: int
    llm_timeout_seconds: float


@dataclass(frozen=True)
class AssessmentRun:
    name: str
    answer_path: Path


@dataclass(frozen=True)
class TokenUsage:
    input_tokens: int
    cached_input_tokens: int
    output_tokens: int
    reasoning_output_tokens: int
    total_tokens: int


@dataclass(frozen=True)
class AssessmentResult:
    markdown: str
    usage: TokenUsage


def load_settings() -> Settings:
    load_dotenv()
    required = ["OPENAI_API_KEY", "OPENAI_BASE_URL", "LLM_TIMEOUT_SECONDS"]
    for number in range(1, 4):
        required.extend(
            [
                f"MODEL_{number}",
                f"MODEL_{number}_INPUT_USD_PER_MILLION",
                f"MODEL_{number}_CACHED_INPUT_USD_PER_MILLION",
                f"MODEL_{number}_OUTPUT_USD_PER_MILLION",
            ]
        )
    missing = [name for name in required if not os.getenv(name, "").strip()]
    if missing:
        raise ValueError(f"Missing .env values: {', '.join(missing)}")

    try:
        models = tuple(
            ModelConfig(
                name=os.environ[f"MODEL_{number}"].strip(),
                input_usd_per_million=float(
                    os.environ[f"MODEL_{number}_INPUT_USD_PER_MILLION"]
                ),
                cached_input_usd_per_million=float(
                    os.environ[f"MODEL_{number}_CACHED_INPUT_USD_PER_MILLION"]
                ),
                output_usd_per_million=float(
                    os.environ[f"MODEL_{number}_OUTPUT_USD_PER_MILLION"]
                ),
            )
            for number in range(1, 4)
        )
    except ValueError as error:
        raise ValueError("All model cost values in .env must be numbers.") from error

    if len({model.name for model in models}) != 3:
        raise ValueError("MODEL_1, MODEL_2, and MODEL_3 must be different.")
    if any(
        rate < 0
        for model in models
        for rate in (
            model.input_usd_per_million,
            model.cached_input_usd_per_million,
            model.output_usd_per_million,
        )
    ):
        raise ValueError("Model cost values cannot be negative.")

    try:
        max_tokens = int(os.getenv("MAX_OUTPUT_TOKENS", "12000"))
    except ValueError as error:
        raise ValueError("MAX_OUTPUT_TOKENS must be an integer.") from error
    if max_tokens <= 0:
        raise ValueError("MAX_OUTPUT_TOKENS must be greater than zero.")

    try:
        llm_timeout_seconds = float(os.environ["LLM_TIMEOUT_SECONDS"])
    except ValueError as error:
        raise ValueError("LLM_TIMEOUT_SECONDS must be a number.") from error
    if llm_timeout_seconds <= 0:
        raise ValueError("LLM_TIMEOUT_SECONDS must be greater than zero.")

    return Settings(
        api_key=os.environ["OPENAI_API_KEY"].strip(),
        base_url=os.environ["OPENAI_BASE_URL"].strip(),
        models=models,  # type: ignore[arg-type]
        max_output_tokens=max_tokens,
        llm_timeout_seconds=llm_timeout_seconds,
    )


def model_alias(model: ModelConfig) -> str:
    name = model.name.lower()
    if "claude" in name:
        return "claude"
    if "gemini" in name:
        return "gemini"
    if "gpt" in name:
        return "gpt"
    return name


def select_models(
    models: tuple[ModelConfig, ...], requested: list[str] | None
) -> tuple[ModelConfig, ...]:
    if not requested:
        return models

    names = {
        item.strip().lower()
        for value in requested
        for item in value.split(",")
        if item.strip()
    }
    selected = tuple(
        model
        for model in models
        if model.name.lower() in names or model_alias(model) in names
    )
    matched_names = {
        name
        for name in names
        if any(name in {model.name.lower(), model_alias(model)} for model in models)
    }
    unknown = sorted(names - matched_names)
    if unknown:
        available = ", ".join(
            f"{model_alias(model)} ({model.name})" for model in models
        )
        raise ValueError(
            f"Unknown model selection: {', '.join(unknown)}. Available: {available}"
        )
    if not selected:
        raise ValueError("Select at least one model.")
    return selected


def infer_task_type(question_dir: Path, explicit: str | None) -> TaskType:
    if explicit:
        return "write_an_email" if explicit == "email" else "academic_discussion"

    parts = {part.lower().replace("-", "_") for part in question_dir.parts}
    if parts & {"write_an_email", "write_email", "email"}:
        return "write_an_email"
    if parts & {
        "academic_discussion",
        "discussion",
        "write_for_an_academic_discussion",
    }:
        return "academic_discussion"
    raise ValueError(
        "Could not infer the task type from the path. Put the question under "
        "write_an_email or academic_discussion, or pass --task."
    )


def find_named_file(directory: Path, names: tuple[str, ...], kind: str) -> Path:
    for name in names:
        candidate = directory / name
        if candidate.is_file():
            return candidate
    raise ValueError(
        f"No {kind} file found in {directory}. Expected one of: {', '.join(names)}"
    )


def discover_runs(question_dir: Path) -> list[AssessmentRun]:
    runs: list[AssessmentRun] = []
    for run_dir in sorted(path for path in question_dir.iterdir() if path.is_dir()):
        try:
            answer_path = find_named_file(
                run_dir, ANSWER_FILENAMES, "candidate response"
            )
        except ValueError:
            continue
        runs.append(AssessmentRun(run_dir.name, answer_path))

    if not runs:
        raise ValueError(
            f"No run folders containing an answer file were found in {question_dir}"
        )
    return runs


def model_filename(model: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "__", model).strip("._-")
    return f"{slug or 'model'}.md"


def usage_and_cost_markdown(model: ModelConfig, usage: TokenUsage) -> list[str]:
    uncached_input_tokens = max(usage.input_tokens - usage.cached_input_tokens, 0)
    input_cost = uncached_input_tokens * model.input_usd_per_million / 1_000_000
    cached_input_cost = (
        usage.cached_input_tokens * model.cached_input_usd_per_million / 1_000_000
    )
    output_cost = usage.output_tokens * model.output_usd_per_million / 1_000_000
    total_cost = input_cost + cached_input_cost + output_cost

    return [
        "---",
        "",
        "## Token Usage and Estimated Cost",
        "",
        f"- **Input tokens:** {usage.input_tokens:,}",
        f"- **Cached input tokens:** {usage.cached_input_tokens:,}",
        f"- **Uncached input tokens:** {uncached_input_tokens:,}",
        f"- **Output tokens:** {usage.output_tokens:,}",
        f"- **Reasoning output tokens:** {usage.reasoning_output_tokens:,}",
        f"- **Total tokens:** {usage.total_tokens:,}",
        "",
        "### Pricing Used (USD per 1M Tokens)",
        "",
        f"- **Uncached input:** ${model.input_usd_per_million:,.4f}",
        f"- **Cached input:** ${model.cached_input_usd_per_million:,.4f}",
        f"- **Output:** ${model.output_usd_per_million:,.4f}",
        "",
        "### Estimated Request Cost",
        "",
        f"- **Uncached input cost:** ${input_cost:.8f}",
        f"- **Cached input cost:** ${cached_input_cost:.8f}",
        f"- **Output cost:** ${output_cost:.8f}",
        f"- **Total estimated cost:** **${total_cost:.8f}**",
        "",
        "> Reasoning tokens are included in output tokens and are not charged twice. "
        "This estimate uses the rates configured in `.env`; your API gateway's "
        "actual charge may differ.",
        "",
    ]


def assessment_markdown(
    result: AssessmentResult,
    model: ModelConfig,
    question_path: Path,
    response_path: Path,
) -> str:
    metadata = [
        "# TOEFL Writing Assessment",
        "",
        f"- **Model:** `{model.name}`",
        f"- **Question:** `{question_path}`",
        f"- **Candidate response:** `{response_path}`",
        "",
    ]
    body = result.markdown.strip().splitlines()
    usage = usage_and_cost_markdown(model, result.usage)
    return "\n".join([*metadata, *body, "", *usage]).rstrip() + "\n"


def completion_token_usage(completion: Any) -> TokenUsage:
    if completion.usage is None:
        raise RuntimeError("The API returned an assessment without token usage data.")

    prompt_details = completion.usage.prompt_tokens_details
    completion_details = completion.usage.completion_tokens_details
    return TokenUsage(
        input_tokens=completion.usage.prompt_tokens,
        cached_input_tokens=(
            (prompt_details.cached_tokens or 0) if prompt_details is not None else 0
        ),
        output_tokens=completion.usage.completion_tokens,
        reasoning_output_tokens=(
            (completion_details.reasoning_tokens or 0)
            if completion_details is not None
            else 0
        ),
        total_tokens=completion.usage.total_tokens,
    )


async def request_assessment(
    client: AsyncOpenAI,
    model: str,
    task_type: TaskType,
    task_prompt: str,
    candidate_response: str,
    max_output_tokens: int,
    timeout_seconds: float,
) -> AssessmentResult:
    evaluator_prompt = build_user_prompt(task_type, task_prompt, candidate_response)
    completion = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": evaluator_prompt}],
        max_completion_tokens=max_output_tokens,
        timeout=timeout_seconds,
    )
    message = completion.choices[0].message
    if message.refusal:
        raise RuntimeError(f"Model refusal: {message.refusal}")
    markdown = (message.content or "").strip()
    if not markdown:
        raise RuntimeError(f"{model} returned an empty assessment.")
    return AssessmentResult(markdown=markdown, usage=completion_token_usage(completion))


async def run(
    question_dir: Path,
    explicit_task: str | None,
    requested_models: list[str] | None = None,
) -> int:
    settings = load_settings()
    selected_models = select_models(settings.models, requested_models)
    question_dir = question_dir.expanduser().resolve()
    if not question_dir.is_dir():
        raise ValueError(f"Question directory does not exist: {question_dir}")

    task_type = infer_task_type(question_dir, explicit_task)
    question_path = find_named_file(question_dir, QUESTION_FILENAMES, "question prompt")
    runs = discover_runs(question_dir)
    task_prompt = question_path.read_text(encoding="utf-8")
    if not task_prompt.strip():
        raise ValueError(f"Question prompt is empty: {question_path}")
    if task_type == "academic_discussion":
        split_discussion_task(task_prompt)

    filenames = [model_filename(model.name) for model in selected_models]
    if len(set(filenames)) != len(selected_models):
        raise ValueError(
            "Model names produce duplicate output filenames; rename the models in .env."
        )

    client = AsyncOpenAI(api_key=settings.api_key, base_url=settings.base_url)
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    )
    with progress:
        progress_task = progress.add_task(
            "Assessing responses", total=len(runs) * len(selected_models)
        )

        async def assess_and_write(
            assessment_run: AssessmentRun, model: ModelConfig
        ) -> bool:
            candidate_response = assessment_run.answer_path.read_text(encoding="utf-8")
            destination = assessment_run.answer_path.parent / model_filename(model.name)
            try:
                async with asyncio.timeout(settings.llm_timeout_seconds):
                    result = await request_assessment(
                        client,
                        model.name,
                        task_type,
                        task_prompt,
                        candidate_response,
                        settings.max_output_tokens,
                        settings.llm_timeout_seconds,
                    )
                destination.write_text(
                    assessment_markdown(
                        result, model, question_path, assessment_run.answer_path
                    ),
                    encoding="utf-8",
                )
                progress.console.print(
                    f"[green]Wrote[/green] {destination.relative_to(question_dir)}"
                )
                return True
            except Exception as error:  # Keep every other request running.
                destination.write_text(
                    f"# Assessment Error\n\n- **Model:** `{model.name}`\n"
                    f"- **Error:** {type(error).__name__}: {error}\n\n"
                    "---\n\n## Token Usage and Estimated Cost\n\n"
                    "Token usage and cost are unavailable because the request failed.\n",
                    encoding="utf-8",
                )
                progress.console.print(
                    f"[red]Failed[/red] {destination.relative_to(question_dir)}: "
                    f"{type(error).__name__}"
                )
                return False
            finally:
                progress.advance(progress_task)

        request_tasks = [
            asyncio.create_task(assess_and_write(assessment_run, model))
            for assessment_run in runs
            for model in selected_models
        ]
        successful = await asyncio.gather(*request_tasks)

    failures = successful.count(False)

    await client.close()
    console.print(
        f"Wrote assessments into the run folders under [bold]{question_dir}[/bold]"
    )
    if failures:
        console.print(
            f"[red]{failures} model request(s) failed; see the generated error files.[/red]"
        )
        return 1
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assess all runs for one TOEFL writing question."
    )
    parser.add_argument(
        "question_dir", type=Path, help="Path to one question directory"
    )
    parser.add_argument(
        "--task",
        choices=("email", "discussion"),
        help="Optional override; normally inferred from the directory path",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        metavar="MODEL",
        help=(
            "Models to run: gpt, claude, gemini, or exact model IDs. "
            "Accepts spaces or commas; omitted means all models."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        raise SystemExit(asyncio.run(run(args.question_dir, args.task, args.models)))
    except (ValueError, OSError) as error:
        console.print(f"[red]Error:[/red] {error}")
        raise SystemExit(2) from error


if __name__ == "__main__":
    main()
