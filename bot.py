from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text=" دونده باهوش!🏃‍♂️", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/887")),
         KeyboardButton(text=" کلمه چین!🧩", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/1100"))],
        [KeyboardButton(text=" ضربه زدن به خرگوش!🐰", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/902")),
         KeyboardButton(text=" پک من!👻", web_app=WebAppInfo(url="https://baazigooshi.com/about-game/1056"))],
        [KeyboardButton(text="باز کردن سایت🌐", web_app=WebAppInfo(url="https://baazigooshi.com"))],
        [KeyboardButton(text="ورود به تورنومنت🏆", web_app=WebAppInfo(url="https://baazigooshi.com/tournament"))]
    ]
    await update.message.reply_text(
        "روی یکی از دکمه‌های زیر بزن:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    app.run_polling()
