import json
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


def create_categories_from_file(file_path):
    """
    Создаёт список категорий из JSON-файла, поддерживая классы Product,
    Smartphone и LawnGrass.

    Args:
        file_path (str): Путь к JSON-файлу с данными о категориях и продуктах.

    Returns:
        list: Список объектов Category с продуктами.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product_type = product_data.get("type", "Product")
            if product_type == "Smartphone":
                product = Smartphone.new_product(product_data)
            elif product_type == "LawnGrass":
                product = LawnGrass.new_product(product_data)
            else:
                product = Product.new_product(product_data)
            products.append(product)

        category = Category(category_data["name"], category_data.get("description", ""))
        for product in products:
            category.add_product(product)
        categories.append(category)

    return categories
