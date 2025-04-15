import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
import logging
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)

@dp.message(Command("start"))
async def start_handler(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("❌ You are not authorized to use this bot.")
        return

    text = (
        "🔥 <b>Welcome to Shamshed Proxy Checker Bot</b>"
"
        "If you need contact click @Shamshed_Boss

"
        "<b>Available Commands:</b>
"
        "1. /start
"
        "2. /check
"
        "3. /live
"
        "4. /dead"
    )
    await message.answer(text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
