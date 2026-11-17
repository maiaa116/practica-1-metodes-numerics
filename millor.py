import ast
import numpy as np

file = open("errors_expl_25.txt","r")
error_expl_25 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()

file = open("errors_expl_49.txt","r")
error_expl_49 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()

file = open("errors_impl_1.txt","r")
error_impl_1 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()

file = open("errors_impl_05.txt","r")
error_impl_05 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
'''
file = open("errors_cranck_1.txt","r")
errors_cranck_1 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()

file = open("errors_cranck_05.txt","r")
errors_cranck_05 = np.fromstring(file.read().strip("[]").replace("\n", " "), sep=" ")
file.close()
'''

