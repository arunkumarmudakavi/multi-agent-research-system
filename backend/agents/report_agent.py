from backend.agents.state import ResearchState, VerifiedFinding, VerifiedFinding


class ReportAgent:
    def execute(self, state: ResearchState) -> ResearchState:
        if state.status != "FACTCHECK_COMPLETED":
            return state

        if not state.verified_findings:
            state.errors.append("No verified findings available for report generation.")
            return state

        report = []
        report.append("# Research Report\n")
        report.append("## Research Topic\n")
        report.append(f"{state.query}\n")
        report.append("")

        confidence_scores = []

        for finding in state.verified_findings.values():
            report.append(f"## {finding.topic}")
            report.append("")
            report.append(finding.content)
            report.append("")
            report.append(f"**Confidence Score:** {finding.confidence_score:.2f}\n")
            report.append("")
            confidence_scores.append(finding.confidence_score)

        if confidence_scores:
            overall_confidence = sum(confidence_scores) / len(confidence_scores)
            report.append("## Overall Confidence\n")
            report.append(f"{overall_confidence:.2f}")

        state.report = "\n".join(report)
        state.status = "COMPLETED"

        return state
