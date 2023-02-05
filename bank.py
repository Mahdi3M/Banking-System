import random
from datetime import datetime
from database import *


def generate_new_id(prefix):
    result = ""
    for i in range(6):
        random_number = random.randint(1,9)
        result += str(random_number)
    return int(prefix + result)


def register(*args):
    print()
    print("── Register──────────────────────────────────")
    print()
    cus_id = generate_new_id("")
    cus_name = input("Full Name: ")
    cus_phone = input("Phone Number: ")
    cus_email = input("Email: ")
    date_became_cus = datetime.today().strftime('%d-%m-%Y')
    not_done = True
    while not_done:
        user_name = input("User Name: ")
        if user_name == "":
            print("\nUser Name cannot be balnk.\n")
        else:
            not_done = args[0].check_user_names(user_name)
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


def create_account(*args):
    print()
    print("── Creating a new user ──────────────────────")
    print()
    acc_id = generate_new_id("1014")
    cus_id = args[1]
    acc_name = input("Account Name: ")
    date_open = datetime.today().strftime('%d-%m-%Y')
    balance = input("Balance: ")
    args[0].insert_acc(acc_id, cus_id, acc_name, date_open, balance)
    return args[1]


def perform_transaction(*args):
    print()
    print("── Requesting Transaction ───────────────────")
    print()
    tnx_id = generate_new_id("103")
    tnx_date = datetime.today().strftime('%d-%m-%Y')
    sender = input("Sender's Account Number: ")
    receiver = input("Recipient's Account Number: ")
    amount = input("Transaction Amount: ")
    args[0].perform_tnx(tnx_id, tnx_date, sender, receiver, amount)
    return args[1]


def update_user_info(*args):
    print()
    print("── Update User Info ─────────────────────────")
    print()
    print("--------------------")
    print("Press ENTER to skip.")
    print("--------------------")
    print()
    sdata = args[0].get_user_info(args[1])
    index = [1,2,3,5,6]
    column = ["cus_name", "cus_phone", "cus_email", "user_name", "password"]
    new_data = ["Full Name: ", "Phone Number: ", "Email: ", "User Name: ", "Password: "]
    for i in range(len(index)):
        print(new_data[i], sdata[0][index[i]])
        data = input("New {}".format(new_data[i]))
        if not data == "":
            args[0].update_user_info(column[i], data, args[1])
        print()
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
        print("{:<5}{:<15}{:<20}{:<15}{:<10}".format("Sr.","Account ID", "Account Name", "Date Created", "Balance"))
        print("{:<5}{:<15}{:<20}{:<15}{:<10}".format("---","----------", "------------", "------------", "-------"))
        for s in sdata:
            print("{:<5}{:<15}{:<20}{:<15}{:<10}".format(n, s[0], s[2], s[3], s[4]))
            n = n+1
    else:
        print("No account found.")
    return args[1]


def view_transaction_history(*args):
    print()
    print("── Transaction History ──────────────────────")
    print()
    acc_no = input("Account Number: ")
    print()
    sdata = args[0].get_tnx_info(acc_no)
    if sdata:
        n = 1
        print("{:<5}{:<20}{:<15}{:<15}{:<10}".format("Sr.","Transaction ID", "Date", "Type", "Amount"))
        print("{:<5}{:<20}{:<15}{:<15}{:<10}".format("---","--------------", "----------", "---------", "---------"))
        for s in sdata:
            tnx_type = "Sent" if s[3] == int(acc_no) else "Received"
            print("{:<5}{:<20}{:<15}{:<15}{:<10}".format(n, s[0], s[1], tnx_type, s[2]))
            n = n+1
    else:
        print("No account found.")
    return args[1]


def logout(*args):
    return None
