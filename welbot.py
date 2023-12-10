from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Get the token from an environment variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Your webhook URL
WEBHOOK_URL = f'https://tg.typetop.xyz/{TOKEN}'

async def set_webhook(app: ApplicationBuilder):
    # Set webhook
    await app.bot.set_webhook(WEBHOOK_URL)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

# Run the webhook setup function
app.run(set_webhook(app))
