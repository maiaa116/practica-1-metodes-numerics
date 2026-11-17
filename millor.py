import ast
import numpy as np
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
'''
suma=0
file = open("errors_cranck_1.txt","r")
errors_cranck_1 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()

suma=0
file = open("errors_cranck_05.txt","r")
errors_cranck_05 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
'''

metode=moduls_errors.index(np.min(moduls_errors))
if metode==0:
    print("el millor mètode és Euler explícit amb r=0,25")
if metode==1:
    print