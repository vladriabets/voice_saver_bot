import telepot
import os
import requests
import time
from telepot.loop import MessageLoop


# Создаёт бота по токену, сохранённому в переменной окружения
TOKEN = os.environ.get('TOKEN')
bot = telepot.Bot(TOKEN)

def add_new_record(file, user_id):
    """Создаёт файл с аудиосообщением в папке, название которой соответствует
     id пользователя, создавшего аудиосообщение"""

    dir_name = str(user_id)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    number = str(len(os.listdir(dir_name)))
    with open(dir_name + '/audio_message_' + number + '.oga', 'wb') as voice_message:
        voice_message.write(file.content)


def on_chat_message(msg):
    """Обработчик сообщений"""

    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'voice':
        user_id = msg['from']['id']
        file_id = msg['voice']['file_id']
        file_info = bot.getFile(file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'
        .format(TOKEN, file_info['file_path']))
        add_new_record(file, user_id)


MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
while True:
    time.sleep(10)
