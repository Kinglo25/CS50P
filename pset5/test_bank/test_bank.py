from bank import value

def test_value():
    assert value("Hey!") == 20
    assert value("Hello") == 0
    assert value("H0w 4re u?") == 20
    assert value("Salut!") == 100
