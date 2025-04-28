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
    assert sample_product in sample_category.products
    assert sample_category.product_count == 1


def test_add_product_invalid_type(sample_category):
    with pytest.raises(ValueError):
        sample_category.add_product("Not a product")


def test_product_count(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert sample_category.product_count == 1
    sample_category.add_product(Product("Another", "Desc", 200.0, 5))
    assert sample_category.product_count == 2


def test_str(sample_category, sample_product):
    sample_category.add_product(sample_product)
    expected = "Test Category, количество продуктов: 10 шт."
    assert str(sample_category) == expected
