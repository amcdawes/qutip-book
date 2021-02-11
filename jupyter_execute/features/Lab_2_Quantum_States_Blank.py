# Quantum states
Useful for working examples and problems with photon quantum states. You may notice some similarity to the Jones Calculus ;-)

from numpy import sqrt
from qutip import *

These are the polarization states:

H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])

Devices:

HWP - Half-wave plate axis at $\theta$ to the horizontal

LP - Linear polarizer, axis at $\theta$

QWP - Quarter-wave plate, axis at $\theta$

Note, these are functions so you need to call them with a specific value of theta.

def HWP(theta):
    return Qobj([[cos(2*theta),sin(2*theta)],[sin(2*theta),-cos(2*theta)]]).tidyup()

def LP(theta):
    return Qobj([[cos(theta)**2,cos(theta)*sin(theta)],[sin(theta)*cos(theta),sin(theta)**2]]).tidyup()

def QWP(theta):
    return Qobj([[cos(theta)**2 + 1j*sin(theta)**2,
                 (1-1j)*sin(theta)*cos(theta)],
                [(1-1j)*sin(theta)*cos(theta),
                 sin(theta)**2 + 1j*cos(theta)**2]]).tidyup()

## Example 1) Check that the $|H\rangle$ state is normalized

H.dag()*H

psi = Qobj([[1+1j], [2-1j]])
psi

psi.dag()

psi.dag().dag()

### 1) verify that the $|V\rangle$ state is normalized

### 2) Verify that the $|H\rangle$ and $|V\rangle$ states are orthogonal. Repeat for the other pairs of states.

### 3) Find the horizontal component $c_H$ of the state $\psi = \frac{1}{\sqrt{5}}|H\rangle + \frac{2}{\sqrt{5}}|V\rangle$

### 4) Verify Eq. (3.18) 

