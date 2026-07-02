from collections import defaultdict
import time

from backend.agents.state import ResearchState, VerifiedFinding
from backend.factcheck.factcheck_client import FactCheckClient


class FactCheckAgent:
    def __init__(self, factcheck_client: FactCheckClient):
        self.factcheck_client = factcheck_client

    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "RESEARCH_COMPLETED":
            return state

        if not state.findings:
            state.errors.append("No findings available for fact-checking.")
            return state

        grouped_sources = defaultdict(list)

        for source in state.sources:
            grouped_sources[source.topic].append(source)

        verified_findings = {}
        # print("Grouped Sources:", grouped_sources)

        try:
            for topic, finding in state.findings.items():
                start = time.time()
                # print(f"Before verify() for topic: {topic}")
                verified_finding = self.factcheck_client.verify(
                    finding=finding,
                    sources=grouped_sources[topic],
                )
                # print(f"After verify() for topic: {topic}")
                end = time.time()
                print(f"Fact Check Verify Time taken {end - start:.2f} seconds")
                verified_findings[topic] = verified_finding
        except Exception as e:
            state.errors.append(str(e))
            return state

        state.verified_findings = verified_findings
        state.status = "FACTCHECK_COMPLETED"

        return state
