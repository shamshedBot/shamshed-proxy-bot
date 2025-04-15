import logging
from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

approved_users = set([OWNER_ID])

@dp.message_handler(commands=["start"])
async def start_cmd(msg: types.Message):
    if msg.from_user.id not in approved_users:
        await msg.reply("⛔ You're not approved to use this bot.")
        return
    await msg.reply("🔥 <b>Welcome to Shamshed Proxy Checker Bot</b>
If you need contact click @Shamshed_Boss

Available Commands:
1. /start
2. /check
3. /live
4. /dead")

@dp.message_handler(commands=["check"])
async def check_proxies(msg: types.Message):
    if msg.from_user.id not in approved_users:
        return await msg.reply("⛔ You're not approved to use this bot.")
    await msg.reply("✅ Checking proxies...")

@dp.message_handler(commands=["live"])
async def live_proxies(msg: types.Message):
    if msg.from_user.id not in approved_users:
        return await msg.reply("⛔ You're not approved to use this bot.")
    await msg.reply("🟢 Showing live proxies...")

@dp.message_handler(commands=["dead"])
async def dead_proxies(msg: types.Message):
    if msg.from_user.id not in approved_users:
        return await msg.reply("⛔ You're not approved to use this bot.")
    await msg.reply("🔴 Showing dead proxies...")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
