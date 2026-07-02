from telegram import Update
from telegram.ext import ContextTypes

from bot.services.products import get_product_by_id


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("product:"):
        product_id = int(data.split(":")[1])
        product = get_product_by_id(product_id)

        if not product:
            await query.message.reply_text("Товар не найден.")
            return

        await query.message.reply_text(
            f"{product['name']}\n\n"
            f"{product['description']}\n"
            f"Цена: ${product['price']}"
        )

    elif data.startswith("cart:add:"):
        product_id = int(data.split(":")[2])
        product = get_product_by_id(product_id)

        if not product:
            await query.message.reply_text("Товар не найден.")
            return

        await query.message.reply_text(
            f"Товар добавлен в корзину:\n{product['name']}"
        )