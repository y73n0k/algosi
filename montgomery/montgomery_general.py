def phi(x, y, R, N, N_):
    t = x * y
    res = (t + ((t % R) * N_ % R) * N) // R
    return res if res < N else res - N


def mult(x, y, R, RR, N, N_, phi):
    z = phi(x, y, R, N, N_)
    return phi(z, RR, R, N, N_)


def ring_mult(x, y, R, RR, N, N_, phi):
    a = phi(x, RR, R, N, N_)
    b = phi(y, RR, R, N, N_)
    return phi(a, b, R, N, N_)


def power(x, k, R, RR, N, N_, phi):
    x = phi(x, RR, R, N, N_)
    e = phi(1, RR, R, N, N_)
    for b in bin(k)[2:]:
        e = phi(e, e, R, N, N_)
        if b == '1':
            e = phi(x, e, R, N, N_)
    return phi(e, 1, R, N, N_)
