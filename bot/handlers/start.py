from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.main_menu import get_main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n\n"
        "Добро пожаловать в бота.",
        reply_markup=get_main_menu()
    )