import sqlite3

with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    #  query = """CREATE TABLE IF NOT  EXISTS expenses(id INTEGER,name TEXT)"""
    query1 = """INSERT into expenses (id,name) values (1,"Коммуналка")"""
    query2 = """INSERT into expenses (id,name) values (2,"Бензин")"""
    query3 = """INSERT into expenses (id,name) values (3,"Интернет")"""
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()