import os
from telegram.ext import Updater, MessageHandler, Filters

from ai.llm import ask_ai

TOKEN = os.getenv("TELEGRAM_TOKEN")


def handle(update, ctx):

    text = update.message.text

    reply = ask_ai(text)

    update.message.reply_text(reply)


def start():

    up = Updater(TOKEN)

    dp = up.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle))

    up.start_polling()

    up.idle()
