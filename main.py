from aiogram import Dispatcher, Bot, types
from asyncio import run

dp=Dispatcher()

async def echo(message: types.Message, bot: Bot):
    await message.copy_to(message.chat.id)

async def start():
    dp.message.register(echo)
    bot = Bot(token="6563336446:AAGbsgymHNM1OuptD-AzLZC3f9nO8iNn8dE")
    await dp.start_polling(bot, polling_timeout=1)

run(start())