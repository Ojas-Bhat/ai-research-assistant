
from agents.planner import PlannerAgent

planner = PlannerAgent()

research_topic = "Impact of artificial intelligence on healthcare in India"

plan = planner.plan(research_topic)

print("\nRESEARCH PLAN")
print("=" * 50)
print(plan)
