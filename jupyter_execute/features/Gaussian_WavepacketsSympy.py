from sympy import *

%matplotlib inline

def Gaussian(x, alpha, beta):
    return 1/(beta*sqrt(pi)) * exp(-(x - alpha)**2/(beta**2))

x,p,a,b = symbols('x p a b')

plot(Gaussian(x,5,0.5))

integrate(Gaussian(x,5,0.5),(x,-oo,oo))

def eipx_Gaussian(x,p,alpha,beta):
    return exp(1j*p*x)*Gaussian(x,alpha,beta)

def psip(p):
    result = integrate(eipx_Gaussian,(p,-oo,oo))
    return result[0]

eipx_Gaussian(2,1,2,3)

integrate(eipx_Gaussian(x,p,a,b),(p,-oo,oo),conds='none')

