import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@gmail.com"
phone = input("Please enter the phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))

print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()
