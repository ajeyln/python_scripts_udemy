import sqlite3

conn =  sqlite3.connect("contacts.sqlite")
name = input("Enter the name which you are searching for: ")

for row in conn.execute("SELECT * FROM contacts where name LIKE ?",(name,)):
    print(row)

conn.close()