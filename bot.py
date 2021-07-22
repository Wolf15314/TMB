import config
import logging
import psutil
import aiogram

from aiogram import Bot, Dispatcher, executor, types

#log level
logging.basicConfig(level=logging.INFO)

#bot init

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("memory used:" )

#run long-polling
if __name__ == "__main__":
