##### IMPORTS
print('hi')
import telegram
import logging
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters

import sys, os
sys.path.append(os.getcwd()+"/python")
from logger import newlog,log
from datahandler import getToken
updater = '_'

##### MESSAGE HANDLERS

def getStatus():
    print("getting status")
    file_creds = "status.txt"
    file = open(file_creds, "r")
    file_contents = file.read()
    file.close()
    print(file_contents)
    return file_contents

def genReply(recieved):
    if recieved == 'status':
        return getStatus()
    else:
        return 'supported commands: status'

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="QubBot Active")

def echo(bot, update):
    recieved=update.message.text
    log(recieved)
    reply = genReply(recieved)
    bot.send_message(chat_id=update.message.chat_id, text=reply)

def file(bot,update):
    recieved=update.message.document
    log(str(recieved))
    print(str(recieved))
    bot.send_message(chat_id=update.message.chat_id,text='checking')

def downloadfile(message):
    file_id = message.document.file_id
    newFile = bot.get_file(file_id)
    newFile.download('voice.ogg')

def boi_up():
    global updater
    log('test')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    bot = telegram.Bot(token=getToken())
    updater = Updater(token=getToken())
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, echo)
    file_handler = MessageHandler(Filters.document,file)

##### ADDING HANDLERS TO DISPATCHER


    # TODO

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(file_handler)
##### START BOT
    updater.start_polling()

def boi_down():
    global updater
    updater.stop()

##### STOP BOT
#updater.stop()
