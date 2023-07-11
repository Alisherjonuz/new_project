from aiogram import types

from loader import dp


@dp.message_handler(text='natija_test')
async def bot_help(message: types.Message):
    f = open("test_name.txt", 'r')
    id = f.read().split(',')
    f.close()
    f = open('test.txt', 'r')
    ans = f.read().split(',')

    text = ""
    for i in range(len(ans)):
        text+=id[i]
        text+="\t"
        text+=ans[i]
        text+=' ta'
        text+="\n"
    
    await message.answer(text)  