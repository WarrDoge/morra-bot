import schedule, requests
from sql import *

#-------------------------
# Check response (approve)
#-------------------------
approve_list = list()
def check_approve(app_name: str, app_link: str):
    response = requests.get(app_link)
    if response == 200:
        approve_list.append(app_name)

#-----------------
# Notify about ban
#-----------------
def ban_notifier(app_name: str, app_link: str, chat_id_list: list):
    notification: str = 'Приложение {0} забанилось!'.format(app_name, app_link)
    
    for user in chat_id_list:
        requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(TOKEN, user, notification))
     
#---------------------
# Notify about approve
#---------------------
def approve_notifier(app_name: str, app_link: str, chat_id_list: list):
    notification: str = 'Приложение {0} вышло в Play Market!'.format(app_name, app_link)
    
    for user in chat_id_list:
        requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(TOKEN, user, notification))  

#---------------
# Check all apps
#---------------
def checks():
    sql.execute('SELECT APP_NAME, APP_LINK, STATUS FROM master')
    app_list = sql.fetchall()
    app_list = list(sum(app_list, ()))
       
    i = 0  
    ban_list = list()
    approve_list = list()
    while i < len(app_list):
        if str(app_list[i]) == 'active':
            response = requests.get(app_list[i-1])
            if response == 404:
                buffer = list()
                buffer.append(app_list[i-2])
                buffer.append(app_list[i-1])
                ban_list.append(buffer)
            
        elif str(app_list[i]) == 'approving':
            response = requests.get(app_list[i-1])
            if response == 200:
                buffer = list()
                buffer.append(app_list[i-2])
                buffer.append(app_list[i-1])
                approve_list.append(buffer)
            
        else:
            print('Skipping banned app...')    
            
        i += 1
            
    if len(ban_list) != 0:
        for app in ban_list:
            sql.execute('SELECT CHAT_ID, STATUS FROM {0}'.format(app[0]))
            user_info = sql.fetchall()
            user_info = list(sum(user_info, ()))
            sql.execute('UPDATE master SET STATUS = {0} WHERE APP_NAME = {1}'.format('ban', app[0]))
            db.commit()
            ban_notifier(app[0], app[1], user_info)
        
    if len(approve_list) != 0:
        for app in approve_list:
            sql.execute('SELECT CHAT_ID, STATUS FROM {0}'.format(app[0]))
            user_info = sql.fetchall()
            user_info = list(sum(user_info, ()))
            sql.execute('UPDATE master SET STATUS = {0} WHERE APP_NAME = {1}'.format('ban', app[0]))
            db.commit()
            approve_notifier(app[0], app[1], user_info)
    
    ban_list.clear()
    approve_list.clear()
  
#---------------------------
# Schedule the check process
#---------------------------
schedule.every(100).minutes.do(checks)
