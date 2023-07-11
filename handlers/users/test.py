from aiogram import types
from loader import dp
from keyboards.default.main import menu
from aiogram.dispatcher import FSMContext
from states.answer import test

@dp.message_handler(text="📊 Haftalik testda qatnashish 📊")
async def bot_start(message: types.Message, state:FSMContext):
    f = open("test_id.txt", 'r')
    list = f.read().split(",")
    f.close()
    chat_id = str(message.from_user.id)
    z = 0
    for i in list:
        if str(i)==chat_id:
            z+=1
    if z==0:
        f = open("ad_image.txt", "r")
        photo_id = f.read()
        f.close()
        f = open("ad.txt", 'r')
        text = f.read()
        f.close()
        text+="\n\nJavoblarni quyidagi tartibda yuboring: abcabc"
        await message.answer_photo(
            photo_id, caption=text
        )
        await  test.answers.set()
    else:
        await message.answer("Bu testda oldin ham qatnashgansiz",reply_markup=menu)


@dp.message_handler(state = test.answers)
async def get_file_id_p(message: types.Message,  state: FSMContext):
    f = open('test_answer.txt', 'r')
    answers = f.read()
    f.close
    ans = str(message.text)
    if len(ans)==len(answers):
        son = 0
        for i in range(len(answers)):
            if ans[i]==answers[i]:
                son+=1
        f = open('test.txt', 'a')
        f.write(str(son))
        f.write(',')
        f.close()
        f = open('test_id.txt', 'a')
        f.write(str(message.from_user.id))
        f.write(',')
        f.close()
        await message.answer(f"To'g'ri javoblar soni: {len(answers)}ta dan  {son}ta")
        await message.answer("Javoblaringiz muvaffaqiyatli saqlandi",reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Javoblar soni savollar soniga teng emas! Iltimos javoblarni qaytadan yuboring.")
        await  test.answers.set()