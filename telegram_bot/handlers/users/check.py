from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from keyboards.inline.choice_buttons import choice
from loader import dp


@dp.message_handler(Command("check"))
async def bot_check(message: Message):
    await message.answer(text="check", reply_markup=choice)