from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
<<<<<<< HEAD
        _ = name, description, price, quantity  # Заглушка для параметров
=======
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class LogMixin:
    def __init__(self, *args, **kwargs):
        print(
            f"Создан объект класса {self.__class__.__name__} "
            f"с параметрами: {args}, {kwargs}"
        )
        super().__init__(*args, **kwargs)


class Product(LogMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )
        super().__init__(name, description, price=price, quantity=quantity)
        self._name = name
        self._description = description
        self._price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
<<<<<<< HEAD
=======
        """Возвращает текущую цену продукта.

        Returns:
            float: Цена продукта в рублях.
        """
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
<<<<<<< HEAD
            print("Цена не должна быть отрицательной или равной нулю")
=======
            print(
                "Цена не должна быть отрицательной или равной нулю"
            )
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
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
<<<<<<< HEAD
    def __init__(self, name, description, price, quantity, efficiency, model,
                 memory, color):
=======
    def __init__(self, name, description, price, quantity, efficiency,
                 model, memory, color):
>>>>>>> 642f89ce80d8db31d33a4c99a66dee00e8899ae7
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
            germination_period=product_data.get(
                "germination_period", "Unknown"
            ),
            color=product_data.get("color", "Unknown")
        )
