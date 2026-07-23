import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 Welcome to Vic AI Technology Study Assistant!\n\n"
        "Ask me any question in Mathematics, English, Science, Social Science, Art, WAEC, JAMB, or any school subject."
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
