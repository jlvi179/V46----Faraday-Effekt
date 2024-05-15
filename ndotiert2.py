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

# Plot 1:


theta11,theta12, theta1, theta21, theta22, theta2, diff,lamb = np.genfromtxt('Messungen2.txt', unpack=True, skip_header=2)

plt.plot(lamb**2, diff, 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
plt.xlabel(r'$\lambda^2 \, / \, \mathrm{\mu m^2}$')
plt.ylabel(r'$\theta_{norm}\, / \, \mathrm{\frac{rad}{m}}$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style

plt.savefig('build/ndotiert2.pdf', bbox_inches = "tight")
plt.clf() 

theta11,theta12, theta1, theta21, theta22, theta2, diff2,lamb2 = np.genfromtxt('Messungen21.txt', unpack=True, skip_header=2)

n = len(lamb)                             # Anzahl der Daten
mean = sum(lamb*diff)/n                      # Mittelwert
sigma = np.sqrt(sum(diff*(lamb - mean)**2))  # Standardabweichung 


def g(a,x,b):
    return a*x+b    # b = 2*sigma**2
 
para, pcov = curve_fit(g, lamb2**2, diff2,p0=[mean,sigma])
a, b = para
pcov = np.sqrt(np.diag(pcov))
fa, fb = pcov
ua = ufloat(a, fa) 
ub = ufloat(b, fb)
#unu0 = ufloat(nu0, fnu0)

print('ua',ua)
print('ub',ub)


theta11,theta12, theta1, theta21, theta22, theta2, diff2a,lamb2a = np.genfromtxt('Messungen2Ausgelassen.txt', unpack=True, skip_header=2)

xx =np.linspace(1,7.2, 10 )
plt.plot(lamb2**2, diff2, 'xk', markersize=6 , label = 'Messdaten', alpha=0.5)
plt.plot(lamb2a**2, diff2a, '+r', markersize=6 , label = 'ausgeschlossene Messdaten', alpha=0.5)
plt.plot(xx, g(xx,*para), 'b', markersize=6 , label = 'Ausgleichsgerade', alpha=0.5)

plt.xlabel(r'$\lambda^2 \, / \, \mathrm{\mu m^2}$')
plt.ylabel(r'$\theta_{norm}\, / \, \mathrm{\frac{rad}{m}}$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style


plt.savefig('build/ndotiert2gerade.pdf', bbox_inches = "tight")
plt.clf() 