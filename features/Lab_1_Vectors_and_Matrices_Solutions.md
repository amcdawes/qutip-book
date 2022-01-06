---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lab 1 - Vectors and Matrices
This notebook demonstrates the use of vectors and matrices in IPython. Note that the basis is not explicit in any of these operations. You must keep track of the basis yourself (using variable names, or notes etc).

```{code-cell} ipython3
from numpy import array, dot, outer, sqrt, matrix
from numpy.linalg import eig, eigvals
from matplotlib.pyplot import hist
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
---
%matplotlib inline
```

```{code-cell} ipython3
rv = array([1,2])  # a row vector
rv
```

```{code-cell} ipython3
cv = array([[3],[4]])  # a column vector
cv
```

Two kinds of vector products we'll see: inner product (dot product) and outer product

### 1) Use the function _dot(vector1, vector2)_ to find the dot product of rv and cv. Does the order of the arguments matter?

```{code-cell} ipython3
dot(rv,cv)
```

```{code-cell} ipython3
try:
  dot(cv,rv)
except ValueError as err:
  print(err)
```

### 2) Use the function _outer(vector1, vector2)_ to find the outer product of rv and cv. Does the order of the arguments matter?

```{code-cell} ipython3
outer(rv,cv)
```

```{code-cell} ipython3
outer(cv,rv)
```

## II. Complex vectors

```{code-cell} ipython3
# Complex numbers in python have a j term:
a = 1+2j
```

```{code-cell} ipython3
v1 = array([1+2j, 3+2j, 5+1j, 4+0j])
```

The complex conjugate changes the sign of the imaginary part:

```{code-cell} ipython3
v1.conjugate()
```

### 3) Use _dot()_ and _.conjugate()_ to find the dot product of v1 and it's own conjugate:

```{code-cell} ipython3
dot(v1.conjugate(),v1)
```

## III. Matrices

```{code-cell} ipython3
# a two-dimensional array
m1 = array([[2,1],[2,1]])
m1
```

```{code-cell} ipython3
# can find transpose with the T method:
m1.T
```

```{code-cell} ipython3
# find the eigenvalues and eigenvectors of a matrix:
eig(m1)
```

Can also use the `matrix` type which is like array but restricts to 2D. Also, `matrix` adds `.H` and `.I` methods for hermitian and inverse, respectively. For more information, see Stack Overflow question [#4151128](http://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u)

```{code-cell} ipython3
m2 = matrix( [[2,1],[2,1]])
```

```{code-cell} ipython3
m2.H
```

```{code-cell} ipython3
eig(m2)
```

```{code-cell} ipython3
# use a question mark to get help on a command
eig?
```

# Examples:
## Example 1.4
Find the eigenvalues and eigenvectors of M = ([0,1],[-2,3]])

```{code-cell} ipython3
M14 = array([[0,1],[-2,3]])
```

```{code-cell} ipython3
eig(M14)
```

Interpret this result:
the two eigenvalues are 1 and 2
the eigenvectors are strange decimals, but we can check them against the stated solution:

```{code-cell} ipython3
1/sqrt(2)  # this is the value for both entries in the first eigenvector
```

```{code-cell} ipython3
1/sqrt(5)  # this is the first value in the second eigenvector
```

```{code-cell} ipython3
2/sqrt(5)  # this is the second value in the second eigenvector
```

```{code-cell} ipython3
eigvals(M14)
```

Signs are opposite compared to the book, but it turns out that (-) doesn't matter in the interpretation of eigenvectors: only "direction" matters (the relative size of the entries).

+++

## Example: Problem 1.16 using Ipython functions

```{code-cell} ipython3
M16 = array([[0,-1j],[1j,0]])
```

```{code-cell} ipython3
evals, evecs = eig(M16)
```

```{code-cell} ipython3
evecs
```

```{code-cell} ipython3
evecs[:,0]
```

```{code-cell} ipython3
evecs[:,1]
```

```{code-cell} ipython3
dot(evecs[:,0].conjugate(),evecs[:,1])
```

# Part 2: Using QuTiP
Keeping track of row and column vectors in Ipython is somewhat artificial and tedious. The QuTiP library is designed to take care of many of these headaches

```{code-cell} ipython3
from qutip import *
```

```{code-cell} ipython3
# Create a row vector:
qv = Qobj([[1,2]])
qv
```

```{code-cell} ipython3
# Find the corresponding column vector
qv.dag()
```

```{code-cell} ipython3
qv2 = Qobj([[1+2j,4-1j]])
qv2
```

```{code-cell} ipython3
qv2.dag()
```

## Vector products in QuTiP
Only need to know one operator: "\*"
The product will depend on the order, either inner or outer

```{code-cell} ipython3
qv2*qv2.dag()  # inner product (dot product)
```

```{code-cell} ipython3
qv2.dag()*qv2  # outer product
```

## Matrix in QuTiP

```{code-cell} ipython3
qm = Qobj([[1,2],[2,1]])
qm
```

```{code-cell} ipython3
qm.eigenenergies()  # in quantum (as we will learn) eigenvalues often correspond to energy levels
```

```{code-cell} ipython3
evals, evecs = qm.eigenstates()
```

```{code-cell} ipython3
evecs
```

```{code-cell} ipython3
evecs[0]
```

# Practice:

+++

## Problem 1.2 using the _hist()_ function.

```{code-cell} ipython3
# Solution
n, bins, patches = hist([10,13,14,14,6,8,7,9,12,14,13,11,10,7,7],bins=5,range=(5,14))
```

```{code-cell} ipython3
# Solution
n
```

```{code-cell} ipython3
# Solution
pvals = n/n.sum()
```

## Problem 1.8
**Hint:** using sympy, we can calculate the relevant integral. The conds='none' asks the solver to ignore any strange conditions on the variables in the integral. This is fine for most of our integrals. Usually the variables are real and well-behaved numbers.

```{code-cell} ipython3
# Solution
from sympy import *
c,a,x = symbols("c a x")
Q.positive((c,a))
first = integrate(c*exp(-a*x),(x,0,oo),conds='none')
print("first = ",first)
second = integrate(a*exp(-a*x),(x,0,oo),conds='none')
print("second = ",second)
```
