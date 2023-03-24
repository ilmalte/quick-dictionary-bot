import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from config import TOKEN
from pprint import pprint
from bs4 import BeautifulSoup
import requests

"""

$ python3.7 bot.py
A simple pronunciation and definition bot 

"""

async def handle(msg):
    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    # utilities
    pprint(msg)
    username = msg['chat']['first_name']
    if content_type == 'text':
        if msg['text'] != '/start':
            text = msg['text']
            # maybe it's better to check input
            text = text.strip()
            # bot.sendMessage(chat_id, text)
            await getMeaning(text.lower())
        else:
            # /start
            message = """ Hey {0}, welcome in Quick Dictionary!\n
                          Send me a word to get its pronunciation and meaning😊 \n
                          Feel free to contact me at @ilmalte if you find any problem,
                          btw, this is just a beta version!""".format(username)
            await bot.sendMessage(chat_id, message)

async def getMeaning(text):
    # create url
    url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + text
    # define headers
    headers = { 'User-Agent': 'Generic user agent' }
    # get page
    page = requests.get(url, headers=headers)
    # let's soup the page
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        # get MP3 and definitions
        try:
            # get MP3
            mp3link = soup.find('div', {'class': 'sound audio_play_button pron-uk icon-audio'}).get('data-src-mp3')
            await bot.sendAudio(chat_id=chat_id, audio=mp3link)
        except:
            await bot.sendMessage(chat_id, 'Pronunciation not found!')
        try:   
            # get definitions
            definitions = soup.find('span', {'class': 'def'}).text
            await bot.sendMessage(chat_id, definitions)
        except:
            await bot.sendMessage(chat_id, 'Meaning not found!')
    except:
        await bot.sendMessage(chat_id, 'Something went wrong...')

# Program startup
bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening...')

# Keep the program running
loop.run_forever()
