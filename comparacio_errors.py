import matplotlib.pyplot as plt

plt.rcParams.update({
    "axes.titlesize": 18,   
    "axes.labelsize": 14,   
    "xtick.labelsize": 12,  
    "ytick.labelsize": 12,  
    "legend.fontsize": 12    
})

show_original = plt.show
plt.show = lambda *a, **k: plt.close('all')    

from euler_expl_25 import error_graus as error_expl_25, x
from euler_expl_49 import error_graus as error_expl_49
from euler_imp import error_graus as error_impl_1, error_graus2 as error_impl_05
from cn_gs import error_graus_t1 as error_cn                          


plt.show = show_original                       
plt.close('all')                               

plt.figure()
plt.plot(x*2, error_expl_49*1e3, color='green', linestyle='-',  label=r"Explícit, $r=0.49$")
plt.plot(x*2, error_expl_25*1e3, color='red',   linestyle='--', label=r"Explícit, $r=0.25$")
plt.xlabel("Posició $x$ (cm)")
plt.ylabel(r"Error absolut ($10^{-3}$ K)")
plt.title(r"Error respecte de l'analítica a t $\approx 71$ s")
plt.legend(loc='best')
plt.show()

plt.figure()
plt.plot(x*2, error_expl_25*1e3, color='green',  linestyle='-',  label=r"Explícit, $r=0.25$")
plt.plot(x*2, error_impl_05*1e3, color='red',    linestyle='--', label=r"Implícit, $r=0.5$")
plt.plot(x*2, error_impl_1*1e3,  color='orange', linestyle='-.', label=r"Implícit, $r=1$")
plt.plot(x*2, error_cn*1e3,      color='blue',   linestyle=':',  label=r"Crank-Nicolson, $r=1$ i $0.5$")
plt.xlabel("Posició $x$ (cm)")
plt.ylabel(r"Error absolut ($10^{-3}$ K)")
plt.ylim(0, 12.5)                      
plt.legend()
plt.title(r"Comparació errors mètodes numèrics a t $\approx 71$ s")
plt.savefig("comparacio_errors_metodes.png", dpi=300, bbox_inches="tight")
plt.show()