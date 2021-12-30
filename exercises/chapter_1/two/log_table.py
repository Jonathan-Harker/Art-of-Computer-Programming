import json
from math import log


def store_log_constants():
    log_constants = {}
    for i in range(2, 100):
        log_table = make_log_table(base=i)
        log_constants[i] = log_table

    with open('log_constants.json', 'w') as f:
        json.dump(log_constants, f)


def make_log_table(base: int) -> dict:
    x = 2
    table = {}
    while x <= 1024:
        table[x] = log(x / (x - 1), base)
        x *= 2
    return table


if __name__ == "__main__":
    store_log_constants()
