"""
IX-CerealKiller CLI Interface

Provides an interactive command-line interface for malware and cybersecurity
queries routed through CerealKillerCore to IX-Gibson.
"""

from core.cerealkiller_core import CerealKillerCore

def run_cerealkiller_cli():
    core = CerealKillerCore()
    print("IX-CerealKiller — Cybersecurity Threats and Malware Analysis Specialist")
    print("Enter your queries below. Type 'exit' to quit.\n")

    while True:
        user_input = input("CerealKiller> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-CerealKiller interface. Stay vigilant.")
            break
        output = core.handle_query(user_input)
        print(f"→ {output}")

if __name__ == "__main__":
    run_cerealkiller_cli()
