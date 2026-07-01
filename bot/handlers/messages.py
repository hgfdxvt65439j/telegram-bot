from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.main_menu import get_main_menu
from bot.services.products import get_products


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

    if text == "🛍 Каталог":
        products = get_products()

        message = "🛍 Каталог товаров:\n\n"

        for product in products:
            message += (
                f"{product['id']}. {product['name']}\n"
                f"Цена: ${product['price']}\n"
                f"{product['description']}\n\n"
            )

        await update.message.reply_text(
            message,
            reply_markup=get_main_menu()
        )

    elif text == "ℹ️ Помощь":
        await update.message.reply_text(
            "Доступные команды:\n"
            "/start — запустить бота\n"
            "/help — помощь\n\n"
            "Кнопка 🛍 Каталог покажет товары.",
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