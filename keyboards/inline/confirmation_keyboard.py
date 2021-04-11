from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

user_callback = CallbackData("begin", "user_id")


def generate_confirmation_keyboard(user_id: int):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "get admin",
            callback_data=user_callback.new(
                being="autoban",
                user_id=user_id,
            )
        )
    )

    return markup
