from telegram import ReplyKeyboardMarkup


def get_main_menu():
    keyboard = [
        ["📋 Меню", "ℹ️ Помощь"],
        ["👤 Профиль"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )