import asyncio
import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command

from aiogram.types import ReplyKeyboardRemove

from aiogram.utils.exceptions import BadRequest

from filters import IsGroup

from loader import dp

from loguru import logger


@dp.message_handler(IsGroup(), Command(commands=["banmepls"], prefixes="/"))
async def ban_me(message: types.Message):
    member_id = message.from_user.id
    member_fullname = message.from_user.full_name

    try:
        await message.chat.kick(user_id=member_id, until_date=datetime.timedelta(minutes=60))

        logger.info(
            f"Пользователь {member_fullname} был забанен!"
        )

        await message.answer(f'Пользовтаель {member_fullname} был забанен по собественному желанию!', reply_markup=ReplyKeyboardRemove())

    except BadRequest:
        logger.info(f"Бот не смог забанить пользователя {member_fullname}")

    await asyncio.sleep(5)

    await message.delete()
