import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.meny import menuStart
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    text = f"Assalomu alekum {message.from_user.full_name}!\nMen sizga ismlar manosini va shakilarni aytaman."
    text += "\nBotni toliq ishlatish uchun /help buyrig'ini yuboring "
    await message.answer(text,reply_markup=menuStart)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    msg += str(message)
    await bot.send_message(chat_id=-1001790100709, text=msg)