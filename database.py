import mysql.connector
from interface import *


class Database:
    def __init__(self, db):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Lightyagami",
                database=db
            )
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
        try:
            query = "SELECT * FROM customer WHERE user_name='"+user_name+"' AND password='"+password+"'"
            self.cur.execute(query)
            sdata = self.cur.fetchall()
            return sdata[0][0]
        except Exception:
            return None


    def insert_cus(self, cus_id, cus_name, cus_phone, cus_email, date_became_cus, user_name, password):
        query = "INSERT INTO customer VALUES({},'{}','{}','{}','{}','{}','{}')".format(
            cus_id, cus_name, cus_phone, cus_email, date_became_cus, user_name, password
        )
        self.cur.execute(query)
        self.con.commit()


    def insert_acc(self, acc_id, cus_id, acc_name, date, balance):
        query = "INSERT INTO account VALUES({},{},'{}','{}',{})".format(
            acc_id, cus_id, acc_name, date, balance
        )
        self.cur.execute(query)
        self.con.commit()


    def perform_tnx(self, tnx_id, tnx_date, sender, receiver, amount):
        query = """ INSERT INTO transactions VALUES({},'{}',{},{},{});
                    UPDATE account SET balance=balance-{} WHERE acc_id={};
                    UPDATE account SET balance=balance+{} WHERE acc_id={};""".format(
            tnx_id, tnx_date, amount, sender, receiver, amount, sender, amount, receiver
        )
        queries = query.split(';')
        for i in queries:
            self.cur.execute(i)
            self.con.commit()

    def del_account(self, acc_id):
        query = "DELETE FROM account WHERE acc_id={}".format(acc_id)
        self.cur.execute(query)
        if self.cur.rowcount:
            self.con.commit()
        else:
            print("Account not found.")


    def get_acc_info(self, cus_id):
        try:
            query =  "SELECT * FROM account WHERE cus_id={}".format(cus_id)
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception:
            return None