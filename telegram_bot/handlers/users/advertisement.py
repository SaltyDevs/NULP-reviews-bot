import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery


from keyboards.inline.choice_buttons import choice
from loader import dp



@dp.message_handler(Command("wow"))
async def show_advertisement(message: Message):
    await message.answer(text="This is user related advertisement(Julie)",
                         reply_markup=choice)
