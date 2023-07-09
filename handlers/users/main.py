from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import menu as main_menu
from loader import dp, bot


# Rus tili BQACAgIAAxkBAAICkmN864gYkzei3SWgyXASoBKHpfaVAAI_IQACRgroSyHfYLXV0bBsKwQ
# work book BQACAgIAAxkBAAICmWN867fafySKXbdGNH1v5v8d3jnOAAJDIQACRgroSwl0BTcWPWdFKwQ
# student's book BQACAgIAAxkBAAICm2N869Getmjyvaxj2PfleaimbvAzAAJNIQACRgroS_xyzexrWwr0KwQ
# ona tili BQACAgIAAxkBAAICnWN86-Ppf9v1EJnHVo9afV5_7u8YAAJQIQACRgroS7Ud9LuaIaBuKwQ
# yapon tili BQACAgIAAxkBAAICn2N86_z9u28YDpQDuv0K_BOvKnkOAAJXIQACRgroS6Dx6W1bsDLCKwQ
# Tarix BQACAgIAAxkBAAICoWN87BC3eZIZyP9o0AZXcanfpQaUAAJZIQACRgroS34aOyVYBI21KwQ
# Tarbiya BQACAgIAAxkBAAICo2N87SFzz0DGN8aUel9WzTz6gh_zAAJgIQACRgroS7JC13e5C4A6KwQ


# Location


@dp.message_handler(text="📍 Joylashuv 📍")
async def bot_start(message: types.Message):
    await bot.send_location(latitude=41.28539, longitude=69.195017, chat_id=message.from_user.id, reply_markup=main_menu)
    await message.answer(text="🏫 100097, Toshkent sh. Chilonzor t. 9-mavze, 33-uy. 🏫")

# About liceum


@dp.message_handler(text="ℹ️ O`quv markaz haqida ma`lumot ℹ️")
async def get_file_id_p(message: types.Message):
    photo_id = "AgACAgIAAxkBAAICfmSnpwM91MKs_qwI14V5jCDOMkoQAALOzjEbQ544SZZJPFIzVFG1AQADAgADeAADLwQ"
    await message.answer_photo(
        photo_id, caption="🌍web-site: www.sirojiddinovral.uz 🌍\n🏫 Litsey asoschisi: Sa’di Hasanovich Sirojiddinov 🏫\n🗓 Tashkil topgan sana: 1998-yil 16-iyul 🗓\n📞 Telefon raqami: +998(71)278-86-49 📞"
    )

# Liceum's director



# write your code here

# Connect with creator of this bot


@dp.message_handler(text="🤖 Bot uchun taklif 🤖")
async def bot_start(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBlWN4_laGwgapioXFFC4zAXwk_J1aAAJfwDEbILrIS369wWZy6S-wAQADAgADeQADKwQ"
    await message.answer_photo(
        photo_id, caption="✅ Taklifingizni ✅ shu 👉 @sirojiddinov_litsey_chat 👈 guruhga yuboring va biz taklifingizni ko'rib chiqib bu botni rivojlantirishga harakat qilamiz. ✊✊✊"
    )

# Cancel to page before
# write your code to this free place
