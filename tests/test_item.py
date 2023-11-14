import pytest
from src.item import Item

@pytest.fixture
def sample_item():
    return Item(name='SampleItem', price=10.0, quantity=5)

def test_repr(sample_item):
    assert repr(sample_item) == "Item(name=SampleItem, price=10.0, quantity=5)"

def test_str(sample_item):
    assert str(sample_item) == "Item: SampleItem, Price: 10.0, Quantity: 5"

def test_name_property(sample_item):
    assert sample_item.name == 'SampleItem'

def test_name_setter(sample_item):
    sample_item.name = 'NewName'
    assert sample_item.name == 'NewName'

def test_name_setter_max_length(sample_item):
    sample_item.name = 'ThisNameIsTooLong'
    assert sample_item.name == 'ThisNameIs'


def test_instantiate_from_csv(tmp_path):
    csv_content = """name,price,quantity
    Item1,10.0,5
    Item2,20.0,3
    Item3,15.0,7
    """
    csv_path = tmp_path / 'test_items.csv'
    csv_path.write_text(csv_content)

    Item.instantiate_from_csv(csv_path)


    assert len(Item.all) == 3
    assert Item.all[0].name == 'Item1'
    assert Item.all[1].price == 20.0
    assert Item.all[2].quantity == 7

@staticmethod
def string_to_number(value: str) -> float:
    """
    Преобразует строку в число.

    :param value: Строка, представляющая число.
    :return: Преобразованное число.
    """
    try:
        if value is not None and value.strip():
            return float(value)
        else:
            return 0.0
    except ValueError:
        return 0.0
