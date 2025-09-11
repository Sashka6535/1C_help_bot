import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher

from Handlers import handlers_routers
from config import load_config


async def main():
    bl.basic_colorized_config(level=logging.INFO)
    config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_routers(handlers_routers)
    await dp.start_polling(bot)
    await bot.session.close()


try:

    asyncio.run(main())
except KeyboardInterrupt:
    logging.info(f"Bot stopped!")
