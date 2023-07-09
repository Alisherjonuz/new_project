from aiogram import types
from keyboards.default.main import menu as main_menu
from loader import dp, bot

def check_id(z):
    f = open('chat_id.txt','r')
    list = f.read().split(',')
    a=0
    for i in list:
        if z==int(i):
            a+=1
    if a!=0:
        return 1
    else:
        return 0
    f.close()

def id_add(i):
    f = open('chat_id.txt', 'a')
    f.write(','+str(i))
    f.close()
def reklama():
    f =  open('chat_id.txt', 'r')
    list = f.read().split(',')
    # return len(list)
    f.close()
def users():
    f =  open('chat_id.txt', 'r')
    list = f.read().split(',')
    return len(list)
    f.close()


@dp.message_handler(text='📊 Bot statistikasi 📊')
async def bot_start(message: types.Message):
    await message.answer(f"🤖 Bot statistikasi 🤖\n\n👤 Bot foydalanuvchilari soni: {users()}ta👤\n\n🧑‍💻 Bot yaratuvchisi: @AlisherNumonov 🧑‍💻",reply_markup=main_menu)

@dp.message_handler(text='Admin_panel')
async def bot_start(message: types.Message):
    await message.answer(f"🤖 Bot admin paneliga xush kelibsiz! 🤖\n\nPastdagi tugmalardan birini tanlang",reply_markup=main_menu)
