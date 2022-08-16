import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(msg: types.Message,state:FSMContext):
    users = await db.select_all_users()

    await msg.answer(f"{len(users)} obunachiga xabar yuboring ")
    await state.set_state("Reklama")



@dp.message_handler(state="Reklama",text="/reklama", user_id=ADMINS)
async def rek_addd(msg: ContentTypes.ANY, state: FSMContext):
    users = db.select_all_users()
    s, b = 1, 1
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0], from_chat_id=msg.from_user.id, message_id=msg.message_id, protect_content=True)
            await asyncio.sleep(0.05)
            s += 1
        except Exception:
            b += 1
            pass

    await msg.answer(f"reklama {s} odmaga yuborildi, {b} odam blokladgan botni")
    await state.finish()