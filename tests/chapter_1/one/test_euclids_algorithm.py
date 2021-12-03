from exercises.chapter_1.one.euclids_algorithm import euclids_algorithm


def test_119_544_returns_17():
    assert euclids_algorithm(119, 544) == 17

    
def test_6099_2166_returns_57():
    assert euclids_algorithm(6099, 2166) == 57
