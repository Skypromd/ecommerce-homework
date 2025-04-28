import pytest
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 1000.0, 10)


def test_new_product():
    product_dict = {
        "name": "New Product",
        "description": "New Desc",
        "price": 500.0,
        "quantity": 3,
    }
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
    assert "Цена не должна быть отрицательной или равной нулю" in captured.out
    assert sample_product.price == 2000


def test_str(sample_product):
    assert str(sample_product) == "Test Product, 1000.0 руб. Остаток: 10 шт."


def test_add():
    p1 = Product("P1", "Desc1", 100, 10)
    p2 = Product("P2", "Desc2", 200, 2)
    assert p1 + p2 == (100 * 10) + (200 * 2)  # 1400


def test_add_invalid_type(sample_product):
    with pytest.raises(ValueError):
        sample_product + "not a product"


def test_smartphone_add():
    s1 = Smartphone("S1", "Desc1", 100.0, 2, 90.0, "X", 64, "Blue")
    s2 = Smartphone("S2", "Desc2", 200.0, 3, 95.0, "Y", 128, "Red")
    assert s1 + s2 == (100 * 2) + (200 * 3)  # 800


def test_lawngrass_add():
    g1 = LawnGrass("G1", "Desc1", 50.0, 2, "Russia", "7 days", "Green")
    g2 = LawnGrass("G2", "Desc2", 75.0, 3, "USA", "5 days", "Dark Green")
    assert g1 + g2 == (50 * 2) + (75 * 3)  # 325


def test_add_different_classes():
    s = Smartphone("Phone", "Desc", 100.0, 1, 90.0, "X", 64, "Blue")
    g = LawnGrass("Grass", "Desc", 50.0, 2, "Russia", "7 days", "Green")
    with pytest.raises(TypeError):
        s + g


def test_add_product_subclass():
    p = Product("P", "Desc", 100.0, 1)
    s = Smartphone("S", "Desc", 200.0, 2, 90.0, "X", 64, "Blue")
    with pytest.raises(TypeError):  # Должна быть TypeError из-за type()
        p + s
