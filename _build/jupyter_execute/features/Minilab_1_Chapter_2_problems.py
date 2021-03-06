# Minilab 1 - Jones Calculus
This notebook demonstrates the use the Jones calculus and provides you with additional practice in IPython.

## Using QuTiP
In order to move smoothly into the quantum mechanics of Chapter 3, we'll use QuTiP as our vector and matrix library from this point forward through the rest of the course.

from qutip import *

# Create a row vector:
rv = Qobj([[1,2]])
rv

# Find the corresponding column vector
rv.dag()

# Create a column vector:
cv = Qobj([[1],[4]])
cv

# Convert to a row vector:
cv.dag()

## Review: Vector products in QuTiP
Only need to know one operator: "\*"
The product will depend on the order, either inner or outer

rv*cv  # inner product (dot product)

rv*rv.dag()  # dot product with itself, need row vector first

rv.norm() # find the length of the vector

# verify that the norm of the vector is the square root of the dot product with itself:
from numpy import sqrt, cos, sin, pi
sqrt(5)

## Review: Matrix in QuTiP

qm = Qobj([[1,2],[2,1]])
qm

qm.eigenenergies()  # in quantum (as we will learn) eigenvalues often correspond to energy levels

evals, evecs = qm.eigenstates()

evecs

# Select the first eigenvector using an index inside square brackets:
# Index counting starts at zero so [0] picks the first one:
evecs[0]

# Activity for Lab:
In order to solve the following problems, make use of these definitions for the various states of polarization and matrices for different devices:

# States:
horiz = Qobj([[1],[0]])
vert = Qobj([[0],[1]])
p45 = 1/sqrt(2)*Qobj([[1],[1]])
m45 = 1/sqrt(2)*Qobj([[1],[-1]])
lcp = 1/sqrt(2)*Qobj([[1],[1j]])
rcp = 1/sqrt(2)*Qobj([[1],[-1j]])

# Operators:
HP = Qobj([[1,0],[0,0]])
VP = Qobj([[0,0],[0,1]])
qwp_p45 = 1/sqrt(2)*Qobj([[1,-1j],[-1j,1]])
qwp_m45 = 1/sqrt(2)*Qobj([[1,1j],[1j,1]])

# To display one of these, simply put it at the end of a cell:
VP

# An example calculation, the state of light after +45 polarization goes through a horizontal polarizer:
HP*p45

def HWP(theta):
    return Qobj([[cos(2*theta),sin(2*theta)],[sin(2*theta),-cos(2*theta)]]).tidyup()

def LP(theta):
    return Qobj([[cos(theta)**2,cos(theta)*sin(theta)],[sin(theta)*cos(theta),sin(theta)**2]]).tidyup()

def QWP(theta):
    return Qobj([[cos(theta)**2 + 1j*sin(theta)**2,
                 (1-1j)*sin(theta)*cos(theta)],
                [(1-1j)*sin(theta)*cos(theta),
                 sin(theta)**2 + 1j*cos(theta)**2]]).tidyup()

## Problem 2.2

# Solution
total = QWP(pi/4)*QWP(pi/2)*HWP(pi/8)

total*horiz

## Problem 2.4

# Solution
result = HWP(pi/1.5)*rcp
result

# Solution
result.dag()*rcp

# Solution
from numpy import linspace
for angle in linspace(0,pi,20): # define a linearly-spaced list of 20 values between 0 and pi
    print( (HWP(angle)*rcp).dag()*rcp )

## Problem 2.10

# Solution
total = QWP(-pi/4)*HP*QWP(pi/4)

total*lcp # Allows LCP through

total*rcp  # does not allow RCP

## Problem 2.11

# Solution
total = QWP(-pi/4)*VP*QWP(pi/4)

total*lcp # Does not allow LCP through

total*rcp # Allows RCP completely

