import sqlite3

db = sqlite3.connect('myDB.db')
cur = db.cursor()
cur.execute("drop table if exists test")
cur.execute("""
    create table test(
    string TEXT,
    number INT
    )""")
cur.execute('insert into test(string, number) values("one",1)')
cur.execute('insert into test(string, number) values("two",2)')
cur.execute('insert into test(string, number) values("three",3)')
cur.execute("SELECT * FROM test")
print(cur.fetchall())
db.close

