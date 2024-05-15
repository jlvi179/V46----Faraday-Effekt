import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

e = 1.602*10**(-19)
eps = 8.854*10**(-12)
c = 2.998*10**8
B = 418*10**(-3)
n = 3.397
N1 = 1.2*10**(18)
N2 = 2.8*10**(18)

def m(a,N):
    return (((N*e**3*B)/(8*np.pi**2*eps*c**3*n*a))**(1/2))

ua1 = ufloat(1.27, 0.22)*10**(6)
ua2 = ufloat(7.3, 0.7)*10**(6)

print(m(ua1, N1))
print(m(ua2, N2))

me = 9.109*10**(-31)

def m0(em):
    return em/me

print(m0(m(ua1,N1)))
print(m0(m(ua2,N2)))

mtheo=0.067
print('abweichung 1', (m0(m(ua1,N1))-mtheo)/mtheo)

print('abweichung 2', (m0(m(ua2,N2))-mtheo)/mtheo)