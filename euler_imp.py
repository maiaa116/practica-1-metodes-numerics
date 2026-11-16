from math import pi
import matplotlib.pyplot as plt
import numpy as np

ta = 0.025
Num=250
deltax=0.01
Delta_t = deltax**2#aixo canvia amb les dues simulacions
dt = int(ta/Delta_t)#nombre de passos que volem fer
x=np.linspace(0,1,101)
n = 101
r = Delta_t/deltax**2
q = 1
Temperatura_0=674.2857142857141

T = np.zeros(n) #temperatures 101 inicials que son zero 
TT = [] #llista que guardarem les temperatures on i es la temperautra en el pas i


for t in range(dt): #faig un for per tots els valors de T fins arribar el demanat
    b = T + Delta_t*q #és un vector que conte tots els elements.
    for l in range(70): #10 iteracions el Gauss hidel
        for i in range(1,n-1): #modifiquem tots els punts que no son frontera per aixo va de 1 a n-1
            T[i] = (r*T[i+1] + r*T[i-1] + b[i])/(2*r+1)

    TT.append(T.copy()) #forma de posarho el TT ja que T no és una llista normal
TT = np.array(TT)


plt.plot(x,TT[249,:])
plt.show()


def funcio_analitica(x,t,q=1, beta=0, N=100):
    resultat=[]
    for a in x: #calculem totes les posicions, i calcula cada temperatura analitica
        suma=0
        for n in range(N):
            suma=suma+ 4*q/((2*n+1)*np.pi)**3*np.sin((2*n+1)*np.pi*a)*(1-np.exp(-(2*n+1)**2*np.pi**2 *t))
        resultat.append(beta+suma)
    return np.array(resultat)

#calculem ara per totes les x
temps = dt * Delta_t
T_analitica = funcio_analitica(x, temps)

error = np.abs(TT[249, :] - T_analitica)
error_graus = error * Temperatura_0

plt.plot(x, error_graus)
plt.title("Gràfic error")
plt.show()




