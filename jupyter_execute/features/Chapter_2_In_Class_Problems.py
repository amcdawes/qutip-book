## 2.3 Find the eigenvalues and vectors of J$_\theta$ for $\theta$=45

from qutip import *
from numpy import cos, sin, pi, deg2rad

qm = Qobj([[cos(pi/4)**2,cos(pi/4)*sin(pi/4)],[cos(pi/4)*sin(pi/4),sin(pi/4)**2]])

qm

qm.eigenstates()

from numpy import sqrt, exp
1/sqrt(2)

phi = 1.5
Jphi = Qobj([[exp(1j)*phi,0],[0,1]])
Jphi 

hvec = Qobj([[1],[0]])
hvec

vvec = Qobj([[0],[1]])
vvec

Jphi*hvec

Jphi*vvec

