import numpy as np

def Gaussian(x, chi, sigma):
    return 1/(sigma*sqrt(2*np.pi)) * np.exp(-(x - chi)**2/(2*sigma**2))

%pylab inline

x = arange(0,10,0.1)

plot(x,Gaussian(x,5,0.5))

import scipy.integrate as integ

integ.quad?

integ.quad(Gaussian, -numpy.inf, numpy.inf, (5,5))

def eipx_Gaussian(x,p,chi,sigma):
    return np.exp(1j*p*x)*Gaussian(x,chi,sigma)
    

def psip(p):
    result = scipy.integrate.quad(eipx_Gaussian,-numpy.inf,numpy.inf,(p,5,0.5))
    return result[0]

plot?



psip(0)

from sympy import *

z = symbols('z')

integrate(Gaussian(z,5,0.5),(z,-oo,oo))

