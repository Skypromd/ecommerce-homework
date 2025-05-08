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


<<<<<<< HEAD
def test_new_product_empty_description():
    product_dict = {
        "name": "Minimal",
        "description": "",
        "price": 100.0,
        "quantity": 1
    }
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Minimal"
    assert new_product.description == ""
    assert new_product.price == 100.0
    assert new_product.quantity == 1


def test_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Invalid", "Desc", 1000.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(
        exc_info.value
    )
=======
def test_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Invalid", "Desc", 1000.0, 0)
    assert ("Товар с нулевым количеством не может быть "
            "добавлен") in str(exc_info.value)
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7


def test_price_setter(sample_product, capsys):
    sample_product.price = 2000
    assert sample_product.price == 2000
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть отрицательной или равной нулю" in captured.out
    assert sample_product.price == 2000


def test_price_setter_valid(sample_product):
    sample_product.price = 1500
    assert sample_product.price == 1500


def test_price_setter_zero(sample_product, capsys):
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть отрицательной или равной нулю" in captured.out
    assert sample_product.price == 1000.0


<<<<<<< HEAD
def test_price_setter_negative(sample_product, capsys):
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть отрицательной или равной нулю" in captured.out
    assert sample_product.price == 1000.0


=======
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
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
    with pytest.raises(TypeError):
        p + s


def test_smartphone_new_product():
    product_dict = {
        "name": "Test Smartphone",
        "description": "Test Desc",
        "price": 1000.0,
        "quantity": 5,
        "efficiency": 90.0,
        "model": "X",
        "memory": 128,
<<<<<<< HEAD
        "color": "Black"
=======
        "color": "Black",
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    }
    new_product = Smartphone.new_product(product_dict)
    assert new_product.name == "Test Smartphone"
    assert new_product.description == "Test Desc"
    assert new_product.price == 1000.0
    assert new_product.quantity == 5
    assert new_product.efficiency == 90.0
    assert new_product.model == "X"
    assert new_product.memory == 128
    assert new_product.color == "Black"


def test_lawngrass_new_product():
    product_dict = {
        "name": "Test Grass",
        "description": "Test Desc",
        "price": 200.0,
        "quantity": 10,
        "country": "Russia",
        "germination_period": "7 days",
<<<<<<< HEAD
        "color": "Green"
=======
        "color": "Green",
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    }
    new_product = LawnGrass.new_product(product_dict)
    assert new_product.name == "Test Grass"
    assert new_product.description == "Test Desc"
    assert new_product.price == 200.0
    assert new_product.quantity == 10
    assert new_product.country == "Russia"
    assert new_product.germination_period == "7 days"
    assert new_product.color == "Green"


def test_log_mixin(capsys):
    product = Product("Log Test", "Test Desc", 1000.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert "Log Test" in captured.out
    assert "Test Desc" in captured.out
    assert "1000.0" in captured.out
    assert "5" in captured.out
    assert product.name == "Log Test"
    assert product.description == "Test Desc"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_log_mixin_smartphone(capsys):
    smartphone = Smartphone("S1", "Desc1", 100.0, 2, 90.0, "X", 64, "Blue")
    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone" in captured.out
    assert "S1" in captured.out
    assert "Desc1" in captured.out
    assert "100.0" in captured.out
    assert "2" in captured.out
    assert smartphone.name == "S1"
    assert smartphone.efficiency == 90.0
    assert smartphone.model == "X"
    assert smartphone.memory == 64
    assert smartphone.color == "Blue"


def test_log_mixin_lawngrass(capsys):
    grass = LawnGrass("G1", "Desc1", 50.0, 2, "Russia", "7 days", "Green")
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out
    assert "G1" in captured.out
    assert "Desc1" in captured.out
    assert "50.0" in captured.out
    assert "2" in captured.out
    assert grass.name == "G1"
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "Green"


<<<<<<< HEAD
=======
def test_new_product_minimal():
    product_dict = {"name": "Minimal", "description": "",
                    "price": 100.0, "quantity": 1}
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Minimal"
    assert new_product.description == ""
    assert new_product.price == 100.0
    assert new_product.quantity == 1


def test_add_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("P1", "Desc1", 100, 0)
    assert ("Товар с нулевым количеством не может "
            "быть добавлен") in str(exc_info.value)


>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
def test_add_zero_price():
    p1 = Product("P1", "Desc1", 0, 10)
    p2 = Product("P2", "Desc2", 0, 2)
    assert p1 + p2 == 0
<<<<<<< HEAD


def test_smartphone_attributes():
    smartphone = Smartphone("S1", "Desc1", 100.0, 2, 90.0, "X", 64, "Blue")
    assert smartphone.efficiency == 90.0
    assert smartphone.model == "X"
    assert smartphone.memory == 64
    assert smartphone.color == "Blue"


def test_lawngrass_attributes():
    grass = LawnGrass("G1", "Desc1", 50.0, 2, "Russia", "7 days", "Green")
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "Green"


def test_smartphone_new_product_empty_fields():
    product_dict = {
        "name": "Test Smartphone",
        "description": "Test Desc",
        "price": 1000.0,
        "quantity": 5
    }
    new_product = Smartphone.new_product(product_dict)
    assert new_product.efficiency == 0.0
    assert new_product.model == "Unknown"
    assert new_product.memory == 0
    assert new_product.color == "Unknown"


def test_lawngrass_new_product_empty_fields():
    product_dict = {
        "name": "Test Grass",
        "description": "Test Desc",
        "price": 200.0,
        "quantity": 10
    }
    new_product = LawnGrass.new_product(product_dict)
    assert new_product.country == "Unknown"
    assert new_product.germination_period == "Unknown"
    assert new_product.color == "Unknown"
=======
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
