import sqlite3

#----------------------------
# Check if user is authorized
#----------------------------
def auth(CHAT_ID: str):
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    
    sql.execute('SELECT CHAT_ID FROM users')
    results = str(sql.fetchall())
    
    db.close()
    
    if CHAT_ID in results:
        return True
    else:
        return False
