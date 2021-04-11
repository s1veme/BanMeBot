from aiogram import types

from loader import dp

from filters import IsGroup
from keyboards.default import ban_menu


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_user(message: types.Message):

    for member in message.new_chat_members:
        await message.answer(f'Приветствую тебя, {member.full_name}!', reply_markup=ban_menu)
