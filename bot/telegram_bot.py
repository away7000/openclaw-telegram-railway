import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from ai.llm import ask_ai

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    reply = ask_ai(text)

    await update.message.reply_text(reply)


async def start_bot():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, handle))

    print("BOT START")

    await app.run_polling()
