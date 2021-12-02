def euclids_algorithm(m: int, n: int):
    if m % n == 0:
        return n

    return euclids_algorithm(m=n, n=m % n)
