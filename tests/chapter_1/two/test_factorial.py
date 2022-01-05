import math

from exercises.chapter_1.two.factorial import Factorial


def test_sum_prime_factor_returns_correct_value():
    fac = Factorial(n=20)
    result = fac.sum_prime_factor(p=2)
    assert result == 18


def test_calculate_factorial():
    fac = Factorial(n=200)
    result = fac.calculate_factorial()
    assert result[1] == math.factorial(200)
