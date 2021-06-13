import sqlite3

#--------------------
# Create master table
#--------------------
db = sqlite3.connect('apps.db')
sql = db.cursor()

sql.execute('''
    CREATE TABLE IF NOT EXISTS master (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
    APP_NAME STRING NOT NULL
	)''')

db.commit()
db.close()
