import config
import logging
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
    await message.answer("memory used:", psutil.virtual_memory()[2], "%" ))

#run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
