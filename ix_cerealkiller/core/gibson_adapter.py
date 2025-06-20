"""
IX-CerealKiller Gibson Adapter

Enables communication between IX-CerealKiller AI and IX-Gibson central knowledge system.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.api_url = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, question: str) -> dict:
        """
        Query IX-Gibson with the given question and return JSON response.

        Args:
            question (str): The question string.

        Returns:
            dict: Response JSON or error details.
        """
        payload = {
            "domain": "cerealkiller",
            "question": question,
            "from": "ix-cerealkiller"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.api_url, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Gibson HTTP {response.status_code}: {response.text}")
            except requests.RequestException as e:
                print(f"Gibson request error attempt {attempt}: {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Failed to communicate with IX-Gibson after retries."}
