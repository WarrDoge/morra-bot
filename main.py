from auth import auth
import telebot, requests

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

#----------
# Start Bot
#----------
bot.polling()
