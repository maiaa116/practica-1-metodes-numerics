import numpy as np
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt

def crank_nicolson(N, ta, lamb):
    #malla:
    x=np.linspace(0,1,N)
    dx=x[1]-x[0]
    dt=lamb*(dx**2)

    #num pasos:
    n_pasos=int(np.round(ta/dt))

    #condicions inicials:
    #creem un vector amb N components (punts de la malla espaial) tots iguals a la condició inicial que es zero
    f = np.zeros(N, dtype=float)

    # creem la matriu que ens acobla els temps passats i futurs per trobar la temperatura actual, utilitzant solve_banded que evita fer files llarguissimes de zeros
    # agafa les diagonals i les fica horitzontals
    M = N - 2 # nombre de nodes interiors, els exteriors no els modifiquem
    ab = np.zeros((3, M))  # taula buida de 3 files i M columnes on ficarem les diagonals
    ab[0, 1:] = -0.5 * lamb       # diagonal superior, comença en la fila 0 i recorre de la columna 1 fins al final
    ab[1, :]  =  1.0 + lamb       # diagonal principal, comença en la fila 1 i recorre totes les columnes
    ab[2, :-1] = -0.5 * lamb      # diagonal inferior, comença en la fila 2 i recorre del principi a la penultima columna

    # fem el bucle temporal que resol la part dreta de la igualtat
    for _ in range(n_pasos):
        # gracies a la nostra adimensionalització q=1 i es simplifica molt el codi
        dreta = (0.5 * lamb * f[:-2] + (1.0 - lamb) * f[1:-1] +  0.5 * lamb * f[2:] + dt) #incloses les condicions de contorn del passat

        # no cal que introduim les condicions de contorn del futur tot i que no estiguin incloses en A, ja que son nules i en estar sumant no aporten res.

        # resolem el sistema A*f_int^(n+1)=dreta per actualitzar el vector de temperatures a l'instant n+1
        # utilitzem solve_banded(num de diagonals per sobre de la principal, per sota), dades del sistema lineal (matriu, vector)) que 
        # resol un sistema del tipus Ax=b retornant x (per A=matriu de bandes)
        f[1:-1] = solve_banded((1, 1), ab, dreta) # guardem totes les noves temperatures interiors

    return x, f

N = 101
t_a = 0.025
 

# cas 1: dt = (dx)^2
x, f_1 = crank_nicolson(N, t_a, ratio_dt_dx2=1.0)

# cas 2: dt = 0.5 * (dx)^2
x, f_1/2 = crank_nicolson(N, t_a, ratio_dt_dx2=0.5)

 