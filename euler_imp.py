from math import pi
import matplotlib.pyplot as plt
import numpy as np

ta = 0.025
Delta_t = 10**(-4)
dt = int(ta/Delta_t)
x=np.linspace(0,1,101)
n = 101
r = 1
q = np.ones(n)

T = np.zeros(n) #temperatures inicials que son zero
TT = [] #llista que guardarem les temperatures on i es la temperautra en el pas i

#TT.append(T.copy()) #forma de posarho el TT ja que T no és una llista normal

for t in range(dt): #faig un for per tots els valors de T fins arribar el demanat
    b = T + Delta_t*q #és un vector que conte tots els elements.
    for l in range(10): #10 iteracions el Gauss hidel
        for i in range(1,n-1): #modifiquem tots els punts que no son frontera per aixo va de 1 a n-1
            T[i] = (r*T[i+1] + r*T[i-1] + b[i])/(2*r+1)

    #TT.append(T.copy())
plt.plot(x,T)
plt.show()