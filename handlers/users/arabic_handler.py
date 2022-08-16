from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.ortga import menyOrtga
from loader import dp
from deep_translator import GoogleTranslator


@dp.message_handler(text="♻️ Uzbek ➡️ Arabic ✅",state="*")
async def arabic_kirish(message: types.Message,state:FSMContext):
    await message.answer("Bu bolimda siz hohlagan Ismlar yoki gapalr jonatib matn korinishdagi uzbekchadan arabcha korinishini olishingiz munkun "
                         "\nhohlagan soz yoki gap yuboring taxminan malumot 91% togri tarjima qilinadi", reply_markup=menyOrtga)
    await state.finish()
    await state.set_state("aruz")


@dp.message_handler(state="aruz")
async def arabic_text(msg:types.Message):
    try:
        text = GoogleTranslator(source="uz",target="ar").translate(text=msg.text)
        await msg.answer(
            f"<b> {text} </b>",
            reply_markup=menyOrtga
        )
    except :await msg.answer("Iltimos uzbekcha ism yoki gap yuboring❗️",reply_markup=menyOrtga)



@dp.message_handler(text="♻️ Arabic ➡️ Uzbek ✅",state="*")
async def uzbek_kirish(message: types.Message,state:FSMContext):
    await message.answer("Bu bolimda siz hohlagan Ismlar yoki gapalr jonatib matn korinishdagi arabchadan uzbekcha  korinishini olishingiz munkun "
                         "\nhohlagan soz yoki gap yuboring taxminan malumot 91% togri tarjima qilinadi", reply_markup=menyOrtga)
    await state.finish()
    await state.set_state("uzar")


@dp.message_handler(state="uzar")
async def arabic_text(msg:types.Message):
    try:
        text = GoogleTranslator(source="ar",target="uz").translate(text=msg.text)
        await msg.answer(
            f"<b> {text} </b>",
            reply_markup=menyOrtga
        )
    except :
        await msg.answer("Iltimos uzbekcha ism yoki gap yuboring❗️",reply_markup=menyOrtga)
