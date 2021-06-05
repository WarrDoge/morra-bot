import sqlite3

#--------------------
# Create master table
#--------------------
db = sqlite3.connect('apps.db')
sql = db.cursor()

sql.execute('''
    CREATE TABLE IF NOT EXISTS master (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    app STRING NOT NULL
	)''')

db.commit()
db.close()
