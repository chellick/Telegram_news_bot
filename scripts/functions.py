import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Привет! Это тестовый бот. Введите /help для получения списка команд.\nВведите /info для получения информации.')


def help(update, context):
    update.message.reply_text('Список команд:\n/start - начало работы с ботом\n/help - список команд\n/info - дополнительная информация')


def info(update, context):
    update.message.reply_text('Чтобы получить дополнительную информацию, вы можете перейти по адресу: https://github.com/chellick/Telegtram_news_bot')


def get_news(update, context):
    update.message.reply_text('Вот список сегодняшних тем из разделов: ')
