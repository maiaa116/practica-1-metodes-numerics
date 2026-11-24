import ast
import numpy as np
import matplotlib.pyplot as plt

suma=0
moduls_errors=[]

file = open("errors_expl_25.txt","r")
error_expl_25 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
for i in range(len(error_expl_25)):
    suma=suma+(error_expl_25[i])**2
moduls_errors.append(np.sqrt(suma))


suma=0
file = open("errors_expl_49.txt","r")
error_expl_49 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
for i in range(len(error_expl_49)):
    suma=suma+(error_expl_49[i])**2
moduls_errors.append(np.sqrt(suma))

suma=0
file = open("errors_impl_1.txt","r")
error_impl_1 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
for i in range(len(error_impl_1)):
    suma=suma+(error_impl_1[i])**2
moduls_errors.append(np.sqrt(suma))

suma=0
file = open("errors_impl_05.txt","r")
error_impl_05 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
for i in range(len(error_impl_05)):
    suma=suma+(error_impl_05[i])**2
moduls_errors.append(np.sqrt(suma))

suma=0
file = open("error_cranck_1.txt","r")
errors_cranck_1 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
for i in range(len(errors_cranck_1)):
    suma=suma+(errors_cranck_1[i])**2
moduls_errors.append(np.sqrt(suma))

suma=0
file = open("error_cranck_05.txt","r")
errors_cranck_05 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()

for i in range(len(errors_cranck_05)):
    suma=suma+(errors_cranck_05[i])**2
moduls_errors.append(np.sqrt(suma))


metode=moduls_errors.index(np.min(moduls_errors))
if metode==0:
    print("el millor mètode és Euler explícit amb r=0,25")
if metode==1:
    print("el millor mètode és Euler explícit amb r=0,49")
if metode==2:
    print("el millor mètode és Euler implícit amb r=1")
if metode==3:
    print("el millor mètode és Euler implícit amb r=0,5")
if metode==4:
    print("el millor mètode és Cranck-Nicholson amb r=1")
if metode==5:
    print("el millor mètode és Cranck-Nicholson amb r=0,5")


plt.figure(figsize=(6.5, 5.8))
x_cm = np.linspace(0, 2, len(error_expl_25))   # posició en cm

plt.plot(x_cm, error_expl_25,    '--o', markersize=1, label="Euler explícit $r=0{,}25$")
plt.plot(x_cm, error_expl_49,    '--o', markersize=1, label="Euler explícit $r=0{,}49$")
plt.plot(x_cm, error_impl_1,     '--o', markersize=1, label="Euler implícit $r=1$")
plt.plot(x_cm, error_impl_05,    '--o', markersize=1, label="Euler implícit $r=0{,}5$")
plt.plot(x_cm, errors_cranck_1,  '--o', markersize=1, label="Crank-Nicolson $r=1$")
plt.plot(x_cm, errors_cranck_05, '--o', markersize=1, linewidth=1, label="Crank-Nicolson $r=0{,}5$")

plt.xlabel("Posició x (cm)")
plt.ylabel("Error absolut (°C)")
plt.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.18),  # Si queda massa a prop o lluny de l'etiqueta x, ajusta aquest valor
    ncol=2,
    frameon=True,
)
plt.tight_layout()
plt.savefig("comparacio.png", dpi=300, bbox_inches="tight")
plt.show()