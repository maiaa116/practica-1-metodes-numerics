import matplotlib.pyplot as plt
import numpy as np

#metode analitic (no ens surt)
'''n= 1000
ri=0
b=35.6
q=1
valors_x=[0, 0.20,0.40,0.60,0.80,1]
llista_2=[]
valors_t=[0,30,22]

for j in valors_x:
    llista_1=[]
    for t in valors_t:
        suma_q=0
        for i in range(n):
            s=-4*q*np.sin((2*i+1)np.pi*j)(1-np.exp(-((2*i+1)*2)*np.pi*2*t))
            suma_q=suma_q+s
        
        llista_1.append(float(suma_q+b))#una llista de totes les n amb els temps 1, 2 3, en la posicio j
    llista_2.append(llista_1)
    
    
print(llista_2)
'''
t=np.linspace(0,1000,n) 
x=np.linspace()
T_analitica = []

for temps in t:
    resultat = []
    for a in x:
        suma = 0
        for n in range(N):
            suma += 4*q/((2*n+1)*np.pi)**3 * np.sin((2*n+1)*np.pi*a) * (1-np.exp(-(2*n+1)**2*np.pi**2*temps))
        resultat.append(beta+suma)

    T_analitica.append(resultat)

T_analitica = np.array(T_analitica)
print(T_analitica)