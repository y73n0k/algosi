from random import randint
from math import gcd


def is_prime(N, iterations=100):
    if N == 1:
        return False

    t = 0
    u = N - 1
    while u & 1 == 0:
        t += 1
        u >>= 1
    for _ in range(iterations):
        a = randint(1, N - 1)
        if gcd(a, N) != 1:
            return False

        a = pow(a, u, N)
        for k in range(t, -1, -1):
            val = pow(a, 1 << k, N)
            if val == 1:
                continue
            if val == N - 1:
                break
            return False
    return True
