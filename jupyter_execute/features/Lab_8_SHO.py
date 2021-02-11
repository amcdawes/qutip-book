# Lab 8 - Simple Harmonic Oscillator states
Problems from Chapter 12

from numpy import sqrt
from qutip import *

## Define the standard operators

N = 10  # pick a size for our state-space
a = destroy(N)
n = a.dag()*a

## Problem 12.1:

a*a.dag() - a.dag()*a

## Problem 12.2:

n*a.dag() - a.dag()*n

n*a.dag() - a.dag()*n == a.dag()

## Problem 12.3 (use n=2 as a test-case):
To define $|2\rangle$ use the `basis(N,n)` command where `N` is the dimension of the vector, and `n` is the quantum number.

psi = basis(N,2)



## Problem 12.5 and 12.6:
These are simple, just view the matrix representation of the operators



## Problem 12.7:
First, define $\hat{X}$ and $\hat{P}$ operators

X=
P=

psi = 1/sqrt(2)*(basis(N,1)+basis(N,2))



## Problem 12.8:

psi = 1/sqrt(2)*(basis(N,2)+basis(N,4))

