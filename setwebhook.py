from telegram import Bot
import os

TOKEN = '6143132501:AAF-1TEVnNuKTR1sHT6-8lVo2MdSl9ZvyVM'

bot = Bot(TOKEN)

url = 'https://echoKamron12121bek.pythonanywhere.com/bot'

print(bot.set_webhook(url))
# print(bot.delete_webhook())
print(bot.get_webhook_info())

