"""
Written by KrishPro @ KP
"""

from modules.query_manager import handle_query
from modules.auth import authenticate
import argparse

def repl():
    """
    Read-eval-print loop
    """
    while True:
        query = input("chakra> ")
        handle_query(query)


def main(args):
    authenticate(args.password)
    repl()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Sudarshana, The Chakra
    """)

    parser.add_argument('--password', '-p', type=str, default=None, required=False,
                        help='password is needed to unlock !')

    args = parser.parse_args()
    main(args)