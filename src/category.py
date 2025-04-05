from src.product import Product

class Category:
    counter = 0

    def __init__(self, name):
        self.name = name
        self.__products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.counter += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self):
        return len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."