import json
import pytest
from unittest.mock import patch, call
from src.main import Product, Category, load_products_from_json, main


# Фикстуры
@pytest.fixture
def sample_product():
    """Создаёт тестовый объект Product."""
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category():
    """Создаёт тестовый объект Category с двумя продуктами."""
    products = [
        Product("Product 1", "Desc 1", 100.0, 5),
        Product("Product 2", "Desc 2", 200.0, 3)
    ]
    return Category("Test Category", "Test Category Description", products)


# Тесты для Product
def test_product_init(sample_product):
    """Проверяет корректность инициализации объекта Product."""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_product_attributes(sample_product):
    """Проверяет типы и корректность атрибутов объекта Product."""
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, float)
    assert isinstance(sample_product.quantity, int)


# Тесты для Category
def test_category_init(sample_category):
    """Проверяет корректность инициализации объекта Category."""
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category.products) == 2
    assert all(isinstance(p, Product) for p in sample_category.products)


def test_category_attributes(sample_category):
    """Проверяет типы и корректность атрибутов объекта Category."""
    assert isinstance(sample_category.name, str)
    assert isinstance(sample_category.description, str)
    assert isinstance(sample_category.products, list)
    assert len(sample_category.products) > 0
    assert sample_category.products[0].name == "Product 1"


def test_category_count():
    """Проверяет подсчёт количества категорий."""
    Category.category_count = 0
    Category.product_count = 0
    products = [Product("P1", "D1", 50.0, 2)]
    Category("Cat1", "Desc1", products)
    assert Category.category_count == 1
    Category("Cat2", "Desc2", products)
    assert Category.category_count == 2


def test_product_count():
    """Проверяет подсчёт количества продуктов."""
    Category.category_count = 0
    Category.product_count = 0
    products1 = [Product("P1", "D1", 50.0, 2)]
    Category("Cat1", "Desc1", products1)
    assert Category.product_count == 1
    products2 = [Product("P2", "D2", 100.0, 3)]
    Category("Cat2", "Desc2", products2)
    assert Category.product_count == 2


# Тесты для load_products_from_json
def test_load_products_from_json(tmp_path):
    """Проверяет загрузку данных из JSON-файла с одной категорией."""
    test_file = tmp_path / "test_products.json"
    data = [
        {
            "name": "Test Category",
            "description": "Test Description",
            "products": [
                {"name": "Test Product", "description": "Test Product Desc",
                 "price": 100.0, "quantity": 10}
            ]
        }
    ]
    test_file.write_text(json.dumps(data))

    Category.category_count = 0
    Category.product_count = 0
    categories = load_products_from_json(test_file)

    assert len(categories) == 1
    category = categories[0]
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 1
    product = category.products[0]
    assert product.name == "Test Product"
    assert product.description == "Test Product Desc"
    assert product.price == 100.0
    assert product.quantity == 10
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_load_products_from_json_empty(tmp_path):
    """Проверяет загрузку данных из пустого JSON-файла."""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("[]")
    Category.category_count = 0
    Category.product_count = 0
    categories = load_products_from_json(empty_file)
    assert len(categories) == 0
    assert Category.category_count == 0
    assert Category.product_count == 0


def test_load_products_from_json_multiple_categories(tmp_path):
    """Проверяет загрузку данных из JSON-файла с несколькими категориями."""
    multi_file = tmp_path / "multi.json"
    data = [
        {"name": "Cat1", "description": "Desc1",
         "products": [{"name": "P1", "description": "D1",
                       "price": 10.0, "quantity": 1}]},
        {"name": "Cat2", "description": "Desc2",
         "products": [
             {"name": "P2", "description": "D2",
              "price": 20.0, "quantity": 2},
             {"name": "P3", "description": "D3",
              "price": 30.0, "quantity": 3}
         ]}
    ]
    multi_file.write_text(json.dumps(data))

    Category.category_count = 0
    Category.product_count = 0
    categories = load_products_from_json(multi_file)

    assert len(categories) == 2
    assert Category.category_count == 2
    assert Category.product_count == 3  # 1 + 2 продукта


# Тест для функции main()
@patch('builtins.print')
def test_main_block(mock_print, tmp_path):
    """Проверяет выполнение функции main() с выводом данных."""
    test_file = tmp_path / "test_main.json"
    data = [
        {
            "name": "Smartphones",
            "description": "Communication devices",
            "products": [
                {"name": "Phone1", "description": "D1", "price": 100.0,
                 "quantity": 5}
            ]
        }
    ]
    test_file.write_text(json.dumps(data))

    Category.category_count = 0
    Category.product_count = 0

    # Тестируем функцию main() с подменой load_products_from_json
    with patch('src.main.load_products_from_json') as mock_load:
        mock_load.return_value = load_products_from_json(test_file)
        main()

    # Проверяем точные вызовы print для одной категории
    expected_calls = [
        call("Категория: Smartphones"),
        call("Описание: Communication devices"),
        call("Количество продуктов в категории: 1"),
        call("  Продукт: Phone1, Цена: 100.0, Количество: 5"),
        call(),
        call("Общее количество категорий: 1"),
        call("Общее количество продуктов: 1")
    ]
    assert mock_print.call_count == len(expected_calls)  # 7 вызовов
    assert mock_print.call_args_list == expected_calls
