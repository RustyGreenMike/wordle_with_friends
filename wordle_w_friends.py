import random
import schedule
import time
import telegram
from telegram.ext import Updater, CommandHandler

# Function gets random word from list. I used a wordlist with only 5 letter words. 
def random_word():
    with open('<YOUR WORDLIST HERE>') as word_file:
        valid_words = list(word_file.read().split())
        return random.choice(valid_words)

# Function handles the /start command. This handles the first instantiation. After the first, the scheduler takes over. 
def start(update, context):
    daily_word = random_word()[:5]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Good morning Wordlers! I am a bot. Your word of the day is: {daily_word}")

# Creates an instance of the Updater class and pass in the bot's API token
updater = Updater(token='<YOUR API KEY HERE>', use_context=True)

# Gets the Dispatcher object from the updater
dispatcher = updater.dispatcher

# Defines command handler to handle the /start command from within Telegram
start_handler = CommandHandler('start', start)

# Adds the command handler to the Dispatcher
dispatcher.add_handler(start_handler)

# Starts the bot
updater.start_polling()

# Schedules message to occur once per day. Only outputs 5 chars as it was outputting a special char too for some reason
schedule.every().day.at("15:45").do(lambda: updater.bot.send_message(chat_id='<YOUR CHAT ID HERE>', text='Good morning Wordlers! I am a bot. Your word of the day is: {}'.format(random_word()[:5])))

# Continuously checks if there are any scheduled tasks to run. Also handles the exit if needed. 
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        # To stop/exit press ctrl+c
        updater.stop()
        break
