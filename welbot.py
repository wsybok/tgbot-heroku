from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import os

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Get the token from an environment variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Your webhook URL
WEBHOOK_URL = f'https://tg.typetop.xyz/{TOKEN}'

async def main():
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command handler
    application.add_handler(CommandHandler("hello", hello))

    # Set up the webhook
    await application.bot.set_webhook(WEBHOOK_URL)

    # Run the bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
