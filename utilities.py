def floor(n: float) -> int:
    r = int(n)
    return r if r == n or n >= 0 else r - 1


def print_primes_from_2(limit=500):
    primes = [2]

    for possible_prime in range(3, limit):
        if is_prime(possible_prime):
            primes.append(possible_prime)

    print(primes)


def is_prime(possible_prime):
    is_prime_number = True
    for i in range(2, possible_prime):
        if possible_prime % i == 0:
            is_prime_number = False
    return is_prime_number
