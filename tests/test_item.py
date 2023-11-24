import csv
import os
import pytest
from src.item import Item, InstantiateCSVError

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

def test_calculate_total_price(sample_item):
    assert sample_item.calculate_total_price() == 50.0

def test_apply_discount(sample_item):
    sample_item.apply_discount()
    assert sample_item.price == 10.0

def test_instantiate_from_csv_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError, match="Отсутствует файл items.csv"):
        Item.instantiate_from_csv()



def test_instantiate_from_csv_successful(tmp_path):
    csv_content = """name,price,quantity
    Item1,10.0,5
    Item2,20.0,3
    Item3,15.0,2
    """
    csv_path = tmp_path / 'test_items.csv'
    csv_path.write_text(csv_content)

    try:
        Item.instantiate_from_csv(csv_path)
        assert len(Item.all) == 4
    finally:
        csv_path.unlink()