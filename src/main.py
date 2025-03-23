import json
from typing import List


class Product:
    """Класс, представляющий продукт в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int):
        """Инициализирует объект продукта.


        Args:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта в рублях.
            quantity (int): Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, представляющий категорию товаров в интернет-магазине."""

    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество продуктов

    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализирует объект категории.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (List[Product]): Список продуктов в категории.
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


def load_products_from_json(file_path: str) -> List[Category]:
    """Загружает данные о категориях и продуктах из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу с данными.

    Returns:
        List[Category]: Список объектов Category, созданных из данных файла.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        categories = []
        for category_data in data:
            products = [
                Product(product['name'], product['description'],
                        product['price'], product['quantity'])
                for product in category_data['products']
            ]
            category = Category(category_data['name'],
                                category_data['description'],
                                products)
            categories.append(category)
        return categories


def main():
    """Демонстрация работы программы: загрузка и вывод данных из JSON."""
    categories = load_products_from_json('products.json')
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество продуктов в категории: {len(category.products)}")
        for product in category.products:
            print(f"  Продукт: {product.name}, Цена: {product.price}, "
                  f"Количество: {product.quantity}")
        print()
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество продуктов: {Category.product_count}")


if __name__ == "__main__":
    main()
