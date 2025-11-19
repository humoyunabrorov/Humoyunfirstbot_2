import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = "8405281889:AAFN7DcAOkDgxH3Z9uOVZrvgfifL3D8U8ws"

dp = Dispatcher()

inline_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="google", url="google.com")]
    ]
)

# command 
@dp.message()
async def text_return(msg: Message):
    # info = msg.text.upper()
    info = msg.text.lower()
    await msg.reply(info, reply_markup=inline_btn)

@dp.message()
async def text_return(msg:Message):
    info = msg.text.lower()
    info = msg.text.upper(``)
  


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # print("Bot ishga tushdi....")
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())