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
    
'''
# Chat buttons template: 

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
'''  
    
#----------
# Start bot
#----------
try: 
    bot.polling()
    
except Exception as error: 
    requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(TOKEN, log_chat, error))

finally:
    db.close()