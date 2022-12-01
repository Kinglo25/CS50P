import project as p
import pytest

b_0 = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
b_1 = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
b_2 = [['-', '-', '-'], ['-', '-', '-'], ['x', 'x', 'x']]
b_3 = [['-', '-', 'o'], ['-', 'o', '-'], ['o', '-', '-']]

def test_filled():
    assert p.filled(b_0) == False
    assert p.filled(b_1) == True
    assert p.filled(b_2) == False
    assert p.filled(b_3) == False

def test_player_has_won():
    assert p.player_has_won(b_0) == False
    assert p.player_has_won(b_1) == True
    assert p.player_has_won(b_2) == True
    assert p.player_has_won(b_3) == True

def test_already_used():
    assert p.already_used(b_0, 1, 1) == False
    assert p.already_used(b_1, 2, 1) == True
    assert p.already_used(b_2, 2, 2) == True
    assert p.already_used(b_3, 0, 0) == False
