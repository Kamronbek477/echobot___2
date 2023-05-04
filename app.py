from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler,Filters,MessageHandler
from main import start,msg



app = Flask(__name__)
TOKEN = '6143132501:AAF-1TEVnNuKTR1sHT6-8lVo2MdSl9ZvyVM'

bot: Bot = Bot(TOKEN)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/bot', methods=['POST', 'GET'])
def webhookbot():

    if request.method == 'GET':
        return 'webhook is working!'

    elif request.method == 'POST':
        data = request.get_json()

        dp = Dispatcher(bot, None, workers=0)

        # create update obj
        update: Update = Update.de_json(data, bot)

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.update,msg))

        # process update
        dp.process_update(update)

        return {"status": 200}