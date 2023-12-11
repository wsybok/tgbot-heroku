#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

import os
import logging
from typing import Optional, Tuple

from telegram import Chat, ChatMember, ChatMemberUpdated, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    CallbackContext,
    ContextTypes,
    MessageHandler,
    filters,
)

# Enable logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def extract_status_change(chat_member_update: ChatMemberUpdated) -> Optional[Tuple[bool, bool]]:
    """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
    the status didn't change.
    """
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get("is_member", (None, None))

    if status_change is None:
        return None

    old_status, new_status = status_change
    was_member = old_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    is_member = new_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    return was_member, is_member


async def track_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Tracks the chats the bot is in."""
    result = extract_status_change(update.my_chat_member)
    if result is None:
        return
    was_member, is_member = result

    # Let's check who is responsible for the change
    cause_name = update.effective_user.full_name

async def greet_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets new users in chats and announces when someone leaves"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
    cause_name = update.chat_member.from_user.mention_html()
    member_name = update.chat_member.new_chat_member.user.mention_html()

    if not was_member and is_member:
        keyboard = [
             [InlineKeyboardButton("👉TypoGraphy Website🌐", url="http://typox.ai")],
             [InlineKeyboardButton("👉Contact Support❓", url='https://t.me/TypoGraphyAI/8168')],
             [InlineKeyboardButton("👉Follow us on X🐦", url="https://twitter.com/TypoX_AI")],
             [InlineKeyboardButton("👉Join Campaign & Win Rewards!🎁", url="https://t.me/TypoGraphyAI/281/8441")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # URL of your product website
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
    # Get the token from an environment variable
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("No TELEGRAM_TOKEN found in environment variables")

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()


    # Handle members joining/leaving chats.
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))


    # Run the bot until the user presses Ctrl-C
    # We pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
