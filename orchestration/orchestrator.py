from AGENTS.learning_diagnostician_agent import run as a
from AGENTS.explanation_designer_agent import run as b
from AGENTS.practice_generator_agent import run as c
from AGENTS.progress_reviewer_agent import run as d
from AGENTS.safety_escalation_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
