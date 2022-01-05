from typing import Union

from utilities import floor


def calculate_modulus(
        x: Union[float, int],
        y: Union[float, int]
) -> float:

    if y == 0:
        return x

    modulus = x - (y * floor(x/y))
    return round(modulus, 2)
