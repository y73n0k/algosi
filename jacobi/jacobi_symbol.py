from math import gcd


def jacobi_symbol(a, b):
    assert b & 1, "b must be odd"
    assert gcd(a, b) == 1, "(a, b) must be 1"

    res = 0
    while b != 1:
        a %= b
        t = 0
        c = a
        if (a << 1) >= b:
            a = a - b
            t = 1
            c = -a

        k = 0
        while not c & 1:
            c >>= 1
            k += 1

        if k & 1:
            t_b = b & 0b1111
            res ^= ((t_b ** 2 - 1) >> 3) & 1

        if t:
            t_b = b & 0b11
            res ^= ((t_b - 1) >> 1) & 1

        t_c = c & 0b111
        t_b = b & 0b111
        res ^= ((t_c - 1) * (t_b - 1) >> 2) & 1

        a, b = b, c

    return 1 - (res << 1)
