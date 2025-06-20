"""
IX-CerealKiller Gibson Adapter

Facilitates communication with IX-Gibson, allowing CerealKiller to
forward queries and receive domain-specific insights.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.endpoint = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, query: str) -> dict:
        """
        Send a query to IX-Gibson and return parsed JSON response.

        Args:
            query (str): User or system query string.

        Returns:
            dict: Parsed response or error information.
        """
        payload = {
            "domain": "cerealkiller",
            "query": query,
            "source": "ix-cerealkiller"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.endpoint, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"[CerealKiller HTTP {response.status_code}] {response.text}")
            except requests.RequestException as e:
                print(f"[CerealKiller] Gibson request error (attempt {attempt}): {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Failed to retrieve response from IX-Gibson after retries."}
