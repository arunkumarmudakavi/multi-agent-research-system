import json
import time

from backend.agents.state import ResearchState, Task
from backend.llm.prompts.planner_prompt import PLANNER_PROMPT


class PlannerAgent:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "PENDING":
            return state

        prompt = PLANNER_PROMPT.format(query=state.query)

        # start = time.time()
        response = self.llm_client.generate(prompt)
        # end = time.time()

        # print(f"Time taken {end - start:.2f} seconds")
        # print("res: ", response)

        try:
            topics = json.loads(response)
        except json.JSONDecodeError:
            state.errors.append("Failed to parse planner response.")
            return state

        tasks = []

        for topic in topics:
            tasks.append(
                Task(topic=topic, description=f"Research {topic} of {state.query}")
            )

        state.tasks = tasks
        state.status = "PLANNING_COMPLETED"

        return state
