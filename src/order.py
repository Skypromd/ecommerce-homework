from src.category import BaseEntity
from src.product import BaseProduct


class ZeroQuantityError(Exception):
    pass


class Order(BaseEntity):
    def __init__(self, name, description, product, quantity):
        super().__init__(name, description)
        if not isinstance(product, BaseProduct):
            raise ValueError(
                "В заказе должен быть объект класса Product или "
                "его наследников"
            )
        if quantity <= 0:
            raise ZeroQuantityError(
                "Товар с нулевым количеством не может быть "
                "добавлен в заказ"
            )
        self._name = name
        self._description = description
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (
            f"Заказ: {self.name}, Товар: {self.product.name}, "
            f"Количество: {self.quantity}, "
            f"Итоговая стоимость: {self.total_price} руб."
        )
