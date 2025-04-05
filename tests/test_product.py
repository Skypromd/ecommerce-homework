# tests/test_product.py
import pytest
from src.product import Product

@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 1000.0, 10)

def test_new_product():
    product_dict = {"name": "New Product", "description": "New Desc", "price": 500.0, "quantity": 3}
    new_product = Product.new_product(product_dict)
    assert new_product.name == "New Product"
    assert new_product.description == "New Desc"
    assert new_product.price == 500.0
    assert new_product.quantity == 3

def test_price_setter(sample_product, capsys):
    sample_product.price = 2000
    assert sample_product.price == 2000
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 2000

def test_str(sample_product):
    assert str(sample_product) == "Test Product, 1000.0 руб. Остаток: 10 шт."

def test_add():
    p1 = Product("P1", "Desc1", 100, 10)
    p2 = Product("P2", "Desc2", 200, 2)
    assert p1 + p2 == (100 * 10) + (200 * 2)  # 1400

def test_add_invalid_type(sample_product):
    with pytest.raises(TypeError):
        sample_product + "not a product"