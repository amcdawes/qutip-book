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

# Lab 8 - Simple Harmonic Oscillator states
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
:inputHidden: false
:outputHidden: false

psi
```

```{code-cell} ipython3
a.dag()*psi
```

```{code-cell} ipython3
a.dag()*basis(N,2) == sqrt(3)*basis(N,3)
```

## Problem 12.5 and 12.6:
These are simple, just view the matrix representation of the operators

```{code-cell} ipython3
a
```

```{code-cell} ipython3
a.dag()
```

## Problem 12.7:
First, define $\hat{X}$ and $\hat{P}$ operators

```{code-cell} ipython3
X = 1/2 * (a + a.dag())
P = 1/2j * (a - a.dag())
```

```{code-cell} ipython3
psi = 1/sqrt(2)*(basis(N,1)+basis(N,2))
ex = psi.dag()*X*psi
exq = psi.dag()*X*X*psi
ep = psi.dag()*P*psi
epq = psi.dag()*P*P*psi
```

```{code-cell} ipython3
deltaX = sqrt(exq[0][0][0] - ex[0][0][0]**2)
deltaP = sqrt(epq[0][0][0] - ep[0][0][0]**2)
```

```{code-cell} ipython3
deltaX * deltaP * 2 # compare to uncertainty relation (ΔxΔp >= 1/2)
# the factor of two is to convert from the unitless version of the operator
```

Alternatively, we can find the indeterminacy bound for ΔX and ΔP (the unitless operators): $$\Delta X \Delta P \geq \frac{1}{2}\left|\left\langle \left[\hat{X},\hat{P}\right] \right\rangle\right|$$

```{code-cell} ipython3
1/2*(psi.dag()*commutator(X,P)*psi).norm()
```

Which is also satisfied by the calculated value (1.41 > 0.25)

+++

## Problem 12.8:

```{code-cell} ipython3
psi = 1/sqrt(2)*(basis(N,2)+basis(N,4))
ex = psi.dag()*X*psi
exq = psi.dag()*X*X*psi
ep = psi.dag()*P*psi
epq = psi.dag()*P*P*psi
```

```{code-cell} ipython3
deltaX = sqrt(exq[0][0][0] - ex[0][0][0]**2)
deltaP = sqrt(epq[0][0][0] - ep[0][0][0]**2)
```

```{code-cell} ipython3
deltaX * deltaP * 2 # to compare to book solution which uses the full x and p operators with units
```

```{code-cell} ipython3

```
