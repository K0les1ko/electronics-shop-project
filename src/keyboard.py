from src.item import Item


class LanguageMixin:
    def change_lang(self) -> None:
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'




class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self._language = 'EN'  # Устанавливаем язык по умолчанию

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, value: str) -> None:
        if value not in {'EN', 'RU'}:
            raise ValueError("Unsupported language")
        self._language = value
