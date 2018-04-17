##### IMPORTS

import telegram
import logging
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters

import sys, os
sys.path.append(os.getcwd()+"/python")
from logger import newlog,log
from datahandler import getToken
updater = '_'

##### MESSAGE HANDLERS

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="HarakatBot Active")

def echo(bot, update):
    recieved=update.message.text
    log(recieved)
    print('recieved:',recieved)
    bot.send_message(chat_id=update.message.chat_id, text=recieved)

def file(bot,update):
    recieved=update.message.document
    log(str(recieved))
    print(str(recieved))
    bot.send_message(chat_id=update.message.chat_id,text='checking')

def downloadfile(message):
    file_id = message.document.file_id
    newFile = bot.get_file(file_id)
    newFile.download('voice.ogg')

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)
    print('wow')

def boi_up():
    global updater
    log('test')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    bot = telegram.Bot(token=getToken())
    updater = Updater(token=getToken())
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, echo)
    caps_handler = CommandHandler('caps', caps, pass_args=True)
    file_handler = MessageHandler(Filters.document,file)

##### ADDING HANDLERS TO DISPATCHER


    # TODO

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(caps_handler)
    dispatcher.add_handler(file_handler)
##### START BOT
    updater.start_polling()

def boi_down():
    global updater
    updater.stop()

##### STOP BOT
#updater.stop()
