from src.item import Item
from src.keyboard import LanguageMixin

class Phone(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int, supported_sim_cards: int) -> None:
        super().__init__(name, price, quantity)
        self._supported_sim_cards = supported_sim_cards

    @property
    def number_of_sim(self):
        return self._supported_sim_cards

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._supported_sim_cards = value

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self._supported_sim_cards})"

    def __str__(self):
        return f"{self.name}"

