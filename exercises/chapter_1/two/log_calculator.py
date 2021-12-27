import json
import os.path


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
        this_dir = os.path.dirname(os.path.realpath(__file__))
        with open(f'{this_dir}/log_constants.json', 'r') as f:
            table = json.load(f)

        return table[str(self.base)][str(numerator)]


if __name__ == "__main__":
    base = 15
    log_x = pow(base, exp=7)
    lc = LogCalculator(base=base)
    print(lc.algo(z=log_x >> 1, x=log_x))
