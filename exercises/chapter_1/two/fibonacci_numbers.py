def print_fibanacci_sequence(limit: int):
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    fib_idx = 2

    while fib_idx <= limit:
        fib_n = fib_n_minus_2 + fib_n_minus_1
        print(fib_idx, float(fib_n))
        fib_n_minus_2, fib_n_minus_1 = fib_n_minus_1, fib_n
        fib_idx += 1


if __name__ == "__main__":
    print_fibanacci_sequence(limit=1000)
