from backend.agents.state import ResearchState, VerifiedFinding


class FactCheckAgent:
    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "RESEARCH_COMPLETED":
            return state

        if not state.findings:
            state.errors.append("No findings available for fact-checking.")
            return state

        verified_findings = {}
        for topic, finding in state.findings.items():
            verified_finding = VerifiedFinding(
                topic=topic,
                content=finding.content,
                confidence_score=0.9  # Assuming a fixed confidence score for demonstration
            )
            verified_findings[topic] = verified_finding

        state.verified_findings = verified_findings
        state.status = "FACTCHECK_COMPLETED"

        return state