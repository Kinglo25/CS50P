from jar import Jar
import pytest

def test_init():
    jar = Jar(42)
    assert jar.capacity == 42


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(42)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(11)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(42)
