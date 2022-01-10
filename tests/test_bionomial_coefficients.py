from exercises.chapter_1.two.binomial_coefficients import calculate_permutations


def test_calculate_permutations():
    assert calculate_permutations(n=9, k=2) == 36
