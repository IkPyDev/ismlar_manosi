# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:46:42 2022

@author: IKROMBE
"""

from bs4 import BeautifulSoup

import requests


# from pprint import pprint as print

def names_girls(ism):
    ism = str(ism).capitalize()
    if "'" in ism:
        ism = ism.replace("'", "‘")
    
    url = f"https://ismlar.com/name/{ism}"

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
    test = html.select("h1")[0].text
    if "404" in test:
        return None

    title = html.select("h1")[0].text.strip()
    forms = html.select("span")[14].text.strip().replace(".", ",\n").replace(" ", "")
    if forms == "xabarbering":
        forms = "❌mavjud emas yoki topilmadi❌"
    name_title = html.select("h2")[0].text
    name_text = html.select("p")[3].text
    if not name_text.strip():
        return "girl_none"

    msg = f"\n\n🧕 <pre> {title} </pre> 🧕"
    msg += f"\n📕<b>{name_title}</b>"
    msg += f"\n📖{name_text}\n\n\n📚Shakilari:{forms}"

    return msg


def names_boys(ism):
    ism = str(ism).capitalize()
    if "'" in ism:
        ism = str(ism).replace("'", "‘")
    
    url = f"https://ismlar.com/name/{ism}"

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
    test = html.select("h1")[0].text
    if "404" in test:
        return None


    title = html.select("h1")[0].text.strip()
    forms = html.select("span")[14].text.strip().replace(".", ",\n").replace(" ", "")
    # name_forms = str()
    # for names in forms:
    #     name_forms += names
    # name_forms.replace(".", ",")
    if forms == "xabarbering":
        forms = "❌mavjud emas yoki topilmadi❌"
    name_title = html.select("h2")[0].text
    name_text = html.select("p")[2].text
    if not name_text.strip():
        return "boy_none"

    msg = f"\n\n👳🏻‍♂ <pre>{title}</pre> 👳🏻‍♂️"
    msg += f"\n<b>📕{name_title}</b>"
    msg += f"\n📖{name_text}\n\n\n📚Shakilari:{forms}"


    return msg

if __name__ == "__main__":
    # print(names_boys("ikrom"))
    print(names_girls("Sa'diya"))
    # print(names_boys("navro'za"))