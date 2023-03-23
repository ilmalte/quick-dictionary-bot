# quick-dictionary-bot
A super simple Telegram bot that given a word it queries and scrapes a dictionary website and answers back its pronunciation and definition!

## How to configure
- Paste token of your bot into `src/config.py`

## How to run standalone
- Install `python` >= 3 and `pip`
- Go to `src` directory
- Run `pip3 install -r requirements.txt` to install dependencies
- Run `python3 bot.py` to start the bot
- Enjoy!

## How to run with Docker
- Install Docker for your plaform
- Run `docker build -t qd-bot . && docker run -d --name qd-bot qd-bot`
- Enjoy!


## Article
https://www.danielemaltese.com/posts/web-scarper-telegram-bot-python/
