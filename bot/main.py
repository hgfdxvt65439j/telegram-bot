from telegram import ReplyKeyboardMarkup


def get_main_menu():
    keyboard = [
        ["🛍 Каталог", "👤 Профиль"],
        ["ℹ️ Помощь"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )