# calculate log2(16) - logb(x)
# input
from math import log

b = 2


def start(x):
    y = 0
    z = x >> 1
    k = 1

    return y, z, x, k


def algo(y, z, x, k):
    if x == 1:
        print(y)
        exit(0)

    while x - z < 1:
        z >>= 1
        k += 1

    x -= z
    z = x >> k
    two_k = pow(base=2, exp=k)
    y += log(two_k / (two_k - 1), b)
    # y += get_log(int(two_k / (two_k - 1)))
    return algo(y, z, x, k)


def get_log(x):
    y, z, x, k = start(x=x)
    algo(y, z, x, k)


get_log(x=2)
