from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello") == "Hll"
    assert shorten("AMAZON") == "MZN"

def test_shorten_empty_str():
    assert shorten("") == ""

def test_shorten_punction():
    assert shorten("Hi! Wow... How r u ?") == "H! Ww... Hw r  ?"

def test_shorten_numbers():
    assert shorten("C3PO and R2D2") == "C3P nd R2D2"
