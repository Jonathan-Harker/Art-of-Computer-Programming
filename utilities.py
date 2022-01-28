def floor(n: float) -> int:
    r = int(n)
    return r if r == n or n >= 0 else r - 1


def get_primes_from_2(limit=500) -> list:
    primes = [2]

    for possible_prime in range(3, limit):
        if is_prime(possible_prime):
            primes.append(possible_prime)

    return primes


def is_prime(possible_prime):
    is_prime_number = True
    for i in range(2, possible_prime):
        if possible_prime % i == 0:
            is_prime_number = False
    return is_prime_number

def get_sorted_list_neighbours(l: list, i: int) -> tuple:
    idx = 1
    for idx, v in enumerate(l):
        if i < v:
            break

    return l[idx - 1], l[idx]
