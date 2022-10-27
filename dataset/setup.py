import sqlite3

connection = sqlite3.connect("football_players_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Messi')")
cursor.execute("insert into list (description) values ('Ronaldo')")
cursor.execute("insert into list (description) values ('Mbappe')")
cursor.execute("insert into list (description) values ('Neymer')")

connection.commit()
connection.close()

print("hello")
