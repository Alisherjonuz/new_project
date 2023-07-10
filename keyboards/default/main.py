from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='ℹ️ O`quv markaz haqida ma`lumot ℹ️'),
            KeyboardButton(text='📍 Joylashuv 📍'),
        ],
        [
            KeyboardButton(text='📊 Bot statistikasi 📊'),
            KeyboardButton(text="📚 Kurslar haqida ma'lumot 📚"),
        ],
        [
            KeyboardButton(text='📊 Haftalik testda qatnashish 📊'),
        ],
    ],
    resize_keyboard=True
)