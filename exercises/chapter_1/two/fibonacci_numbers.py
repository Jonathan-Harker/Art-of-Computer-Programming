from math import sqrt

from utilities import is_prime

PHI = 0.5 * (1 + sqrt(5))


def print_fibanacci_sequence(limit: int):
    fib_n_minus_2 = 0
    fib_n_minus_1 = 0
    fib_idx = 1

    while fib_idx <= limit:
        fib_n = get_fib_n(fib_n_minus_1, fib_n_minus_2)
        gt = ((PHI ** fib_idx) / sqrt(5) > fib_n)
        print_fib(fib_idx, fib_n, gt)

        result_equal_to_square_of_n(fib_idx, fib_n)
        find_the_prime(fib_idx, fib_n)

        fib_idx, fib_n_minus_1, fib_n_minus_2 = change_variables(fib_idx, fib_n, fib_n_minus_1)


def find_the_prime(fib_idx, fib_n):
    if not is_prime(fib_idx):
        if is_prime(fib_n):
            print(f"FOUND THE PRIME - {fib_n}")


def change_variables(fib_idx, fib_n, fib_n_minus_1):
    fib_n_minus_2, fib_n_minus_1 = fib_n_minus_1, fib_n
    fib_idx += 1
    return fib_idx, fib_n_minus_1, fib_n_minus_2


def print_fib(fib_idx, fib_n, gt):
    print(fib_idx, float(fib_n), gt)


def get_fib_n(fib_n_minus_1, fib_n_minus_2):
    fib_n = fib_n_minus_2 + fib_n_minus_1

    if fib_n == 0:
        fib_n = 1

    return fib_n


def result_equal_to_square_of_n(fib_idx, fib_n):
    if fib_n == fib_idx ** 2:
        print(f"{fib_idx} squares are equal to the fibonacci number")


if __name__ == "__main__":
    print_fibanacci_sequence(limit=100)
