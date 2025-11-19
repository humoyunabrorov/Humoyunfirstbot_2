import asyncio


from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8392024061:AAFn3tsqsdk-BMJC1OaGu6s8eNcMcva1qQc"

dp = Dispatcher()


# Command handler
 





@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Assalomu alekum bot ishga tushdi...")

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer("Qanday yordam bera olaman?")

@dp.message(Command("admin"))
async def command_admin_handler(message: Message) -> None:
    await message.answer("tez orada admin siz bilan boglanadi.")

@dp.message(Command("settings"))
async def command_settings_handler(message: Message) -> None:
    await message.answer("nimani o`zgartirmoqchisiz.")

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("bot ishga tushdi....")
    asyncio.run(main())       