"""
IX-CerealKiller CLI Interface

Command-line interface to interact with the forensic incident analysis module.
"""

import sys
from core.query_processor import IXCerealKillerQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Analyze incident [your incident report]\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXCerealKillerQueryProcessor()
    response = processor.process_query(query)

    print("\n🕵️ IX-CerealKiller Response 🕵️")
    print(response)

if __name__ == "__main__":
    main()
