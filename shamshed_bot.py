import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

BOT_TOKEN = "7696979981:AAFFmynvUB4AtEuMlo7IOZNI_YDzgF1XmA8"
OWNER_ID = 8114177038

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(msg: Message):
    if msg.from_user.id != OWNER_ID:
        await msg.answer("🚫 You are not authorized to use this bot.")
        return
    await msg.answer("""🔥 Welcome to Shamshed Proxy Checker Bot
If you need contact click @Shamshed_Boss

Available Commands:
1. /start
2. /check
3. /live
4. /dead.""")
    
async def main():
    await asyncio.sleep(3)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import threading
    from aiohttp import web

    async def handle(request):
        return web.Response(text="Bot is alive!")

    def start_web():
        app = web.Application()
        app.router.add_get("/", handle)
        web.run_app(app, port=8080)

    threading.Thread(target=start_web).start()
    asyncio.run(main())