import numpy as np
import matplotlib.pyplot as plt

# La funcio a resoldre es:
# (1 + 2*(r/2)) θ_i^{n+1} - (r/2)(θ_{i-1}^{n+1} + θ_{i+1}^{n+1}) = (1 - r) θ_i^n + (r/2)(θ_{i-1}^n + θ_{i+1}^n) + Δt̂

# Fem algunes substitucions i queda simplificat:
# (1 + 2a)x_i - a(x_{i-1} + x_{i+1}) = d_i

#Comencem definint la funcio de gauss seidel

def gauss_seidel(x, d, a, e_max=1e-12, it_max=100000):
    # x conte les temperatures dels punts interiors
    # d vector del terme independent
    # a = r/2
    # e_max error maxim entre dues passes per donar el bucle per terminat
    # it_max limit maxim de iteracions (per si no convergeix)

    M = len(x) # mida del sistema (punts interiors)

    for it in range(1, it_max + 1): # iteracions fins arribar a l'error desitjat
        error_maxim = 0.0 # comptador de error max a zero (important nombre decimal)

        for i in range(M): # recorre tots els punts interiors
            esq = x[i - 1] if i > 0 else 0.0  # busca el vei esquerre i si és el contron li asigna 0
            dre = x[i + 1] if i < M - 1 else 0.0 # lo mateix per al dret
            nou = (d[i] + a * (esq + dre)) / (1 + 2 * a) # nova temperatura del punt i
            # ara calculem el error de aquest punt respecte l'anterior i si supera al maxim antic l'actualitza
            error_maxim = max(error_maxim, abs(nou - x[i]))
            x[i] = nou # sobreescriu el valor antic i pel nou
        if error_maxim < e_max:
            return it # si el error maxim es menor que la tolerancia desitjada para el bucle i retorne quantes voltes ha donat
    
    raise RuntimeError("Gauss-Seidel no convergeix") # si es supera el nombre de iteracions maximes


# Ara definim la funcio cranck nicolson que evoluciona en el temps les solucions que es troben amb gauss seidel

def crank_nicolson_gs(N, r, t_final, e_max=1e-12):
    # N nombre totals de punts en l'espai, incloent els contorns
    # r relacio del mallat
    # t_final temps on s'atura la simulacio
    # e_max toleracia exigida a gauss seidel

    dx = 1.0 / (N - 1) # pas espaial
    dt = r * dx**2 # pas temporal
    passos = int(round(t_final / dt)) # numero de salts temporals

    x = np.linspace(0.0, 1.0, N)
    theta = np.zeros((passos + 1, N)) # matriu 2D de temperatures (fila = temps n ; columna = posicio i)
    iteracions = 0 # iteracions que fa gauss seidel


    for n in range(passos): # bucle que es repeteix per cada salt temporal

        # calculem el vector independent de gauss seidel pels M punts interiors
        d = (1 - r) * theta[n, 1:-1] + 0.5 * r * (theta[n, 2:] + theta[n, :-2]) + dt
        
        # copiem els punts interiors de la fila n a la fila n+1 com a punt de partida
        theta[n + 1, 1:-1] = theta[n, 1:-1]
        
        # apliquem gauss seifel a la fila n+1 i ens guardem quantes iteracions ha utilitzat
        iteracions += gauss_seidel(theta[n + 1, 1:-1], d, 0.5 * r, e_max)

    return x, theta[-1], passos, iteracions / passos, theta

        # x son les N posicions espaials (eix x per graficar)
        # theta[-1] ultima fila de temperatures (temperatures finals)
        # passos numero de salts temporals
        # iteracions/passos = mitjana de iteracions per cada salt temporal
        # theta tota la matriu de temperatures

# una vegada definides les funcions les apliquem al nostre problema: 

# definim els parametres del problema

cv, rho, kappa, sigma = 3698.0, 1081.0, 0.56, 0.472   
L, Tc, V0 = 0.02, 36.5, 40.0                         
 
P_ext = sigma * (V0 / np.sqrt(2)) ** 2 / L**2         
alpha = kappa / (cv * rho)                           
tau = L**2 / alpha                                   
dT0 = P_ext * L**2 / kappa                           

N, t_a = 101, 0.025

x_exacte = np.linspace(0, 1, N)

# calculem la solucio numerica per a r = 1.0 i r = 0.5 (relacions de mallat)
x, th_1, passos_1, it_1, _ = crank_nicolson_gs(N, 1.0, t_a)
x, th_05, passos_05, it_05, _ = crank_nicolson_gs(N, 0.5, t_a)

T_1 = Tc + dT0 * th_1
T_05 = Tc + dT0 * th_05

centre = N // 2
print(f"r = 1.0: {passos_1} passos, {it_1:.1f} iter/pas, "
        f"θ(0.5) = {th_1[centre]:.6f}, T(centre) = {T_1[centre]:.2f} ºC")
print(f"r = 0.5: {passos_05} passos, {it_05:.1f} iter/pas, "
        f"θ(0.5) = {th_05[centre]:.6f}, T(centre) = {T_05[centre]:.2f} ºC")

# comparem les dues solucions numeriques entre si
dif_max = np.max(np.abs(th_1 - th_05))
print(f"Diferència màxima entre r=1.0 i r=0.5: {dif_max:.2e} ({dT0 * dif_max:.2e} K)")

# grafiquem el perfil de temperatures
plt.figure(figsize=(7, 4))
plt.plot(x * L * 100, T_1, label="Crank-Nicolson (r = 1.0)")
plt.plot(x * L * 100, T_05, "--", label="Crank-Nicolson (r = 0.5)")
plt.xlabel("Posició x (cm)")
plt.ylabel("Temperatura (ºC)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()