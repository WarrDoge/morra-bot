import sqlite3

#-----------------------------------------
# Create app table and add to master table
#-----------------------------------------
db = sqlite3.connect('apps.db')
sql = db.cursor()

sql.execute('''
    CREATE TABLE IF NOT EXISTS {0} (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name STRING NOT NULL,
    app_link STRING NOT NULL,
    status STRING NOT NULL,
    chat_id STRING NOT NULL
	)'''.format(app_name))

sql.execute('INSERT INTO master(app) VALUES({0})'.format(app_name))

db.commit()
db.close()
