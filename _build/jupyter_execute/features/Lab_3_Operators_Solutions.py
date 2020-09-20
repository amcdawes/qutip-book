# Lab 3: Operators
An overview of operator properties

import matplotlib.pyplot as plt
from numpy import sqrt,cos,sin,arange,pi
from qutip import *
%matplotlib inline

H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])

## Example 1: the outer product and the projection operator

We already have the $|H\rangle$ state represented as a vector in the HV basis, so the $\hat{P}_H$ operator is the outer product $|H\rangle\langle H|$ (a ket then a bra):

H

Ph = H*H.dag()
Ph

Same with the $\hat{P}_V$ operator:

Pv = V*V.dag()
Pv

## Example 2: Verify Eq. 4.38 for the HV basis states. Repeat for the ±45, and LR basis

identity(2)

Ph + Pv == identity(2)

P45*P45.dag()

M45*M45.dag()

P45*P45.dag() + M45*M45.dag()

L*L.dag()

R*R.dag()

L*L.dag() + R*R.dag()

## Example 3: Represent the $\hat{R}_p(\theta)$ operator in the HV basis and verify your representation by operating on $|H\rangle$ and $|V\rangle$ states. Use the following template function definition.

def Rp(theta):
    return Qobj([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]).tidyup()

Rp(pi/2)

V==Rp(pi/2)*H

# Solution Goes Here
H==Rp(-pi/2)*V

## 1) Using the $\hat{R}_p(\theta)$ operator, verify the operator properties described in Sections 4.1 and 4.2. Specifically, verify Eqns. 4.6, 4.7, 4.16, 4.18, 4.22, and 4.27

# Solution Goes Here
# 4.6
(Rp(pi/2) + Rp(pi/3)) * P45 == Rp(pi/2)*P45 + Rp(pi/3)*P45

#4.7
Rp(pi/3)*(P45 + H) == Rp(pi/3)*P45 + Rp(pi/3)*H

#4.16
H.dag()*Rp(pi/4).dag() == P45.dag()

#4.18
dag(Rp(pi/3)*Rp(pi/4)) == (Rp(pi/3)*Rp(pi/4)).dag() == Rp(pi/4).dag()*Rp(pi/3).dag()

#4.22
Rp(pi/3).dag() * Rp(pi/3) == identity(2)

#4.27
Rp(pi/3).dag() == Rp(-pi/3)

## Example: the similarity transform
The following defines a function that creates a similarity transform matrix. It takes the two old basis vectors and the two new basis vectors as arguments. To apply the transform, simply multiply the matrix onto the state vector or ooperator matrix. Following the examples below, explore this transform.

def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])

We can define a similarity transform that converts from $HV\rightarrow \pm 45$

Shv45 = sim_transform(H,V,P45,M45)  # as found in Example 4.A.1, Eq. 4.A.10.
Shv45

Shv45 * H  # compare to Eq. 4.A.12

## 4) Use the similarity transform to represent $|V\rangle$ in the ±45 basis

Shv45 * V

## 5) Represent $\hat{P}_H$ in the ±45 basis.
Check your answer against Eqns. 4.A.17 and 4.72

Shv45 * Ph * Shv45.dag()

## 6) Represent $\hat{P}_V$ in the ±45 basis.

Shv45 * Pv * Shv45.dag()

