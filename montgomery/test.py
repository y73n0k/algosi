from montgomery_general import mult, power, ring_mult, phi
from util import get_coefs

from random import randint

###
print("test 1")
for _ in range(100):
    while True:
        N = randint(1, 1 << 32)
        R = N + randint(1, 1 << 32)

        try:
            RR, N_ = get_coefs(R, N)
            break
        except AssertionError:
            continue

    x, y = randint(0, N), randint(0, N)
    k = randint(0, 1 << 32)

    print(f"{N=}, {R=}, {x=}, {y=}, {k=}")
    assert mult(x, y, R, RR, N, N_, phi) == x * y % N
    assert ring_mult(x, y, R, RR, N, N_, phi) == x * y * R % N
    assert power(x, k, R, RR, N, N_, phi) == pow(x, k, N)


###
print("test 2")
from montgomery_bn import phi as phi_bn
from math import log, ceil


for _ in range(100):
    while True:
        N = randint(1, 1 << 32)
        b = randint(2, 1 << 8)
        n = ceil(log(N, b))

        R = (b, n)

        try:
            RR, N_ = get_coefs(R[0] ** R[1], N)
            break
        except AssertionError:
            continue


    x, y = randint(0, N), randint(0, N)
    k = randint(0, 1 << 32)

    print(f"{N=}, {R=}, {x=}, {y=}, {k=}")
    assert mult(x, y, R, RR, N, N_, phi_bn) == x * y % N
    assert ring_mult(x, y, R, RR, N, N_, phi_bn) == x * y * pow(R[0], R[1], N) % N
    assert power(x, k, R, RR, N, N_, phi_bn) == pow(x, k, N)


###
print("test 3")
from montgomery_2n import phi as phi_2n


for _ in range(100):
    N = randint(1, 1 << 32) | 1
    R = (2, N.bit_length())

    RR, N_ = get_coefs(R[0] ** R[1], N)

    x, y = randint(0, N), randint(0, N)
    k = randint(0, 1 << 32)

    print(f"{N=}, {R=}, {x=}, {y=}, {k=}")
    assert mult(x, y, R, RR, N, N_, phi_2n) == x * y % N
    assert ring_mult(x, y, R, RR, N, N_, phi_2n) == x * y * pow(R[0], R[1], N) % N
    assert power(x, k, R, RR, N, N_, phi_2n) == pow(x, k, N)
