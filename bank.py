import random
from datetime import datetime
from database import *


def generate_new_account_number():
    result = ""
    for i in range(6):
        random_number = random.randint(1,9)
        result += str(random_number)
    return "1014" + result


def create_account(db):
    print("── Creating a new user ──────────────────────")
    acc_no = int(generate_new_account_number())
    user_name = input("Full Name: ")
    date = datetime.today().strftime('%d-%m-%Y')
    balance = float(input("Balance: "))
    gender = input("Gender: ")
    city = input("City of Residence: ")
    phn_no = input("Phone Number: ")
    db.insert(acc_no, user_name, date, gender, balance, city, phn_no)


def perform_transaction(db):
    print("Transaction Complete")


def update_account_info(db):
    print("Account Updated")


def delete_account(db):
    print("Account Deleted")


def search_account_info(db):
    print("Account Info:")


def view_customer_list(db):
    print("Customer List:")


def exit_system(db):
    clean_terminal_screen()
    quit()


def display_menu():
    """
        Displays the welcome menu and asks the user for a
        command to perform (which then performs).
        This also acts as the UI and receives the information
        regarding of the respective functions.
        """
    clean_terminal_screen()

    print()

    print("  ┌────────────────┐  ╭───────────────────────╮           ")
    print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Create Account  │           ")
    print("  │  ╰┼┼╮          │  ├───────────────────────┴─────╮     ")
    print("  │  ╰┼┼╯          │  │ ▶︎ 2 • Perform Transaction   │     ")
    print("  │                │  ├────────────────────────────┬╯     ")
    print("  │  D R A G O N   │  │ ▶︎ 3 • Update Account Info  │      ")
    print("  │  B A N K       │  ├───────────────────────┬────╯      ")
    print("  │                │  │ ▶︎ 4 • Delete Account  │           ")
    print("  │                │  ├───────────────────────┴────╮      ")
    print("  │                │  │ ▶︎ 5 • Search Account Info  │      ")
    print("  │                │  ├────────────────────────────┴╮     ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 6 • View Customer's List  │     ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ├────────────────────┬────────╯     ")
    print("  │                │  │ ▶︎ 7 • Exit System  │              ")
    print("  └────────────────┘  ╰────────────────────╯              ")

    user_choice = input("\n  ☞ Enter your command: ")

    return user_choice
