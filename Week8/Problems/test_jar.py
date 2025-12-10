import pytest
from jar import Jar

#Tests that the "__init__" function is working.
def test_init():
    with pytest.raises(ValueError):
        Jar(-31)

    with pytest.raises(ValueError):
        Jar("cat")

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(8)
    assert jar.capacity == 8
    assert jar.size == 0

#Tests that the "__str__" is working.
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

#Tests that the "deposit" function is working.
def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(9)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)

    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit(4)

#Tests that the withdraw function is working.
def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(5)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)

    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.withdraw(5)
