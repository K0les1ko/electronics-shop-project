from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.name) == "Dark Project KD87A"

    assert str(kb._language) == "EN"

    kb.change_lang()
    assert str(kb._language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb._language) == "EN"

    kb._language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter
