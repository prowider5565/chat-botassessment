from aiogram.fsm.state import State, StatesGroup


class MessageState(StatesGroup):
    content = State()
