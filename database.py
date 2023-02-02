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
            sql = """CREATE TABLE IF NOT EXISTS account
            (account_number INT primary key,user_name TEXT,date TEXT,gender TEXT,balance FLOAT,city TEXT,phone TEXT)
            """
            self.cur.execute(sql)
            self.con.commit()

    def insert(self, acc_no, user_name, date, gender, balance, city, phn_no):
        query = "INSERT INTO account VALUES({},'{}','{}','{}',{},'{}','{}')".format(
            acc_no, user_name, date, gender, balance, city, phn_no
        )
        self.cur.execute(query)
        self.con.commit()