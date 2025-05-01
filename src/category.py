from abc import ABC, abstractmethod
from src.product import Product


class ZeroQuantityError(Exception):
    pass


class BaseEntity(ABC):
    @abstractmethod
    def __init__(self, name, description):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass


class Category(BaseEntity):
    def __init__(self, name, description="", products=None):
        self._name = name
        self._description = description
        self.products = products if products is not None else []

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def add_product(self, product):
        print("Начало обработки добавления товара")
        try:
            if not isinstance(product, Product):
                raise ValueError(
                    "Можно добавлять только объекты класса Product или "
                    "его наследников"
                )
            if product.quantity <= 0:
                raise ZeroQuantityError(
                    "Товар с нулевым количеством не может быть добавлен "
                    "в категорию"
                )
            self.products.append(product)
            print(f"Товар '{product.name}' успешно добавлен в категорию")
        except (ValueError, ZeroQuantityError) as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def product_count(self):
        return len(self.products)

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
