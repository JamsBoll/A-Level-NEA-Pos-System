import sqlite3

#define connection
connection = sqlite3.connect("loginInfo.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS logins(usernames TEXT, passwords TEXT)"""

cursor.execute(command1)
cursor.execute("DELETE FROM logins")
#add to db
cursor.execute("INSERT INTO logins VALUES ('Root', 'root')")
cursor.execute("INSERT INTO logins VALUES ('Jamie', 'KIWI')")
cursor.execute("INSERT INTO logins VALUES ('Admin', 'Jamie12345')")
cursor.execute("INSERT INTO logins VALUES ('test', '')")
connection.commit()


#get results
cursor.execute("SELECT * FROM logins")
results = cursor.fetchall()
print(results)

