#!/usr/bin/env python
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Application, ChatMemberHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def greet_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets new users in chats"""
    chat_member_update = update.chat_member
    new_member = chat_member_update.new_chat_member
    if new_member.status in ["member", "administrator"]:
        member_name = new_member.user.mention_html()

        keyboard = [
             [InlineKeyboardButton("👉TypoGraphy Website🌐", url="http://typox.ai")],
             [InlineKeyboardButton("👉Contact Support❓", url='https://t.me/TypoGraphyAI/8168')],
             [InlineKeyboardButton("👉Follow us on X🐦", url="https://twitter.com/TypoX_AI")],
             [InlineKeyboardButton("👉Join Campaign & Win Rewards!🎁", url="https://t.me/TypoGraphyAI/281/8441")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        Typo20_url = "https://t.me/TypoGraphyAI/1/8024"
        Search_url = "https://t.me/TypoGraphyAI/1/8400"
        AI_url = "https://t.me/TypoGraphyAI/1/8164"
        
        await update.effective_chat.send_message(
            f"🌟 <b>{member_name} Welcome aboard TypoGraphy AI!</b> 🌟\n\n"
            f"🧭 <b>Quick Navigation:</b> \n\n"
            f"1️⃣ <a href='{Typo20_url}'>TypoGraphy AI 2.0</a>👈\n\n"
            f"2️⃣ <a href='{Search_url}'>Search, Quote, & Share Features</a>👈\n\n"
            f"3️⃣ <a href='{AI_url}'>AI + Web3 Products Comparative Analysis</a>👈\n\n"
            f"🚨 <b>Please NOTICE:</b> We will NEVER DM you first! 🛑 Stay safe and informed.",
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup
        )

def main() -> None:
    """Start the bot."""
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("No TELEGRAM_TOKEN found in environment variables")

    application = Application.builder().token(token).build()
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))

    application.run_polling()

if __name__ == "__main__":
    main()
