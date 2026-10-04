def get_coefs(R, N):
    a, b =  R, N
    s, t = 1, 0
    u, v = 0, 1

    while b != 0:
        q, r = divmod(a, b)
        s = s - q * t
        u = u - q * v

        s, t = t, s
        u, v = v, u
        a, b = b, r
    assert a == 1, "R and N must be coprime"

    return (R * R) % N, R-u
