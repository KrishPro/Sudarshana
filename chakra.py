"""
Written by KrishPro @ KP
"""

from modules.auth import authenticate
import argparse

def main(args):
    authenticate(args.password)
    print("Welcome to Sudarshana")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Sudarshana, The Chakra
    """)

    parser.add_argument('--password', '-p', type=str, default=None, required=False,
                        help='password is needed to unlock !')

    args = parser.parse_args()
    main(args)