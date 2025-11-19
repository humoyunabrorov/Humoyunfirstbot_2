# import asyncio


# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.types import Message

# TOKEN = "8392024061:AAFn3tsqsdk-BMJC1OaGu6s8eNcMcva1qQc"

# dp = Dispatcher()


# Command handler
 
# @dp.message(Command("start"))
# async def command_start_handler(message: Message) -> None:
#     await message.answer("Assalomu alekum bot ishga tushdi...")

# @dp.message(Command("start"))
# async def start_cmd(msg: Message):
    

#     user_id = msg.from_user.id
#     user_username = msg.from_user.username
#     user_first_name = msg.from_user.first_name
#     user_last_name = msg.from_user.last_name
#     user_premium = msg.from_user.is_premium
#     user_bot = msg.from_user.is_bot

#     data = f"""
#     sening malumotlaring
#     ID:{user_id}
#     Username:{user_username}
#     last_name:{user_last_name}
#     First_name:{user_first_name}
#     Premium:{user_premium}
#     Botmi:{user_bot}
# """
#     await msg.reply(data)


@dp.message()
async def echo(msg: Message):
    son = msg.text
    if int (son) == 1:
        await msg.reply("yanvar")
    elif int(son) ==2: 
       await msg.reply("fevral") 
    elif int(son) ==3:
        await msg.reply("mart")
    elif int (son) ==4:
        await msg.reply("aprel")
    elif int(son) ==5:
        await msg.reply("may")
    elif int(son) ==6:
        await msg.reply("iyun")
    elif int(son) ==7:
        await msg.reply("iyul")  
    elif int(son) ==8:
        await msg.reply("avgust")
    elif int (son) ==9:
        await msg.reply("sentabr")
    elif int (son) == 10:
        await msg.reply("oktabr")
    elif int (son) ==11:
        await msg.reply("noyabr")
    elif int (son) ==12:
        await msg.reply("dekabr")

    else:
      await msg.reply("bunaqa oy yoq")




# async def main() -> None:
#     bot = Bot(token=TOKEN)
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     print("bot ishga tushdi....")
#     asyncio.run(main())       