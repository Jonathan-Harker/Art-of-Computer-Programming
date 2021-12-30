class OnlyOnes:
    def __init__(self, n: int, base: int) -> int:
        self.n = n
        self.base = base

    def make_only_ones(self, total=0, i=0):
        if i > self.n:
            return total

        return self.make_only_ones(total=total + pow(self.base, i), i=i + 1)


if __name__ == "__main__":
    ones = OnlyOnes(n=4, base=10)
    r = ones.make_only_ones()
    print(r)
