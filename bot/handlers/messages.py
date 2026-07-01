from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.main_menu import get_main_menu


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

    if text == "📋 Меню":
        await update.message.reply_text(
            "Главное меню:\n\n"
            "👤 Профиль — информация о тебе\n"
            "ℹ️ Помощь — список команд",
            reply_markup=get_main_menu()
        )

    elif text == "ℹ️ Помощь":
        await update.message.reply_text(
            "Доступные команды:\n"
            "/start — запустить бота\n"
            "/help — помощь\n\n"
            "Также можешь пользоваться кнопками меню.",
            reply_markup=get_main_menu()
        )

    elif text == "👤 Профиль":
        await update.message.reply_text(
            f"Твой профиль:\n\n"
            f"ID: {user.id}\n"
            f"Имя: {user.first_name}\n"
            f"Username: @{user.username if user.username else 'нет'}",
            reply_markup=get_main_menu()
        )

    else:
        await update.message.reply_text(
            "Я пока не понимаю это сообщение.\n"
            "Используй кнопки меню 👇",
            reply_markup=get_main_menu()
        )