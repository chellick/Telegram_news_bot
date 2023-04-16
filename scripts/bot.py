from aiogram.contrib.fsm_storage.memory import MemoryStorage
from state import SetProfile
import aiogram
import os
from parc import *
from botsql import *


file_p = os.path.join('C:/Users/Matvey/OneDrive/Рабочий стол/Token bot.txt')

with open(file_p, 'r') as f:
    TOKEN = f.read()


bot = aiogram.Bot(token=TOKEN)
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)

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
        "/info - получить дополнительную информацию",
        "/set_profile - установить профиль Habr"
    ]
    help_message = "Список всех доступных команд:\n\n"
    help_message += "\n".join(commands)
    await message.answer(help_message)


@dp.message_handler(commands="info")
async def info(message: aiogram.types.Message):
    await message.answer('Если нужна допольнительная информация, рекомендую посетить репозиторий: [ссылка](https://github.com/chellick/Telegtram_news_bot)', parse_mode="Markdown", disable_web_page_preview=True)


@dp.message_handler(commands="set_profile")
async def choose_theme(message: aiogram.types.Message):
    user_id = message.from_user.id
    if fetch_themes(int(user_id), '') is None:
        await SetProfile.state.set()
        await message.answer('Пришлите ссылку на ваш профиль Habr.com')
    else:
        await message.answer('Видимо, у вас уже есть профиль! Чтобы открыть его, воспользуйтесь /my_profile')


@dp.message_handler(state=SetProfile.state)
async def save_themes(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    if 'https://habr.com' in message.text:
        r = get_profile_themes(message.text)
        result = get_message(r)
        user_id = message.from_user.id
        user_url = message.text
        set_themes(int(user_id), str(user_url))
        await message.answer(f'Ваши темы:\n{result}', parse_mode="Markdown", disable_web_page_preview=True)
        await state.finish()
    else:
        await message.answer('Неправильная ссылка, попробуйте снова')
        await state.finish()
    

@dp.message_handler(commands="my_profile")
async def my_profile(message: aiogram.types.Message):
    user_id = message.from_user.id
    url = fetch_themes(int(user_id), str())
    if url is None:
        await message.answer('У вас ещё нет профиля! Чтобы настроить, выберите /set_profile')
    else:
        result = get_message(get_profile_themes(url))
        await message.answer(f'Это ваш профиль! Вот ваши сохраненные темы:\n{result}', parse_mode="Markdown", disable_web_page_preview=True)


@dp.message_handler(commands="news")
async def news(message: aiogram.types.Message):
    user_id = message.from_user.id
    url = fetch_themes(int(user_id), str())
    if url is None:
        await message.answer('У вас ещё нет профиля! Чтобы настроить, выберите /set_profile')
    else:
        text = []
        arr = get_profile_themes(url)
        for n in range(len(arr)):
            text.append(get_news(arr[n][1]))
        text = get_message(text)
        await message.answer(f'Вот список ваших сегодняшних тем: \n{text}', parse_mode="Markdown", disable_web_page_preview=True)

        



if __name__ == '__main__':
    aiogram.utils.executor.start_polling(dp, skip_updates=True)
