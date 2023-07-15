import logging
import wikipedia
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup,ReplyKeyboardMarkup
import first
import curse


button1 = InlineKeyboardButton(text ="➕ObunaBo'lish",callback_data="randomvalue_of10" )
button2 = InlineKeyboardButton(text ="✅Tasdiqlash",callback_data="randomvalue_of100" )
keyboard_reply = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("🧾Wikipedia", "💸Curse")

keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2)


res =requests.get("https://api.telegram.org/bot6219929580:AAEq3XTWjwOlpzAHIv4N12Y3Qe4lsOX5z-M/getUpdates").json()

API_TOKEN = '6219929580:AAEq3XTWjwOlpzAHIv4N12Y3Qe4lsOX5z-M'
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Wikipediya Botiga Hush Kelibsiz{first.firstname()}!\nQuyidagi kanallga obuna bo'lmasangiz bo'tdan foydalana olmaysiz ",reply_markup=keyboard_reply)


# @dp.message_handler()
# async def sendWiki(message: types.Message):
#     try:
#         rspond=wikipedia.summary(message.text)
#         await message.answer(rspond)
#     except:
#         await message.answer("Bu mavzuga oid maqola topilmadi")

@dp.message_handler()
async def echo(message: types.Message):
    
    if message.text =="assalomu alaykum" or message.text == "Assalomu Alaykum " or message.text == "Salom" or message.text == "salom" or message.text == "Assalomu alaykum " :
        await message.answer(f"Va alaykum assalom\n{first.firstname()}")
    if message.text == "🧾Wikipedia":
        await message.answer("Wikipedia bo'limi")
    
    if message.text == "💸Curse":
        await message.answer(f"1 Aqsh dollari {curse.curses()} som")



@dp.callback_query_handler(text= ["randomvalue_of10","randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer("new")
    if call.data == "randomvalue_of100":
        await call.message.answer("Bu botda siz!\nWikipediyadan to'liq foydalanishingiz!\nUSD UZS Valyutalarni bilishingiz mumkin")





if __name__ == '__main__':
    executor.start_polling(dp,)