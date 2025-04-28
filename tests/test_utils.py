import json

import pytest

from src.utils import create_categories_from_file


@pytest.fixture
def temp_json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy",
                    "description": "256GB",
                    "price": 150000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


def test_create_categories_from_file(temp_json_file):
    categories = create_categories_from_file(temp_json_file)
    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 1
    product = categories[0].products[0]
    assert product.name == "Samsung Galaxy"
    assert product.description == "256GB"
    assert product.price == 150000.0
    assert product.quantity == 5
    assert str(product) == "Samsung Galaxy, 150000.0 руб. Остаток: 5 шт."
