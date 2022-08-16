from aiogram import types

from keyboards.default.meny import menuStart
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.reply(f"Bosh menyudan foydalaning✅",reply_markup=menuStart)
