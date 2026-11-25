import matplotlib.pyplot as plt
import numpy as np



#metode analitic 
t=np.linspace(0,1000,1000) #1000 temps diferents per fer el for
x=np.linspace(0,1,100) #les x possibles
N=100 #nombre de vegades que farem el sumatori
q=1 #consant q del guio
T_analitica = [] #llista on posarem els T analitics

for temps in t:
    resultat = []
    for a in x:
        suma = 0
        for n in range(N):#sumatori per calcular 
            suma += 4*q/((2*n+1)*np.pi)**3 * np.sin((2*n+1)*np.pi*a) * (1-np.exp(-(2*n+1)**2*np.pi**2*temps))
        resultat.append(suma)

    T_analitica.append(resultat)

T_analitica = np.array(T_analitica)
print(T_analitica)

