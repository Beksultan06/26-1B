from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

TELEGRAM_TOKEN = '7320076710:AAGqkVYjIB_wzYyYH8BRzV0dQtROupnYGlk'

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Бот активен! Добро пожаловать!")

async def main():
    await dp.start_polling(bot)