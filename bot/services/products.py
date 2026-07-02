CATEGORIES = {
    "phones": {
        "title": "📱 Смартфоны",
        "products": [
            {
                "id": 1,
                "name": "iPhone 15",
                "price": 799,
                "description": "Смартфон Apple iPhone 15",
            },
            {
                "id": 2,
                "name": "Samsung Galaxy S24",
                "price": 699,
                "description": "Флагманский смартфон Samsung",
            },
        ],
    },
    "headphones": {
        "title": "🎧 Наушники",
        "products": [
            {
                "id": 3,
                "name": "AirPods Pro",
                "price": 249,
                "description": "Беспроводные наушники Apple",
            },
        ],
    },
}


def get_categories():
    return CATEGORIES


def get_products_by_category(category_key):
    return CATEGORIES.get(category_key, {}).get("products", [])

def get_product_by_id(product_id: int):
    for category in CATEGORIES.values():
        for product in category["products"]:
            if product["id"] == product_id:
                return product
    return None