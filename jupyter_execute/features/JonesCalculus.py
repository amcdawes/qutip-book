# Jones Calculus (Vectors and Matrices)
Useful for working examples and problems with polarization

import matplotlib.pyplot as plt
from numpy import *
from qutip import *

These are the polarization states:

H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])

R

Devices:

HWP - Half-wave plate axis at $\theta$ to the horizontal

LP - Linear polarizer, axis at $\theta$

QWP - Quarter-wave plate, axis at $\theta$

Note, these are functions so you need to call them with a specific value of theta.

def HWP(theta):
    return Qobj([[cos(2*theta),sin(2*theta)],[sin(2*theta),-cos(2*theta)]]).tidyup()

HWP(0)

def LP(theta):
    return Qobj([[cos(theta)**2,cos(theta)*sin(theta)],[sin(theta)*cos(theta),sin(theta)**2]]).tidyup()

def QWP(theta):
    return Qobj([[cos(theta)**2 + 1j*sin(theta)**2,
                 (1-1j)*sin(theta)*cos(theta)],
                [(1-1j)*sin(theta)*cos(theta),
                 sin(theta)**2 + 1j*cos(theta)**2]]).tidyup()

Try a linear polarizer at $+45^\circ$ acting on a vertical beam

out = LP(pi/4)*V
out

Have to interpret this result: it is a constant times the D polarization state:

1/sqrt(2)*P45

Notice, that it is also a combination of the H and V states:

1/2.0*H + 1/2.0*V

This should be somewhat obvious from the vector itself.

Next, find out the intensity of the light that is transmitted. This is given by the "norm" of the vector, sometimes also called the magnitude: $|\mathbf{a}|$

out.norm()  # equivalent to sqrt(0.5**2 + 0.5**2)

