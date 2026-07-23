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

    try:
        response = model.generate_content(question)
        answer = response.text
    except Exception:
        answer = "Sorry, I couldn't process your request right now. Please try again later."

    await update.message.reply_text(answer)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Vic AI Technology Study Assistant is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
