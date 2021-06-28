from aiogram import Dispatcher
from loguru import logger

from .chat_filters import IsGroup, IsPrivate
from .user_filters import IsAdmin


def setup(dp: Dispatcher):
    logger.info('Подключение filters...')

    text_messages = [
        dp.message_handlers,
        dp.edited_message_handlers,
        dp.channel_post_handlers,
        dp.edited_channel_post_handlers,
    ]

    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)