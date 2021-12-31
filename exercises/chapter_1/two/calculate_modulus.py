from typing import Union


def calculate_modulus(
        x: Union[float, int],
        y: Union[float, int]
) -> float:

    if y == 0:
        return x

    modulus = x - (y * floor(x/y))
    return round(modulus, 2)


def floor(n: float) -> int:
    r = int(n)
    return r if r == n or n >= 0 else r - 1
