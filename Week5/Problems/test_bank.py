import pytest
from bank import value

#Tests if the greeting starts with "hello".
def test_hello():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"
    assert value("hello, YOU.") == "$0"

#Tests if the greeting starts with "h".
def test_h():
    assert value("hi") == "$20"
    assert value("HEY THERE!") == "$20"
    assert value("How are you") == "$20"

#Tests if the user write something else.
def test_else():
    assert value("greetings") == "$100"
    assert value("31") == "$100"
