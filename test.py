import sqlite3
import os
# code_path = os.getcwd()
code_path = "f:\\Nextcloud\\Documents\\Scripts\\udemy\\flask\\Flask5\\code"
# Create the database
connection = sqlite3.connect(os.path.join(code_path, 'data.db'))

cursor = connection.cursor()
# Create the table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
# Insert a new user to the db
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'asdf')
]
# Insert many users at once
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)
# Must commit the data
connection.commit()

connection.close()
