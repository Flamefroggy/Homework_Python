from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from controller import solve_task
from log import logging

bot = Bot(token='')
updater = Updater(token='')
dispather = updater.dispatcher


def start(update, contex):
    contex.bot.send_message(update.effective_chat.id, 'Привет!\nПеред вами калькулятор\nВведите пример, без пробелов, можно со скобками:')


def input_task(update, contex):
    task = update.message.text
    original = task
    rezult = solve_task(task)
    text = original + " = " + str(rezult)
    logging(update.effective_chat.id, text)
    contex.bot.send_message(update.effective_chat.id, text)
    contex.bot.send_message(update.effective_chat.id,'Вводите новый пример ')


start_handler = CommandHandler('start', start)
input_task_handler = MessageHandler(Filters.text, input_task)

dispather.add_handler(start_handler)
dispather.add_handler(input_task_handler)

updater.start_polling()
updater.idle()