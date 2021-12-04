from exercises.chapter_1.one.exercise_one import rearrange_numbers


def test_rearrange_ints_are_correct():
    input_array = [1, 2, 3, 4]
    output_array = [2, 3, 4, 1]
    assert rearrange_numbers(input_array) == output_array
