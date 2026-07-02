from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_product_buttons(product_id: int):
    keyboard = [
        [
            InlineKeyboardButton("Подробнее", callback_data=f"product:{product_id}"),
            InlineKeyboardButton("В корзину", callback_data=f"cart:add:{product_id}"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)