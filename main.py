import telebot, requests
from sql import *

#----------------
# Bot credentials
#----------------
bot = telebot.TeleBot(TOKEN)

#--------------
# Start command
#--------------
@bot.message_handler(commands=['start'])
def command_start(message):
    if auth(message.chat.id):
        pass
    
#----------
# Start bot
#----------
try: 
    bot.polling()
    
except Exception as error: 
    requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(TOKEN, log_chat, error))

finally:
    db.close()