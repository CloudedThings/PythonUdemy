import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter the name your looking for: ")
for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(row)

conn.close()
