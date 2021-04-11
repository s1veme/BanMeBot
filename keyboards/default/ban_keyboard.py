from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ban_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/banmepls')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
