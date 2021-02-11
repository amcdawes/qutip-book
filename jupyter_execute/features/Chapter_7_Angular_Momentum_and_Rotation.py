## Chapter 7 - Angular Momentum and Rotation

from numpy import sqrt, pi, exp, angle
from qutip import *

Our usual spin operators (spin-1/2)

pz = basis(2,0)
mz = basis(2,1)
px = 1/sqrt(2)*(pz + mz)
mx = 1/sqrt(2)*(pz - mz)
py = 1/sqrt(2)*(pz + 1j*mz)
my = 1/sqrt(2)*(pz - 1j*mz)
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()
Splus = Sx + 1j*Sy
Sminus = Sx - 1j*Sy

Define the spin-1 operators. We use J just to keep them apart. Could be S instead.

Jx = 1/sqrt(2)*Qobj([[0,1,0],[1,0,1],[0,1,0]])
Jy = 1/sqrt(2)*Qobj([[0,-1j,0],[1j,0,-1j],[0,1j,0]])
Jz = Qobj([[1,0,0],[0,0,0],[0,0,-1]])
Jplus = Jx + 1j*Jy
Jminus = Jx - 1j*Jy

Jz

## Rotations of spin-1/2

Rz90 = (-1j*pi/2*Sz).expm()

Rz90

Rz90*px

Doesn't look like example 7.4 because it's not simplified. How to check:

exp(-1j*pi/4)*py

 Yes, this agrees.

Can also use inner product:

py.dag()*Rz90*px

(py.dag()*Rz90*px).norm()

angle(0.707 - 0.707j) == -pi/4

## Find the spin-1 states (the eigenstates of the corresponding matrix)
According to the postulates, the allowed values of an observable are the eigenvalues with corresponding eigenstates.

We know the matrix representation of Jx, Jy, Jz in the Z-basis so we can find all 9 states (in the Z basis). Why nine? There are three possible values $\hbar$, 0, $-\hbar$ for each of three directions.

yevals, (yd,y0,yu) = Jy.eigenstates()
zevals, (zd,z0,zu) = Jz.eigenstates()
xevals, (xd,x0,xu) = Jx.eigenstates()
xd = -xd  # fix the signs to match book
yu = -yu  # fix the signs to match book

y0

Rz90 = (-1j*pi/2*Jz).expm()

Rz90*x0

(y0.dag()*Rz90*x0).norm()

### 7.10 A spin-1 particle is measured to have $S_y=\hbar$. What is the probability that a subsequent measurement will yield $S_z=0$? $S_z=\hbar$? $S_z=-\hbar$?

(z0.dag()*yu).norm()**2

(zu.dag()*yu).norm()**2

(zd.dag()*yu).norm()**2

yu

