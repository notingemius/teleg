from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    # URL вашего веб-приложения
    web_app_url = "https://0952eb17-5904-466e-8d0a-334094455dbe-00-23tcw29h248ap.spock.replit.dev/"
  # Замените на ваш URL

    # Создаём кнопку для запуска WebApp
    keyboard = [
        [InlineKeyboardButton("Играть 🐹", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть игру в приложении:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token("7983144115:AAGv_GnPQBy0Gt4TNfY1ian-Fu80Rxcm3SI").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
