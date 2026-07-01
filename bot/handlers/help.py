from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.main_menu import get_main_menu


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — запустить бота\n"
        "/help — помощь",
        reply_markup=get_main_menu()
    )