import datetime

from aiogram import types

from loader import dp

from aiogram.utils.exceptions import BadRequest

from filters import IsGroup
from keyboards.inline import generate_confirmation_keyboard, user_callback

from loguru import logger


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_user(message: types.Message):

    if message.date < datetime.datetime.now() - datetime.timedelta(minutes=1):
        return False

    for member in message.new_chat_members:
        await message.reply(f'Приветствую тебя, {member.full_name}!', reply_markup=generate_confirmation_keyboard(member.id))


@dp.callback_query_handler(user_callback.filter())
async def user_confirm(query: types.CallbackQuery, callback_data: dict):
    being = callback_data.get("being")
    user_id = int(callback_data.get("user_id"))
    chat_id = int(query.message.chat.id)
    user_fullname = query.message.from_user.full_name

    if query.from_user.id != user_id:
        return

    if being == "autoban":
        try:
            await query.message.chat.kick(user_id=user_id, until_date=datetime.timedelta(minutes=60))

            logger.info(
                f"Пользователь {user_fullname} был забанен!"
            )

            await query.message.answer(f'Пользовтаель {user_fullname} был забанен по собественному желанию!')

        except BadRequest:
            logger.info(f"Бот не смог забанить пользователя {user_fullname}")

    await asyncio.sleep(5)

    await query.message.delete()
