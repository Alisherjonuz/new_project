from aiogram import types
from keyboards.default.main import menu
from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAICdGSnpcDbV0IB3uGv2S2NW-1eBAKgAAK3zjEbQ544SZU0w6miw0YTAQADAgADeAADLwQ"
    await message.answer_photo(
        photo_id, caption="🧐 Uzur bunday buyruq topilmadi 🧐\n\n🔽 Pastdagi tugmalardan birini tanlang 🔽",reply_markup=menu
    )
