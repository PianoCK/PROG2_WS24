# test_calc.py
from calc import add


def test_add():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -2) == -4
