"""
IX-CerealKiller Core Reasoning Module

Contains the main logic for IX-CerealKiller AI, enhanced to utilize IX-Gibson
for domain-specific expert queries via GibsonAdapter.
"""

from .gibson_adapter import GibsonAdapter

class CerealKillerCore:
    def __init__(self):
        self.gibson_adapter = GibsonAdapter()

    def answer_query(self, question: str) -> str:
        """
        Process user query by offloading to IX-Gibson.

        Args:
            question (str): User input question.

        Returns:
            str: Answer from IX-Gibson or fallback error message.
        """
        response = self.gibson_adapter.query_gibson(question)
        if "error" in response:
            return f"[CerealKiller Error]: {response['error']}"
        return response.get("answer", "[CerealKiller]: No answer available.")
