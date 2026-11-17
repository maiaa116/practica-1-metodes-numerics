import numpy as np

# La funcio a resoldre es:
# (1 + 2*(r/2)) θ_i^{n+1} - (r/2)(θ_{i-1}^{n+1} + θ_{i+1}^{n+1}) = (1 - r) θ_i^n + (r/2)(θ_{i-1}^n + θ_{i+1}^n) + Δt̂

# Fem algunes substitucions i queda simplificat:
# (1 + 2a)x_i - a(x_{i-1} + x_{i+1}) = d_i

#Comencem definint la funcio de gauss seidel

def gauss_seidel(x, d, a, e_max=1e-12, it_max=100000):
    # x conte les temperatures dels punts interiors
    # d vector del terme independent
    # a = r/2
    # e_max error maxim entre dues passes per donar el bucle per terminat
    # it_max limit maxim de iteracions (per si no convergeix)

    M = len(x) # mida del sistema (punts interiors)

    for it in range(1, itmax + 1): # iteracions fins arribar a l'error desitjat
        error_maxim = 0.0 # comptador de error max a zero (important nombre decimal)

        for i in range(M): # recorre tots els punts interiors
            esq = x[i - 1] if i > 0 else 0.0  # busca el vei esquerre i si és el contron li asigna 0
            dre = x[i + 1] if i < M - 1 else 0.0 # lo mateix per al dret
            nou = (d[i] + a * (esq + dre)) / (1 + 2 * a) # nova temperatura del punt i
            # ara calculem el error de aquest punt respecte l'anterior i si supera al maxim antic l'actualitza
            error_maxim = max(error_maxim, abs(nou - x[i]))
            x[i] = nou # sobreescriu el valor antic i pel nou
        if error_maxim < e_max:
            return it # si el error maxim es menor que la tolerancia desitjada para el bucle i retorne quantes voltes ha donat
    raise RuntimeError("Gauss-Seidel no convergeix") # si es supera el nombre de iteracions maximes
