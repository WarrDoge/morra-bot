import schedule, requests
from sql import *

#---------------------
# Check Response (ban)
#---------------------
ban_list = list()
def check_ban(app_name: str, app_link: str):
    response = requests.get(app_link)
    if response == 404:
        ban_list.append(app_name)

#-------------------------
# Check Response (approve)
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
    sql.execute('SELECT APP_NAME FROM master')
    names_list = sql.fetchall()

    apps_list = list()
    for app_name in names_list:
       sql.execute('SELECT APP_NAME, APP_LINK, STATUS FROM {0}'.format(app_name))
       app_info = sql.fetchall()
       apps_list.append(app_info)
       
    for app in apps_list:
        if 'active' in str(app[2]):
            check_ban(app[0], app[1])
        elif 'approving'in str(app[2]):
            check_approve(app[0], app[1])
        else:
            print('Skipping banned app: {0}...'.format(app))
            
    if len(ban_list) != 0:
        for app_name in ban_list:
            sql.execute('SELECT CHAT_ID, STATUS FROM {0}'.format(app_name))
            user_info = sql.fetchall()
            sql.execute('SELECT APP_LINK, STATUS FROM {0}'.format(app_name))
            app_link = sql.fetchall()
            sql.execute('UPDATE {0} SET STATUS = {1} WHERE ID = 1'.format(app_name, 'ban'))
            ban_notifier(app_name, app_link, user_info)
        
    if len(approve_list) != 0:
        for app_name in ban_list:
            sql.execute('SELECT CHAT_ID, STATUS FROM {0}'.format(app_name))
            user_info = sql.fetchall()
            sql.execute('SELECT APP_LINK, STATUS FROM {0}'.format(app_name))
            app_link = sql.fetchall()
            sql.execute('UPDATE {0} SET STATUS = {1} WHERE ID = 1'.format(app_name, 'active'))  
            approve_notifier(app_name, app_link, user_info)
    
    ban_list.clear()
    approve_list.clear()
  
#---------------------------
# Schedule the check process
#---------------------------
schedule.every(100).minutes.do(checks)
