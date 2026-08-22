"""Fail-closed educational governance for F93 Student Tutor."""

PROTECTED_ACTIONS = {
    "final_grade",
    "disciplinary_action",
    "student_record_change",
    "external_submission",
    "accommodation_decision",
    "academic_integrity_finding",
}

REQUIRED_REVIEWS = (
    "learning_goal_reviewed",
    "learner_context_reviewed",
    "content_accuracy_reviewed",
    "practice_alignment_reviewed",
    "accessibility_reviewed",
    "privacy_reviewed",
    "safety_escalation_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding educational authority is outside tutor scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required tutoring review", "missing": missing}

    blockers = []
    if context.get("content_accuracy_gap"):
        blockers.append("instructional content accuracy unresolved")
    if context.get("practice_answer_leakage"):
        blockers.append("practice design leaks restricted answers")
    if context.get("assessment_integrity_risk"):
        blockers.append("academic or assessment integrity risk unresolved")
    if context.get("accessibility_gap"):
        blockers.append("learner accessibility need unresolved")
    if context.get("student_privacy_risk"):
        blockers.append("student privacy risk unresolved")
    if context.get("unsafe_escalation_gap"):
        blockers.append("required educator or safety escalation unresolved")
    if context.get("unsupported_learner_inference"):
        blockers.append("unsupported learner-specific inference detected")
    if context.get("overreliance_risk"):
        blockers.append("tutor behavior creates material overreliance risk")

    if blockers:
        return {"allowed": False, "reason": "student-tutoring governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "tutoring package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
