import pytest
from src.keyboard import Keyboard


def test_keyboard_initial_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    kb.change_lang()
    assert kb.language == 'RU'

    kb.change_lang()
    assert kb.language == 'EN'


def test_keyboard_set_invalid_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    with pytest.raises(ValueError, match="Unsupported language"):
        kb.language = 'CH'
