from backend.agents.state import ResearchState, Source
from backend.search.search_client import SearchClient


class SearchAgent:
    def __init__(self, search_client: SearchClient):
        self.search_client = search_client

    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "PLANNING_COMPLETED":
            return state

        if not state.tasks:
            state.errors.append("No tasks found to search.")
            return state

        sources = []

        try:
            for task in state.tasks:
                sources.extend(self.search_client.search(task))
        except Exception as e:
            state.errors.append(str(e))
            return state

        state.sources = sources
        state.status = "SEARCH_COMPLETED"

        return state
