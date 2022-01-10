from exercises.chapter_1.two.factorial import Factorial


def print_table(n: int, start: int = 0):
    permutations = store_permutations(n=n, start=start)
    for row in permutations:
        print(row)


def store_permutations(n: int, start: int) -> list:
    table = []
    for i in range(start, n + 1):

        row = []
        for j in range(start, n + 1):
            if i >= j:
                row.append(calculate_permutations(i, j))
            else:
                row.append(0)

        table.append(row)
    return table


def calculate_permutations(n: int, k: int):
    n_fac = Factorial(n).calculate_factorial()[1]
    k_fac = Factorial(k).calculate_factorial()[1]
    diff_fac = Factorial(n - k).calculate_factorial()[1]
    return int(n_fac / (k_fac * diff_fac))


class Permutations:
    def __init__(self):
        self.factors_1 = None
        self.factors_2 = None

    def permutations_as_prime_number_products(self, n: int, k: int):
        self.factors_1 = Factorial(k).calculate_factorial()[0]
        self.factors_2 = Factorial(n - k).calculate_factorial()[0]
        k_diff = self.merge_factors("+")

        self.factors_1 = Factorial(n).calculate_factorial()[0]
        self.factors_2 = k_diff
        return self.merge_factors("-")

    def merge_factors(self, operator: str) -> dict:
        result = {}
        for key in self.factors_1:
            if key in self.factors_2:
                if operator == "+":
                    self.add_factors(key, result)
                if operator == "-":
                    self.deduct_factors(key, result)
                if result[key] == 0:
                    result.pop(key)
            else:
                result[key] = self.factors_1[key]

        if operator == "+":
            self.add_missing_keys(result)

        return result

    def add_factors(self, key: str, result: dict):
        result[key] = self.factors_1[key] + self.factors_2[key]

    def deduct_factors(self, key: str, result: dict):
        result[key] = self.factors_1[key] - self.factors_2[key]

    def add_missing_keys(self, result):
        for key in self.factors_2:
            if key not in result:
                result[key] = self.factors_2[key]


if __name__ == "__main__":
    print(calculate_permutations(52, 13))
    print(Permutations().permutations_as_prime_number_products(52, 13))
    print_table(n=10)
