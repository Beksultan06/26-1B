from celery import shared_task
import asyncio
from telegram.utils import send_telegram_message, CHAT_ID

@shared_task
def send_telegram_message_task(text:str, chat_id : int = None):
    if chat_id is None:
        chat_id = CHAT_ID
    asyncio.run(send_telegram_message(text, chat_id))