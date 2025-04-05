# main.py
from src.category import Category
from src.product import Product

if __name__ == "__main__":
    # Тест 1: Ручное создание продуктов и категории
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны")
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print("Тест 1: Ручное создание категории")
    print(category1)  # Используем __str__

    # Тест 2: Добавление продукта
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nТест 2: После добавления продукта")
    print(category1)
    print(f"Количество продуктов (по списку): {category1.product_count}")

    # Тест 3: Метод new_product
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": 5}
    )
    print("\nТест 3: Создание продукта через new_product")
    print(new_product)  # Используем __str__

    # Тест 4: Проверка сеттера цены
    print("\nТест 4: Проверка сеттера цены")
    new_product.price = 800
    print(new_product.price)  # Ожидаем 800
    new_product.price = -100
    print(new_product.price)  # Ожидаем "Цена не должна..." и 800
    new_product.price = 0
    print(new_product.price)  # Ожидаем "Цена не должна..." и 800

    # Тест 5: Сложение продуктов
    print("\nТест 5: Сложение продуктов")
    print(f"product1 + product2 = {product1 + product2}")
    print(f"product1 + product3 = {product1 + product3}")
    print(f"product2 + product3 = {product2 + product3}")

    # Тест 6: Создание категорий из файла (раскомментируйте, если есть data.json)
    # print("\nТест 6: Создание категорий из файла")
    # categories = create_categories_from_file("data.json")
    # for cat in categories:
    #     print(cat)