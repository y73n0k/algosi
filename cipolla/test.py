from cipolla import sqrt_mod

from Crypto.Util.number import getPrime
from random import randint


for _ in range(300):
    p = getPrime(32)
    a = randint(0, p - 1)
    if pow(a, (p - 1) // 2, p) == p - 1:
        assert sqrt_mod(a, p) is None
    else:
        for v in sqrt_mod(a, p):
            assert pow(v, 2, p) == a
