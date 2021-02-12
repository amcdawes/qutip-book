# Chapter 1
## 1.1 Probability
### 1.1.1 Moments of Measured Data

Arrays of data, and their average and sum in python

import matplotlib.pyplot as plt
from numpy import array, sin, sqrt, dot, outer
%matplotlib inline

x = array([1,2,3])

x.sum()

x.mean()

The formal definition (and to make sure we match with the book) is to take the sum and divide by the number of items in the sample:

x.sum()/len(x)

#### Higher order moments
Operate on the sample, python does this element-by-element, then do the same thing as above:

x**2

(x**2).sum() # Note the parenthesis!

(x**2).sum()/len(x)

#### It works for functions too:

sin(x)

sin(x).sum()/len(x)

#### Variance

x.var()  # Variance

x.std()  # Standard Deviation

x.std()**2 == x.var()  # Related by a square root

### Example 1.1

x_m = array([9,5,25,23,10,22,8,8,21,20])

x_m.mean()

(x_m**2).sum()/len(x_m)

sqrt(281.3 - (15.1)**2)

x_m.std()

Close enough!

### 1.1.2 Probability

#### Example 1.2

n, bins, patches = plt.hist(x_m,bins=7)

The hist function has several possible arguments, we use bins=7 to match the example.

n/10.0*array([6,9,12,15,18,21,24])  # counts times each bin-center value

sum(_)

n/10.0*array([6,9,12,15,18,21,24])**2  # counts times each bin-center value

sum(_)

## 1.2 Linear Algebra
### 1.2.1 Vectors and Basis sets
We'll use the qutip library, even though this is all just linear algebra:

rvec = array([1,2])  # A row vector

rvec

cvec = array([[1],[2]])  # A column vector

cvec

cvec*rvec # Actually the outer product:

dot(rvec,cvec)

outer(cvec,rvec)

However, try running
```
dot(cvec,rvec)
```
it won't work (think about why not!)

