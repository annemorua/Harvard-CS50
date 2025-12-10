import pytest
from numb3rs import validate

#Tests that it is returning true when conditions are met.
def test_valid():
    assert validate("123.234.12.78") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

#Tests that it is returning false when conditions are not met.
def test_invalid():
    assert validate("12.34") == False
    assert validate("123.432.543.321") == False
    assert validate("256.23.34.456") == False
    assert validate("12.234.56.78.90") ==   False
    assert validate("cat") == False
    assert validate("12,23.45-56") == False
