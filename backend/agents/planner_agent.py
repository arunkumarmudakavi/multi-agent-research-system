from backend.agents.state import ResearchState, Task


class PlannerAgent:
    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "PENDING":
            return state

        query = state.query
        state.tasks = [
            Task(
                topic="Overview",
                description=f"Research overview of {query}"
            ),
            Task(
                topic="Benefits",
                description=f"Research benefits of {query}"
            ),
            Task(
                topic="Challenges",
                description=f"Research challenges of {query}"
            ),
            Task(
                topic="Future Trends",
                description=f"Research future trends of {query}"
            ),
        ]

        state.status = "PLANNING_COMPLETED"

        return state
