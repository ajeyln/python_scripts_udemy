import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number:")

# update_sql = "UPDATE contacts SET email = 'rad@email.com' WHERE contacts.phone =456"
update_sql = "UPDATE contacts SET email=? WHERE phone=?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql,(new_email,phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.close()
for name, phone, email in db.execute("Select * from contacts"):
    print("Name: {} ".format(name))
    print("Phone: {} ".format(phone))
    print("Email: {} ".format(email))
    print("*" * 120)

db.close()