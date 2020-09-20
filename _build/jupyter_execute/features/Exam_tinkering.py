%pylab inline
from qutip import *

e = Qobj([[2,1],[1,2]])
e

e.eigenstates()

pz = Qobj([[1],[0]])
mz = Qobj([[0],[1]])
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()

psi = 1/sqrt(5)*py + 1/sqrt(5)*px + 1/sqrt(3)*pz
psi.norm()

psi.dag()*e*psi

psi.dag()*e*e*psi

7.66 - 2.6**2

