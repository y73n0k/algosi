from fermat import is_prime as f_is_prime
from solovey_shtrassen import is_prime as ss_is_prime
from miller_rabin import is_prime as mr_is_prime

from random import getrandbits

for _ in range(100):
    v = getrandbits(32)
    assert mr_is_prime(v) == ss_is_prime(v) == f_is_prime(v)
