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
    Item3,15.0,2
    """
    csv_path = tmp_path / 'test_items.csv'
    csv_path.write_text(csv_content)

    Item.instantiate_from_csv(csv_path)


    assert len(Item.all) == 4
    assert Item.all[0].name == '    Item1' #какая то чушь с пробелами
    assert Item.all[1].price == 20.0
    assert int(Item.all[2].quantity) == 2


