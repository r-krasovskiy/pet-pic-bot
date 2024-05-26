import logging
import os

import random
import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

URL_CAT = 'https://api.thecatapi.com/v1/images/search'
URL_DOG = 'https://api.thedogapi.com/v1/images/search'


def get_new_pet_image():
    """Get from the server a new image of dog or cat based on random choise."""
    if random.randint(0, 100) % 2 == 0:
        response = requests.get(URL_CAT)
    else:
        response = requests.get(URL_DOG)
    response = response.json()
    random_pet = response[0].get('url')
    return random_pet


def get_new_cat_image():
    """Get a cat image from the server."""
    response = requests.get(URL_CAT)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def get_new_dog_image():
    """Get a dog image from the server."""
    response = requests.get(URL_DOG)
    response = response.json()
    random_dog = response[0].get('url')
    return random_dog


def new_pet(update, context):
    """Send a random pet (cat or dog) pic via Telegram message."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_pet_image())


def new_cat(update, context):
    """Send a random cat pic via Telegram message."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_cat_image())


def new_dog(update, context):
    """Send a random dog pic via Telegram message."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_dog_image())


def wake_up(update, context):
    """Start chatting."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['/kitty', '/doggy'],
        ['/kitty_or_doggy']
        ],
        resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Хочешь увидеть фото кошечки или собачки? '
        'Тогда скорей нажимай одну из кнопок ниже!'.format(name),
        reply_markup=button
    )


def main():
    """Contain the main logic of the progrmm."""
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('kitty', new_cat))
    updater.dispatcher.add_handler(CommandHandler('doggy', new_dog))
    updater.dispatcher.add_handler(CommandHandler('kitty_or_doggy', new_pet))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
