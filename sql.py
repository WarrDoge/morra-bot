import sqlite3

#---------------
# SQL Connection
#---------------
db = sqlite3.connect('sql.db')
sql = db.cursor()

#----------------
# Create users DB
#----------------
sql.execute('''
    CREATE TABLE IF NOT EXISTS users (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CHAT_ID STRING NOT NULL,
    TOKEN STRING NOT NULL
	)''')

db.commit()

#--------------------
# Create master table
#--------------------

sql.execute('''
    CREATE TABLE IF NOT EXISTS master (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
    APP_NAME STRING NOT NULL
	)''')

db.commit()

#-----------------------------------------
# Create app table and add to master table
#-----------------------------------------
def add_app(app_name: str):
    sql.execute('''
        CREATE TABLE IF NOT EXISTS {0} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        APP_NAME STRING NOT NULL,
        APP_LINK STRING NOT NULL,
        STATUS STRING NOT NULL,
        CHAT_ID STRING NOT NULL
        )'''.format(app_name))

    sql.execute('INSERT INTO master(app) VALUES({0})'.format(app_name))

    db.commit()

#----------------------------
# Check if user is authorized
#----------------------------
def auth(CHAT_ID: str):
    sql.execute('SELECT CHAT_ID FROM users')
    results = str(sql.fetchall())
    
    if CHAT_ID in results:
        return True
    else:
        return False
