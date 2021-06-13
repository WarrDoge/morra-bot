import sqlite3

#-----------------------------------------
# Create app table and add to master table
#-----------------------------------------
db = sqlite3.connect('apps.db')
sql = db.cursor()

sql.execute('''
    CREATE TABLE IF NOT EXISTS {0} (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
    APP_NAME STRING NOT NULL,
    APP_LINK STRING NOT NULL,
    STATUS STRING NOT NULL,
    CHAT_ID STRING NOT NULL
	)'''.format(APP_NAME))

sql.execute('INSERT INTO master(app) VALUES({0})'.format(APP_NAME))

db.commit()
db.close()
