import random
from datetime import datetime
from database import *


def generate_new_customer_id():
    result = ""
    for i in range(6):
        random_number = random.randint(1,9)
        result += str(random_number)
    return int(result)


def register(*args):
    cus_id = generate_new_customer_id()
    print(cus_id)
    cus_name = input("Full Name: ")
    cus_phone = input("Phone Number: ")
    cus_email = input("Email: ")
    date_became_cus = datetime.today().strftime('%d-%m-%Y')
    user_name = input("User Name: ")
    password = input("Password: ")
    args[0].insert_cus(cus_id, cus_name, cus_phone, cus_email, date_became_cus, user_name, password)
    return None


def login(*args):
    print()
    print("── Login ────────────────────────────────────")
    print()
    user_name = input("Enter User name: ")
    password = input("Enter Password: ")
    cus_id = args[0].check_login(user_name, password)
    if cus_id:
        return cus_id
    else:
        print("Wrong username or Password!!")
        return None


def exit_system(*args):
    clean_terminal_screen()
    quit()


def generate_new_account_number():
    result = ""
    for i in range(6):
        random_number = random.randint(1,9)
        result += str(random_number)
    return int("1014" + result)


def create_account(*args):
    print()
    print("── Creating a new user ──────────────────────")
    print()
    acc_id = generate_new_account_number()
    cus_id = args[1]
    acc_name = input("Account Name: ")
    date_open = datetime.today().strftime('%d-%m-%Y')
    balance = float(input("Balance: "))
    args[0].insert_acc(acc_id, cus_id, acc_name, date_open, balance)
    return args[1]


def perform_transaction(*args):
    print()
    print("── Requesting Transaction ───────────────────")
    print()
    tnx_id = int("123"+ str(generate_new_customer_id()))
    tnx_date = datetime.today().strftime('%d-%m-%Y')
    sender = int(input("Sender's Account Number: "))
    receiver = int(input("Recipient's Account Number: "))
    amount = float(input("Transaction Amount: "))
    args[0].perform_tnx(tnx_id, tnx_date, sender, receiver, amount)
    return args[1]


def update_user_info(*args):
    print("Account Updated")
    return args[1]


def delete_account(*args):
    print()
    print("── Delete Account ───────────────────────────")
    print()
    acc_no = input("Account Number: ")
    args[0].del_account(acc_no)
    return args[1]


def search_account_info(*args):
    print()
    print("── Account Info ─────────────────────────────")
    print()
    sdata = args[0].get_acc_info(args[1])
    if sdata:
        n = 1
        print("{:<5}{:<15} {:<20} {:<15} {:<10}".format("Sr.","Account ID", "Account Name", "Date Created", "Balance"))
        print("{:<5}{:<15} {:<20} {:<15} {:<10}".format("---","----------", "------------", "------------", "-------"))
        for s in sdata:
            print("{:<5}{:<15} {:<20} {:<15} {:<10}".format(n, s[0], s[2], s[3], s[4]))
            n = n+1
    else:
        print("No account found.")
    return args[1]


def view_transaction_history(*args):
    print("Customer List:")
    return args[1]


def logout(*args):
    return None
