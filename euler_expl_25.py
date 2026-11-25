from math import pi
import matplotlib.pyplot as plt
import numpy as np
n=101 #nombre de punts en l'espai
r=0.25 #parametre de t
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
n=101
r=0.25

plt.rcParams.update({"axes.titlesize": 16, "axes.labelsize": 15, "xtick.labelsize": 12, "ytick.labelsize": 12, "legend.fontsize": 12})

ro=1081
c_v=3698
k=0.56
sigma=0.472
t_0=0.02**2*c_v*ro/k #Calculem el temps inicial, amb els valors caracteristics
Temperatura_0=t_0*(sigma*((40/np.sqrt(2))/0.02)**2)/(c_v*ro) #la temperatura caracterisitica
print(Temperatura_0)
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
    if T[o, 38] > T50: #mirem un rang molt gran i per quina temperatura el punt 36 dons superopr a T50
        temps_optim=o-1
        break

t = np.arange(1001)*0.25*delta_x**2 #que fa el arange
t_real=t*t_0 #el convertim en real
temps_real = t_real[temps_optim]
print(temps_real)
X, Tt = np.meshgrid(x*2, t_real) #distància en cm i temps en segons


##GRAFIC QUE ENS DEMANEN
h=round(0.025/(r*delta_x**2))#fila que correspont t=0.025
plt.plot(x*2, T[h, :]*Temperatura_0 + 36.5, color='green', label=r"Explícit, $r=0.25$")
plt.axvspan(0.375*2, 0.625*2, color='blue', alpha=0.2, label=r"Regió malalta")
plt.axhline(50, color='red', linewidth=0.8, alpha=0.4, label="50 ºC")
plt.xlabel("Posició x (cm)")
plt.ylabel("Temperatura (°C)")
#plt.title(f"Temperatura a t =0.025s amb $\Delta t={r}\Delta x^2$")
plt.legend()
plt.tick_params(direction="in", top=True, right=True)
plt.show()


##PLA 3D DE LES TEMPERATURES I LES POSICIONS AMB PLANS PER VEURE ELS LIMITS
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Tt, T_C, cmap='inferno', rstride=10, cstride=1, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 50), color='red',  alpha=0.25, rstride=100, cstride=20, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 80), color='red', alpha=0.25, rstride=100, cstride=20, linewidth=0)
ax.set_xticks([0, 0.5, 1, 1.5, 2])
ax.set_yticks([0, 20, 40, 60])
#Diferentes temperatures (eix y) per diferentes posicions (eix x)
ax.set_xlabel("Posició x (cm)")
ax.set_ylabel("Temps t (s)")
ax.set_zlabel("T (°C)")
ax.set_title("Evolució de la temperatura (Euler explícit, r = 0.25)")
fig.colorbar(surf, shrink=0.6, label="T (°C)")
plt.show()


# PLA 3D evolucio de la temperatura per la portada
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Tt, T_C, cmap='inferno', rstride=10, cstride=1, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 50), color='red',  alpha=0.25, rstride=100, cstride=20, linewidth=0)
ax.plot_surface(X, Tt, np.full_like(X, 80), color='red', alpha=0.25, rstride=100, cstride=20, linewidth=0)
ax.set_xticks([0, 0.5, 1, 1.5, 2])
ax.set_yticks([0, 20, 40, 60])
ax.set_zticks([40, 60, 80])
ax.set_xlabel("x (cm)")
ax.set_ylabel("t (s)")
#ax.set_zlabel("T (°C)")
#ax.set_title("Evolució de la temperatura (Euler explícit, r = 0.25)")
fig.colorbar(surf, shrink=0.6, label="T (°C)")
plt.show()



#represetem per al temps òptim trobat abans

plt.figure(figsize=(6.5, 5))
plt.plot(x * 2, T_C[temps_optim, :], color="green")
plt.axvspan(0.375 * 2, 0.625 * 2, color='blue', alpha=0.2, label=r"Regió malalta")
plt.axhline(50, color='red', linewidth=0.8, alpha=0.4, label="50 °C")
plt.xlabel("Posició x (cm)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.tick_params(direction="in", top=True, right=True)
plt.tight_layout()
plt.show()



# error:

def funcio_analitica(x,t,q=1, beta=0, N=1000):
    resultat=[]
    for a in x: #calculem totes les posicions, i calcula cada temperatura analitica
        suma=0
        for n in range(N):
            suma=suma+ 4*q/((2*n+1)*np.pi)**3*np.sin((2*n+1)*np.pi*a)*(1-np.exp(-(2*n+1)**2*np.pi**2 *t))
        resultat.append(beta+suma)
    return np.array(resultat)

#calculem ara per totes les x
T_analitica=funcio_analitica(x,t[1000]) #calculem per totes les x amb una t determinada t posició 1000
error=np.abs(T[1000, :]- T_analitica) # esto és l'error adimensional
error_graus=error*Temperatura_0 




with open("errors_expl_25.txt","w") as errors1:
    errors1.write(str(error_graus))

plt.plot(x, error_graus)
plt.title("Grafic error")
plt.show()


#solució analítica per al problema i comparacio amb la trobada amb el mètode

for o in range(len(t)):
    T_analitica_punt = funcio_analitica([x[38]], t[o])[0]
    if T_analitica_punt > T50:
        temps_optim_analitic = o - 1
        break

temps_real_analitic = t_real[temps_optim_analitic]
error_temps = abs(temps_real - temps_real_analitic)

print("Temps òptim numèric (s):", temps_real)
print("Temps òptim analític (s):", temps_real_analitic)
print("Error del temps (s):", error_temps)
print("Temps òptim adimensional:", t[temps_optim])

T_analitic_t_analitic_C = funcio_analitica(x, t[temps_optim_analitic]) * Temperatura_0 + 36.5
T_euler_t_euler_C = T_C[temps_optim, :]
error_temps_C = np.abs(T_analitic_t_analitic_C - T_euler_t_euler_C)

plt.figure(figsize=(6.5, 5)) #representem l'error entre aquests dos
plt.plot(x * 2, error_temps_C / 1e-4, color="green")
plt.xlabel("Posició x (cm)")
plt.ylabel("Error absolut ($10^{-4}$ °C)")
plt.tick_params(direction="in", top=True, right=True)
plt.tight_layout()
plt.show()

#animacions si
pas = max(1, len(t_real) // 200)
indexs = range(0, len(t_real), pas)

# 1 (com avança la funcio)
fig1, ax1 = plt.subplots(figsize=(7, 4.5)) #primer definim la funció per a un temps concret
linia, = ax1.plot(x * 2, T_C[0, :], color="green", linewidth=1.4, label="Temperatura T(x, t)")
ax1.axhline(50, color="red", linestyle="--", linewidth=1, label="50 °C")
ax1.axhline(80, color="red", linestyle="--", linewidth=1, label="80 °C")
ax1.set_xlim(0, 2)
ax1.set_ylim(35, max(85, np.max(T_C) * 1.05))
ax1.set_xlabel("Posició x (cm)")
ax1.set_ylabel("Temperatura (°C)")
ax1.legend(loc="upper left", fontsize=9)
ax1.grid(False)


titol1 = ax1.set_title("Evolució de la temperatura  |  t = 0.00 s", fontsize=12, pad=12)
fig1.subplots_adjust(top=0.86)

#després anem actualitzant cada temps
def actualitzar_funcio(k):
    linia.set_ydata(T_C[k, :])
    titol1.set_text(f"Evolució de la temperatura  |  t = {t_real[k]:.2f} s")
    return linia, titol1

anim_funcio = FuncAnimation(fig1, actualitzar_funcio, frames=indexs, interval=100, blit=False)
plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()
anim_funcio.save("animacio_temperatura.gif", writer="pillow", fps=15, dpi=150)

# 2(heatmap)
blau_roig = LinearSegmentedColormap.from_list("blau_roig", ["blue", "red"])

fig2, ax2 = plt.subplots(figsize=(4.5, 4.5))
mapa = ax2.imshow(T_C[0:1, :].T, aspect="auto", origin="lower", extent=[0, 1, 0, 2], cmap=blau_roig, vmin=36.5, vmax=np.max(T_C))
ax2.set_xticks([])
ax2.set_ylabel("Posició x (cm)")
ax2.grid(False)
fig2.colorbar(mapa, ax=ax2, label="T (°C)")

titol2 = ax2.set_title("Mapa tèrmic  |  t = 0.00 s", fontsize=11, pad=12)
fig2.subplots_adjust(top=0.86)

def actualitzar_heatmap(k):
    mapa.set_data(T_C[k:k+1, :].T)
    titol2.set_text(f"Mapa tèrmic  |  t = {t_real[k]:.2f} s")
    return mapa, titol2

anim_heatmap = FuncAnimation(fig2, actualitzar_heatmap, frames=indexs, interval=100, blit=False)
plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()
anim_heatmap.save("animacio_heatmap.gif", writer="pillow", fps=15, dpi=150)