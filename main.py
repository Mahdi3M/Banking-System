# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from bank import *
from database import *
from interface import *


# ─── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    mydb = Database("bank")
    logged_cus_id = None
    while True:
        page, choice = display_menu() if logged_cus_id else display_login_menu()
        action = {
            (1,1): login,
            (1,2): register,
            (1,3): exit_system,
            (2,1): create_account,
            (2,2): perform_transaction,
            (2,3): update_user_info,
            (2,4): delete_account,
            (2,5): search_account_info,
            (2,6): view_transaction_history,
            (2,7): logout,
        }

        try:
            action_taken = action[(page, int(choice))]
        except Exception:
            print("Invalid Command.")
        else:
            logged_cus_id = action_taken(mydb, logged_cus_id)

        print()
        print_horizontal_line()
        input("PRESS ENTER TO CONTINUE ")
        print()
