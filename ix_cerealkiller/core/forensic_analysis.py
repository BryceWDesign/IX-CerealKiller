"""
IX-CerealKiller Core Forensic Analysis Module

Provides advanced data pattern recognition and cybercrime profiling
to assist in forensic investigations and threat attribution.
"""

import re
from typing import List, Dict

class ForensicAnalysis:
    def __init__(self):
        # Basic known patterns for cybercrime signature detection
        self.patterns = {
            "ransomware": ["encrypt", "decrypt", "ransom", "payment", "bitcoin", "wallet"],
            "phishing": ["credential", "login", "verify", "account", "password", "security alert"],
            "ddos": ["traffic spike", "denial", "service unavailable", "botnet"],
            "data leak": ["exposed", "confidential", "personal data", "breach", "leak"]
        }

    def detect_patterns(self, text: str) -> List[str]:
        """
        Scan the input text for known forensic patterns.
        Returns a list of matched crime types.
        """
        text_lower = text.lower()
        matches = []
        for crime, keywords in self.patterns.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                    matches.append(crime)
                    break
        return matches

    def profile_incident(self, incident_report: str) -> Dict[str, List[str]]:
        """
        Analyze an incident report and return crime type classification
        and detected keywords for profiling.
        """
        matched_crimes = self.detect_patterns(incident_report)
        found_keywords = []
        for crime in matched_crimes:
            found_keywords.extend(self.patterns[crime])
        return {
            "crime_types": matched_crimes,
            "keywords_found": found_keywords
        }

# Standalone test
if __name__ == "__main__":
    fa = ForensicAnalysis()
    report = "We detected a traffic spike indicating a possible denial of service attack."
    print(fa.profile_incident(report))
