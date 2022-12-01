import fuel, pytest

def test_convert():
    assert fuel.convert("10/100") == 10
    assert fuel.convert("100/100") == 100

def test_convert_zero_div():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_convert_no_int():
    with pytest.raises(ValueError):
        fuel.convert("a/b")

def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        fuel.convert("100/10")

def test_gauge():
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(50) == '50%'
    assert fuel.gauge(42) == '42%'

