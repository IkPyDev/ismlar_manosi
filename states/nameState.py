from aiogram.dispatcher.filters.state import StatesGroup,State


class NamesState(StatesGroup):
    boys = State()
    girls = State()