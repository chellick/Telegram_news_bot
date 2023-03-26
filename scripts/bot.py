from aiogram.contrib.fsm_storage.memory import MemoryStorage
import telegram
import aiogram as ai
import os
import asyncio as io




file_p = os.path.join('C:/Users/Matvey/OneDrive/Рабочий стол/Token bot.txt')

with open(file_p, 'r') as f:
    TOKEN = f.read()




bot = ai.Bot(token=TOKEN)
storage = MemoryStorage()
disp = ai.Dispatcher(bot, storage)

@disp.message_handler(commands="start")
async def start(message: ai.types.Message):
    user_id = message.from_user.id
    await message.answer("Привет! Я Test Habr Bot! Пропиши /help, чтобы получить всю палитру комманд!")





@disp.message_handler(commands="help")
async def help(message: ai.types.Message):
    text = ''
    commands = [
        "/start - начать работу",
        "/help - список всех команд"
    ]
    help_message = "Список всех доступных команд:\n\n"
    help_message += "\n".join(commands)
    await message.answer(help_message)



if __name__ == '__main__':
    ai.utils.executor.start_polling(disp, skip_updates=True)




