from math import log

from exercises.chapter_1.two.calculate_modulus import calculate_modulus, floor


def assert_modulus(x, y, expected):
    assert calculate_modulus(x, y) == expected


def test_calculate_modulus():
    assert_modulus(100, 3, 1)
    assert_modulus(100, 7, 2)
    assert_modulus(-100, 7, 5)
    assert_modulus(-100, 0, -100)
    assert_modulus(5, -3, -1)
    assert_modulus(18, -3, 0)
    assert_modulus(-2, -3, -2)
    assert_modulus(1.1, 1, 0.1)
    assert_modulus(0.11, 0.1, 0.01)
    assert_modulus(0.11, -0.1, -0.09)


def test_floor():
    assert floor(1.1) == 1
    assert floor(-1.1) == -2
    assert floor(0.99999) == 0
    assert floor(log(35, 2)) == 5
