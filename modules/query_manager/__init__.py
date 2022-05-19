"""
Written by KrishPro @ KP
"""

from modules.help import show_help
import subprocess


def handle_query(query: str):
    if query.strip() == "": return
    
    elif basic_commands(query):
        return

    elif cli_commands(query):
        return

    elif query.strip().lower() == "help":
        show_help()


    


def cli_commands(query):
    basic_cli_commands = ["ls", "bash", "pwd", "git", "pip", "conda"]

    def execute(command):
        try:
            subprocess.call([command])
        except:
            subprocess.call(command.split())

    if query[0] == "!":
        execute(query[1:])
        return True
    elif query.split(" ")[0] in basic_cli_commands:
        execute(query)
        return True

    return False


def basic_commands(query: str):
    q = query.strip().lower()

    if (q == "exit") or (q == "quit"):
        print("Exitting...")
        exit()
    
    elif (q == "cls") or (q == "clear"):
        subprocess.call(['cls'])
        return True

    return False