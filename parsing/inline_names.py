from bs4 import BeautifulSoup
import requests
from aiogram.types import InlineQueryResultArticle,InputTextMessageContent,InlineKeyboardMarkup,InlineKeyboardButton
from random import randint
def inline_names(ism:str):
    result = []
    ism = str(ism).capitalize()
    if "'" in ism:
        ism = ism.replace("'", "‘")
    try:
        url = f"https://ismlar.com/name/{ism}"

        response = requests.get(url)
        html = BeautifulSoup(response.content, 'html.parser')
        test = html.select("h1")[0].text
        if "404" in test:
            # print("hato boldi")
            result.append(InlineQueryResultArticle(
                id=f"{ism}001",
                title=f"❌{ism} boyicha malumot topilmadi❌",
                input_message_content=InputTextMessageContent(
                    message_text=f'❌ {ism} boyicha malumot topilmadi ❌ '
                ),
                description=f"❌malumot yoq❌",
                url="https://t.me/IMRB_BOT"))
            return result

        title = html.select("title")[0].text.split()[0]
        idd = f"{title}001"
        forms = html.select("div > span")[0].text + html.select("div > span")[1].text
        if "xabar bering" in forms:
            forms = None
        name_title = html.select("h2")[0].text
        name_text = html.select("div > p")[2].text
        if not name_text:
            name_text = html.select("div > p")[-1].text

        markub = InlineKeyboardMarkup()
        markub.add(InlineKeyboardButton(f"🚀{title} ismini ulashish ",switch_inline_query=f"{title}"
        ))
        markub.add(InlineKeyboardButton(f'✅Boshqa ismlar manosi(IMRB_BOT)',url="t.me/imrb_bot"))


        if forms:
            result.append(InlineQueryResultArticle(
            id=idd,
            title=f'✅{title}',
            input_message_content=InputTextMessageContent(
                message_text=f"✅<pre>{title}</pre>\n"
                             f"📕<b>{name_title}</b>\n"
                             f"📖{name_text}\n"
                             f"📚{forms}"
                             f"\n\n\n✅Malumotlar 👉👉👉 <tg-spoiler> t.me/IMRB_bot </tg-spoiler> 👈👈👈 Olindi "
                ),
            reply_markup=markub,
            url="https://t.me/IMRB_BOT",
            description=f'{name_title} Bilish uchun bosing 🤚'
            ))
        elif not forms:
            result.append(InlineQueryResultArticle(
                id=idd,
                title=f'✅{title}',
                input_message_content=InputTextMessageContent(
                    message_text=f"✅<pre>{title}</pre>\n"
                                 f"📕<b>{name_title}</b>\n"
                                 f"📖{name_text}\n"
                                 f"\n\n\n✅Malumotlar 👉👉👉 <tg-spoiler> t.me/IMRB_bot </tg-spoiler> 👈👈👈Olindi "
                ),
                reply_markup=markub,
                url="https://t.me/IMRB_BOT",
                description=f'{name_title} Bilish uchun bosing 🤚'))
        return result
    except Exception :
        pass



if __name__ == "__main__":
    print(inline_names("sa'diya"))







