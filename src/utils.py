# src/utils.py
import json
from src.category import Category
from src.product import Product


def create_categories_from_file(file_path):
    # Чтение файла и ранний выход из with
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Обработка данных после закрытия файла
    categories = []
    for category_data in data:
        products = [
            Product(**product)  # Распаковка словаря на именованные аргументы
            for product in category_data['products']
        ]
        category = Category(category_data['name'])
        for product in products:
            category.add_product(product)
        categories.append(category)

    return categories