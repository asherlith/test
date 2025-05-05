import threading
import requests
from flask import Flask
from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

# --- تنظیمات ---
BOT_TOKEN = "7796483522:AAE_5jtLXJZi_I8nugfrSIqZgvtCh6pZRaQ"
DELETE_WEBHOOK_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"

# --- حذف webhook قبلی ---
try:
    response = requests.get(DELETE_WEBHOOK_URL)
    if response.status_code == 200:
        print("✅ Webhook حذف شد.")
    else:
        print(f"⚠️ حذف Webhook با خطا مواجه شد: {response.text}")
except Exception as e:
    print(f"❌ خطا در حذف Webhook: {e}")

# --- Flask app برای alive نگه‌داشتن سرویس ---
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Bot is alive!'

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

# --- بات تلگرام ---
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

# اجرای Flask در Thread جدا
threading.Thread(target=run_flask).start()

# ساخت اپ تلگرام و اجرای polling
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
