from aiogram.contrib.fsm_storage.memory import MemoryStorage
import telegram
import aiogram as ai
import os



file_p = os.path.join('C:/Users/Matvey/OneDrive/Рабочий стол/Token bot.txt')

with open(file_p, 'r') as f:
    TOKEN = f.read()

print(TOKEN)


bot = ai.Bot(token=TOKEN)
storage = MemoryStorage()
disp = ai.Dispatcher(bot, storage)

@disp.message_handler(commands="start")
async def start(message: ai.types.Message):
    await message.answer("Привет! Я Test Habr Bot!")



if __name__ == '__main__':
    ai.utils.executor.start_polling(disp, skip_updates=True)