import time
import telepot
from telepot.loop import MessageLoop
import token
import json


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])

#TOKEN = sys.argv[1]  # get token from command-line
with open ("token.json", "r") as json_token:
    TOKEN = json.load(json_token)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)