import sqlite3

#----------------
# Create users DB
#----------------
db = sqlite3.connect('users.db')
sql = db.cursor()

sql.execute('''
    CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id STRING NOT NULL,
    token STRING NOT NULL
	)''')

db.commit()
db.close()
