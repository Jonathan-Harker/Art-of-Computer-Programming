import math

import numpy


class Primes:
    def __init__(self, limit=500):
        self.limit = limit
        self.primes = numpy.empty(limit, int)
        self.primes[0] = 2
        self.n = 3
        self.j = 0

    def get_primes_numbers(self):
        increment_number = True
        is_prime = True
        index = 1

        while self.j < self.limit - 1:
            if is_prime:
                self.add_prime()

            while True:
                if not increment_number:
                    increment_number = True
                else:
                    self.n += 2
                    index = 1

                q, remainder = self.divide_num_by_prime_factor(index)
                if remainder != 0:
                    break

            if q > self.primes[index]:
                index += 1
                increment_number = False
                is_prime = False
            else:
                is_prime = True

    def add_prime(self):
        self.j += 1
        self.primes[self.j] = self.n

    def divide_num_by_prime_factor(self, k):
        div = self.n / self.primes[k]
        q = math.floor(div)
        r = self.n - (q * self.primes[k])
        return q, r


if __name__ == "__main__":
    primes = Primes(limit=100)
    primes.get_primes_numbers()
    print(list(primes.primes))
