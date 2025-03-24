# tests/test_utils.py
import pytest
import json
from src.utils import create_categories_from_file

# Фикстура для создания временного файла с данными
@pytest.fixture
def temp_json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "products": [
                {"name": "Samsung Galaxy", "description": "256GB", "price": 150000.0, "quantity": 5}
            ]
        }
    ]
    file_path = tmp_path / "test_data.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    return file_path

# Тест утилитарной функции: Создание категорий из файла
def test_create_categories_from_file(temp_json_file):
    categories = create_categories_from_file(temp_json_file)
    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    assert "Samsung Galaxy, 150000.0 руб. Остаток: 5 шт." in categories[0].products
    assert categories[0].product_count == 1
