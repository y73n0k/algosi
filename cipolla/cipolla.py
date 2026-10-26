from random import randint


def sqrt_mod(a, p):
    if a == 0:
        return (0, )

    if pow(a, (p - 1) // 2, p) != 1:
        return None

    while True:
        b = randint(0, p - 1)
        D = (pow(b, 2, p) - 4 * a) % p
        if pow(D, (p - 1) // 2, p) == p - 1:
            break

    def mul(f1, f2):
        c1, c2 = f1
        d1, d2 = f2
        return ((c1 * d1 * b + c2 * d1 + c1 * d2) % p, (c2 * d2 - c1 * d1 * a) % p)

    base = (1, 0)
    res = (0, 1)
    for c in bin((p + 1) // 2)[2:]:
        res = mul(res, res)
        if c == "1":
            res = mul(base, res)
    assert res[0] == 0
    return (res[1], p - res[1])
