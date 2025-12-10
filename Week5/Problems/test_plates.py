import pytest
from plates import is_valid

#Tests that the valid plates returns true.
def test_valid():
    assert is_valid("AB") == True
    assert is_valid("AB12") == True
    assert is_valid("ABC123") == True
    assert is_valid("ABCDE1") == True
    assert is_valid("ABCDEF") == True

#Tests that the invalid plates returns false.
def test_invalid():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABC012") == False
    assert is_valid("123") == False
    assert is_valid("123ABC") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB!12.") == False
