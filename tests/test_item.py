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
    assert Item.all[0].name.strip() == 'Item1'
    assert Item.all[1].price == 20.0
    assert int(Item.all[2].quantity) == 2

    # Тесты name_setter_max_length
    assert Item.all[0].name.strip() == 'Item1'
    assert Item.all[3].price == 0.0  # цена для Item.all[3] осталась 0.0

    # calculate_total_price правильно рассчитывает общую стоимость товара
    assert Item.all[0].calculate_total_price() == float(Item.all[0].quantity) * 10.0

