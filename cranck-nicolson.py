import numpy as np

def crank-nicolson(N, ta, lamb, beta, q):
  #malla:
  x=np.linspace(0,1,N)
  dx=x[1]-x[0]
  dt=lamb*(dx**2)

  #num pasos:
  n_pasos=int(np.round(ta/dt))

	#condicions inicials:
	#creem un vector amb N components (punts de la malla espaial) tots iguals a la condició inicial
	f=np.full(N,beta,dtype=float)

 	# FONT DE CALOR:
	# creem un vector q_int que injecti calor a tots els punts interiors en cada instant de temps
	q_int=q(x[1:-1])

  # creem la matriu que ens acobla els temps passats i futurs per trobar la temperatura actual, utilitzant solve_banded que evita fer files llarguissimes de zeros
  # agafa les diagonals i les fica horitzontals
  M = N - 2 # nombre de nodes interiors, els exteriors no els modifiquem
  ab = np.zeros((3, M))  # taula buida de 3 files i M columnes on ficarem les diagonals
  ab[0, 1:] = -0.5 * lamb       # diagonal superior, comença en la fila 0 i recorre de la columna 1 fins al final
  ab[1, :]  =  1.0 + lamb       # diagonal principal, comença en la fila 1 i recorre totes les columnes
  ab[2, :-1] = -0.5 * lamb      # diagonal inferior, comença en la fila 2 i recorre del principi a la penultima columna

  # fem el bucle temporal



 