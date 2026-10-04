def phi(x, y, R, N, N_):
    b, n = R
    zi = 0
    for _ in range(n):
        x, xi = divmod(x, b)
        
        t = zi + xi * y
        zi = (t + ((t % b) * N_ % b) * N) // b

    return zi if zi < N else zi - N
