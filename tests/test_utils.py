<<<<<<< HEAD
import json
import pytest
from src.utils import create_categories_from_file
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


@pytest.fixture
def sample_json_file(tmp_path):
    data = [
        {
            "name": "Test Category",
            "description": "Test Description",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Test Desc",
                    "price": 1000.0,
                    "quantity": 5,
                },
                {
                    "name": "Test Smartphone",
                    "description": "Test Desc",
                    "price": 2000.0,
                    "quantity": 3,
                    "type": "Smartphone",
                    "efficiency": 90.0,
                    "model": "X",
                    "memory": 128,
                    "color": "Black",
                },
                {
                    "name": "Test Grass",
                    "description": "Test Desc",
                    "price": 300.0,
                    "quantity": 7,
                    "type": "LawnGrass",
                    "country": "Russia",
                    "germination_period": "7 days",
                    "color": "Green",
                },
            ],
        }
    ]
    file_path = tmp_path / "test.json"
=======
import pytest
import json
from src.utils import create_categories_from_file


@pytest.fixture
def temp_json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "products": [
                {
                    "type": "Smartphone",
                    "name": "Samsung Galaxy",
                    "description": "256GB",
                    "price": 150000.0,
                    "quantity": 5,
                    "efficiency": 90.0,
                    "model": "X",
                    "memory": 128,
                    "color": "Blue",
                }
            ],
        },
        {
            "name": "Трава",
            "products": [
                {
                    "type": "LawnGrass",
                    "name": "Green Grass",
                    "description": "Fast growing",
                    "price": 200.0,
                    "quantity": 10,
                    "country": "Russia",
                    "germination_period": "7 days",
                    "color": "Green",
                }
            ],
        },
    ]
    file_path = tmp_path / "test_data.json"
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


<<<<<<< HEAD
def test_create_categories_from_file(sample_json_file, capsys):
    categories = create_categories_from_file(sample_json_file)
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Test Category"
    assert categories[0].description == "Test Description"
    assert len(categories[0].products) == 3
    assert isinstance(categories[0].products[0], Product)
    assert isinstance(categories[0].products[1], Smartphone)
    assert isinstance(categories[0].products[2], LawnGrass)
    assert categories[0].products[0].name == "Test Product"
    assert categories[0].products[1].name == "Test Smartphone"
    assert categories[0].products[2].name == "Test Grass"
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert "Создан объект класса Smartphone" in captured.out
    assert "Создан объект класса LawnGrass" in captured.out
    assert "Товар 'Test Product' успешно добавлен в категорию" in captured.out


def test_create_categories_empty_file(tmp_path):
=======
def test_create_categories_from_file(temp_json_file):
    categories = create_categories_from_file(temp_json_file)
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 1
    product = categories[0].products[0]
    assert product.name == "Samsung Galaxy"
    assert product.description == "256GB"
    assert product.price == 150000.0
    assert product.quantity == 5
    assert str(product) == "Samsung Galaxy, 150000.0 руб. Остаток: 5 шт."

    assert categories[1].name == "Трава"
    assert len(categories[1].products) == 1
    grass = categories[1].products[0]
    assert grass.name == "Green Grass"
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert str(grass) == "Green Grass, 200.0 руб. Остаток: 10 шт."


def test_create_categories_empty_json(tmp_path):
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
    data = []
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    categories = create_categories_from_file(file_path)
    assert len(categories) == 0
<<<<<<< HEAD
=======


def test_create_categories_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("invalid json")
    with pytest.raises(json.JSONDecodeError):
        create_categories_from_file(file_path)


def test_create_categories_missing_keys(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy",
                    # Отсутствуют description, price, quantity
                }
            ],
        }
    ]
    file_path = tmp_path / "missing.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    with pytest.raises(KeyError):
        create_categories_from_file(file_path)
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
