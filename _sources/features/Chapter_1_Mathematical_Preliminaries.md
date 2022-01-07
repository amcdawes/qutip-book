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

# Chapter 1: Mathematical Preliminaries
## 1.1 Probability
### 1.1.1 Moments of Measured Data

+++

Arrays of data, and their average and sum in python

```{code-cell} ipython3
import matplotlib.pyplot as plt
from numpy import array, sin, sqrt, dot, outer
%matplotlib inline
```

```{code-cell} ipython3
x = array([1,2,3])
```

```{code-cell} ipython3
x.sum()
```

```{code-cell} ipython3
x.mean()
```

The formal definition (and to make sure we match with the book) is to take the sum and divide by the number of items in the sample:

```{code-cell} ipython3
x.sum()/len(x)
```

#### Higher order moments
Operate on the sample, python does this element-by-element, then do the same thing as above:

```{code-cell} ipython3
x**2
```

```{code-cell} ipython3
(x**2).sum() # Note the parenthesis!
```

```{code-cell} ipython3
(x**2).sum()/len(x)
```

#### It works for functions too:

```{code-cell} ipython3
sin(x)
```

```{code-cell} ipython3
sin(x).sum()/len(x)
```

#### Variance

```{code-cell} ipython3
x.var()  # Variance
```

```{code-cell} ipython3
x.std()  # Standard Deviation
```

```{code-cell} ipython3
x.std()**2 == x.var()  # Related by a square root
```

### Example 1.1

```{code-cell} ipython3
x_m = array([9,5,25,23,10,22,8,8,21,20])
```

```{code-cell} ipython3
x_m.mean()
```

```{code-cell} ipython3
(x_m**2).sum()/len(x_m)
```

```{code-cell} ipython3
sqrt(281.3 - (15.1)**2)
```

```{code-cell} ipython3
x_m.std()
```

Close enough!

+++

### 1.1.2 Probability

+++

#### Example 1.2

```{code-cell} ipython3
n, bins, patches = plt.hist(x_m,bins=7)
```

The hist function has several possible arguments, we use bins=7 to match the example.

```{code-cell} ipython3
n/10.0*array([6,9,12,15,18,21,24])  # counts times each bin-center value
```

```{code-cell} ipython3
sum(_)
```

```{code-cell} ipython3
n/10.0*array([6,9,12,15,18,21,24])**2  # counts times each bin-center value
```

```{code-cell} ipython3
sum(_)
```

## 1.2 Linear Algebra
### 1.2.1 Vectors and Basis sets
We'll use the qutip library, even though this is all just linear algebra:

```{code-cell} ipython3
rvec = array([1,2])  # A row vector
```

```{code-cell} ipython3
rvec
```

```{code-cell} ipython3
cvec = array([[1],[2]])  # A column vector
```

```{code-cell} ipython3
cvec
```

```{code-cell} ipython3
cvec*rvec # Actually the outer product:
```

```{code-cell} ipython3
dot(rvec,cvec)
```

```{code-cell} ipython3
outer(cvec,rvec)
```

+++ {"nteract": {"transient": {"deleting": false}}}

However, try running
```
dot(cvec,rvec)
```
it won't work (think about why not!)

+++ {"nteract": {"transient": {"deleting": false}}}
