from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "learning_goal": "support mastery through guided tutoring",
    "learning_goal_reviewed": True,
    "learner_context_reviewed": True,
    "content_accuracy_reviewed": True,
    "practice_alignment_reviewed": True,
    "accessibility_reviewed": True,
    "privacy_reviewed": True,
    "safety_escalation_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
