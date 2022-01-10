import math

from exercises.chapter_1.two.factorial import Factorial


def assert_factorial_is_correct(n):
    fac = Factorial(n=n)
    result = fac.calculate_factorial()
    assert result[1] == math.factorial(n)


def test_calculate_factorial():
    assert_factorial_is_correct(2)
    assert_factorial_is_correct(7)
    assert_factorial_is_correct(200)


def test_sum_prime_factor_returns_correct_value():
    fac = Factorial(n=20)
    result = fac.sum_prime_factor(p=2)
    assert result == 18
