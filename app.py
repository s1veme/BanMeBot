from utils.notify_admins import on_startup_notify
import handlers
from aiogram import executor

from loguru import logger

from loader import dp
import middlewares
import filters

filters.setup(dp)


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
