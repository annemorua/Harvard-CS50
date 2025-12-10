import pytest
from seasons import minutes, words
from datetime import date

#Tests if the "minutes" function is working.
def test_minutes():
    birth = date(2000, 12, 12)
    today = date(2024, 7, 4)
    assert minutes(birth, today) == 12391200

#Tests if the "words" function is working.
def test_words():
    assert words(12391200) == "twelve million, three hundred ninety-one thousand, two hundred"
