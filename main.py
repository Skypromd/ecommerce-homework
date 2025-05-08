<<<<<<< HEAD
from src.product import Product
from src.category import Category


if __name__ == '__main__':
=======
from src.product import Product, Smartphone, LawnGrass
from src.category import Category
from src.utils import create_categories_from_file
from src.order import Order


def print_product_details(prod):
    print(f"  Название: {prod.name}")
    print(f"  Описание: {prod.description}")
    print(f"  Цена: {prod.price}")
    print(f"  Количество: {prod.quantity}")
    if isinstance(prod, Smartphone):
        print(f"  Производительность: {prod.efficiency}")
        print(f"  Модель: {prod.model}")
        print(f"  Память: {prod.memory}")
        print(f"  Цвет: {prod.color}")
    elif isinstance(prod, LawnGrass):
        print(f"  Страна: {prod.country}")
        print(f"  Срок прорастания: {prod.germination_period}")
        print(f"  Цвет: {prod.color}")


if __name__ == "__main__":
    # Проверка обработки нулевого количества
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    try:
        product_invalid = Product(
            "Бракованный товар", "Неверное количество", 1000.0, 0
        )
<<<<<<< HEAD
    except ValueError:
        print(
            "Возникла ошибка ValueError при попытке добавить продукт "
            "с нулевым количеством"
=======
    except ValueError as e:
        print(
            "Возникла ошибка ValueError при попытке добавить продукт с "
            f"нулевым количеством: {e}"
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт с "
            "нулевым количеством"
        )

<<<<<<< HEAD
=======
    # Создание продуктов
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

<<<<<<< HEAD
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

=======
    # Создание категории смартфонов
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Вывод информации о категории
    print("\nКатегория смартфонов:")
    print(f"  {category1}")
    print(f"  Средняя цена: {category1.middle_price():.2f} руб.")
    for prod in category1.products:
        print_product_details(prod)
        print()

    # Создание пустой категории
    category_empty = Category(
        "Пустая категория", "Категория без продуктов", []
    )
    print("\nПустая категория:")
    print(f"  {category_empty}")
    print(f"  Средняя цена: {category_empty.middle_price():.2f} руб.")

    # Создание категории телевизоров
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product4]
    )

<<<<<<< HEAD
    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(category1.middle_price())
    category_empty = Category(
        "Пустая категория", "Категория без продуктов", []
    )
    print(category_empty.middle_price())
    print(Category.total_product_count)
=======
    # Вывод информации о категории телевизоров
    print("\nКатегория телевизоров:")
    print(f"  {category2}")
    print(f"  Средняя цена: {category2.middle_price():.2f} руб.")
    for prod in category2.products:
        print_product_details(prod)
        print()

    # Демонстрация загрузки из data.json
    print("\nКатегории из файла data.json:")
    categories = create_categories_from_file("data.json")
    for category in categories:
        print(f"  {category}")
        print(f"  Средняя цена: {category.middle_price():.2f} руб.")
        for prod in category.products:
            print_product_details(prod)
            print()

    # Демонстрация класса Order
    print("\nЗаказы:")
    order1 = Order("Заказ 1", "Покупка смартфона", product1, 2)
    print(order1)
    order2 = Order("Заказ 2", "Покупка телевизора", product4, 1)
    print(order2)
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
