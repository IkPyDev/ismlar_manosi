from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Botga faqat ismlarni ozini Yuborish kerak va Imloviy xatolarsiz.",
            "Botga ism manosi qidirib unga qoshimchalar bilan qidirilmaydi,",
            "Misollar :Tog'ri qidirish \n✅Ikrom\n✅murod\n✅ZAFAR\n✅Mushtariy\n✅hilola\n\n\nNatog'ri qidirish\n",
            "❌Ikrombek\n❌Murodjon\n❌Sardorxon\n va yana agar siz Tutuq belgisanidan foydalanmoqchi bosayiz bita qoshtirnoqdan foydalaning",
            "Misol:<code>Navro'za</code>",
            "Agar hatolikga korsangiz @IkPyDev murojat qilingsizlar ")

    
    await message.answer("\n".join(text))