from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import commands, logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

def main() -> None:
    # Read token from file
    try:
        with open("token") as f:
            TOKEN = f.readline().strip()
    except FileNotFoundError:
        logger.critical("Token file not found. Exiting.")
        return

    # Create application using token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", commands.start))
    application.add_handler(CommandHandler("help", commands.help))
    application.add_handler(CommandHandler("toss", commands.coin_toss))

    #application.add_handler(CommandHandler("id", commands.get_id))

    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()