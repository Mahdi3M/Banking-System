CREATE TABLE IF NOT EXISTS customer(
    cus_id INTEGER primary key,
    cus_name TEXT,
    cus_phone TEXT,
    cus_email TEXT,
    date_became_cus TEXT,
    user_name TEXT,
    password TEXT);

CREATE TABLE IF NOT EXISTS account(
    acc_id INTEGER primary key,
    cus_id INTEGER,
    acc_name TEXT,
    date_open TEXT,
    balance REAL);

CREATE TABLE IF NOT EXISTS transactions(
    txn_id INTEGER primary key,
    txt_date TEXT,
    txn_amount REAL,
    acc_id_from INTEGER,
    acc_id_to INTEGER);

ALTER TABLE account ADD FOREIGN KEY (cus_id) REFERENCES customer (cus_id);
ALTER TABLE transactions ADD FOREIGN KEY (acc_id_from) REFERENCES account (acc_id);
ALTER TABLE transactions ADD FOREIGN KEY (acc_id_to) REFERENCES account (acc_id);