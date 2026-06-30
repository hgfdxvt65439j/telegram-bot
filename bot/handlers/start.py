from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.main_menu import get_main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Бот работает ✅",
        reply_markup=get_main_menu()
    )