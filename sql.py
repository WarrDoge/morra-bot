import sqlite3

#---------------
# SQL connection
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
    APP_NAME STRING NOT NULL,
    APP_LINK STRING NOT NULL,
    STATUS STRING NOT NULL,
	)''')
db.commit()

#-----------------------------------------
# Create app table and add to master table
#-----------------------------------------
def add_app(app_name: str, app_link: str, status: str):
    sql.execute('''
        CREATE TABLE IF NOT EXISTS {0} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CHAT_ID STRING NOT NULL
        )'''.format(app_name))

    sql.execute('INSERT INTO master(APP_NAME, APP_LINK, STATUS) VALUES({0}, {1}, {2})'.format(app_name, app_link, status))
    db.commit()

#---------
# Get apps
#---------
def get_apps():
    sql.execute('SELECT APP_NAME, APP_LINK, STATUS FROM master')
    app_list = sql.fetchall()
    return app_list

#---------
# Add user
#---------
def add_user(chat_id: str):
    sql.execute('INSERT INTO users(CHAT_ID) VALUES({0})'.format(chat_id))
    db.commit()
    
#------------
# Delete user
#------------
def delete_user(chat_id: str):
    sql.execute('DELETE FROM users WHERE CHAT_ID={0}}'.format(chat_id))
    db.commit()
    
#----------
# Get users
#----------
def get_users():
    sql.execute('SELECT CHAT_ID FROM users')
    user_list = sql.fetchall()
    return user_list
     
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
