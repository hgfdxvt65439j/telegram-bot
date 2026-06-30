from telegram.ext import ApplicationBuilder, CommandHandler

from bot.config import BOT_TOKEN
from bot.handlers.start import start
from bot.handlers.help import help_command

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()