from backend.agents.state import ResearchState, VerifiedFinding, VerifiedFinding


class ReportAgent:
    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "FACTCHECK_COMPLETED":
            return state

        if not state.verified_findings:
            state.errors.append("No verified findings available for report generation.")
            return state

        sections = []
        sections.append(f"# Research Report\n\nTopic: {state.query}")
        for topic, verified_finding in state.verified_findings.items():
            sections.append(f""" {topic}
{verified_finding.content}
Confidence Score: {verified_finding.confidence_score}""")

        state.report = "\n\n".join(sections)
        state.status = "COMPLETED"

        return state
