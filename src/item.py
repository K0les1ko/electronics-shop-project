import csv
import json

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Unsupported operand type. You can only add Item instances.")

    def __repr__(self):
        """
        Магический метод для представления объекта в виде строки, которая может быть использована для его воссоздания.
        """
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __str__(self):
        """
        Магический метод для представления объекта в виде читаемой строки.
        """
        return f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return float(self.price) * float(self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        cls.all = []  # Очистка списка all
        with open(filename, 'r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            print(reader)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = str(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Преобразует строку в число.

        :param value: Строка, представляющая число.
        :return: Преобразованное число.
        """
        try:
            if value is not None and value.strip():
                return int(float(value))  # Преобразование строки в int после float
            else:
                return 0.0
        except ValueError:
            return 0.0

    def to_json(self, filename):
        item_data = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
