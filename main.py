import telebot, requests
from sql import *

#---------------
# SQL Connection
#---------------
db = sqlite3.connect('sql.db')
sql = db.cursor()

#----------------
# Bot Credentials
#----------------
bot = telebot.TeleBot(TOKEN)

#--------------
# Start Command
#--------------
@bot.message_handler(commands=['start'])
def command_start(message):
    if auth(message.chat.id):
        pass
#----------
# Start Bot
#----------
try: 
    bot.polling()
    
except Exception as error: requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(TOKEN, log_chat, error))

finally:
    db.close()