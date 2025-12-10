import pytest
from um import count

#Tests that the word alone works.
def test_solo():
    assert count("um, um") == 2
    assert count("um um yes") == 2

#Tests that if a word contains "um" in it, it does not count it.
def test_words():
    assert count("yummy gummy") == 0
    assert count("hummy bird") == 0

#Tests with capital letters and punctuation marks.
def test_mayus():
    assert count("UM NO") == 1
    assert count("hello, UM, WORD") == 1

