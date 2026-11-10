
from llm import generate_response
from tools.web_search import search_web


class ResearcherAgent:

    def __init__(self):
        self.role = "Research Analyst"

    def research_task(self, task: dict) -> dict:

        print(f"\nResearching: {task['description']}")

        # Step 1: Search the web
        search_results = search_web(task["description"])

        # Step 2: Prepare the search results
        context = ""

        for i, result in enumerate(search_results, start=1):
            context += f"""
            Source {i}
            Title: {result['title']}
            URL: {result['url']}
            Content: {result['content']}
            """

        # Step 3: Ask the LLM to analyse the results
        prompt = f"""
        You are an expert research analyst.

        Research task:
        {task['description']}

        Below are the web search results:

        {context}

        Instructions:
        1. Summarise the important findings.
        2. Identify important facts and statistics.
        3. Mention any limitations or missing information.
        4. Use only information supported by the provided sources.
        5. Do not invent statistics or citations.

        Write a clear and detailed research summary.
        """

        summary = generate_response(prompt)

        # Step 4: Return the research output
        return {
            "task_id": task["task_id"],
            "task": task["description"],
            "summary": summary,
            "sources": [
                {
                    "title": result["title"],
                    "url": result["url"]
                }
                for result in search_results
            ]
        }
