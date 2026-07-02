from collections import defaultdict
import time

from backend.agents.state import Finding, ResearchState
from backend.research.research_client import ResearchClient


class ResearchAgent:
    def __init__(self, research_client: ResearchClient):
        self.research_client = research_client

    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "SEARCH_COMPLETED":
            return state

        if not state.sources:
            state.errors.append("No sources available for research.")
            return state

        grouped_sources = defaultdict(list)

        for source in state.sources:
            grouped_sources[source.topic].append(source)

        findings = {}
        try:
            for topic, sources in grouped_sources.items():
                # start = time.time()
                summary = self.research_client.summarize(topic=topic, sources=sources)
                # end = time.time()

                # print(f"Research summarize Time taken {end - start:.2f} seconds")

                findings[topic] = Finding(topic=topic, content=summary)
        except Exception as e:
            state.errors.append(str(e))
            return state

        state.findings = findings
        state.status = "RESEARCH_COMPLETED"

        return state
