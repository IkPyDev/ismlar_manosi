from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.meny import menuStart
from loader import dp
from states.nameState import NamesState
from parsing.names import names_boys,names_girls
from keyboards.default.ortga import menyOrtga
from keyboards.default.arabic import arabic

@dp.message_handler(text="📚Ismlar boyicha qoshimcha malumotlar",state="*")
async def ortga_qaytish(message: types.Message):
    await message.answer("<b>Qoshimcha malumotlar Bolimi</b>", reply_markup=arabic)


@dp.message_handler(text="🔙Ortga",state="*")
async def ortga_qaytish(message: types.Message,state:FSMContext):
    await message.answer("Bosh menyudasiz", reply_markup=menuStart)
    await state.finish()

@dp.message_handler(text="🤴Bollar ismini manosi",state="*")
async def boys_start(message: types.Message, state:FSMContext):
    await message.answer("O'g'ilbolar ismini jonating men sizga Manosini jonataman\nMisol:<pre>Ikrom</pre>",reply_markup=menyOrtga)
    await state.finish()
    await NamesState.boys.set()


@dp.message_handler(text="👸Qizlar ismini manosi",state="*")
async def girl_start(message: types.Message,state:FSMContext):
    await message.answer("Qizlar ismini jonating men sizga Manosini jonataman\nMisol:<pre>Mushtariy</pre>",reply_markup=menyOrtga)
    await state.finish()
    await NamesState.girls.set()


@dp.message_handler(state=NamesState.boys)
async def Boys_name_state(message:types.Message):

    number = str(message.text)
    if len(number) <= 20:

        text = names_boys(message.text)

        if not text:
            await message.answer(f"<pre>{message.text}</pre> malumot topilmadi \nagar ismigiz bolib malumot chiqmagan bolsa \n🧑‍💻adminga murojat qiling ",reply_markup=menyOrtga )

        elif text == "boy_none":
            await message.answer(f"<pre>{message.text.strip()}</pre>🧕 bu Qizbollar ismi❗❗❗ Qizbollar ismi bolimidan qidiring ☑",
                                 reply_markup=menyOrtga)

        else:
            text_link = "<a href='https://t.me/IsmlarManosiRo_bot'>Ismlar Manosi RoBot</a>"
            msg =f'{text}\n\n\n{text_link}'
            markub = types.InlineKeyboardMarkup()
            markub.add(types.InlineKeyboardButton(f"🚀{message.text} ismini ulashish ",switch_inline_query=f"{message.text.capitalize()}"))
            await message.answer(f"{msg}",reply_markup=markub)
    else:
        await message.reply("Iltomos ism yuboring ❗")





@dp.message_handler(state=NamesState.girls)
async def girl_name_state(message:types.Message):
    number = str(message.text)
    if len(number) <= 20:

        text = names_girls(message.text)
        if not text:
            await message.answer(f"<pre>{message.text}</pre> malumot topilmadi \nagar ismigiz bolib malumot chiqmagan bolsa \n🧑‍💻adminga murojat qiling ",reply_markup=menyOrtga )
        elif text == "girl_none":
            await message.answer(f"<pre>{message.text.strip()}</pre>👳 bu O'g'ilbolar ismi❗❗❗ O'g'il bollar ismi bolimidan qidiring ☑",reply_markup=menyOrtga)

        else:
            text_link = "<a href='https://t.me/IsmlarManosiRo_bot'>Ismlar Manosi RoBot</a>"
            msg = f'{text}\n\n\n{text_link} '
            markub = types.InlineKeyboardMarkup()
            markub.add(types.InlineKeyboardButton(f"🚀{message.text.capitalize()} ismini ulashish ",switch_inline_query=f"{message.text.capitalize()}"))
            await message.answer(msg,reply_markup=markub)

    else:
        await message.reply("Iltomos ism yuboring ❗")