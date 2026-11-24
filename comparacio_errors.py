import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg") # per no obrir finestres de grafic

from euler_expl_25 import error_graus as error_25, x
from euler_expl_49 import error_graus as error_49

plt.plot(x*2, error_49*1e3, color='green', linestyle='-',  label=r"Explícit, $r=0.49$")
plt.plot(x*2, error_25*1e3, color='red',   linestyle='--', label=r"Explícit, $r=0.25$")
plt.xlabel("Posició $x$ (cm)")
plt.ylabel(r"Error absolut ($10^{-3}$ K)")
plt.title(r"Error respecte de l'analítica a $\hat{t}\approx 0{,}025$")
plt.legend()
plt.plot()