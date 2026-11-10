from jacobi_symbol import jacobi_symbol
from random import randint
from math import gcd


def is_prime(N, iterations=100):
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    for _ in range(iterations):
        a = randint(1, N - 1)
        if gcd(a, N) != 1:
            return False
        if pow(a, (N - 1) // 2, N) != jacobi_symbol(a, N) % N:
            return False
    return True
