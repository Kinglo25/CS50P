from numb3rs import validate

def test_validate_no_numbers():
    assert validate("abc.abc.abc.abc") == False
    assert validate("abc12.1.2.3") == False
    assert validate("cat") == False

def test_validate_out_of_bound():
    assert validate("1.2.3.4214124134") == False
    assert validate("512.512.512.512") == False

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("-123.255.255.255") == False
    assert validate("1.255xZX.255.255") == False
    assert validate("1.270.255.255") == False
