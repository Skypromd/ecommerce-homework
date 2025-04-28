class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает текущую цену продукта.

        Returns:
            float: Цена продукта в рублях.
        """
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть отрицательной или равной нулю")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise ValueError(
                "Можно складывать только объекты класса Product или "
                "его наследников"
            )
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
            efficiency=product_data.get("efficiency", 0.0),
            model=product_data.get("model", "Unknown"),
            memory=product_data.get("memory", 0),
            color=product_data.get("color", "Unknown")
        )


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country,
                 germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
            country=product_data.get("country", "Unknown"),
            germination_period=product_data.get("germination_period",
                                                "Unknown"),
            color=product_data.get("color", "Unknown")
        )
