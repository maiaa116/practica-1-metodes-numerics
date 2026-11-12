import matplotlib.pyplot as plt
import numpy as np
n=101 #nombre de punts en l'espai
r=0.25 #parametre de t

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

for l in range(1000):
    for i in range(1, n-1):
        T[l+1, i] = T[l, i] + r*(T[l, i+1] - 2*T[l, i] + T[l, i-1]) + 0.25*delta_x**2

T50=(50-36.5)/Temperatura_0
T80=(80-36.5)/Temperatura_0
T_C = T*Temperatura_0 + 36.5

t = np.arange(1001)*0.25*delta_x**2
X, Tt = np.meshgrid(x, t)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Tt, T_C, cmap='inferno', rstride=10, cstride=1, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 50), color='cyan',  alpha=0.3, rstride=100, cstride=20, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 80), color='lime', alpha=0.3, rstride=100, cstride=20, linewidth=0)

ax.set_xlabel("x̂")
ax.set_ylabel("t̂")
ax.set_zlabel("T (°C)")
ax.set_title("Evolució de la temperatura (Euler explícit, r = 0.25)")
fig.colorbar(surf, shrink=0.6, label="T (°C)")
plt.show()