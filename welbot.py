from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask, request
import os

app = Flask(__name__)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Telegram bot token from environment variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Set up the telegram bot application
telegram_app = ApplicationBuilder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("hello", hello))

# Webhook endpoint
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    asyncio.create_task(telegram_app.update_queue.put(update))
    return 'OK'

if __name__ == "__main__":
    telegram_app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 5000)),
        url_path=TOKEN,
        webhook_url=f"https://{os.environ.get('welbot')}.herokuapp.com/{TOKEN}"
    )
    app.run(debug=True)

