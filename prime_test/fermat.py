from random import randint
from math import gcd


def is_prime(N, iterations=100):
    for _ in range(iterations):
        a = randint(1, N - 1)
        if gcd(a, N) != 1:
            return False
        if pow(a, N - 1, N) != 1:
            return False
    return True
