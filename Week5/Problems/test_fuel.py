import pytest
from fuel import convert, gauge

#Tests that the fracctions is made correctly.
def test_valid():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

#Tests that when the numeraor is greater than the denominator, the denominator is 0, or not a fraction, raises an error.
def test_invalid():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

#Tests that "gauge" returns teh percetage or the proper letter.
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(18) == "18%"
    assert gauge(31) == "31%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

