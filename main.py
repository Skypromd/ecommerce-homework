from src.product import Smartphone, LawnGrass
from src.category import Category
from src.utils import create_categories_from_file


def print_product_details(product):
    print(f"  Название: {product.name}")
    print(f"  Описание: {product.description}")
    print(f"  Цена: {product.price}")
    print(f"  Количество: {product.quantity}")
    if isinstance(product, Smartphone):
        print(f"  Производительность: {product.efficiency}")
        print(f"  Модель: {product.model}")
        print(f"  Память: {product.memory}")
        print(f"  Цвет: {product.color}")
    elif isinstance(product, LawnGrass):
        print(f"  Страна: {product.country}")
        print(f"  Срок прорастания: {product.germination_period}")
        print(f"  Цвет: {product.color}")


if __name__ == "__main__":
    # Создание смартфонов
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512,
        "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3,
        "Note 11", 1024, "Синий"
    )

    # Вывод атрибутов смартфонов
    print("Смартфоны:")
    print_product_details(smartphone1)
    print()
    print_product_details(smartphone2)
    print()
    print_product_details(smartphone3)

    # Создание газонной травы
    grass1 = LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия",
        "7 дней", "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней",
        "Темно-зеленый"
    )

    # Вывод атрибутов газонной травы
    print("\nГазонная трава:")
    print_product_details(grass1)
    print()
    print_product_details(grass2)

    # Проверка сложения
    print("\nСложение:")
    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)
    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    # Создание категорий вручную
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны",
        [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )

    # Добавление продукта
    category_smartphones.add_product(smartphone3)

    # Вывод информации о категории
    print("\nКатегория смартфонов:")
    print(f"  {category_smartphones}")
    for item in category_smartphones.products:
        print_product_details(item)
        print()

    # Проверка ограничения добавления
    try:
        category_smartphones.add_product("Not a product")
    except ValueError:
        print("Возникла ошибка ValueError при добавлении не продукта")
    else:
        print("Не возникла ошибка ValueError при добавлении не продукта")

    # Использование create_categories_from_file
    print("\nКатегории из файла data.json:")
    categories = create_categories_from_file("data.json")
    for category in categories:
        print(f"  {category}")
        for item in category.products:
            print_product_details(item)
            print()
