#!/usr/bin/env python3
import logging
import commands
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def message_handler(update: Update, context: CallbackContext) -> None:
    pass


def main() -> None:
    """Start the bot."""
    try:
        with open("token") as f:
            TOKEN = f.readline().strip()
    except FileNotFoundError:
        print("Token file not found. Exiting.")
        return

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add commands
    dispatcher.add_handler(CommandHandler("start", commands.start))
    dispatcher.add_handler(CommandHandler("help", commands.help))

    # Add message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()