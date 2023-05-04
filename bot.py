from telegram.ext import Updater, CommandHandler,Filters,MessageHandler
import os

from main import start,msg

TOKEN = os.environ.get('TOKEN')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.update,msg))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()