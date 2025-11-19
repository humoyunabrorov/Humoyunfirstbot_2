import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import inline_keyboard_button,inline_keyboard_markup

TOKEN = "8273836827:AAEgp4MaMKWrfN85Fyze1LOJm2o_VJpmGtA"
dp = Dispatcher()

inline_btn = inline_keyboard_markup(
inline_keyboard=[
    [inline_keyboard_button(text="google", url="google.com")],

    ]
),

@dp.message()
async def text_return(msg:Message):
    # info = msg.text.upper()
    
    # info = msg.text.lower()
    # info = msg.text.capitalize()
    await msg.reply(info,reply_markup=inline_btn)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())