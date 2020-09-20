# Chapter 4 in-class problems
## Using what you learned in Lab, answer questions 4.7, 4.8, 4.10, 4.11, 4.12, and 4.13

from numpy import sqrt, pi, cos, sin
from qutip import *

### Remember, these states are represented in the HV basis:

H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])

The sim_transform function creates the matrix $\bar{\mathbf{S}}$ that can convert from one basis to another. As an example, it will create the tranform matrix to convert from HV to ±45 if you run:

    Shv45 = sim_transform(H,V,P45,M45)    #  creates the matrix Shv45
    
Then you can convert a ket from HV to ±45 by applying the Shv45 matrix:

    Shv45*H    #  will convert H from the HV basis to the ±45 basis
    
To convert operators, you have to sandwich the operator between $\bar{\mathbf{S}}$ and $\bar{\mathbf{S}}^\dagger$:

    Shv45*Ph*Shv45.dag()     #  converts Ph from HV basis to the ±45 basis.

def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])

ShvLR = sim_transform(H,V,L,R)

ShvLR*H

ShvLR*V

## 4.11: Express $\hat{R}_p(\theta)$ in ±45 basis

def Rp(theta):
    return Qobj([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]).tidyup()

Rp(1.3)

Shv45 = sim_transform(H,V,P45,M45)

## 4.12: 

Rp45 = Shv45*Rp(pi/4)*Shv45.dag()

Rp45*Shv45*P45 == Shv45*V   # convert P45 to the ±45 basis

Rp45* Qobj([[1],[0]])

ShvLR = sim_transform(H,V,L,R)

ShvLR*Rp(pi/4)*ShvLR.dag()

