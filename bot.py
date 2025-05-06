import requests
import threading
from flask import Flask, request
from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

# --- تنظیمات ---
BOT_TOKEN = "توکن_بات_تو_اینجا"
APP_URL = "https://your-app-name.onrender.com"  # دامنه‌ای که Render بهت داده
WEBHOOK_URL = f"{APP_URL}/webhook"

# حذف Webhook قبلی و تنظیم جدید
DELETE_WEBHOOK_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
SET_WEBHOOK_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}"

try:
    requests.get(DELETE_WEBHOOK_URL)
    requests.get(SET_WEBHOOK_URL)
    print("✅ Webhook تنظیم شد.")
except Exception as e:
    print(f"❌ خطا در تنظیم Webhook: {e}")

# --- Flask app ---
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Bot is alive!"

@flask_app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), app.bot)
    app.update_queue.put(update)
    return 'OK'

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

# --- ساخت اپ ---
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# اجرای Flask در Thread جدا
def run_flask():
    flask_app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    app.run_polling(stop_signals=None)  # polling فقط برای هندل queue، نه برای گرفتن پیام
