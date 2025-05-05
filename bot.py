from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
import threading
from flask import Flask

# Flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Bot is running!'

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

# Telegram bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text=" دونده باهوش!🏃‍♂️🏃‍♂️", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/887")),
         KeyboardButton(text=" کلمه چین!🧩🔠️", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/1100"))],
        [KeyboardButton(text=" ضربه زدن به خرگوش!🐰🥊", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/902")),
         KeyboardButton(text=" پک من!👻👾", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/1056"))],
        [KeyboardButton(text="باز کردن سایت🌐", web_app=WebAppInfo(url="https://baazigooshi.com"))],
        [KeyboardButton(text="ورود به تورنومنت🍻🏆🥇", web_app=WebAppInfo(url="https://baazigooshi.com/tournament"))]
    ]
    await update.message.reply_text(
        "روی دکمه زیر بزن:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Start Flask in a thread
threading.Thread(target=run_flask).start()

app = Application.builder().token("7796483522:AAE_5jtLXJZi_I8nugfrSIqZgvtCh6pZRaQ").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
