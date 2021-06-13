import sqlite3

#----------------
# Create users DB
#----------------
db = sqlite3.connect('users.db')
sql = db.cursor()

sql.execute('''
    CREATE TABLE IF NOT EXISTS users (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CHAT_ID STRING NOT NULL,
    TOKEN STRING NOT NULL
	)''')

db.commit()
db.close()
