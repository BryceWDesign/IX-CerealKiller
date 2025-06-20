"""
IX-CerealKiller User Interface

Handles user interaction via command line, routing queries to CerealKillerCore,
which communicates with IX-Gibson for expert responses.
"""

from core.cerealkiller_core import CerealKillerCore

def run_cerealkiller_cli():
    core = CerealKillerCore()
    print("IX-CerealKiller AI — Enter your question or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye from IX-CerealKiller!")
            break
        answer = core.answer_query(user_input)
        print(f"CerealKiller: {answer}")

if __name__ == "__main__":
    run_cerealkiller_cli()
