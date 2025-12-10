import pytest
from twttr import shorten

#Tests that it is returning the tweets without vowels.
def test_vowels():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("lower UPPER") == "lwr PPR"
    assert shorten("aeiouAEIOU") == ""
    assert shorten("31") == "31"
    assert shorten("Hello there!") == "Hll thr!"
