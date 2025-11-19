import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


TOKEN = "8273836827:AAEgp4MaMKWrfN85Fyze1LOJm2o_VJpmGtA"
dp = Dispatcher()

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="uzbekistan"),KeyboardButton(text="germaniya")], 
        [KeyboardButton(text="korea"),KeyboardButton(text="xitoy")],
        [KeyboardButton(text="brazilya"),KeyboardButton(text="turkiya")],
        [KeyboardButton(text="portugaliya"),KeyboardButton(text="argentina")],
        [KeyboardButton(text="fransiya"),KeyboardButton(text="xorvatiya")],
        [KeyboardButton(text="oislandiya"),KeyboardButton(text="polsha")],
    ],
    resize_keyboard=True,
    input_field_placeholder="tanlang jigar",
    one_time_keyboard=True
)

# Command handler
@dp.message(Command("start"))
async def start_cmd(msg: Message):
    await msg.reply("nma gap jigar quyidagi tugmalardan birini tanlang",reply_markup=menu_btn) 
    

@dp.message(Command("help"))
async def start_cmd(msg: Message):
    await msg.reply("help",reply_markup=help_btn) 
help_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1️⃣"),KeyboardButton(text="2️⃣"),KeyboardButton(text="3️⃣")],
        [KeyboardButton(text="4️⃣"),KeyboardButton(text="5️⃣"),KeyboardButton(text="6️⃣")],
        [KeyboardButton(text="7️⃣"),KeyboardButton(text="8️⃣"),KeyboardButton(text="9️⃣")],
        [KeyboardButton(text="✳️"),KeyboardButton(text="0️⃣"),KeyboardButton(text="➕")],
    ],
resize_keyboard=True,
input_field_placeholder="tanlang jigar",
one_time_keyboard=True
)        
 
 
# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot ishga tushdi....")
    asyncio.run(main())