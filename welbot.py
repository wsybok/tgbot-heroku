from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update, ParseMode
import os

app = Flask(__name__)

# Existing code ...

def test(update, context):
    update.message.reply_text("Test successful! The bot is working.")

def main():
    global bot
    global TOKEN
    global dispatcher

    TOKEN = os.environ.get("TELEGRAM_TOKEN", "YOUR_FALLBACK_TOKEN")  # Get token from environment variable
    bot = Bot(TOKEN)
    dispatcher = Dispatcher(bot, None, workers=0)

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("test", test))  # Add the test command handler
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # Start the webhook
    bot.set_webhook("https://welbot-157d47a7fe95.herokuapp.com/" + TOKEN)

    # Existing code ...

if __name__ == '__main__':
    main()
    app.run(threaded=True)

