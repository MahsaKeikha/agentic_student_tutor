from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
    return {
        "learning_goal_reviewed": True,
        "learner_context_reviewed": True,
        "content_accuracy_reviewed": True,
        "practice_alignment_reviewed": True,
        "accessibility_reviewed": True,
        "privacy_reviewed": True,
        "safety_escalation_reviewed": True,
        "human_approval": True,
    }


def test_complete_review_can_release_tutoring_package():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_grading_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_final_grade_is_never_autonomous():
    assert authorize("final_grade", valid_context())["allowed"] is False


def test_content_accuracy_gap_blocks_release():
    context = valid_context()
    context["content_accuracy_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_answer_leakage_blocks_release():
    context = valid_context()
    context["practice_answer_leakage"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_accessibility_gap_blocks_release():
    context = valid_context()
    context["accessibility_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_privacy_risk_blocks_release():
    context = valid_context()
    context["student_privacy_risk"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_required_escalation_gap_blocks_release():
    context = valid_context()
    context["unsafe_escalation_gap"] = True
    assert orchestrate(context)["release_allowed"] is False
