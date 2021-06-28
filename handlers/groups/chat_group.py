import asyncio
import datetime
from typing import Text

from aiogram import types
from aiogram.dispatcher.filters import Command

from aiogram.utils.exceptions import BadRequest

from filters import IsGroup

from loader import dp, bot

from loguru import logger
    

@dp.message_handler(IsGroup(), text=bot.get('BLACKLIST_WORDS'))
async def ban_me_text(message: types.Message):
    member_id = message.from_user.id
    member_fullname = message.from_user.username

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, can_send_media_messages=False, can_send_other_messages=False, until_date=datetime.timedelta(minutes=60))

        logger.info(
            f"Пользователь {member_fullname} получил мут!"
        )

        await message.answer(f'Пользовтаель {member_fullname} был забанен по собественному желанию!')
    
    except BadRequest:
        logger.info(f"Бот не смог забанить пользователя {member_fullname}")