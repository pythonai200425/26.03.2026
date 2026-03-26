
# TEST DRIVEN DEVELOPMENT
import pytest
from rectangle import Rectangle

def test_hekef_small_numbers():
    rectangle = Rectangle(2, 3)

    actual = rectangle.get_hekef()
    expected = (2 + 3) * 2

    assert expected == actual

def test_area_small_numbers():
    rectangle = Rectangle(2, 3)

    actual = rectangle.get_area()
    expected = 2 * 3

    assert expected == actual


