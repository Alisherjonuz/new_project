from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
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




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    await message.answer(f"Botning 🏘 bosh sahifasiga 🏘 xush kelibsiz!",reply_markup=main_menu)
    if check_id(id)==0:
        id_add(id)