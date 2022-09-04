#!/usr/bin/env python3
from telegram import ForceReply, Update
from telegram.ext import CallbackContext

# All command functions go here, unless their implementation is too large
# then they should be placed in their .py files and imported here for ease of use

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("Uh, I don't know how I could help you!")

