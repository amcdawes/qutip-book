---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernel_info:
  name: python3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lab 8: Simple Harmonic Oscillator states
Problems from Chapter 12

```{code-cell} ipython3
from numpy import sqrt
from qutip import *
```

## Define the standard operators

```{code-cell} ipython3
N = 10  # pick a size for our state-space
a = destroy(N)
n = a.dag()*a
```

## Problem 12.1:

```{code-cell} ipython3
a*a.dag() - a.dag()*a
```

## Problem 12.2:

```{code-cell} ipython3
n*a.dag() - a.dag()*n
```

```{code-cell} ipython3
n*a.dag() - a.dag()*n == a.dag()
```

## Problem 12.3 (use n=2 as a test-case):
To define $|2\rangle$ use the `basis(N,n)` command where `N` is the dimension of the vector, and `n` is the quantum number.

```{code-cell} ipython3
psi = basis(N,2)
```

```{code-cell} ipython3

```

## Problem 12.5 and 12.6:
These are simple, just view the matrix representation of the operators

```{code-cell} ipython3

```

## Problem 12.7:
First, define $\hat{X}$ and $\hat{P}$ operators

```
X=
P=
```

```{code-cell} ipython3

```

```{code-cell} ipython3
psi = 1/sqrt(2)*(basis(N,1)+basis(N,2))
```

```{code-cell} ipython3

```

## Problem 12.8:

```{code-cell} ipython3
psi = 1/sqrt(2)*(basis(N,2)+basis(N,4))
```

```{code-cell} ipython3

```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
  source_hidden: false
nteract:
  transient:
    deleting: false
---

```
