import sqlite3

#----------------------------
# Check if user is authorized
#----------------------------
def auth(chat_id: str):
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    
    sql.execute('SELECT chat_id FROM users')
    results = str(sql.fetchall())
    
    db.close()
    
    if chat_id in results:
        return True
    else:
        return False
