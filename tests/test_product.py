# tests/test_product.py
import pytest
from src.product import Product

# Фикстура для создания продукта
@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 1000.0, 10)

# Тест задания 3: Проверка метода new_product
def test_new_product():
    product_dict = {"name": "New Product", "description": "New Desc", "price": 500.0, "quantity": 3}
    new_product = Product.new_product(product_dict)
    assert new_product.name == "New Product"
    assert new_product.description == "New Desc"
    assert new_product.price == 500.0
    assert new_product.quantity == 3

# Тест задания 4: Проверка сеттера и геттера цены
def test_price_setter(sample_product, capsys):
    # Проверка установки корректной цены
    sample_product.price = 2000
    assert sample_product.price == 2000

    # Проверка установки отрицательной цены
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 2000  # Цена не изменилась

    # Проверка установки нулевой цены
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 2000  # Цена не изменилась
