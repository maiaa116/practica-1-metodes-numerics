import matplotlib.pyplot as plt
import numpy as np
n=101
r=0.25

ro=1081
c_v=3698
k=0.56
sigma=0.472
t_0=0.02**2*c_v*ro/k
Temperatura_0=t_0*c_v*ro/(sigma*((40/np.sqrt(2))/0.02)**2)

x=np.linspace(0,1,n)
delta_x=1/(n-1)
s=np.linspace(1,1000,1000)
#a temps zero tot a la mateix temperatura
T_temps0=[]
T_temps1=[]
for i in range (n):
    T_temps0.append(1)

for t in s:
    T_temps1 = [1]

    for i in range(1, n-1): #genera tots els punts en un determinat t
        T_temps1.append(T_temps0[i] + r*(T_temps0[i+1]-2*T_temps0[i]+T_temps0[i-1])+0.01**2*r)

    T_temps1.append(1)

    T_temps0 = T_temps1.copy()

print(T_temps1)
print((273+50)/Temperatura_0)
print((273+80)/Temperatura_0)

plt.plot(x, T_temps1)
plt.xlabel("x̂")
plt.ylabel("T̂")
plt.title("Perfil de temperatura a t̂ = 0.025 (Euler explícit, r = 0.25)")
plt.grid()
plt.show()