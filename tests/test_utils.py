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
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


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
    data = []
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    categories = create_categories_from_file(file_path)
    assert len(categories) == 0
