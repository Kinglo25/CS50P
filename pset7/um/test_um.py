from um import count

def test_count_with_valid_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um um um") == 3
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_count_unvalid_um():
    assert count("Yum!") == 0
    assert count("Yumi..") == 0
    assert count("ummmmm?") == 0

def test_count_no_um():
    assert count("Salut") == 0