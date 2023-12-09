from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update, ParseMode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def start(update, context):
    update.message.reply_text("Hello! Welcome to the group.")

def welcome(update, context):
    for member in update.message.new_chat_members:
        update.message.reply_text(f"Welcome, {member.full_name}!")

def main():
    global bot
    global TOKEN
    global dispatcher

    TOKEN = os.environ.get("TELEGRAM_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")  # Get token from environment variable
    bot = Bot(TOKEN)
    dispatcher = Dispatcher(bot, None, workers=0)

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # Start the webhook
    bot.set_webhook("https://welbot-157d47a7fe95.herokuapp.com/" + TOKEN)

if __name__ == '__main__':
    main()
    app.run(threaded=True)
