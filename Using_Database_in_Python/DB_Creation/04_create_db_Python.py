import sqlite3

# Creating data base "contacts"
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)") # If table contacts was not created
db.execute("INSERT INTO contacts(name,phone,email) VALUES ('Ajey',123,'aj@email.com')")
db.execute("INSERT INTO contacts VALUES ('Radha',456,'rd@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

#for name, phone, email in cursor:
#    print("Name: {} ".format(name))
#    print("Phone: {} ".format(phone))
#    print("Email: {} ".format(email))
#    print("*" * 120)

cursor.close()
db.commit() # To update the value to database
db.close()