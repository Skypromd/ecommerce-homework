from src.product import Product


class Category:
    def __init__(self, name, description="", products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError(
                "Можно добавлять только объекты класса Product или "
                "его наследников"
            )
        self.products.append(product)

    @property
    def product_count(self):
        return len(self.products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
