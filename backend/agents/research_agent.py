from backend.agents.state import Finding, ResearchState


class ResearchAgent:
    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "SEARCH_COMPLETED":
            return state

        if not state.sources:
            state.errors.append("No sources found to research.")
            return state

        findings = {}
        for source in state.sources:
            finding = Finding(
                topic=source.topic,
                content=(
                    f"Research findings generated " f"from source: {source.title}"
                ),
            )
            findings[source.topic] = finding

        state.findings = findings
        state.status = "RESEARCH_COMPLETED"

        return state
