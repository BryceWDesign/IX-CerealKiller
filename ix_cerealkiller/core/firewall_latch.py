"""
IX-CerealKiller Firewall Latch

Implements a runtime firewall latch system that monitors incoming queries,
blocks suspicious inputs flagged by anomaly detectors, and isolates compromised sessions.
"""

import threading
from typing import Set

class FirewallLatch:
    def __init__(self):
        self.locked_sessions: Set[str] = set()
        self.lock = threading.Lock()

    def lock_session(self, session_id: str):
        with self.lock:
            self.locked_sessions.add(session_id)
            print(f"[!] Session {session_id} locked due to anomaly detection")

    def unlock_session(self, session_id: str):
        with self.lock:
            if session_id in self.locked_sessions:
                self.locked_sessions.remove(session_id)
                print(f"[+] Session {session_id} unlocked")

    def is_locked(self, session_id: str) -> bool:
        with self.lock:
            return session_id in self.locked_sessions

# Example usage
if __name__ == "__main__":
    latch = FirewallLatch()
    session = "session_1234"
    latch.lock_session(session)
    print(f"Is session locked? {latch.is_locked(session)}")
    latch.unlock_session(session)
    print(f"Is session locked? {latch.is_locked(session)}")
