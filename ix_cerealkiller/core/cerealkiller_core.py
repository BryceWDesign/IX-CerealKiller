"""
IX-CerealKiller Core Module

Handles queries related to cybersecurity threats and malware analysis,
leveraging IX-Gibson for domain expertise.
"""

from .gibson_adapter import GibsonAdapter

class CerealKillerCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def handle_query(self, query: str) -> str:
        """
        Send a query to IX-Gibson and return malware-focused response.

        Args:
            query (str): User input related to cybersecurity threats.

        Returns:
            str: Answer or error message.
        """
        response = self.gibson.query_gibson(query)
        if "error" in response:
            return f"[CerealKiller Error] {response['error']}"
        return response.get("answer", "[CerealKiller] No answer available.")
