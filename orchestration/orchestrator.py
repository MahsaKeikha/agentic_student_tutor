from AGENTS.explanation_designer_agent import run as explanation
from AGENTS.learning_diagnostician_agent import run as diagnostician
from AGENTS.practice_generator_agent import run as practice
from AGENTS.progress_reviewer_agent import run as progress
from AGENTS.safety_escalation_agent import run as escalation
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run tutoring specialists and apply fail-closed educational governance."""
    results = [
        diagnostician(context),
        explanation(context),
        practice(context),
        progress(context),
        escalation(context),
    ]
    governance = authorize("tutoring_release", context)
    return {
        "system": "F93",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_grading_authority": False,
        "autonomous_disciplinary_authority": False,
    }
