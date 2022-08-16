from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤴Bollar ismini manosi"),
            KeyboardButton(text="👸Qizlar ismini manosi"),
        ],
        [
            KeyboardButton(text='📚Ismlar boyicha qoshimcha malumotlar'),
        ],
    ],
    resize_keyboard=True)