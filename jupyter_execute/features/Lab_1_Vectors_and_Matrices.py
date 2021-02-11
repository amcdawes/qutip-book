# Lab 1 - Vectors and Matrices
This notebook demonstrates the use of vectors and matrices in IPython. Note that the basis is not explicit in any of these operations. You must keep track of the basis yourself (using variable names, or notes etc).

from numpy import array, dot, outer, sqrt, matrix
from numpy.linalg import eig, eigvals
from matplotlib.pyplot import hist

%matplotlib inline

rv = array([1,2])  # a row vector
rv

cv = array([[3],[4]])  # a column vector
cv

Two kinds of vector products we'll see: inner product (dot product) and outer product

### 1) Use the function _dot(vector1, vector2)_ to find the dot product of rv and cv. Does the order of the arguments matter?

dot(rv,cv)

dot(cv,rv)

### 2) Use the function _outer(vector1, vector2)_ to find the outer product of rv and cv. Does the order of the arguments matter?

outer(rv,cv)

outer(cv,rv)

## II. Complex vectors

# Complex numbers in python have a j term:
a = 1+2j

v1 = array([1+2j, 3+2j, 5+1j, 4+0j])

The complex conjugate changes the sign of the imaginary part:

v1.conjugate()

### 3) Use _dot()_ and _.conjugate()_ to find the dot product of v1 and it's own conjugate:

dot(v1.conjugate(),v1)

## III. Matrices

# a two-dimensional array
m1 = array([[2,1],[2,1]])
m1

# can find transpose with the T method:
m1.T

# find the eigenvalues and eigenvectors of a matrix:
eig(m1)

Can also use the `matrix` type which is like array but restricts to 2D. Also, `matrix` adds `.H` and `.I` methods for hermitian and inverse, respectively. For more information, see Stack Overflow question [#4151128](http://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u)

m2 = matrix( [[2,1],[2,1]])

m2.H

eig(m2)

# use a question mark to get help on a command
eig?

# Examples:
## Example 1.4
Find the eigenvalues and eigenvectors of M = ([0,1],[-2,3]])

M14 = array([[0,1],[-2,3]])

eig(M14)

Interpret this result:
the two eigenvalues are 1 and 2
the eigenvectors are strange decimals, but we can check them against the stated solution:

1/sqrt(2)  # this is the value for both entries in the first eigenvector

1/sqrt(5)  # this is the first value in the second eigenvector

2/sqrt(5)  # this is the second value in the second eigenvector

eigvals(M14)

Signs are opposite compared to the book, but it turns out that (-) doesn't matter in the interpretation of eigenvectors: only "direction" matters (the relative size of the entries).

## Example: Problem 1.16 using Ipython functions

M16 = array([[0,-1j],[1j,0]])

evals, evecs = eig(M16)

evecs

evecs[:,0]

evecs[:,1]

dot(evecs[:,0].conjugate(),evecs[:,1])

# Part 2: Using QuTiP
Keeping track of row and column vectors in Ipython is somewhat artificial and tedious. The QuTiP library is designed to take care of many of these headaches

from qutip import *

# Create a row vector:
qv = Qobj([[1,2]])
qv

# Find the corresponding column vector
qv.dag()

qv2 = Qobj([[1+2j,4-1j]])
qv2

qv2.dag()

## Vector products in QuTiP
Only need to know one operator: "\*"
The product will depend on the order, either inner or outer

qv2*qv2.dag()  # inner product (dot product)

qv2.dag()*qv2  # outer product

## Matrix in QuTiP

qm = Qobj([[1,2],[2,1]])
qm

qm.eigenenergies()  # in quantum (as we will learn) eigenvalues often correspond to energy levels

evals, evecs = qm.eigenstates()

evecs

evecs[1]

# Practice:

## Problem 1.2 using the _hist()_ function.
Create a histogram of the data and from it estimate the probability distribution. Use min and max values for the range of 5 and 14, and use 5 bins (5 and 6 go in the first bin).

# Solution
data = [10,13,14,14,6,8,7,9,12,14,13,11,10,7,7]
# Fill in the hist() function:
n, bins, patches = hist(data, bins=9, range=(5,14))

bins+0.5

# Solution
hist?

# Solution


## Problem 1.8
Find the constant $c$ that normalizes the probability density:
$$p(x) =
\begin{cases}
ce^{-ax},  & x \geq 0 \\[2ex]
0 & x < 0
\end{cases}
$$

**Hint:** using sympy, we can calculate the relevant integral. The conds='none' asks the solver to ignore any strange conditions on the variables in the integral. This is fine for most of our integrals. Usually the variables are real and well-behaved numbers.

# Partial Solution:
from sympy import *
c,a,x = symbols("c a x")
Q.positive((c,a))
first = integrate( ... ,(x,0,oo),conds='none')  # put the function in ...

check = integrate(  ,(x,0,oo),conds='none')