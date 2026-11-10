
import json
from llm import generate_response


class PlannerAgent:
    def __init__(self):
        self.role = "Research Planner"
        self.goal = "Break a research topic into clear, actionable tasks."

    def plan(self, topic: str) -> dict:
        prompt = f"""
        You are an expert research planner.

        Research topic: {topic}

        Break this topic into exactly 5 specific research tasks.

        Return your response in this exact JSON structure:

        {{
            "topic": "{topic}",
            "tasks": [
                {{
                    "task_id": 1,
                    "description": "Research task description"
                }}
            ]
        }}

        Return valid JSON only.
        Do not include markdown formatting or explanations.
        """

        response = generate_response(prompt)

        try:
            plan = json.loads(response)
            return plan
        except json.JSONDecodeError:
            raise ValueError(
                f"Planner returned invalid JSON:\n{response}"
            )
