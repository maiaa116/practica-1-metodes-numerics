from math import pi
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "axes.titlesize": 14,  
    "axes.labelsize": 14,  
    "xtick.labelsize": 12,  
    "ytick.labelsize": 12, 
    "legend.fontsize": 12   
})



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
    dif=1
    while dif>10**-20: #70 iteracions el Gauss Seidel
        for i in range(1,n-1): #modifiquem tots els punts que no son frontera per aixo va de 1 a n-1
            TTT=T.copy()
            T[i] = (r*T[i+1] + r*T[i-1] + b[i])/(2*r+1)
            dif=np.abs(np.max(T-TTT))

    TT.append(T.copy()) #forma de posarho el TT ja que T no és una llista normal
TT = np.array(TT)

Delta_t2 = 0.5*deltax**2#aixo canvia amb les dues simulacions
dt2 = int(ta/Delta_t2)#nombre de passos que volem fer
r2 = Delta_t2/deltax**2

T2 = np.zeros(n) #temperatures 101 inicials que son zero 
TT2 = [] #llista que guardarem les temperatures on i es la temperautra en el pas i


for t in range(dt2): #faig un for per tots els valors de T fins arribar el demanat
    b2 = T2 + Delta_t2*q #és un vector que conte tots els elements.
    dif2=1
    while dif2>10**-20: #70 iteracions el Gauss seidel
        for i in range(1,n-1): #modifiquem tots els punts que no son frontera per aixo va de 1 a n-1
            TTT2=T2.copy()
            T2[i] = (r2*T2[i+1] + r2*T2[i-1] + b2[i])/(2*r2+1)
            dif2=np.abs(np.max(T2-TTT2))
    TT2.append(T2.copy()) #forma de posarho el TT ja que T no és una llista normal
TT2 = np.array(TT2)





plt.plot(x*2,TT[dt-1,:]*Temperatura_0 + 36.5,color="red", label=r"Implícit, $r=1$")   # <-- label
plt.plot(x*2,TT2[dt2-1,:]*Temperatura_0 + 36.5, alpha=0.4, linestyle= "--", label=r"Implícit, $r=0.5$")   # <-- label
plt.axvspan(0.375*2, 0.625*2, color='blue', alpha=0.2, label="Teixit malalt (0.5 cm)")   # <-- label
plt.axhline(50, color='red', linewidth=0.8, alpha=0.4, label="50 °C")   # <-- label
plt.axhline(80, color='red', linewidth=0.8, alpha=0.4, label="80 °C")   # <-- label
plt.xlabel("Posició x (cm)")
plt.ylabel("Temperatura (ºC)")
plt.title(f"Perfil de temperatura a t = 0,025s")   # <-- títol
plt.legend()   # <-- llegenda
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

with open("errors_impl_1.txt", "w") as errors3:
    errors3.write(str(error_graus))

erro2 = np.abs(TT2[499, :] - T_analitica)
error_graus2 = erro2 * Temperatura_0

with open("errors_impl_05.txt", "w") as errors4:
    errors4.write(str(error_graus2))

plt.plot(x, error_graus)
plt.plot(x, error_graus2)
plt.title("Gràfic error")
plt.show()

