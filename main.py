import telepot
import os
import requests
import time
from pprint import pprint
from telepot.loop import MessageLoop


# Создание бота по токену, сохранённому в переменной окружения
TOKEN = os.environ.get('TOKEN')
bot = telepot.Bot(TOKEN)

def on_chat_message(msg):
    """Обработчик сообщений"""

    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'voice':
        user_id = msg['from']['id']
        file_id = msg['voice']['file_id']
        file_info = bot.getFile(file_id)
        print(file_info)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'
        .format(TOKEN, file_info['file_path']))
        with open('voice.oga', 'wb') as voice_message:
            voice_message.write(file.content)

        print(file)

    pprint(msg)


MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
while True:
    time.sleep(10)
