"""
IX-CerealKiller Query Processor

Handles forensic pattern queries and incident profiling requests,
leveraging core forensic analysis capabilities.
"""

from core.forensic_analysis import ForensicAnalysis

class IXCerealKillerQueryProcessor:
    def __init__(self):
        self.forensic = ForensicAnalysis()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("analyze incident"):
            # Expect the incident report after the command
            incident = query_lower[len("analyze incident"):].strip()
            if not incident:
                return "Please provide the incident report text after 'Analyze incident'."
            profile = self.forensic.profile_incident(incident)
            crimes = ', '.join(profile["crime_types"]) or "No known crime types detected"
            keywords = ', '.join(profile["keywords_found"]) or "No keywords matched"
            return f"Crime Types Detected: {crimes}\nKeywords Found: {keywords}"

        elif "what is" in query_lower or "define" in query_lower:
            return (
                "IX-CerealKiller specializes in analyzing forensic data patterns and profiling cybercrime incidents. "
                "Try queries like 'Analyze incident [text]' to get started."
            )
        else:
            return (
                "IX-CerealKiller cannot process that query. Please ask forensic analysis-related questions "
                "or use 'Analyze incident [text]' for incident profiling."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXCerealKillerQueryProcessor()
    print(qp.process_query("Analyze incident Possible ransomware encrypting files"))
    print(qp.process_query("What is forensic analysis?"))
