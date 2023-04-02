from aiogram.contrib.fsm_storage.memory import MemoryStorage
import telegram
import aiogram
import os
import asyncio as io




file_p = os.path.join('C:/Users/Matvey/OneDrive/Рабочий стол/Token bot.txt')

with open(file_p, 'r') as f:
    TOKEN = f.read()




bot = aiogram.Bot(token=TOKEN)
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage)

@dp.message_handler(commands="start")
async def start(message: aiogram.types.Message):
    user_id = message.from_user.id
    await message.answer("Привет! Я Test Habr Bot! Пропиши /help, чтобы получить всю палитру комманд!")





@dp.message_handler(commands="help")
async def help(message: aiogram.types.Message):
    text = ''
    commands = [
        "/start - начать работу",
        "/help - список всех команд",
        "/info - получить дополнительную информацию"
    ]
    help_message = "Список всех доступных команд:\n\n"
    help_message += "\n".join(commands)
    await message.answer(help_message)


@dp.message_handler(commands="info")
async def info(message: aiogram.types.Message):
    await message.answer('Если нужна допольнительная информация, рекомендую посетить репозиторий: [ссылка](https://github.com/chellick/Telegtram_news_bot)', parse_mode="Markdown")


@dp.message_handler(commands="choose_theme")
async def choose_theme(message: aiogram.types.Message):
    await message.answer

if __name__ == '__main__':
    aiogram.utils.executor.start_polling(dp, skip_updates=True)




