import random

from exercises.chapter_1.one.euclids_algorithm import euclids_algorithm


def run():
    int_1 = int(random.randint(1, 1000))
    int_2 = int(random.randint(1, 1000))
    return int_1, int_2, euclids_algorithm(int_1, int_2)


if __name__ == '__main__':
    result = (0, 0, 0)

    while result[2] < 4:
        result = run()

    print(
        f"n: {result[0]}, m: {result[1]}, result: {result[2]}"
    )
