from message_handler import logger
import threading


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def timer(bot, update):
    t = threading.Timer()
    t.start(30, mirror, args=[bot, update])


def mirror(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hai scritto: ' + update.message.text)
