import pytest
from working import convert

#Tests if the input has hours with colons.
def test_colon():
    assert convert("9:40 AM to 11:20 AM") == "09:40 to 11:20"
    assert convert("10:45 AM to 3:10 PM") == "10:45 to 15:10"
    assert convert("2:30 PM to 9:50 PM") == "14:30 to 21:50"

#Tests if the input has hours without colons.
def test_nocolon():
    assert convert("9 AM to 11 AM") == "09:00 to 11:00"
    assert convert("10 AM to 3 PM") == "10:00 to 15:00"
    assert convert("2 PM to 9 PM") == "14:00 to 21:00"

#Tests the two previous cases at the same time.
def test_mixed():
    assert convert("3 AM to 8:10 AM") == "03:00 to 08:10"
    assert convert("11:35 AM to 4 PM") == "11:35 to 16:00"
    assert convert("1 PM to 7:08 PM") == "13:00 to 19:08"

#Tests that it raises an error if the input is not adequate.
def test_no():
    with pytest.raises(ValueError):
        convert("11:34 AM 2:45 PM")
    with pytest.raises(ValueError):
        convert("4:68 AM to 7 PM")
    with pytest.raises(ValueError):
        convert("8:41 to 11:30")
