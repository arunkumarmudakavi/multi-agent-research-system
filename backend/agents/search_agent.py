from backend.agents.state import ResearchState, Source


class SearchAgent:
    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "PLANNING_COMPLETED":
            return state

        if not state.tasks:
            state.errors.append("No tasks found to search.")
            return state

        sources = []

        for task in state.tasks:
            sources.append(
                Source(
                    topic=task.topic,
                    title=task.description,
                    url=f"https://example.com/{task.description.replace(' ', '-').lower()}",
                    content=f"This is the content for {task.description} .",
                )
            )

        state.sources = sources
        state.status = "SEARCH_COMPLETED"

        return state
