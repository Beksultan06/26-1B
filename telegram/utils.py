from aiogram import Bot
import os

TELEGRAM_TOKEN = '7320076710:AAGqkVYjIB_wzYyYH8BRzV0dQtROupnYGlk'
CHAT_ID = '5771196980'

bot = Bot(token=TELEGRAM_TOKEN)

async def send_telegram_message(text : str, chat_id : int = int(CHAT_ID)):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
    except Exception as e:
        print(f"Ошибка отправки в Телеграм: {e}")