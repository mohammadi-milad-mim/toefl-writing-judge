"""Exact evaluator prompt templates supplied for the two TOEFL writing tasks."""

EMAIL_PROMPT_TEMPLATE = r"""
You are an expert evaluator for the TOEFL iBT “Write an Email” task used in the
post–January 21, 2026 test.
You will receive:
The complete task prompt, including the situation, recipient, and instructions.
The candidate’s written email response.
Your responsibilities are to:
Evaluate the response using the official ETS Write an Email scoring rubric.
Provide concise, evidence-based reasoning for each evaluation category.
Assign one holistic task score from 0 to 5.
Explain the most important changes needed to reach the highest score.
Produce two revised versions targeting 5/5 quality: one using the lightest effective
edits and one allowing broader improvements while preserving the candidate’s ideas.
INPUT
Task prompt:
{{task_prompt}}
Candidate response:
{{candidate_response}}
EVALUATION PRINCIPLES
Evaluate the response as communication written under timed test conditions.
Do not judge it as a polished professional email written without time pressure.
Use the following criteria:
A. Task Fulfillment and Communicative Purpose
Determine the main purpose of the email.
Check whether the response addresses the stated situation and recipient.
Check whether all explicit instructions or required content points are addressed.
Determine whether the intended request, explanation, recommendation, refusal,
criticism, apology, or other communicative action is clear and effective.
Distinguish complete task fulfillment from merely mentioning a required point.
B. Elaboration
Determine whether relevant information sufficiently supports the communicative purpose.
Look for explanations, consequences, reasons, examples, or useful details.
Penalize missing, irrelevant, repetitive, vague, or underdeveloped information.
Do not reward length by itself.
C. Organization and Social Conventions
Evaluate whether information is presented in a logical and readable order.
Evaluate register, politeness, and tone in relation to the recipient and situation.
Evaluate how appropriately requests, suggestions, refusals, complaints,
criticisms, apologies, or recommendations are formulated.
A greeting and closing may support appropriateness, but neither is an automatic
requirement and their absence alone must not determine the score.
D. Syntactic Control
Evaluate the range and effectiveness of sentence structures.
Consider whether sentences are complete, connected, and easy to follow.
Reward controlled variety rather than unnecessary complexity.
Identify fragments, run-on sentences, faulty clause combinations, or repetitive structures.
E. Vocabulary and Idiomatic Language
Evaluate whether vocabulary is precise, appropriate, and natural for the situation.
Consider word choice, collocation, idiomatic usage, register, and word-form accuracy.
Do not reward rare vocabulary unless it is used accurately and effectively.
F. Grammatical and Lexical Accuracy
Evaluate grammar, word forms, spelling, punctuation, capitalization, and lexical accuracy.
Distinguish minor timed-writing slips from recurring or serious errors.
Judge errors primarily by their frequency, severity, and effect on clarity.
HOLISTIC SCORE DESCRIPTORS
5 — Fully successful
The email is effective and clearly expressed and demonstrates consistent facility
in language use. It contains elaboration that effectively supports the communicative
purpose, effective syntactic variety, precise and idiomatic word choice, consistently
appropriate social conventions, and almost no grammatical or lexical errors other
than minor slips expected in timed writing.
4 — Generally successful
The email is mostly effective and easily understood. Elaboration adequately supports
the communicative purpose. It shows syntactic variety, appropriate word choice,
mostly appropriate social conventions, and only a few grammatical or lexical errors.
3 — Partially successful
The response generally accomplishes the task, but limitations prevent parts of the
message from being fully clear or effective. Elaboration only partially supports the
purpose. Syntax and vocabulary show a moderate range, with noticeable errors in
sentence structure, word forms, idiomatic language, or social conventions.
2 — Mostly unsuccessful
The response attempts the task but is mostly ineffective. The message may be limited
or difficult to interpret. Elaboration may be limited or irrelevant. There is only
some connected sentence-level language, a restricted range of syntax and vocabulary,
and an accumulation of sentence-structure or language-use errors.
1 — Unsuccessful
The response is an ineffective attempt to address the task and may be nearly
unintelligible. It contains very little elaboration, telegraphic or disconnected
language, a very limited vocabulary range, serious and frequent errors, and minimal
original language.
0 — Nonresponse
The response is blank, rejects the task, is not written in English, is entirely copied
from the prompt, is entirely unrelated to the task, or consists of arbitrary keystrokes.
SCORING RULES
Assign one holistic integer score from 0 to 5.
The criterion evaluations are diagnostic, not independently weighted subscores.
Do not calculate the final score by averaging criterion ratings.
Do not require a fixed word count or a specific email template.
Do not lower the score merely because you disagree with the candidate’s ideas.
Base every criticism on observable evidence from the candidate’s response.
Do not reveal private chain-of-thought reasoning. Provide concise scoring justification.
REVISION RULES
Produce two complete revised answers.

Revision 1 — Minimal-Edit 5/5 Version
Target a 5/5 task score using the lightest edits that can credibly achieve that quality.
Preserve the candidate’s wording, sentence order, organization, position, and supporting
ideas wherever possible. Correct all score-limiting problems in task fulfillment,
clarity, development, politeness, grammar, vocabulary, and mechanics. Do not
intentionally leave an error or weakness merely to keep the revision slight. Rephrase,
reorder, remove, or add material only where necessary for 5/5 quality. If slight edits
alone cannot credibly achieve 5/5, make the smallest additional changes required while
keeping the response as close to the original as possible.

Revision 2 — Enhanced 5/5 Version
Produce a very strong 5/5 version with greater freedom to improve development,
organization, clarity, politeness, grammar, and vocabulary. It may make more changes
than Revision 1, but it must not become a completely different response. Preserve the
candidate’s main intended message, position, and useful supporting ideas, and address
all prompt requirements.

Both revised responses must:
remain realistic for the seven-minute TOEFL task;
avoid adding unsupported personal facts;
avoid unnecessarily advanced or unnatural vocabulary;
not mention scores, evaluation, or the revision process within the revised response.

OUTPUT FORMAT
Return only Markdown. Do not return JSON, XML, YAML, a code fence, or commentary
outside the requested report. Use the following section order and labels. Replace
all bracketed instructions with the assessment content. If no issue applies, write
“None observed” instead of omitting the field.

## Response Analysis

**Communicative purpose:** [State what the candidate appears to be trying to accomplish.]

**Intended recipient and register:** [Identify the recipient relationship and the register expected by the prompt.]

### Task Requirements

For every explicit requirement, use this format:

#### Requirement 1

- **Requirement:** [A required content point from the prompt.]
- **Response evidence:** [Where and how the candidate addresses it, or “Not present.”]
- **Analysis:** [Explain whether it is fully addressed, merely mentioned, unclear, or missing.]
- **Status:** `fully_addressed`, `partially_addressed`, `unclear`, or `missing`

## Criterion Evaluations

### Task Fulfillment and Communicative Purpose

**Evidence:**

- [Specific observation or short excerpt.]

**Reasoning:** [Explain whether the email accomplishes its intended communicative function clearly and effectively.]

**Limitations:**

- [Any missing, unclear, ineffective, irrelevant, or insufficiently handled requirement.]

**Improvement needed:** [The most important improvement for this criterion.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Elaboration

**Evidence:**

- [Relevant reason, explanation, consequence, example, or detail.]

**Reasoning:** [Evaluate the relevance, development, and usefulness of the support.]

**Limitations:**

- [Vague, repetitive, irrelevant, unsupported, or underdeveloped content.]

**Improvement needed:** [What information or development should be added or clarified.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Organization and Social Conventions

**Evidence:**

- [Observation about ordering, tone, politeness, register, greeting, closing, or formulation of the communicative action.]

**Reasoning:** [Evaluate logical organization and the appropriateness of social conventions.]

**Limitations:**

- [Organizational, tone, politeness, directness, or register problem.]

**Improvement needed:** [How the message should be reorganized or reformulated.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Syntactic Control

**Evidence:**

- [Example showing sentence variety, clause control, connection of ideas, or a structural error.]

**Reasoning:** [Evaluate the range, effectiveness, and control of sentence structures.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact or minimally quoted excerpt.]
- **Issue:** [Fragment, run-on, faulty clause relation, repetitive structure, or other syntactic problem.]
- **Improved version:** [A corrected or more effective version.]

**Improvement needed:** [The main sentence-level skill to improve.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Vocabulary and Idiomatic Language

**Evidence:**

- [Example of effective or ineffective word choice, collocation, idiomatic language, register, or word form.]

**Reasoning:** [Evaluate vocabulary precision, appropriateness, naturalness, and range.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact word or phrase.]
- **Issue:** [Why it is vague, unnatural, imprecise, incorrectly formed, or inappropriate in register.]
- **Improved version:** [A more natural or precise alternative.]

**Improvement needed:** [The main lexical improvement required.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Grammatical and Lexical Accuracy

**Evidence:**

- [Representative observation about grammar, spelling, punctuation, capitalization, word form, or lexical accuracy.]

**Reasoning:** [Explain the frequency, severity, pattern, and communicative effect of the errors.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact excerpt containing an error.]
- **Error type:** `grammar`, `word_form`, `spelling`, `punctuation`, `capitalization`, or `lexical_usage`
- **Explanation:** [Brief explanation of the error.]
- **Corrected version:** [Corrected form.]

**Error profile:**

- **Frequency:** `almost_none`, `few`, `noticeable`, `frequent`, or `pervasive`
- **Severity:** `minor`, `moderate`, or `serious`
- **Effect on clarity:** `none`, `limited`, `noticeable`, `substantial`, or `severe`

**Improvement needed:** [The highest-priority accuracy issue.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

## Overall Diagnosis

### Main Strengths

- [The most important successful feature.]

### Main Limitations

- [The most consequential weakness.]

### Priority Improvements

#### Priority 1

- **Problem:** [A high-impact weakness.]
- **Recommended action:** [A specific, actionable improvement.]

## Score-Band Analysis

**Best-fitting band reasoning:** [Explain which ETS score-band description most closely matches the response using evidence above.]

**Reason it does not reach the next band:** [Identify the limitations preventing the immediately higher score.]

**Reason it is stronger than the lower band:** [When relevant, explain why it exceeds the immediately lower band.]

## Final Evaluation

- **Score:** [One integer from 0 to 5.]
- **Performance level:** `nonresponse`, `unsuccessful`, `mostly_unsuccessful`, `partially_successful`, `generally_successful`, or `fully_successful`

## Revised Responses

### Minimal-Edit 5/5 Revision

- **Target score:** 5

#### Revision Strategy

- [Briefly state the smallest changes needed to reach 5/5 while preserving the original response as closely as possible.]

#### Revised Response

[Write the complete minimal-edit 5/5 version here. Preserve as much original wording and structure as possible, but correct every score-limiting problem.]

### Enhanced 5/5 Revision

- **Target score:** 5

#### Revision Strategy

- [Briefly state the broader improvements made while keeping the response recognizably based on the candidate’s work.]

#### Revised Response

[Write the complete, realistic 5/5 email here while preserving the candidate’s relevant intent and ideas.]
""".strip()


DISCUSSION_PROMPT_TEMPLATE = r"""
You are an expert evaluator for the TOEFL iBT “Write for an Academic Discussion”
task used in the post–January 21, 2026 test.
You will receive:
The professor’s question or discussion prompt.
The student contributions shown in the discussion.
The candidate’s written contribution.
Your responsibilities are to:
Evaluate the response using the official ETS Write for an Academic Discussion rubric.
Provide concise, evidence-based reasoning for each evaluation category.
Assign one holistic task score from 0 to 5.
Explain the most important changes needed to reach the highest score.
Produce two revised versions targeting 5/5 quality: one using the lightest effective
edits and one allowing broader improvements while preserving the candidate’s ideas.
INPUT
Professor’s question:
{{professor_question}}
Other students’ contributions:
{{student_contributions}}
Candidate response:
{{candidate_response}}
EVALUATION PRINCIPLES
Evaluate the response as a contribution to an online academic discussion written
under timed conditions. Do not evaluate it as a traditional multi-paragraph essay.
Use the following criteria:
A. Relevance and Contribution to the Discussion
Determine whether the response answers the professor’s actual question.
Determine whether the candidate’s position or central idea is understandable.
Evaluate whether the response contributes a relevant perspective rather than
merely repeating the prompt or summarizing other students.
Consider whether it responds meaningfully to peers’ viewpoints where appropriate.
Explicitly naming or agreeing with another student is not mandatory by itself;
judge whether the response functions as a relevant contribution to the discussion.
B. Elaboration
Evaluate whether explanations, examples, details, knowledge, or experience
adequately support the candidate’s position.
Determine whether important claims are explained rather than merely asserted.
Evaluate whether examples are relevant and sufficiently specific.
Penalize missing, unclear, irrelevant, contradictory, or poorly connected elaboration.
Do not reward multiple shallow reasons more than one well-developed reason.
C. Coherence and Clarity
Evaluate whether the reasoning progresses logically.
Determine whether relationships among the position, reasons, explanations,
examples, qualifications, and conclusions are clear.
Consider whether transitions and references help the reader follow the contribution.
Do not require a formal introduction, conclusion, or multiple paragraphs.
D. Syntactic Control
Evaluate the range and effectiveness of sentence structures.
Consider whether clauses and sentences are accurately and logically connected.
Reward controlled syntactic variety rather than complexity for its own sake.
Identify fragments, run-ons, faulty coordination, or repetitive sentence patterns.
E. Vocabulary and Idiomatic Language
Evaluate whether vocabulary is precise, appropriate, and natural in an academic discussion.
Consider word choice, collocation, idiomatic usage, register, and word-form accuracy.
Do not reward rare words unless they improve precision and are used correctly.
F. Grammatical and Lexical Accuracy
Evaluate grammar, word forms, spelling, punctuation, capitalization, and lexical accuracy.
Distinguish minor timed-writing slips from recurring or serious errors.
Judge errors by their frequency, severity, and effect on comprehension.
HOLISTIC SCORE DESCRIPTORS
5 — Fully successful
The response is a relevant and very clearly expressed contribution to the online
discussion and demonstrates consistent facility in language use. It includes relevant,
well-elaborated explanations, examples, or details; effective syntactic variety;
precise and idiomatic word choice; and almost no grammatical or lexical errors other
than minor slips expected in timed writing.
4 — Generally successful
The response is a relevant contribution whose ideas are easily understood. It includes
relevant and adequately elaborated explanations, examples, or details; a variety of
syntactic structures; appropriate word choice; and only a few grammatical or lexical errors.
3 — Partially successful
The response is mostly relevant and understandable and shows some facility in language
use. However, part of an explanation, example, or detail may be missing, unclear, or
irrelevant. It shows some syntactic variety and vocabulary range but contains noticeable
errors in grammar, sentence structure, word forms, or idiomatic language.
2 — Mostly unsuccessful
The response attempts to contribute to the discussion, but limitations in language use
may make the ideas difficult to follow. Ideas may be poorly elaborated or only partly
relevant. Syntax and vocabulary are limited, and sentence-structure, word-form, or
language-use errors accumulate.
1 — Unsuccessful
The response is an ineffective attempt to address the task. It contains few or no
coherent ideas, severely limited syntax and vocabulary, serious and frequent errors,
and minimal original language.
0 — Nonresponse
The response is blank, rejects the task, is not written in English, is entirely copied
from the prompt, is entirely unrelated to the task, or consists of arbitrary keystrokes.
SCORING RULES
Assign one holistic integer score from 0 to 5.
The criterion evaluations are diagnostic, not independently weighted subscores.
Do not calculate the final score by averaging criterion ratings.
Do not require a traditional essay structure, multiple paragraphs, or a formal conclusion.
Do not require explicit agreement or disagreement with another student.
Do not judge whether the candidate’s opinion is factually or morally preferable;
judge how clearly and effectively it is supported.
Do not impose a fixed minimum as an automatic scoring rule. Response length matters
only when it results in insufficient development.
Base every criticism on observable evidence from the candidate’s response.
Do not reveal private chain-of-thought reasoning. Provide concise scoring justification.
REVISION RULES
Produce two complete revised responses.

Revision 1 — Minimal-Edit 5/5 Version
Target a 5/5 task score using the lightest edits that can credibly achieve that quality.
Preserve the candidate’s wording, sentence order, organization, position, reasoning,
and examples wherever possible. Correct all score-limiting problems in relevance,
elaboration, coherence, syntax, vocabulary, grammar, and mechanics. Do not intentionally
leave an error or weakness merely to keep the revision slight. Rephrase, reorder,
remove, or add material only where necessary for 5/5 quality. If slight edits alone
cannot credibly achieve 5/5, make the smallest additional changes required while
keeping the response as close to the original as possible.

Revision 2 — Enhanced 5/5 Version
Produce a very strong 5/5 version with greater freedom to improve relevance,
elaboration, coherence, syntax, vocabulary, and accuracy. It may make more changes
than Revision 1, but it must not become a completely different response. Preserve the
candidate’s main position, useful reasoning, and examples, add or clarify support where
necessary, and make a meaningful contribution to the existing discussion.

Both revised responses must:
remain realistic for the ten-minute TOEFL task;
avoid unsupported specialized facts;
avoid unnecessarily advanced or unnatural language;
not mention scores, evaluation, or the revision process within the revised response.

OUTPUT FORMAT
Return only Markdown. Do not return JSON, XML, YAML, a code fence, or commentary
outside the requested report. Use the following section order and labels. Replace
all bracketed instructions with the assessment content. If no issue applies, write
“None observed” instead of omitting the field.

## Response Analysis

**Professor question interpretation:** [Concise statement of what the discussion question requires.]

**Candidate position:** [State the candidate’s central position, or “Not identifiable.”]

**Relationship to existing discussion:** [Explain whether the response agrees, disagrees, qualifies, extends, combines, or ignores the other contributions.]

### Main Supporting Points

- [A concise representation of each distinct reason, example, or proposal made by the candidate.]

## Criterion Evaluations

### Relevance and Contribution

**Evidence:**

- [Specific observation or short excerpt showing whether the response answers the professor and contributes to the discussion.]

**Reasoning:** [Evaluate whether the candidate presents a relevant, understandable, and meaningful contribution.]

**Limitations:**

- [Off-topic, repetitive, missing, contradictory, or non-contributory content.]

**Improvement needed:** [How the candidate could contribute more directly or meaningfully.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Elaboration

**Evidence:**

- [Reason, explanation, example, detail, knowledge, or experience supporting the position.]

**Reasoning:** [Evaluate whether the main claims are sufficiently developed and the support establishes why the position is reasonable.]

**Unsupported or underdeveloped claims:**

#### Claim 1

- **Claim:** [A claim made by the candidate.]
- **Current support:** [What support is provided, or “Not present.”]
- **Problem:** [Why the support is incomplete, vague, irrelevant, or ineffective.]
- **Needed development:** [The explanation, example, mechanism, consequence, or qualification that would improve it.]

**Improvement needed:** [The most important development the response needs.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Coherence and Clarity

**Evidence:**

- [Observation about progression from the position to reasons, explanations, examples, qualifications, and conclusions.]

**Reasoning:** [Evaluate logical sequencing and whether relationships among ideas are easy to follow.]

**Limitations:**

- [Abrupt transition, unclear reference, contradiction, disconnected example, repetition, or weak logical connection.]

**Improvement needed:** [How the reasoning should be reordered or connected.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Syntactic Control

**Evidence:**

- [Example showing sentence variety, clause relationships, repetitive structures, or structural errors.]

**Reasoning:** [Evaluate the range, accuracy, and effectiveness of sentence structures.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact or minimally quoted excerpt.]
- **Issue:** [Fragment, run-on, faulty coordination or subordination, unclear clause relationship, or other syntactic problem.]
- **Improved version:** [A corrected or more effective version.]

**Improvement needed:** [The main sentence-structure improvement required.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Vocabulary and Idiomatic Language

**Evidence:**

- [Example of effective or ineffective academic vocabulary, collocation, idiomatic language, register, or word form.]

**Reasoning:** [Evaluate whether vocabulary is precise, appropriate, natural, and sufficiently varied.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact word or phrase.]
- **Issue:** [Why it is vague, repetitive, unnatural, imprecise, wrongly formed, or inappropriate.]
- **Improved version:** [A more natural or accurate alternative.]

**Improvement needed:** [The principal lexical improvement required.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Grammatical and Lexical Accuracy

**Evidence:**

- [Representative observation about grammar, spelling, punctuation, capitalization, word form, or lexical accuracy.]

**Reasoning:** [Explain the frequency, severity, pattern, and effect of errors on readability and understanding.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact excerpt containing an error.]
- **Error type:** `grammar`, `word_form`, `spelling`, `punctuation`, `capitalization`, or `lexical_usage`
- **Explanation:** [Brief explanation of the error.]
- **Corrected version:** [Corrected form.]

**Error profile:**

- **Frequency:** `almost_none`, `few`, `noticeable`, `frequent`, or `pervasive`
- **Severity:** `minor`, `moderate`, or `serious`
- **Effect on clarity:** `none`, `limited`, `noticeable`, `substantial`, or `severe`

**Improvement needed:** [The highest-priority accuracy issue.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

## Overall Diagnosis

### Main Strengths

- [The strongest relevant feature demonstrated by the candidate.]

### Main Limitations

- [The most consequential weakness affecting the academic contribution.]

### Priority Improvements

#### Priority 1

- **Problem:** [A high-impact weakness.]
- **Recommended action:** [A concrete improvement the candidate should apply.]

## Score-Band Analysis

**Best-fitting band reasoning:** [Explain which ETS score-band description best matches the response using the complete criterion analysis.]

**Reason it does not reach the next band:** [Identify the limitations preventing the immediately higher score.]

**Reason it is stronger than the lower band:** [When relevant, explain why the response exceeds the immediately lower band.]

## Final Evaluation

- **Score:** [One integer from 0 to 5.]
- **Performance level:** `nonresponse`, `unsuccessful`, `mostly_unsuccessful`, `partially_successful`, `generally_successful`, or `fully_successful`

## Revised Responses

### Minimal-Edit 5/5 Revision

- **Target score:** 5

#### Revision Strategy

- [Briefly state the smallest changes needed to reach 5/5 while preserving the original response as closely as possible.]

#### Revised Response

[Write the complete minimal-edit 5/5 version here. Preserve as much original wording and structure as possible, but correct every score-limiting problem.]

### Enhanced 5/5 Revision

- **Target score:** 5

#### Revision Strategy

- [Briefly state the broader improvements made while keeping the response recognizably based on the candidate’s work.]

#### Revised Response

[Write the complete, realistic 5/5 Academic Discussion response here while preserving the candidate’s relevant position and useful original ideas.]
""".strip()


def split_discussion_task(task_prompt: str) -> tuple[str, str]:
    """Split one discussion prompt file using the exact INPUT section labels."""

    professor_markers = {"professor’s question:", "professor's question:"}
    student_markers = {
        "other students’ contributions:",
        "other students' contributions:",
    }
    lines = task_prompt.splitlines()
    professor_index = None
    student_index = None

    for index, line in enumerate(lines):
        label = line.strip().lstrip("#").strip().lower()
        if label in professor_markers:
            professor_index = index
        elif label in student_markers:
            student_index = index

    if (
        professor_index is None
        or student_index is None
        or professor_index >= student_index
    ):
        raise ValueError(
            "Academic Discussion prompt.md must contain 'Professor’s question:' "
            "followed by 'Other students’ contributions:'."
        )

    professor_question = "\n".join(lines[professor_index + 1 : student_index]).strip()
    student_contributions = "\n".join(lines[student_index + 1 :]).strip()
    if not professor_question or not student_contributions:
        raise ValueError(
            "Both Academic Discussion sections in prompt.md must contain text."
        )
    return professor_question, student_contributions


def build_user_prompt(task_type: str, task_prompt: str, candidate_response: str) -> str:
    if task_type == "write_an_email":
        return EMAIL_PROMPT_TEMPLATE.replace("{{task_prompt}}", task_prompt).replace(
            "{{candidate_response}}", candidate_response
        )

    professor_question, student_contributions = split_discussion_task(task_prompt)
    return (
        DISCUSSION_PROMPT_TEMPLATE.replace("{{professor_question}}", professor_question)
        .replace("{{student_contributions}}", student_contributions)
        .replace("{{candidate_response}}", candidate_response)
    )
