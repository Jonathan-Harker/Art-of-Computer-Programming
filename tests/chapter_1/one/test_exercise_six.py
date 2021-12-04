from exercises.chapter_1.one.exercise_six import EuclidsAlgorithmCounted


def test_euclids_algo_counted_returns_count():
    euclids_algo = EuclidsAlgorithmCounted()
    result = euclids_algo.euclids_algorithm_counted(m=5, n=5)
    assert result['counter'] == 1


def test_get_avg_times_run_returns_float():
    euclids_algo = EuclidsAlgorithmCounted()
    result = euclids_algo.get_average_times_run(max_m=5, n=5)
    assert isinstance(result, float)


def test_avg_times_when_n_is_five_and_m_is_four_equals_two():
    euclids_algo = EuclidsAlgorithmCounted()
    assert euclids_algo.get_average_times_run(max_m=4, n=5) == 2.0


def test_avg_times_when_n_is_five_and_m_is_twenty_equals_two_point_four():
    euclids_algo = EuclidsAlgorithmCounted()
    assert euclids_algo.get_average_times_run(max_m=20, n=5) == 2.4
