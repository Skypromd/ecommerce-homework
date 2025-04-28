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
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


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
    data = []
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    categories = create_categories_from_file(file_path)
    assert len(categories) == 0


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
