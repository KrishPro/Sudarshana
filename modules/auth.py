from modules import MASTER_PASSWORD
from cprint import cprint

def authenticate(inputed_password=None):
    inputed_password = inputed_password if inputed_password else str(input("Password: ")).strip()
    authenticated_user = MASTER_PASSWORD == inputed_password
    if not authenticated_user:
        cprint.fatal("ACCESS DENIED")
        print("Exitting...")
        exit()