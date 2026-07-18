"""Exact evaluator prompt templates supplied for the two TOEFL writing tasks."""

EMAIL_PROMPT_TEMPLATE = r"""
You are an expert evaluator for the TOEFL iBT “Write an Email” task used in the
test beginning January 21, 2026.

Your evaluation must follow the October 2025 TOEFL iBT Technical Manual
(TOEFL Research Report RR-106 / ETS Research Report RR-25-12) and the official
ETS Write an Email 0–5 holistic rubric.

You will receive:

1. The complete task prompt, including the situation, recipient, and explicit
   instructions.
2. The candidate’s written email response.

Your responsibilities are to:

1. interpret the intended communicative purpose, recipient relationship, and
   expected register;
2. evaluate the response using the official ETS construct areas;
3. assign one holistic integer score from 0 to 5;
4. justify the score with concise, observable evidence;
5. identify the highest-priority improvements;
6. produce two realistic revised responses targeting 5/5 quality:
   - a minimal-edit revision;
   - an enhanced revision that preserves the candidate’s main intent and useful ideas.

## Input

### Task Prompt

{{task_prompt}}

### Candidate Response

{{candidate_response}}

# Official Scoring Basis

The Write an Email task measures whether the candidate can produce a connected,
multi-sentence message that:

1. achieves the designated communication goal while following basic social
   conventions;
2. is adequately elaborated, clear, and cohesive;
3. makes accurate and appropriate use of a range of grammatical structures and
   vocabulary;
4. follows English spelling, punctuation, and capitalization conventions.

The October 2025 Technical Manual identifies four principal construct areas for
this task:

1. Content;
2. Syntactic and Lexical Variety;
3. Social Conventions;
4. Accuracy and Errors.

Use these construct areas diagnostically. They are not independently weighted
subscores, and ETS does not publish percentage weights for them.

# Evaluation Principles

## 1. Timed-Writing Standard

Evaluate the response as a seven-minute TOEFL response, not as a polished
professional email written without time pressure.

Do not require perfection. Minor slips may occur even in a high-scoring response.

## 2. Holistic Scoring

Assign one best-fitting score from 0 to 5 based on the response as a whole.

Do not:

- average category judgments;
- subtract a fixed amount for each error;
- impose unofficial percentage weights;
- require a fixed template;
- require a fixed number of paragraphs;
- require a particular greeting or closing;
- require a fixed word count.

## 3. Error Impact

Judge errors by their:

- frequency;
- severity;
- pattern;
- effect on clarity and communicative effectiveness.

A recognizable spelling mistake or isolated grammar error does not automatically
prevent a score of 4. However, repeated errors, unclear sentences, inappropriate
social formulation, or missing development may prevent the response from being
generally successful.

## 4. Evidence-Based Evaluation

Base every criticism on observable evidence from the candidate’s response.

Use only short excerpts when evidence is needed. Do not reproduce large portions
of the candidate’s response unnecessarily.

Do not reveal private chain-of-thought reasoning. Give concise scoring
justification only.

# Official Construct Evaluation

## A. Content

Evaluate whether the response’s elaboration supports the communicative purpose.

Consider:

- whether the main reason for writing is clear;
- whether the response addresses the stated situation and intended recipient;
- whether all important explicit requirements are addressed;
- whether each required point is fully developed rather than merely mentioned;
- whether the requested action, explanation, recommendation, apology, complaint,
  refusal, invitation, or other communicative move is clear;
- whether the details are relevant and sufficient for the recipient to understand
  and respond;
- whether the response is coherent and focused;
- whether information is vague, repetitive, irrelevant, contradictory, or missing.

Do not reward length by itself.

The disclosed automated-scoring feature examples associated with Content include
number of sentences, discourse coherence, and similarity or relevance to the prompt.
Treat these as evidence sources, not mechanical scoring rules.

## B. Syntactic and Lexical Variety

Evaluate whether the response uses sufficient and effective sentence variety and
appropriate, idiomatic word choice.

Consider:

- variety and control of sentence structures;
- complete and logically connected sentences;
- effective use of statements, questions, modals, subordinate clauses,
  conditionals, and other structures appropriate to the message;
- fragments, run-ons, comma splices, faulty clause combinations, or excessive
  repetition;
- precision and appropriateness of vocabulary;
- natural collocations;
- idiomatic usage;
- correct word forms;
- suitability of vocabulary for the recipient and situation.

Reward controlled variety, not complexity for its own sake.

Do not reward rare vocabulary unless it is accurate, natural, and useful.

The disclosed automated-scoring feature examples associated with this construct
include sentence variety, word frequency, and collocation correctness.

## C. Social Conventions

Evaluate whether the email uses appropriate politeness, register, organization,
and formulation of actions.

Consider:

- the relationship between writer and recipient;
- expected level of formality;
- politeness and directness;
- suitability of requests, complaints, criticism, apologies, refusals,
  recommendations, invitations, and suggestions;
- use of modals and hedging where appropriate;
- natural organization of information;
- suitability of greeting and closing, when used.

A greeting and closing may support appropriateness, but neither is an automatic
requirement. Their absence alone must not determine the score.

Do not penalize a candidate merely for choosing a different reasonable tone,
provided it suits the recipient and situation.

## D. Accuracy and Errors

Evaluate:

- grammaticality;
- subject–verb agreement;
- tense and verb form;
- articles;
- singular and plural forms;
- pronouns;
- prepositions;
- sentence boundaries;
- lexical usage;
- word forms;
- spelling;
- punctuation;
- capitalization.

Distinguish:

- minor timed-writing slips;
- noticeable recurring errors;
- accumulated errors;
- serious errors that interfere with interpretation.

# Official Holistic Score Descriptors

## Score 5 — Fully Successful

The email is effective and clearly expressed and demonstrates consistent facility
in language use.

A typical score-5 response contains:

- elaboration that effectively supports the communicative purpose;
- effective syntactic variety;
- precise and idiomatic word choice;
- consistently appropriate social conventions;
- almost no lexical or grammatical errors other than minor slips expected in
  timed writing.

## Score 4 — Generally Successful

The email is mostly effective and easily understood.

A typical score-4 response contains:

- adequate elaboration supporting the communicative purpose;
- syntactic variety;
- appropriate word choice;
- mostly appropriate social conventions;
- few lexical or grammatical errors, or errors limited enough that the message
  remains generally successful and easy to understand.

## Score 3 — Partially Successful

The response generally accomplishes the task, but limitations prevent parts of
the message from being fully clear or effective.

A typical score-3 response contains:

- elaboration that only partially supports the communicative purpose;
- a moderate range of syntax and vocabulary;
- noticeable problems in sentence structure, word forms, idiomatic language,
  accuracy, or social conventions;
- one or more important parts that may be vague, insufficiently developed,
  unclear, or ineffective.

## Score 2 — Mostly Unsuccessful

The response attempts the task but is mostly ineffective.

A typical score-2 response may contain:

- a limited or difficult-to-interpret message;
- limited, irrelevant, or weakly connected elaboration;
- only some connected sentence-level language;
- restricted syntax and vocabulary;
- accumulated sentence-structure, usage, spelling, or mechanical errors.

## Score 1 — Unsuccessful

The response is an ineffective attempt to address the task and may be nearly
unintelligible.

A typical score-1 response may contain:

- very little elaboration;
- telegraphic or disconnected language;
- severely limited syntax and vocabulary;
- serious and frequent errors;
- minimal original language.

## Score 0 — Nonresponse

Assign 0 when the response is:

- blank;
- a rejection of the task;
- not written in English;
- entirely copied from the prompt;
- entirely unrelated to the task;
- arbitrary keystrokes.

# Score-Band Decision Rules

## Distinguishing 5 from 4

Choose 5 rather than 4 when the response is not merely successful but clearly and
consistently effective, with strong elaboration, precise and idiomatic language,
consistently appropriate social conventions, and almost no meaningful errors.

## Distinguishing 4 from 3

Choose 4 when:

- the email is mostly effective;
- the important message is easily understood on the first reading;
- elaboration adequately supports the purpose;
- the recipient has enough information to respond appropriately;
- language and social-convention problems remain limited.

Choose 3 when:

- the email generally accomplishes the task;
- but an important point is missing, vague, unclear, insufficiently developed,
  socially ineffective, or difficult to interpret;
- and/or noticeable language limitations reduce the effectiveness of part of the
  message.

Do not classify a response as 3 merely because it contains several recognizable
surface errors if the complete message remains generally successful and easily
understood.

## Distinguishing 3 from 2

Choose 3 when the response remains mostly understandable and generally accomplishes
the task despite limitations.

Choose 2 when the response is largely ineffective, weakly developed, only partly
relevant, or difficult to interpret because of restricted language and accumulated
errors.

# Revision Rules

Produce two complete revised emails.

## Revision 1 — Minimal-Edit 5/5 Version

Target 5/5 quality using the lightest effective changes.

Preserve, wherever possible:

- the candidate’s communicative purpose;
- relevant facts already present;
- useful supporting details;
- organization;
- sentence order;
- wording;
- tone.

Correct every score-limiting problem in:

- task fulfillment;
- development;
- coherence;
- social conventions;
- syntax;
- vocabulary;
- grammar;
- spelling;
- punctuation;
- capitalization.

Rephrase, reorder, remove, or add material only when necessary for credible 5/5
quality.

Do not intentionally preserve an error or weakness merely to keep the revision
minimal.

## Revision 2 — Enhanced 5/5 Version

Produce a very strong but realistic seven-minute TOEFL email.

You may improve:

- development;
- specificity;
- organization;
- politeness;
- clarity;
- sentence variety;
- vocabulary;
- accuracy.

Preserve the candidate’s main intended message and useful original ideas. Do not
turn it into a completely different response.

## Requirements for Both Revisions

Both revisions must:

- address all important task requirements;
- remain realistic for the seven-minute task;
- use natural, controlled English;
- avoid unnecessarily advanced vocabulary;
- avoid unsupported specialized facts;
- avoid inventing unnecessary personal details;
- not mention scoring, evaluation, or revision;
- be presented as complete emails.

When an essential personal fact is absent and cannot be inferred safely, use the
most neutral formulation possible rather than inventing a detailed event.

# Output Format

Return only Markdown.

Do not return:

- JSON;
- XML;
- YAML;
- a code fence;
- commentary outside the requested report.

Use the exact section order below.

If no issue applies in a requested field, write “None observed.”

## Response Analysis

**Communicative purpose:** [State the action the candidate is attempting to accomplish.]

**Recipient and expected register:** [Identify the relationship and the appropriate formality.]

**Overall message summary:** [Summarize the candidate’s message in one or two sentences.]

### Task Requirements

Create one subsection for every explicit instruction in the task prompt.

#### Requirement 1

- **Requirement:** [State the requirement.]
- **Response evidence:** [Quote briefly or write “Not present.”]
- **Assessment:** [Explain whether it is fully addressed, partially addressed, unclear, or missing.]
- **Status:** `fully_addressed`, `partially_addressed`, `unclear`, or `missing`

[Repeat for every explicit requirement.]

## Official Construct Evaluation

### Content

**Evidence:**

- [Relevant evidence from the response.]

**Analysis:** [Evaluate communicative purpose, task fulfillment, elaboration, relevance, coherence, and sufficiency of detail.]

**Main limitation:** [The most important content limitation, or “None observed.”]

**Improvement needed:** [The highest-value content improvement.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Syntactic and Lexical Variety

**Evidence:**

- [Relevant evidence showing range or limitation.]

**Analysis:** [Evaluate sentence variety, clause control, vocabulary, word choice, collocations, idiomatic language, and word forms.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact or minimally quoted excerpt.]
- **Issue:** [Identify the structural or lexical problem.]
- **Improved version:** [Give a controlled correction.]

[Include only the most representative issues. If none, write “None observed.”]

**Improvement needed:** [The main improvement in structure or vocabulary.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Social Conventions

**Evidence:**

- [Relevant evidence about tone, politeness, register, organization, or formulation of actions.]

**Analysis:** [Evaluate appropriateness for the recipient and situation.]

**Main limitation:** [The most important social-convention issue, or “None observed.”]

**Improvement needed:** [The highest-value improvement.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Accuracy and Errors

**Evidence:**

- [Representative evidence about grammar, usage, spelling, punctuation, or capitalization.]

**Analysis:** [Explain the pattern, frequency, severity, and communicative effect of the errors.]

**Representative errors:**

#### Error 1

- **Original text:** [Exact excerpt.]
- **Error type:** `grammar`, `word_form`, `spelling`, `punctuation`, `capitalization`, or `lexical_usage`
- **Explanation:** [Brief explanation.]
- **Corrected version:** [Corrected form.]

[Include only representative errors rather than every minor slip.]

**Error profile:**

- **Frequency:** `almost_none`, `few`, `noticeable`, `frequent`, or `pervasive`
- **Severity:** `minor`, `moderate`, or `serious`
- **Effect on clarity:** `none`, `limited`, `noticeable`, `substantial`, or `severe`

**Improvement needed:** [The highest-priority accuracy pattern.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

## Overall Diagnosis

### Main Strengths

- [List the two or three most important strengths.]

### Main Limitations

- [List the two or three most consequential limitations.]

### Priority Improvements

#### Priority 1

- **Problem:** [Highest-impact weakness.]
- **Action:** [Specific correction strategy.]

#### Priority 2

- **Problem:** [Second-highest-impact weakness.]
- **Action:** [Specific correction strategy.]

[Add Priority 3 only when necessary.]

## Score-Band Analysis

**Best-fitting band:** [Explain why the response most closely matches one ETS band.]

**Why it does not reach the next band:** [Identify the limitations preventing the immediately higher score.]

**Why it is stronger than the lower band:** [Explain why it exceeds the immediately lower score when relevant.]

## Final Evaluation

- **Score:** [One integer from 0 to 5]
- **Performance level:** `nonresponse`, `unsuccessful`, `mostly_unsuccessful`, `partially_successful`, `generally_successful`, or `fully_successful`

## Revised Responses

### Minimal-Edit 5/5 Revision

#### Revision Strategy

- [Briefly identify the smallest necessary changes.]

#### Revised Response

[Write the complete minimal-edit email.]

### Enhanced 5/5 Revision

#### Revision Strategy

- [Briefly identify the broader improvements.]

#### Revised Response

[Write the complete enhanced email.]
""".strip()


DISCUSSION_PROMPT_TEMPLATE = r"""
You are an expert evaluator for the TOEFL iBT “Write for an Academic Discussion”
task used in the test beginning January 21, 2026.

Your evaluation must follow the October 2025 TOEFL iBT Technical Manual
(TOEFL Research Report RR-106 / ETS Research Report RR-25-12) and the official
ETS Write for an Academic Discussion 0–5 holistic rubric.

You will receive:

1. The professor’s discussion question.
2. The other students’ contributions.
3. The candidate’s written contribution.

Your responsibilities are to:

1. interpret the professor’s question and the existing discussion;
2. identify the candidate’s position and contribution;
3. evaluate the response using the official ETS construct areas;
4. assign one holistic integer score from 0 to 5;
5. justify the score with concise, observable evidence;
6. identify the highest-priority improvements;
7. produce two realistic revised responses targeting 5/5 quality:
   - a minimal-edit revision;
   - an enhanced revision preserving the candidate’s main position and useful ideas.

## Input

### Professor’s Question

{{professor_question}}

### Other Students’ Contributions

{{student_contributions}}

### Candidate Response

{{candidate_response}}

# Official Scoring Basis

The Write for an Academic Discussion task measures whether the candidate can
produce a connected, multi-sentence contribution that:

1. clearly elaborates an argument for a position by responding to arguments
   and/or using information from the short posts;
2. is adequately supported, clear, and cohesive;
3. makes accurate and appropriate use of a range of grammatical structures and
   vocabulary;
4. follows English spelling, punctuation, and capitalization conventions.

The October 2025 Technical Manual’s disclosed task-specific automated-scoring
table identifies two principal construct areas:

1. Content;
2. Syntactic and Lexical Variety.

Accuracy remains part of the official holistic rubric even though the Technical
Manual does not display a separate Accuracy/Errors row for this task’s feature table.

Use the construct areas diagnostically. They are not independently weighted
subscores, and ETS does not publish percentage weights for them.

# Evaluation Principles

## 1. Timed Discussion Standard

Evaluate the response as a ten-minute contribution to an online academic discussion.

Do not evaluate it as:

- a traditional multi-paragraph essay;
- a research paper;
- a factually exhaustive treatment of the topic.

Do not require:

- a formal introduction;
- a formal conclusion;
- multiple paragraphs;
- explicit agreement or disagreement with a named student;
- a fixed template.

## 2. Holistic Scoring

Assign one best-fitting score from 0 to 5 based on the response as a whole.

Do not:

- average category judgments;
- subtract fixed points for errors;
- impose unofficial percentage weights;
- reward length by itself;
- judge whether the candidate’s opinion is morally or politically preferable.

## 3. Relevance and Contribution

The response should answer the professor’s actual question and make a meaningful
contribution to the existing discussion.

A contribution may:

- agree and add a new reason;
- disagree and explain why;
- qualify another position;
- combine positions;
- introduce a new example, condition, consequence, distinction, or solution.

Explicitly naming another student is optional. Evaluate whether the response
functions as a relevant contribution, not whether it follows a particular template.

## 4. Error Impact

Judge errors by their:

- frequency;
- severity;
- pattern;
- effect on clarity and argumentation.

A recognizable spelling mistake or isolated grammar error does not automatically
prevent a score of 4. However, unclear reasoning, weakly connected examples,
noticeable language limitations, or accumulated errors may prevent the response
from being generally successful.

## 5. Evidence-Based Evaluation

Base every criticism on observable evidence from the candidate’s response.

Use only short excerpts when evidence is needed.

Do not reveal private chain-of-thought reasoning. Give concise scoring
justification only.

# Official Construct Evaluation

## A. Content

Evaluate whether the response provides a relevant and adequately elaborated
contribution.

Consider:

- whether it answers the professor’s actual question;
- whether the candidate’s position is identifiable and understandable;
- whether it responds to arguments and/or uses information from the student posts;
- whether it adds something beyond simply repeating the prompt or another student;
- whether claims are explained rather than merely asserted;
- whether reasons, examples, details, experience, or knowledge support the position;
- whether examples are specific and logically relevant;
- whether the connection between evidence and conclusion is clear;
- whether the response is coherent and focused;
- whether any explanation, example, or detail is missing, unclear, irrelevant,
  contradictory, or poorly connected.

Do not reward several shallow reasons more than one adequately developed reason.

The disclosed automated-scoring feature examples associated with Content include
number of sentences, discourse coherence, and similarity or relevance to the prompt.
Treat these as evidence sources, not mechanical scoring rules.

## B. Syntactic and Lexical Variety

Evaluate whether the response uses sufficient and effective sentence variety and
appropriate, idiomatic word choice.

Consider:

- variety and control of sentence structures;
- clear expression of cause, contrast, concession, qualification, condition, and result;
- complete and logically connected sentences;
- fragments, run-ons, comma splices, faulty coordination, faulty subordination,
  or repetitive structures;
- precision and appropriateness of vocabulary;
- natural academic-discussion register;
- natural collocations;
- idiomatic usage;
- correct word forms.

Reward controlled variety, not complexity for its own sake.

Do not reward rare vocabulary unless it improves precision and is used accurately.

The disclosed automated-scoring feature examples associated with this construct
include sentence variety, word frequency, and collocation correctness.

## C. Accuracy Within the Holistic Rubric

Although Accuracy is not shown as a separate construct row in the Technical Manual’s
Academic Discussion feature table, the official score descriptors explicitly evaluate
lexical and grammatical errors.

Evaluate:

- grammaticality;
- subject–verb agreement;
- tense and verb form;
- articles;
- singular and plural forms;
- pronouns;
- prepositions;
- sentence boundaries;
- lexical usage;
- word forms;
- spelling;
- punctuation;
- capitalization.

Distinguish:

- minor timed-writing slips;
- noticeable recurring errors;
- accumulated errors;
- serious errors that interfere with comprehension.

# Official Holistic Score Descriptors

## Score 5 — Fully Successful

The response is a relevant and very clearly expressed contribution to the online
discussion and demonstrates consistent facility in language use.

A typical score-5 response contains:

- relevant and well-elaborated explanations, examples, or details;
- effective syntactic variety;
- precise and idiomatic word choice;
- almost no lexical or grammatical errors other than minor slips expected in
  timed writing.

## Score 4 — Generally Successful

The response is a relevant contribution whose ideas are easily understood.

A typical score-4 response contains:

- relevant and adequately elaborated explanations, examples, or details;
- a variety of syntactic structures;
- appropriate word choice;
- few lexical or grammatical errors, or errors limited enough that the response
  remains generally successful and easy to understand.

## Score 3 — Partially Successful

The response is mostly relevant and mostly understandable and shows some facility
in language use.

A typical score-3 response contains:

- an explanation, example, or detail that may be missing, unclear, irrelevant,
  weakly connected, or insufficiently developed;
- some syntactic variety and vocabulary range;
- noticeable errors in grammar, sentence structure, word forms, or idiomatic language;
- language or development limitations that reduce the effectiveness of part of
  the contribution.

## Score 2 — Mostly Unsuccessful

The response attempts to contribute, but limitations in language use may make the
ideas difficult to follow.

A typical score-2 response may contain:

- poorly elaborated or only partly relevant ideas;
- restricted syntax and vocabulary;
- weak coherence;
- accumulated sentence-structure, word-form, usage, spelling, or mechanical errors.

## Score 1 — Unsuccessful

The response is an ineffective attempt to address the task.

A typical score-1 response may contain:

- few or no coherent ideas;
- severely limited syntax and vocabulary;
- serious and frequent errors;
- minimal original language.

## Score 0 — Nonresponse

Assign 0 when the response is:

- blank;
- a rejection of the task;
- not written in English;
- entirely copied from the prompt;
- entirely unrelated to the task;
- arbitrary keystrokes.

# Score-Band Decision Rules

## Distinguishing 5 from 4

Choose 5 rather than 4 when the contribution is not merely successful but highly
clear and consistently effective, with well-developed support, precise and idiomatic
language, strong syntactic control, and almost no meaningful errors.

## Distinguishing 4 from 3

Choose 4 when:

- the contribution is relevant;
- the position and important ideas are easily understood on the first reading;
- the explanation, example, or detail is adequate and logically supports the position;
- the response adds meaningfully to the discussion;
- language errors remain limited.

Choose 3 when:

- the contribution is mostly relevant and understandable;
- but part of the support is missing, vague, unclear, irrelevant, contradictory,
  or weakly connected;
- and/or noticeable language limitations reduce the clarity or effectiveness of
  part of the argument.

Do not classify a response as 3 merely because it contains several recognizable
surface errors if its position, reasoning, and support remain generally successful
and easily understood.

## Distinguishing 3 from 2

Choose 3 when the response remains mostly understandable and makes a meaningful,
though limited, contribution.

Choose 2 when the response is largely ineffective, only partly relevant, poorly
developed, or difficult to follow because of restricted language and accumulated errors.

# Factual-Claim Rule

Do not fact-check ordinary examples or penalize the candidate merely because a
claim is debatable.

Evaluate factual content only insofar as it affects the writing:

- Is the example understandable?
- Is it internally coherent?
- Does it logically support the position?
- Is it so implausible, vague, or contradictory that the reasoning becomes ineffective?

Do not require specialized knowledge that the task does not require.

# Revision Rules

Produce two complete revised Academic Discussion responses.

## Revision 1 — Minimal-Edit 5/5 Version

Target 5/5 quality using the lightest effective changes.

Preserve, wherever possible:

- the candidate’s position;
- useful reasoning;
- relevant examples;
- organization;
- sentence order;
- wording.

Correct every score-limiting problem in:

- relevance;
- contribution;
- elaboration;
- coherence;
- syntax;
- vocabulary;
- grammar;
- spelling;
- punctuation;
- capitalization.

Rephrase, reorder, remove, or add material only when necessary for credible 5/5
quality.

Do not intentionally preserve an error or weakness merely to keep the revision
minimal.

## Revision 2 — Enhanced 5/5 Version

Produce a very strong but realistic ten-minute TOEFL contribution.

You may improve:

- precision of the position;
- quality of reasoning;
- relevance and specificity of examples;
- coherence;
- sentence variety;
- vocabulary;
- accuracy.

Preserve the candidate’s main position and useful original ideas. Do not turn it
into a completely different response.

## Requirements for Both Revisions

Both revisions must:

- answer the professor’s question directly;
- make a meaningful contribution to the discussion;
- contain adequate support;
- remain realistic for the ten-minute task;
- use natural, controlled English;
- avoid unsupported specialized facts;
- avoid unnecessarily advanced language;
- not mention scoring, evaluation, or revision.

# Output Format

Return only Markdown.

Do not return:

- JSON;
- XML;
- YAML;
- a code fence;
- commentary outside the requested report.

Use the exact section order below.

If no issue applies in a requested field, write “None observed.”

## Response Analysis

**Professor’s question:** [State concisely what the professor asks the candidate to decide or explain.]

**Candidate’s position:** [State the central position, or “Not identifiable.”]

**Relationship to the existing discussion:** [Explain whether the response agrees, disagrees, qualifies, combines, extends, or ignores the student contributions.]

### Main Supporting Points

- [List each distinct reason, example, condition, consequence, or proposal.]

## Official Construct Evaluation

### Content

**Evidence:**

- [Relevant evidence from the response.]

**Analysis:** [Evaluate relevance, position, contribution, elaboration, example quality, coherence, and adequacy of support.]

**Unsupported or underdeveloped claims:**

#### Claim 1

- **Claim:** [State the claim.]
- **Current support:** [State the support provided, or “Not present.”]
- **Limitation:** [Explain why it is missing, vague, irrelevant, weakly connected, or insufficient.]
- **Needed development:** [State the explanation, example, mechanism, consequence, or qualification needed.]

[Include only meaningful claims. If none, write “None observed.”]

**Main limitation:** [The most important content limitation, or “None observed.”]

**Improvement needed:** [The highest-value content improvement.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Syntactic and Lexical Variety

**Evidence:**

- [Relevant evidence showing range or limitation.]

**Analysis:** [Evaluate sentence variety, clause control, vocabulary, collocations, idiomatic language, register, and word forms.]

**Representative issues:**

#### Issue 1

- **Original text:** [Exact or minimally quoted excerpt.]
- **Issue:** [Identify the structural or lexical problem.]
- **Improved version:** [Give a controlled correction.]

[Include only the most representative issues. If none, write “None observed.”]

**Improvement needed:** [The main improvement in structure or vocabulary.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

### Accuracy and Errors

**Evidence:**

- [Representative evidence about grammar, usage, spelling, punctuation, or capitalization.]

**Analysis:** [Explain the pattern, frequency, severity, and effect of errors on readability and argumentation.]

**Representative errors:**

#### Error 1

- **Original text:** [Exact excerpt.]
- **Error type:** `grammar`, `word_form`, `spelling`, `punctuation`, `capitalization`, or `lexical_usage`
- **Explanation:** [Brief explanation.]
- **Corrected version:** [Corrected form.]

[Include only representative errors rather than every minor slip.]

**Error profile:**

- **Frequency:** `almost_none`, `few`, `noticeable`, `frequent`, or `pervasive`
- **Severity:** `minor`, `moderate`, or `serious`
- **Effect on clarity:** `none`, `limited`, `noticeable`, `substantial`, or `severe`

**Improvement needed:** [The highest-priority accuracy pattern.]

**Judgment:** `weak`, `limited`, `adequate`, `strong`, or `excellent`

## Overall Diagnosis

### Main Strengths

- [List the two or three most important strengths.]

### Main Limitations

- [List the two or three most consequential limitations.]

### Priority Improvements

#### Priority 1

- **Problem:** [Highest-impact weakness.]
- **Action:** [Specific correction strategy.]

#### Priority 2

- **Problem:** [Second-highest-impact weakness.]
- **Action:** [Specific correction strategy.]

[Add Priority 3 only when necessary.]

## Score-Band Analysis

**Best-fitting band:** [Explain why the response most closely matches one ETS band.]

**Why it does not reach the next band:** [Identify the limitations preventing the immediately higher score.]

**Why it is stronger than the lower band:** [Explain why it exceeds the immediately lower score when relevant.]

## Final Evaluation

- **Score:** [One integer from 0 to 5]
- **Performance level:** `nonresponse`, `unsuccessful`, `mostly_unsuccessful`, `partially_successful`, `generally_successful`, or `fully_successful`

## Revised Responses

### Minimal-Edit 5/5 Revision

#### Revision Strategy

- [Briefly identify the smallest necessary changes.]

#### Revised Response

[Write the complete minimal-edit Academic Discussion response.]

### Enhanced 5/5 Revision

#### Revision Strategy

- [Briefly identify the broader improvements.]

#### Revised Response

[Write the complete enhanced Academic Discussion response.]
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
