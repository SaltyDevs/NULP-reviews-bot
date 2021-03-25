
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from callback_datas import action_callback



"""
choice = InlineKeyboardMarkup(row_width=1)

write_review = InlineKeyboardButton(text="Написати відгук", callback_data="")
read_review = InlineKeyboardButton(text="Прочитати відгук", callback_data="")
choice.insert(write_review)
choice.insert(read_review)
"""


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написати відгук!", callback_data="write"),
            InlineKeyboardButton(text="Прочитати відгук", callback_data="read")
        ]
    ]
)
