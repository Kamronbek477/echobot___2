from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    first_name = update.message.from_user.first_name
    chat_id = update.message.chat.id
    bot = context.bot
    bot.send_message(chat_id,text=f"Assalomu aleyko'm, 👋{first_name}")

def msg(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    bot.send_message(chat_id,text)