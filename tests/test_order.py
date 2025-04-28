import pytest
from src.order import Order, ZeroQuantityError
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 1000.0, 10)


def test_order_creation(sample_product):
    order = Order("Test Order", "Test Description", sample_product, 3)
    assert order.name == "Test Order"
    assert order.description == "Test Description"
    assert order.product == sample_product
    assert order.quantity == 3
    assert order.total_price == 3000.0


def test_order_invalid_product():
    with pytest.raises(ValueError):
        Order("Test Order", "Test Description", "not a product", 3)


def test_order_invalid_quantity():
    order_product = Product("Test", "Desc", 1000.0, 10)
    with pytest.raises(ZeroQuantityError):
        Order("Test Order", "Test Description", order_product, 0)


def test_order_str(sample_product):
    order = Order("Test Order", "Test Description", sample_product, 3)
    expected = (
        "Заказ: Test Order, Товар: Test Product, Количество: 3, "
        "Итоговая стоимость: 3000.0 руб."
    )
    assert str(order) == expected
