from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="باز کردن سایت", web_app=WebAppInfo(url="https://baazigooshi.com"))]
    ]
    await update.message.reply_text(
        "روی دکمه زیر بزن:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
app = Application.builder().token("7796483522:AAE_5jtLXJZi_I8nugfrSIqZgvtCh6pZRaQ").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
