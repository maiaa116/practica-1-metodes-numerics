import matplotlib.pyplot as plt

plt.rcParams.update({"axes.titlesize": 16, "axes.labelsize": 15, "xtick.labelsize": 12, "ytick.labelsize": 12, "legend.fontsize": 12})

show_original = plt.show
plt.show = lambda *a, **k: plt.close('all')    

from euler_expl_25 import error_graus as error_expl_25, x
from euler_expl_49 import error_graus as error_expl_49

plt.show=show_original                       
plt.close('all')                               

plt.figure()
plt.plot(x*2, error_expl_49*1e3, color='green', linestyle='-',  label=r"Explícit, $r=0.49$")
plt.plot(x*2, error_expl_25*1e3, color='red',   linestyle='--', label=r"Explícit, $r=0.25$")
plt.xlabel("Posició $x$ (cm)")
plt.ylabel(r"Error absolut ($10^{-3}$ °C)")
#plt.title(r"Error respecte de l'analítica a t $\approx 71$ s")
plt.legend(loc='best')
plt.tick_params(direction="in", top=True, right=True)
plt.show()
