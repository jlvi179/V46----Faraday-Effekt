import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray

cm, B = np.genfromtxt('BFeld.txt', unpack=True, skip_header=1)

def g(x):
    return 418*x/x

xx = np.linspace(86, 112, 10)
plt.plot(xx, g(xx), 'y--', markersize=6 , label = 'Maximaler Wert', alpha=0.5)
plt.plot(cm, B, 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
plt.xlabel(r'$r \, / \, \mathrm{mm}$')
plt.ylabel(r'$B \, / \, \mathrm{mT}$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style


plt.savefig('build/BFeld.pdf', bbox_inches = "tight")
plt.clf() 