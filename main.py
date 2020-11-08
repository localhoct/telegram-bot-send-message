from pyrogram import Client
from time import sleep
from pyrogram import errors

api_id = #put ur api id here(int)
api_hash = "put ur api hash" #put ur api hash here(str)
client = Client("name",api_id,api_hash) 

with client as app:
    iter1 = app.iter_dialogs()
    for dialog in iter1:
        message = f'''

Type ur message here :)

    '''

        try:
            app.send_message(dialog.chat.id , message,disable_web_page_preview=True)
            print('sended')
            sleep(5)
        except:
            continue


