import json


def algo(y: int, z: int, x: int, k: int, base: int) -> float:
    if x == 1:
        return int(y)

    while x - z < 1:
        z >>= 1
        k += 1

    x -= z
    z = x >> k
    two_k = pow(base=2, exp=k)
    y += lookup_log(numerator=two_k, base=base)
    return algo(y, z, x, k, base)


def lookup_log(numerator: int, base: int) -> float:
    with open('log_constants.json', 'r') as f:
        table = json.load(f)

    return table[str(base)][str(numerator)]


if __name__ == "__main__":
    log_x = 8 * 8 * 8 * 8 * 8
    print(algo(y=0, z=log_x >> 1, x=log_x, k=1, base=8))
