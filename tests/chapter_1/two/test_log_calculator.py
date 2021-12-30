import pytest

from exercises.chapter_1.two.log_calculator import LogCalculator


@pytest.mark.parametrize(
    "base, exp", [
        (2, 2), (2, 4), (2, 8), (2, 16),
        (3, 2), (3, 4), (3, 8), (3, 16),
        (4, 2), (4, 4), (4, 8), (4, 16),
        (5, 2), (5, 4), (5, 8), (5, 16),
        (6, 2), (6, 4), (6, 8), (6, 16),
        (7, 2), (7, 4), (7, 8), (7, 16),
        (8, 2), (8, 4), (8, 16),
    ]
)
def test_log_calc_is_correct(base, exp):
    log_x = pow(base, exp=exp)
    lc = LogCalculator(base=base)
    result = lc.algo(z=log_x >> 1, x=log_x)
    assert result == exp
