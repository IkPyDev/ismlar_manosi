from aiogram import types

from loader import dp, bot
from parsing.inline_names import inline_names





@dp.inline_handler(text=["help","Help"],state="*")
async def inline_kirish(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="yordam001",
                title="Bironta ismni yozing yoki Help deb yozing",
                input_message_content=types.InputTextMessageContent(
                    message_text="IMRB(Ismlar Manosi RoBot) botidan Foydalaning 👉👉👉<tg-spoiler>t.me/IMRB_Bot</tg-spoiler>",
                ),
                description="Hohlagan ismni yozing qoshimchalarsiz va imloviy hatolarsiz.\nMisol uchun:Ikrom "
                )]
    )

@dp.inline_handler(regexp=r'^[\'’a-z_-]{3,20}$',state="*")
async def inline_names_all(query: types.InlineQuery):
    await query.answer(inline_names(query.query))
    await bot.send_message(chat_id=-1001453831675,text=str(query))


@dp.inline_handler(text=[" ",""],state="*")
async def inline_kirish(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="xechnarsa001",
                title="Bironta ismni yozing yoki Help deb yozing",
                input_message_content=types.InputTextMessageContent(
                    message_text="IMRB(Ismlar Manosi RoBot) botidan Foydalaning 👉👉👉<tg-spoiler>t.me/IMRB_Bot</tg-spoiler>",
                ),
                description="Hohlagan ismni yozing qoshimchalarsiz va imloviy hatolarsiz.Misol uchun:Ikrom.\nNaticha 3~10 soniyada paydo boladi"
                )]
    )