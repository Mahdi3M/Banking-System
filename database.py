import sqlite3
from interface import *


class Database:
    def __init__(self, db):
        try:
            self.con = sqlite3.connect(db)
        except Exception:
            print("Database is not connected.")
            input("PRESS ENTER TO CONTINUE ")
            clean_terminal_screen()
            quit()
        else:
            self.cur = self.con.cursor()
            fd = open('table.sql', 'r')
            sql_file = fd.read()
            fd.close()

            sql_commands = sql_file.split(';')

            for command in sql_commands:
                try:
                    self.cur.execute(command)
                except Exception as msg:
                    print("Command skipped: ", msg)
            self.con.commit()

    def check_login(self, user_name, password):
        query = "SELECT * FROM customer WHERE user_name='" + user_name + "' AND password='" + password + "'"
        try:
            self.cur.execute(query)
            sdata = self.cur.fetchall()
            return sdata[0][0]
        except Exception:
            return None

    def check_user_names(self, user_name):
        query = "SELECT * FROM customer WHERE user_name='" + user_name + "'"
        try:
            self.cur.execute(query)
            sdata = self.cur.fetchall()
        except Exception:
            print("Error.")
        else:
            if len(sdata):
                print("\nUser name already taken.\n")
                return True
            else:
                return False

    def insert_cus(self, cus_id, cus_name, cus_phone, cus_email, date_became_cus, user_name, password):
        query = "INSERT INTO customer VALUES(?,?,?,?,?,?,?)"
        try:
            self.cur.execute(query,(cus_id, cus_name, cus_phone, cus_email, date_became_cus, user_name, password))
        except Exception:
            print("Could not insert into Customer.")
        else:
            self.con.commit()

    def insert_acc(self, acc_id, cus_id, acc_name, date, balance):
        query = "INSERT INTO account VALUES(?,?,?,?,?)"
        try:
            self.cur.execute(query, (acc_id, cus_id, acc_name, date, float(balance)))
        except Exception:
            print("Could not insert into Account.")
        else:
            self.con.commit()

    def perform_tnx(self, tnx_id, tnx_date, sender, receiver, amount):
        try:
            sender = int(sender)
            receiver = int(receiver)
            amount = float(amount)
        except Exception:
            print("Invalid input.")
        else:
            query = """ INSERT INTO transactions VALUES({},'{}',{},{},{});
                        UPDATE account SET balance=balance-{} WHERE acc_id={};
                        UPDATE account SET balance=balance+{} WHERE acc_id={};""".format(
                tnx_id, tnx_date, amount, sender, receiver, amount, sender, amount, receiver
            )
            queries = query.split(';')
            for i in queries:
                try:
                    self.cur.execute(i)
                except Exception:
                    print("Error During Update")
                else:
                    self.con.commit()

    def del_account(self, acc_id):
        try:
            acc_id = int(acc_id)
        except Exception:
            print("Invalid input.")
        else:
            query = "DELETE FROM account WHERE acc_id={}".format(acc_id)
            try:
                self.cur.execute(query)
            except Exception:
                print("Counld not delete the account.")
            else:
                if self.cur.rowcount:
                    self.con.commit()
                else:
                    print("Account not found.")

    def get_user_info(self, cus_id):
        query = "SELECT * FROM customer WHERE cus_id={}".format(cus_id)
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception:
            print("Error.")
            return None

    def get_acc_info(self, cus_id):
        query = "SELECT * FROM account WHERE cus_id={}".format(cus_id)
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception:
            print("Error.")
            return None

    def get_tnx_info(self, acc_id):
        try:
            acc_id = int(acc_id)
        except Exception:
            print("Invalid input.")
        else:
            query = "SELECT * FROM transactions WHERE acc_id_from={} OR acc_id_to={}".format(acc_id, acc_id)
            try:
                self.cur.execute(query)
                return self.cur.fetchall()
            except Exception:
                print("Error.")
                return None

    def update_user_info(self, col, data, cus_id):
        query = "UPDATE customer SET " + col + "='" + data + "' WHERE cus_id={}".format(cus_id)
        try:
            self.cur.execute(query)
        except Exception:
            print("Could not update {}".format(col))
        else:
            self.con.commit()
