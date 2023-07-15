import logging
import first 
from aiogram import Bot, Dispatcher, executor, types
import requests


API_TOKEN = '6333778008:AAHRnXaLli2P4hkjDW45RLNWw0Q33YC2b-8'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def firstname():
    l=[]
    res = requests.get(
        f"https://api.telegram.org/bot{API_TOKEN}/getUpdates"
    ).json()

    for result in res["result"]:
        l.append(result["message"]["from"]["first_name"])
        return l[0]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply(f"botimizga hush kelibsiz\n{firstname()}")



@dp.message_handler()
async def echo(message: types.Message):

    if message.text =="assalomu alaykum" or message.text == "Assalomu Alaykum " or message.text == "Salom" or message.text == "salom" or message.text == "Assalomu alaykum " :
        await message.answer(f"Va alaykum assalom\n{firstname()}")

    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)