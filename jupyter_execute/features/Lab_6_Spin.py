# Lab 6 - Spin
A few new operators (or new names for the same ones!)
The three axes, x, y, z spin components can be measured with $SA_x$, $SA_y$, and $SA_z$ devices.

**We'll use $\hbar=1$ for numerical results**, this is fairly standard practice, but can be tricky to remember.

from numpy import sin,cos,pi,sqrt
from qutip import *

pz = Qobj([[1],[0]])  # +z
mz = Qobj([[0],[1]])  # -z
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])  # +x
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])  # -x
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])  # +y
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])  # -y
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()

## Example: determine $P(S_x = \frac{\hbar}{2} ||-y\rangle)$

((px.dag()*my).norm())**2

## Example: verify the commutation relation: $\left[\hat{S}_x,\hat{S}_z\right] = -i\hbar\hat{S}_y$

Sx*Sz - Sz*Sx == -1j*Sy  # remember, h = 1

## Ex: find $\langle \hat{S}_x\rangle$ for the state $|\psi\rangle=|+Z\rangle$.


pz.dag()*Sx*pz

This makes sense given that $S_x$ can be either $\frac{+\hbar}{2}$ or $\frac{-\hbar}{2}$ with equal probability. Similarly, if the state is $|\psi\rangle=|+x\rangle$.

px.dag()*Sx*px

Again, in units of $\hbar$.

## Lab instructions:

1. Calculate the expectation value $\langle S_z \rangle$ for the states $|+x\rangle, |+y\rangle, |+z\rangle$

2. Calculate the expectation value $\langle S_z \rangle$ for the state $|\psi\rangle = \frac{1}{\sqrt{2}}|+x\rangle + \frac{1}{\sqrt{2}}|-x\rangle$. Interpret this result, does it make sense? Is there a simpler way to write this state?

3. Represent the spin-squared operator $\hat S^2$ as a matrix.

4. Verify that the $\hat S^2$ commutes with each spin component: $\hat S_x, \hat S_y, \hat S_z$

5. Find the expectation value of $S^2$ for the three postive spins: $|+x\rangle, |+y\rangle, and |+z\rangle$. Interpret your results. Do the values differ? Should they?

6. Problem 6.9, 6.11, 6.12 from Chapter 6

