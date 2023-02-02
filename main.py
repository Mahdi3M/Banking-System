# ─── IMPORTS ────────────────────────────────────────────────────────────────────

# import math
# import json
# import random
# from os.path import exists
from bank import *
from database import *


# ─── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    mydb = Database("bank")
    while True:
        choice = display_menu()
        action = {
            1: create_account,
            2: perform_transaction,
            3: update_account_info,
            4: delete_account,
            5: search_account_info,
            6: view_customer_list,
            7: exit_system,
        }

        try:
            action_taken = action[int(choice)]
        except Exception:
            print("Invalid Command. Please choose between 1-7.")
        else:
            action_taken(mydb)

        print()
        print_horizontal_line()
        input("PRESS ENTER TO CONTINUE ")
        print()
