from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class get_info(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    image = State() # ism
    text = State() # email
    author = State() # Tel raqami