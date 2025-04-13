import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler

# Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Ваш chat_id (узнать можно через @userinfobot)

def send_message(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Не забудь выпить таблетки!")
    context.bot.send_message(chat_id=CHAT_ID, text="И сходи на тренировку!!!")

def start(update, context):
    update.message.reply_text("🔄 Бот запущен! Ожидайте уведомлений.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Настройка расписания (каждый день в 9:30 утра)
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_message, 'cron', hour=17, minute=00, args=[updater])
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()