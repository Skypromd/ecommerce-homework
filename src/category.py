from src.product import Product

class Category:
    counter = 0  # Класс-атрибут

    def __init__(self, name):
        self.name = name
        self.__products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.counter += 1  # Увеличиваем счетчик

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)

    @property
    def product_count(self):
        return len(self.__products)
