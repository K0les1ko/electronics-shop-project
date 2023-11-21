import pytest
from src.phone import Phone

@pytest.fixture
def sample_phone():
    return Phone("SamplePhone", 500.0, 3, 2)

def test_repr(sample_phone):
    assert repr(sample_phone) == "Phone('SamplePhone', 500.0, 3, 2)"

def test_str(sample_phone):
    assert str(sample_phone) == "SamplePhone"

def test_number_of_sim_property(sample_phone):
    assert sample_phone.number_of_sim == 2

def test_number_of_sim_setter(sample_phone):
    sample_phone.number_of_sim = 4
    assert sample_phone.number_of_sim == 4

def test_number_of_sim_setter_invalid(sample_phone):
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        sample_phone.number_of_sim = 0