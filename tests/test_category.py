import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.total_product_count = 0
    yield


@pytest.fixture
def sample_category():
    return Category("Test Category")


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 1000.0, 10)


def test_add_product(sample_category, sample_product, capsys):
    sample_category.add_product(sample_product)
    assert sample_product in sample_category.products
    assert sample_category.product_count == 1
    assert Category.total_product_count == 1
    captured = capsys.readouterr()
    assert "Товар 'Test Product' успешно добавлен в категорию" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_add_product_invalid_type(sample_category, capsys):
    sample_category.add_product("Not a product")
    captured = capsys.readouterr()
    assert (
        "Ошибка: Можно добавлять только объекты класса Product или "
        "его наследников" in captured.out
    )
    assert "Обработка добавления товара завершена" in captured.out
    assert sample_category.product_count == 0
    assert Category.total_product_count == 0


def test_add_product_zero_quantity(sample_category, capsys):
    product_zero = Product("Zero Product", "Desc", 1000.0, 1)
    product_zero.quantity = 0
    sample_category.add_product(product_zero)
    captured = capsys.readouterr()
    assert (
        "Ошибка: Товар с нулевым количеством не может быть добавлен "
        "в категорию" in captured.out
    )
    assert "Обработка добавления товара завершена" in captured.out
    assert sample_category.product_count == 0
    assert Category.total_product_count == 0


def test_add_product_invalid_type_message(sample_category, capsys):
    sample_category.add_product("Invalid")
    captured = capsys.readouterr()
    assert (
        "Ошибка: Можно добавлять только объекты класса Product или "
        "его наследников" in captured.out
    )
    assert "Обработка добавления товара завершена" in captured.out
    assert sample_category.product_count == 0
    assert Category.total_product_count == 0


def test_product_count(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert sample_category.product_count == 1
    sample_category.add_product(Product("Another", "Desc", 200.0, 5))
    assert sample_category.product_count == 2
    assert Category.total_product_count == 2


def test_str(sample_category, sample_product):
    sample_category.add_product(sample_product)
    expected = "Test Category, количество продуктов: 10 шт."
    assert str(sample_category) == expected


def test_empty_category():
    category = Category("Empty Category", "No products")
    assert category.product_count == 0
    assert str(category) == "Empty Category, количество продуктов: 0 шт."
    assert Category.total_product_count == 0
    assert category.category_count == 1


def test_add_multiple_products(sample_category, sample_product):
    sample_category.add_product(sample_product)
    sample_category.add_product(Product("Another", "Desc", 200.0, 5))
    assert sample_category.product_count == 2
    assert Category.total_product_count == 2


def test_category_properties(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == ""
    assert sample_category.category_count == 1


def test_middle_price(sample_category, sample_product):
    sample_category.add_product(sample_product)
    sample_category.add_product(Product("Another", "Desc", 2000.0, 5))
    assert sample_category.middle_price() == 1500.0  # (1000 + 2000) / 2


def test_middle_price_empty(sample_category):
    assert sample_category.middle_price() == 0


def test_middle_price_single_product(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert sample_category.middle_price() == 1000.0


def test_str_multiple_products(sample_category, sample_product):
    sample_category.add_product(sample_product)
    sample_category.add_product(Product("Another", "Desc", 200.0, 5))
    expected = "Test Category, количество продуктов: 15 шт."
    assert str(sample_category) == expected


def test_middle_price_main_scenario():
    # Проверка middle_price для сценария из main.py
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    assert category.middle_price() == (180000.0 + 210000.0 + 31000.0) / 3


def test_total_product_count():
    # Проверка total_product_count
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    _ = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    _ = Category("Телевизоры", "Телевизоры", [product4])
    assert Category.total_product_count == 4
