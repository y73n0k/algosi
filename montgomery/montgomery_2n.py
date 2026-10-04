def phi(x, y, R, N, N_):
    _, n = R
    zi = 0
    for _ in range(n):
        xi = x & 1
        x >>= 1
        
        t = zi + xi * y
        if t & 1:
            zi = (t + N) >> 1
        else:
            zi = t >> 1

    return zi if zi < N else zi - N
