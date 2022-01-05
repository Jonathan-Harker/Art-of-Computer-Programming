from typing import List

from utilities import floor


class Factorial:
    def __init__(self, n: int):
        self.n = n

    def calculate_factorial(self):
        total = 1
        prime_products = []
        primes = self.get_primes()

        for prime in primes:
            power = self.sum_prime_factor(p=prime)
            total *= prime ** power
            prime_products.append(f"{prime} to the power of {power}")

        return prime_products, total

    def get_primes(self):
        return [p for p in self.prime_numbers() if self.n > p]

    def sum_prime_factor(self, p: int, k=1, total=0) -> int:
        if self.n < p ** k:
            return total

        total += floor(self.n / p ** k)
        return self.sum_prime_factor(p=p, k=k+1, total=total)

    def prime_numbers(self) -> List[int]:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
