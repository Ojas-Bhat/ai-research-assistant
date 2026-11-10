
from agents.researcher import ResearcherAgent

researcher = ResearcherAgent()

task = {
    "task_id": 1,
    "description": "Assess current adoption levels of AI technologies across Indian hospitals and primary healthcare centers."
}

result = researcher.research_task(task)

print("\nRESEARCH FINDINGS")
print("=" * 60)

print("\nTask:", result["task"])
print("\nSummary:")
print(result["summary"])

print("\nSources:")

for source in result["sources"]:
    print("-", source["title"])
    print(" ", source["url"])
