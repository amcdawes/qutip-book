# Chapter 7 - Angular Momentum

We'll use $\hbar=1$ for numerical results, this is fairly standard practice, but can be tricky to remember.

from numpy import sin,cos,pi,sqrt
from qutip import *

pz = Qobj([[1],[0]])
mz = Qobj([[0],[1]])
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()
Splus = Sx + 1j*Sy
Sminus = Sx - 1j*Sy

Splus*mz

Splus*pz

Sminus*pz

Sminus*mz

Splus

Sminus

