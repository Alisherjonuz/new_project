from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.test import get_info


@dp.message_handler(text = '/test')
async def bot_edit(message: types.Message):    
    await message.answer("Iltimos test rasmini yuboring")
    f = open("test_id.txt", 'w')
    f.write('')
    f.close()
    f = open("test.txt", 'w')
    f.write('')
    f.close()
    await get_info.image.set()



@dp.message_handler(state = get_info.image, content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message,  state: FSMContext):
    f = open('ad_image.txt', 'w')
    f.write(str(message.photo[-1].file_id))
    f.close()
    await message.answer("Rasm muvaffaqiyatli saqlandi")
    await message.answer("Endi esa tagiga text yozing")
    await get_info.text.set()

@dp.message_handler(state = get_info.text)
async def get_file_id_p(message: types.Message,  state: FSMContext):
    f = open('ad.txt', 'w')
    f.write(str(message.text))
    f.close()
    await message.answer("Text muvaffaqiyatli saqlandi")
    await message.answer("Endi esa Javoblarini kiriting")
    await get_info.answer.set()


@dp.message_handler(state = get_info.answer)
async def get_file_id_p(message: types.Message,  state: FSMContext):
    f = open('test_answer.txt', 'w')
    f.write(str(message.text))
    f.close()
    await message.answer("Javoblari ham muvaffaqiyatli saqlandi")
    await state.finish()