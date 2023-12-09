from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
import asyncio

async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Welcome to the group.")

async def welcome(update: Update, context):
    for member in update.message.new_chat_members:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome, {member.full_name}!")

async def main():
    TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Ensure TOKEN is set in your environment variables

    application = Application.builder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    welcome_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)

    application.add_handler(start_handler)
    application.add_handler(welcome_handler)

    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
