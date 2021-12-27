import json


class LogCalculator:
    def __init__(self, base: int):
        self.base = base
        self.y = 0
        self.k = 1

    def algo(self, x: int, z: int) -> float:
        if x == 1:
            return int(self.y)

        while x - z < 1:
            z >>= 1
            self.k += 1

        x -= z
        self.y += self.lookup_log(numerator=pow(base=2, exp=self.k))
        return self.algo(x=x, z=x >> self.k)

    def lookup_log(self, numerator: int) -> float:
        with open('log_constants.json', 'r') as f:
            table = json.load(f)

        return table[str(self.base)][str(numerator)]


if __name__ == "__main__":
    log_x = 8 * 8 * 8 * 8 * 8
    lc = LogCalculator(base=8)
    print(lc.algo(z=log_x >> 1, x=log_x))
