from jacobi_symbol import jacobi_symbol

from Crypto.Util.number import getPrime
from random import randint


lt = lambda x, p: (2 * pow(x, (p - 1) // 2, p) - p) // (2 - p)

for _ in range(100):
    p = getPrime(32)
    a = randint(1, p - 1)
    assert lt(a, p) == jacobi_symbol(a, p)


assert jacobi_symbol(2, 15) == 1
assert jacobi_symbol(10, 21) == -1
assert jacobi_symbol(5, 21) == 1