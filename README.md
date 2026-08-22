# F93 | Agentic Student Tutor | L3 Gold Standard | v1.0

A governed multi-agent tutoring reference system for learning-goal analysis, misconception detection, adaptive explanation, practice generation, progress review, and escalation to a qualified human educator when needed.

## Five-agent architecture

- Learning Diagnostician
- Explanation Designer
- Practice Generator
- Progress Reviewer
- Safety and Escalation

## Gold-standard tutoring governance

F93 is fail closed. Tutoring release requires reviewed learning goals and learner context, content-accuracy review, practice alignment, accessibility review, privacy review, safety-escalation review, and explicit qualified-human approval.

Release is blocked for instructional accuracy gaps, answer leakage, assessment-integrity risks, unresolved accessibility needs, student privacy risks, missing educator or safety escalation, unsupported learner-specific inference, or material overreliance risk.

The reference system cannot autonomously assign final grades, impose discipline, change student records, decide accommodations, make academic-integrity findings, or submit externally on behalf of a student or institution.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out tutoring-governance suite.
