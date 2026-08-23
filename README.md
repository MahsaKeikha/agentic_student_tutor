# F93 Agentic Student Tutor

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for tutoring across learning-goal analysis, misconception detection, adaptive explanation, practice generation, progress review, accessibility, academic-integrity boundaries, and qualified human escalation.

F93 is designed as a reusable multi-agent tutoring reference for educational settings where students need structured help without transferring grading, disciplinary, accommodation, or institutional authority to an automated system.

This repository supports learning assistance. It does not assign final grades, determine misconduct, modify student records, decide accommodations, impersonate students, submit work on their behalf, or replace qualified educators.

## Tutoring lifecycle

```text
learner goal + course context
          |
          v
 learning diagnosis
          |
          v
 adaptive explanation
          |
          v
 practice generation
          |
          v
 progress review
          |
          v
 safety + escalation
          |
          v
 qualified human support
```

The workflow is fail closed. Content-accuracy gaps, answer leakage, assessment-integrity risks, unsupported learner-specific inference, privacy violations, accessibility barriers, unresolved overreliance risk, or missing escalation pathways remain blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Learning Diagnostician Agent | Identifies target concepts, prerequisite gaps, and likely misconceptions from available evidence | What does the learner appear to understand, and what evidence supports that conclusion? |
| Explanation Designer Agent | Adapts explanations, examples, analogies, and scaffolding to the learning goal | What explanation would help without overstating certainty or replacing the learner's own work? |
| Practice Generator Agent | Produces aligned practice and graduated challenge | What practice would strengthen the target skill without leaking restricted assessment answers? |
| Progress Reviewer Agent | Reviews evidence of improvement and remaining gaps | What has the learner demonstrated, and what still requires practice or educator review? |
| Safety and Escalation Agent | Enforces privacy, integrity, accessibility, and escalation boundaries | When should tutoring stop, narrow scope, or hand off to a qualified human? |

No agent independently assigns grades or makes consequential academic judgments.

## Repository structure

```text
AGENTS/
├── learning_diagnostician_agent.py
├── explanation_designer_agent.py
├── practice_generator_agent.py
├── progress_reviewer_agent.py
└── safety_escalation_agent.py

SKILLS/
├── diagnostic_reasoning.py
├── explanation_adaptation.py
├── practice_design.py
├── mastery_review.py
└── escalation_policy.py

TOOLS/
├── concept_map_tool.py
├── misconception_check_tool.py
├── practice_builder_tool.py
├── progress_log_tool.py
└── source_check_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Tutoring context

A useful tutoring record can include:

```text
subject
course_or_level
learning_goal
known_prerequisites
current_task
allowed_assistance
assessment_status
accessibility_needs
source_materials
educator_constraints
```

The tutor should reason from the actual learning context rather than assuming one explanation style or difficulty level fits every learner.

## Learning goals

Tutoring should begin with an explicit learning target.

Examples include:

- explain a concept
- solve a class of problems
- interpret evidence
- write a proof
- debug code
- analyze a text
- practice a language skill
- prepare for an exam
- review feedback

A broad request should be decomposed into concrete concepts or skills before progress is assessed.

## Concept maps

`TOOLS/concept_map_tool.py` supports deterministic representation of concept dependencies.

A concept map can track:

```text
concept_id
concept_name
prerequisites
related_concepts
mastery_evidence
misconceptions
practice_status
```

This helps the tutoring workflow distinguish a surface error from a deeper prerequisite gap.

## Diagnostic reasoning

The Learning Diagnostician Agent should infer cautiously from observable evidence such as:

- learner explanations
- worked steps
- answers to practice questions
- questions asked
- recurring error patterns
- instructor feedback provided by the learner

It should not infer intelligence, disability, motivation, mental-health status, or other sensitive characteristics from limited academic behavior.

## Misconception checks

`TOOLS/misconception_check_tool.py` supports structured checks for common conceptual errors.

A misconception record can include:

```text
concept
observed_error
possible_misconception
supporting_evidence
confidence
counterexample_or_probe
review_state
```

A suspected misconception should remain a hypothesis until the learner's reasoning provides sufficient evidence.

## Adaptive explanations

The Explanation Designer Agent can vary:

- level of abstraction
- number of intermediate steps
- examples
- visual or verbal framing
- analogy use
- mathematical detail
- terminology
- pacing

Adaptation should support understanding rather than simply making the answer easier to copy.

## Scaffolding

Useful scaffolding can follow a progression such as:

```text
prompt -> hint -> partial structure -> worked example -> independent practice
```

The tutor should avoid jumping immediately to a full solution when a smaller hint would better support learning.

## Worked examples

Worked examples can be useful when they are clearly separated from active graded work.

A worked example should ideally:

- use a similar but not identical problem when integrity matters
- make reasoning steps visible
- explain why each step is taken
- identify common mistakes
- connect back to the learning objective

## Socratic tutoring

Question-driven tutoring can help learners articulate reasoning.

Useful prompts include asking the learner to:

- explain the next step
- identify assumptions
- compare two approaches
- predict an outcome
- find an error
- justify a conclusion

Socratic questioning should not become needless obstruction when the learner genuinely needs direct explanation.

## Practice generation

`TOOLS/practice_builder_tool.py` supports aligned practice design.

Practice can vary by:

- difficulty
- concept
- representation
- context
- number of steps
- degree of scaffolding
- transfer distance

The Practice Generator should avoid creating exercises that accidentally reproduce restricted assessment items.

## Retrieval and spacing

Where appropriate, tutoring can use retrieval practice and spaced review.

A progress plan can revisit concepts after delays rather than relying only on immediate repetition.

The repository does not claim one fixed spacing schedule is optimal for every learner or subject.

## Mastery evidence

The Progress Reviewer should distinguish exposure from demonstrated understanding.

Evidence of stronger mastery can include:

- correct independent explanation
- successful novel problem solving
- transfer to a different context
- accurate error detection
- consistent performance over time

A single correct answer should not automatically be labeled mastery.

## Progress logs

`TOOLS/progress_log_tool.py` provides deterministic progress records.

A useful entry can include:

```text
date_or_session
learning_goal
concepts_practiced
evidence_of_understanding
remaining_gaps
practice_completed
next_step
educator_escalation
```

Progress logs should avoid unnecessary sensitive personal information.

## Source checking

`TOOLS/source_check_tool.py` supports checking the provenance of instructional claims and references.

The tutor should distinguish:

- course-provided material
- textbook material
- instructor guidance
- verified external sources
- general explanation
- uncertain or disputed information

The system should never fabricate citations or claim that a source supports material it has not verified.

## Academic-integrity boundary

Tutoring and answer production are not the same task.

F93 should examine whether a request involves:

- homework
- take-home exams
- quizzes
- coding assessments
- essays
- lab reports
- admissions assignments
- competitions
- certification tests

When rules are known, assistance should follow them. When rules are unclear and the task appears graded, the tutor should favor explanation, hints, analogous examples, and learning support over producing a submission-ready answer.

## Answer leakage

Answer leakage occurs when tutoring reveals restricted answers in a way that defeats the intended assessment.

Examples include:

- providing a complete solution to a live closed-book exam question
- reconstructing answer keys
- giving direct answers to protected test items
- completing an individual graded assignment contrary to course rules

The Safety and Escalation Agent should block or narrow assistance in these cases.

## Authorship

The system must not impersonate a student or conceal who created submitted academic work.

It may help with:

- brainstorming
- outlining
- explanation
- feedback
- practice
- revision guidance

Submission rules remain controlled by the course or institution.

## Academic-integrity findings

F93 does not determine whether a student cheated.

It must not infer misconduct from:

- writing style alone
- model-detection scores alone
- sudden improvement alone
- similarity without context

Academic-integrity findings require human review, evidence, policy context, and due process.

## Student privacy

Tutoring systems should minimize collection of identifiable student information.

Sensitive academic data can include:

- names
- student IDs
- grades
- accommodations
- disability information
- disciplinary information
- advising notes
- private communications

Only information necessary for the learning task should be retained.

## Accessibility

Tutoring should support multiple ways of accessing explanations when practical.

Accessibility considerations can include:

- clear structure
- readable formatting
- accessible equations
- descriptive text for visuals
- language clarity
- alternative explanation modes
- manageable cognitive load
- pacing

Formal accommodations remain the responsibility of authorized institutional processes.

## Accessibility boundary

F93 may adapt presentation or tutoring style, but it does not autonomously grant or deny formal accommodations.

If a learner requests an institutional accommodation decision, the workflow should direct that decision to the appropriate authorized human process.

## Overreliance

A tutoring system should strengthen learner capability rather than create unnecessary dependence.

Overreliance indicators can include:

- repeated requests for direct answers without engagement
- inability to explain copied solutions
- using the tutor as a substitute for all independent practice
- avoidance of instructor feedback

The appropriate response is educational scaffolding, not punishment or unsupported judgment.

## Confidence and uncertainty

The tutor should communicate uncertainty when content is ambiguous, source material is incomplete, or multiple conventions exist.

It should not present uncertain information as settled simply to appear confident.

## Error correction

When the tutor detects an error in its own prior explanation, it should:

1. identify the error clearly
2. correct the reasoning
3. explain the impact
4. update the learning path if necessary

Silent correction makes it harder for learners to understand what changed.

## Emotional and motivational boundaries

Tutoring can be encouraging, but it should avoid manipulative dependency or pretending to have human emotional authority.

The system should not pressure a learner to keep interacting or imply that the learner needs the tutor rather than educators, peers, or independent study.

## Safety and escalation

The Safety and Escalation Agent can trigger human handoff when:

- course rules are unclear for a consequential assessment
- content accuracy cannot be established
- a learner needs formal accommodation decisions
- a grade dispute requires institutional authority
- an academic-integrity issue arises
- repeated misunderstanding requires instructor intervention
- the request falls outside educational tutoring scope

Escalation is a normal workflow outcome, not a failure.

## Human authority boundaries

F93 must not autonomously:

- assign or change grades
- make pass or fail decisions
- determine misconduct
- impose discipline
- modify student records
- decide accommodations
- impersonate a student
- submit assignments
- access restricted assessment systems without authorization
- fabricate citations or course policy
- claim educator approval

Final educational authority remains with qualified educators and authorized institutional processes.

## End-to-end reference workflow

A typical F93 tutoring workflow follows this sequence:

1. Define the learner's goal and course context.
2. Identify the relevant concept map and prerequisites.
3. Gather observable evidence of current understanding.
4. Form tentative misconception hypotheses where appropriate.
5. Select an explanation strategy and level of scaffolding.
6. Check whether the task is graded or otherwise integrity-sensitive.
7. Provide explanation or hints without prohibited answer leakage.
8. Generate aligned practice.
9. Review independent learner performance.
10. Update the progress record.
11. Review accessibility and privacy needs.
12. Check for overreliance or unresolved content uncertainty.
13. Escalate to a qualified human when required.
14. Preserve evidence and state for reproducibility.
15. Keep all consequential academic authority with humans.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and benchmark material under `benchmarks/`.

Evaluation should test both instructional quality and governance behavior.

Useful dimensions include:

- diagnostic calibration
- misconception handling
- explanation accuracy
- scaffolding quality
- practice alignment
- answer-leakage prevention
- academic-integrity boundaries
- privacy enforcement
- accessibility handling
- unsupported inference prevention
- escalation behavior
- human-authority enforcement

Held-out scenarios should include tempting cases where the easiest response would be to provide a restricted answer rather than support learning.

## Failure states

Useful explicit states include:

```text
LEARNING GOAL INCOMPLETE
PREREQUISITE GAP
MISCONCEPTION UNCERTAIN
CONTENT ACCURACY UNVERIFIED
ANSWER LEAKAGE RISK
ACADEMIC INTEGRITY RISK
PRACTICE MISALIGNED
STUDENT PRIVACY RISK
ACCESSIBILITY REVIEW REQUIRED
UNSUPPORTED LEARNER INFERENCE
OVERRELIANCE RISK
EDUCATOR ESCALATION REQUIRED
FINAL GRADING AUTHORITY PROHIBITED
STUDENT RECORD MODIFICATION PROHIBITED
ACCOMMODATION DECISION PROHIBITED
```

The system should never fabricate learner evidence, mastery, grades, accommodations, misconduct findings, course rules, citations, or educator approval.

## Observability

The `observability/` layer supports traceable tutoring execution.

Useful telemetry includes:

- concepts reviewed
- misconception hypotheses
- explanations selected
- hints provided
- practice generated
- progress evidence
- integrity flags
- privacy flags
- accessibility flags
- escalation state

Observability supports debugging and academic review. It does not create educational authority.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11, and 3.12.

## Reproducibility

For a tutoring session intended to be reviewed or reproduced, version at minimum:

- course context
- learning goal
- concept map
- source materials
- practice items
- integrity constraints
- explanation strategy
- progress evidence
- unresolved gaps
- escalation state

Personal student information should be minimized even when reproducibility is important.

## L3 Gold Standard

F93 follows the library's L3 Gold Standard structure through five specialist agents, deterministic tutoring tools, explicit orchestration and state, safety boundaries, observability, held-out governance evaluation, CI, fail-closed tutoring gates, and qualified human escalation.

This maturity designation describes the engineering and governance structure of the repository. It is not evidence of institutional approval, educator certification, formal accommodation authority, grading authority, or permission to bypass academic-integrity rules.

## Extending F93

Common extensions include:

- learning-management systems
- course content repositories
- textbook indexes
- practice banks
- concept graphs
- accessibility tooling
- progress dashboards
- educator escalation workflows
- citation systems
- tutoring analytics

New integrations should preserve student privacy, academic integrity, source provenance, accessibility, and human educational authority.

## Example applications

F93 can serve as a reference architecture for:

- STEM tutoring
- programming tutoring
- language learning
- writing support
- exam preparation
- concept review
- homework guidance
- graduate-level study support
- professional education
- self-directed learning

Each implementation should be adapted to the learner, subject, course rules, and institutional context.

## Design principles

1. Start from explicit learning goals and observable evidence.
2. Treat misconceptions as hypotheses until supported by learner reasoning.
3. Use scaffolding to strengthen independent thinking.
4. Separate tutoring from unauthorized answer production.
5. Preserve academic integrity and authorship boundaries.
6. Minimize student data and unsupported personal inference.
7. Design explanations for accessibility and clarity.
8. Treat progress as demonstrated evidence, not mere exposure.
9. Escalate when educational or institutional authority is required.
10. Keep grading, discipline, accommodations, and student records under human control.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F93 as a tutoring and academic-governance reference architecture. Validate content, course rules, assessment constraints, privacy requirements, accessibility needs, and escalation pathways against the actual learning environment before relying on the system. Final academic decisions remain with appropriately qualified and authorized humans.