
from llm import generate_response


class PlannerAgent:

    def __init__(self):
        self.role = "Research Planner"
        self.goal = "Break a research topic into clear, actionable tasks."

    def plan(self, topic: str) -> str:

        prompt = f"""
        You are an expert {self.role}.

        Your goal is: {self.goal}

        Given the following research topic:
        {topic}

        Break this topic into 5 specific research tasks.

        Each task must:
        - Focus on one aspect of the topic.
        - Be clear and actionable.
        - Help answer the overall research question.

        Return the tasks as a numbered list.
        Do not write anything else.
        """

        response = generate_response(prompt)

        return response
