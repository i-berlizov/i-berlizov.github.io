import asyncio
from aiogram import Bot

def open_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        value = file.read()
        return value

TOKEN = open_file('token.txt')
CHAT_ID = open_file('chat_id.txt')


async def send_notification(text):
    bot = Bot(token=TOKEN)

    # Отправляем разные уведомления
    await bot.send_message(CHAT_ID, text)
    await bot.session.close()



def open_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        value = file.read()
        return value

