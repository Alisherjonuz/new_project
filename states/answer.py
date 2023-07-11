from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class test(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    name = State() # ism
    answers = State() # ism