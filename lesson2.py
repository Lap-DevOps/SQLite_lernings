import sqlite3
import datetime

with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS payments(
            id INTEGER,
            amount REAL,
            payments_date INTEGER,
            expense_id INTEGER)
            """
    cursor.execute(query)
    db.commit()


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))


def get_data(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


insert_payments = [
    (1, 120, get_timestamp(2020, 9, 1), 1),
    (2, 12, get_timestamp(2020, 9, 2), 3),
    (3, 120, get_timestamp(2020, 9, 3), 2),
    (4, 120, get_timestamp(2020, 9, 4), 2),
    (5, 120, get_timestamp(2020, 9, 5), 2),
    (6, 120, get_timestamp(2020, 9, 6), 2),
    (7, 120, get_timestamp(2020, 9, 7), 2),
]

with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS payments(
            id INTEGER,
            amount REAL,
            payments_date INTEGER,
            expense_id INTEGER
            """

# with sqlite3.connect("db/database.db") as db:
#     cursor = db.cursor()
#     query = """INSERT INTO payments (id,amount, payments_date, expense_id)
#                                     VALUES(?,?,?,?)
#                                     """
#     cursor.executemany(query, insert_payments)
#     db.commit()
#     print("Строк добавлено", cursor.rowcount)


with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    query = """SELECT * FROM payments"""
    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[1]
        print(res)
    print(sum)

with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    query = """SELECT amount, payments_date, name FROM payments JOIN expenses
                ON expenses.id=payments.expense_id WHERE expense_id =2"""
    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[0]
        print(res, get_data(res[1]))
    print(sum)

with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    query = """SELECT amount, payments_date, name FROM payments JOIN expenses
                ON expenses.id=payments.expense_id 
                WHERE (payments_date > %(from)d)
                AND (payments_date <%(to)d)""" % {"from": get_timestamp(2020, 9, 2), "to": get_timestamp(2020, 9, 4)}
    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[0]
        print(res, get_data(res[1]))
    print(sum)
