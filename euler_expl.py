import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
n=101
r=0.25

ro=1081
c_v=3698
k=0.56
sigma=0.472
t_0=0.02**2*c_v*ro/k
Temperatura_0=t_0*(sigma*((40/np.sqrt(2))/0.02)**2)/(c_v*ro)

x=np.linspace(0,1,n)
delta_x=1/(n-1)
s=np.linspace(1,1000,1000)

T = np.zeros((1001, n))

for l in range(1000):
    for i in range(1, n-1):
        T[l+1, i] = T[l, i] + r*(T[l, i+1] - 2*T[l, i] + T[l, i-1]) + 0.25*delta_x**2

T50=(50-36.5)/Temperatura_0
T80=(80-36.5)/Temperatura_0
T_C = T*Temperatura_0 + 36.5

for o in range (1000):
    if T[o, 36] > T50:
        temps_optim=o-1
        break





t = np.arange(1001)*0.25*delta_x**2
t_real=t*t_0
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
