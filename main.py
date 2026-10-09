import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Windows terminalida emoji/unicode xatolarini oldini olish
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import asyncio
import logging

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

from database import init_db
from handlers import router

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    if not BOT_TOKEN:
        print("❌ XATO: BOT_TOKEN topilmadi! .env faylini tekshiring.", flush=True)
        return

    print("🚀 Pramida bot ishga tushmoqda...", flush=True)

    await init_db()

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(router)

    print("================================", flush=True)
    print("🎓 PRAMIDA O'QUV MARKAZI", flush=True)
    print("🤖 BOT ISHGA TUSHDI", flush=True)
    print("================================", flush=True)

    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        pass
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())