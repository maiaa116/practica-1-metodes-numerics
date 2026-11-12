from math import pi
import matplotlib.pyplot as plt
import numpy as np
n=101 #nombre de punts en l'espai
r=0.25 #parametre de t
from matplotlib.animation import FuncAnimation
n=101
r=0.25

ro=1081
c_v=3698
k=0.56
sigma=0.472
t_0=0.02**2*c_v*ro/k #Calculem el temps inicial, amb els valors caracteristics
Temperatura_0=t_0*(sigma*((40/np.sqrt(2))/0.02)**2)/(c_v*ro) #la temperatura caracterisitica

x=np.linspace(0,1,n) #generar una llista de 0-1 amb n punts
delta_x=1/(n-1)#calcular l'increment de x
s=np.linspace(1,1000,1000) #aixo no ho fem servir pero es els numero de incraments que fa t

T = np.zeros((1001, n)) #creo una matriu plena de 0 de 1001x101
#reprsenta cada fila un instnat de temps (1001) i cada columna (101)



for l in range(1000): #recorem tots les insants de T (menys el 0???)
    for i in range(1, n-1): #recorem tots els punts de l'espai
        T[l+1, i] = T[l, i] + r*(T[l, i+1] - 2*T[l, i] + T[l, i-1]) + 0.25*delta_x**2

T50=(50-36.5)/Temperatura_0
T80=(80-36.5)/Temperatura_0
T_C = T*Temperatura_0 + 36.5 #temperatura real

for o in range (1000):
    if T[o, 36] > T50: #mirem un rang molt gran i per quina temperatura el punt 36 dons superopr a T50
        temps_optim=o-1
        break


t = np.arange(1001)*0.25*delta_x**2 #que fa el arange
t_real=t*t_0 #el convertim en real
X, Tt = np.meshgrid(x, t)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Tt, T_C, cmap='inferno', rstride=10, cstride=1, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 50), color='cyan',  alpha=0.3, rstride=100, cstride=20, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 80), color='lime', alpha=0.3, rstride=100, cstride=20, linewidth=0)
temps_real = t_real[temps_optim]
print(temps_real)


ax.set_xlabel("x̂")
ax.set_ylabel("t̂")
ax.set_zlabel("T (°C)")
ax.set_title("Evolució de la temperatura (Euler explícit, r = 0.25)")
fig.colorbar(surf, shrink=0.6, label="T (°C)")
plt.show()

plt.plot(x, T_C[temps_optim, :])
plt.axhline(50)
plt.axhline(80)
plt.show()


fig3,ax3=plt.subplots()
line,=ax3.plot(x,T_C[0,:])
ax3.axhline(50, color='cyan', linestyle='--', label='50 °C')
ax3.axhline(80, color='green', linestyle='--', label='80 °C')

ax3.set_xlim(0, 1)
ax3.set_ylim(36.5, 100)
ax3.set_xlabel("Posició x̂")
ax3.set_ylabel("Temperatura (°C)")
ax3.legend()

def actualitzar(moment):
    line.set_ydata(T_C[moment, :])
    ax3.set_title("Temperatura a t=" + str(t[moment]))
    return line,

animacio= FuncAnimation(fig3, actualitzar, frames=len(t), interval=10, blit=False)
plt.show()



# error:

def funcio_analitica(x,t,q=1, beta=0, N=100):
    resultat=[]
    for a in x:
        suma=0
        for n in range(N):
            suma=suma+ 4*q/((2*n+1)*np.pi)**3*np.sin((2*n+1)*np.pi*a)*(1-np.exp(-(2*n+1)**2*np.pi**2 *t))
        resultat.append(beta+suma)
    return np.array(resultat)

T_analitica=funcio_analitica(x,t[1000])
error=np.abs(T[1000, :]- T_analitica) # esto és l'error adimensional
error_graus=error*Temperatura_0 

plt.plot(x, error_graus)
plt.show()
