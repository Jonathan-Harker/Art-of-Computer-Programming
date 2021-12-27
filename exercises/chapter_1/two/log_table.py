from math import log


def make_log_table(base: int) -> dict:
    x = 2
    table = {}
    while x < 1000:
        table[x] = log(x / (x - 1), base)
        x *= 2
    return table
