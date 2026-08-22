from orchestration.orchestrator import orchestrate


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "content_accuracy_gap": True}, False),
    ({**base(), "practice_answer_leakage": True}, False),
    ({**base(), "assessment_integrity_risk": True}, False),
    ({**base(), "accessibility_gap": True}, False),
    ({**base(), "student_privacy_risk": True}, False),
    ({**base(), "unsupported_learner_inference": True}, False),
    ({**base(), "overreliance_risk": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
