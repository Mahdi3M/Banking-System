CREATE TABLE IF NOT EXISTS customer(
    cus_id INT primary key,
    cus_name TEXT,
    cus_phone TEXT,
    cus_email TEXT,
    date_became_cus TEXT,
    user_name TEXT,
    password TEXT);

CREATE TABLE IF NOT EXISTS account(
    acc_id INT primary key,
    cus_id INT,
    acc_name TEXT,
    date_open TEXT,
    balance FLOAT);

CREATE TABLE IF NOT EXISTS transactions(
    txn_id INT primary key,
    txt_date TEXT,
    txn_amount FLOAT,
    acc_id_from INT,
    acc_id_to INT);

ALTER TABLE account ADD FOREIGN KEY (cus_id) REFERENCES customer (cus_id);
ALTER TABLE transactions ADD FOREIGN KEY (acc_id_from) REFERENCES account (acc_id);
ALTER TABLE transactions ADD FOREIGN KEY (acc_id_to) REFERENCES account (acc_id);