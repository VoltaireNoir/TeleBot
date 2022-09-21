#!/usr/bin/env python3
from telegram import ForceReply, Update, Animation, Sticker
from telegram.ext import ContextTypes
import random, asyncio, logging

# All command functions go here, unless their implementation is too large
# then they should be placed in their .py files and imported here for ease of use

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Uh oh, I don't know how I could help you!")


async def coin_toss(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Coin toss requested")
    # IDs for media stored on Telegram's server
    LOADING_GIF_ID = "CgACAgUAAxkDAAMUYxWtM8zT6CEQFzs5mVodW66_qjYAAmIGAALAKrBU7V09eSPo2b0pBA", "AgADagYAAsAqsFQ"
    HEADS_ID = "CAACAgUAAxkDAAN9YxXJh1HRWj9iW3Bicn6P-xOpZ3YAArAGAALAKrBUAb9ML3lUOEIpBA", "AgADsAYAAsAqsFQ"
    TAILS_ID = "CAACAgUAAxkDAAN_YxXJz-PXVEDa_2G1U36f3JJv-7QAArEGAALAKrBUb-oCzAago38pBA", "AgADsQYAAsAqsFQ"

    loading_gif = Animation(LOADING_GIF_ID[0],LOADING_GIF_ID[1],638,544,3.3)
    heads_sticker = Sticker(HEADS_ID[0],HEADS_ID[1],512,512,False,False,"REGULAR")
    tails_sticker = Sticker(TAILS_ID[0],TAILS_ID[1],512,512,False,False,"REGULAR")

    loading = await update.message.reply_animation(loading_gif,duration=3.3)
    await asyncio.sleep(3.3)
    await loading.delete()
    await update.message.reply_sticker(
        random.choice([heads_sticker,tails_sticker]))
    logging.info("Coint toss complete")

# Send media to upload to Telegram servers and retreive ID to reuse in the future
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = "media/CoinTailsT.png"
    with open(file,"rb") as f:
        msg = await update.message.reply_sticker(f)
    print(msg.sticker.file_id)
    print(msg.sticker.file_unique_id)

async def pick(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Item Picker requested")
    command = update.message.text.split(" ")
    if len(command)>1:
        await update.message.reply_text(random.choice(list(command[1:])))
    else:
        await update.message.reply_text("Dont forget to include options DUH!")
    logging.info("item picked")