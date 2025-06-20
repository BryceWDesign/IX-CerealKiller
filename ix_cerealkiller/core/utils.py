"""
IX-CerealKiller Utility Functions

Provides text normalization and basic validation utilities
for forensic incident input processing.
"""

import re

def normalize_text(text: str) -> str:
    """
    Normalize input text by stripping whitespace and
    removing unwanted characters for consistent processing.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\-\.,]', '', text)
    return text

def is_valid_incident_report(text: str) -> bool:
    """
    Validates that the input text is suitable for forensic analysis.
    """
    return bool(text and len(text) > 10 and any(c.isalpha() for c in text))

# Example usage
if __name__ == "__main__":
    samples = [
        "  Possible ransomware encrypting files... ",
        "!!!",
        "",
        "DDoS detected at midnight"
    ]
    for sample in samples:
        normalized = normalize_text(sample)
        valid = is_valid_incident_report(normalized)
        print(f"Original: '{sample}' | Normalized: '{normalized}' | Valid: {valid}")
