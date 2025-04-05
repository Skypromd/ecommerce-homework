import pytest
from src.category import Category
from src.product import Product

@pytest.fixture
def sample_category():
    return Category("Test Category")

@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 1000.0, 10)

def test_add_product(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert "Test Product, 1000.0 руб. Остаток: 10 шт." in sample_category.products
    assert sample_category.product_count == 1

def test_products_property(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert sample_category.products == "Test Product, 1000.0 руб. Остаток: 10 шт."

def test_counter_increment(sample_category, sample_product):
    initial_counter = Category.counter
    sample_category.add_product(sample_product)
    assert Category.counter == initial_counter + 1

def test_str(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert str(sample_category) == "Test Category, количество продуктов: 10 шт."