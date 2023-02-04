import os


def clean_terminal_screen():
    """
    Cleans the terminal screen by performing a system
    clear command. Cls on windows and Clear on UNIX ones.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_horizontal_line():
    """
    A pretty decorative horizontal line.
    """
    print("─────────────────────────────────────────────")


def display_login_menu():
    """
        Displays the welcome menu and asks the user for a
        command to perform (which then performs).
        This also acts as the UI and receives the information
        regarding of the respective functions.
        """
    clean_terminal_screen()

    print()

    print("  ┌────────────────┐  ╭──────────────╮         ")
    print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Login  │         ")
    print("  │  ╰┼┼╮          │  ├──────────────┴──╮      ")
    print("  │  ╰┼┼╯          │  │ ▶︎ 2 • Register  │      ")
    print("  │                │  ├─────────────────┴──╮   ")
    print("  │  D R A G O N   │  │ ▶︎ 3 • Exit System  │   ")
    print("  │  B A N K       │  ╰────────────────────╯   ")
    print("  │                │                           ")
    print("  │                │                           ")
    print("  │                │                           ")
    print("  │                │                           ")
    print("  │ ║│┃┃║║│┃║│║┃│  │                           ")
    print("  │ ║│┃┃║║│┃║│║┃│  │                           ")
    print("  │                │                           ")
    print("  └────────────────┘                           ")

    user_choice = input("\n  ☞ Enter your command: ")

    return 1, user_choice


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
    print("  │                │  ├─────────────────────────┬───╯     ")
    print("  │  D R A G O N   │  │ ▶︎ 3 • Update User Info  │         ")
    print("  │  B A N K       │  ├───────────────────────┬─╯         ")
    print("  │                │  │ ▶︎ 4 • Delete Account  │           ")
    print("  │                │  ├───────────────────────┴──╮        ")
    print("  │                │  │ ▶︎ 5 • View Account Info  │        ")
    print("  │                │  ├──────────────────────────┴──────╮ ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 6 • View Transaction History  │ ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ├───────────────┬─────────────────╯ ")
    print("  │                │  │ ▶︎ 7 • Logout  │                   ")
    print("  └────────────────┘  ╰───────────────╯                   ")

    user_choice = input("\n  ☞ Enter your command: ")

    return 2, user_choice