import os

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from agent.core import run_agent

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    user = str(update.message.chat_id)

    text = update.message.text

    reply = run_agent(user, text)

    await update.message.reply_text(reply)


def start_bot():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT, handle)
    )

    print("AGENT START")

    app.run_polling()
