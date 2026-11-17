import numpy as np

# La funcio a resoldre es:
# (1 + 2*(r/2)) θ_i^{n+1} - (r/2)(θ_{i-1}^{n+1} + θ_{i+1}^{n+1}) = (1 - r) θ_i^n + (r/2)(θ_{i-1}^n + θ_{i+1}^n) + Δt̂

# Fem algunes substitucions i queda simplificat:
# (1 + 2a)x_i - a(x_{i-1} + x_{i+1}) = d_i

def gauss_seidel(x, d, a, e_max=1e-12, it_max=100000):
    # x conte les temperatures dels punts interiors
    # d vector del terme independent
    # a = r/2
    # e_max error maxim entre dues passes per donar el bucle per terminat
    # it_max limit maxim de iteracions (per si no convergeix)

    M = len(x) # mida del sistema (punts interiors)

    for it in range(1, itmax + 1):
        canvi = 0.0

        for i in range(M):
            esq = x[i - 1] if i > 0 else 0.0 
            dre = x[i + 1] if i < M - 1 else 0.0 
            nou = (d[i] + a * (esq + dre)) / (1 + 2 * a)
            canvi = max(canvi, abs(nou - x[i]))
            x[i] = nou
        if canvi < tol:
            return it
    raise RuntimeError("Gauss-Seidel no convergeix")
