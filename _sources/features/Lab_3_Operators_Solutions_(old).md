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

# Lab 3: Operators
An overview of operator properties

```{code-cell} ipython3
import matplotlib.pyplot as plt
from numpy import sqrt,cos,sin,pi,arange
from qutip import *
```

```{code-cell} ipython3
H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
```

## Example 1: the outer product and the projection operator

+++

We already have the $|H\rangle$ state represented as a vector in the HV basis, so the $\hat{P}_H$ operator is the outer product $|H\rangle\langle H|$:

```{code-cell} ipython3
Ph = H*H.dag()
Ph
```

Same with the $\hat{P}_V$ operator:

```{code-cell} ipython3
Pv = V*V.dag()
Pv
```

## 1) Verify Eq. 4.38 for the HV basis states. Repeat for the 45, and ± basis

```{code-cell} ipython3

```

## 2) Represent the $\hat{R}_p(\theta)$ operator in the HV basis and verify your representation by operating on $|H\rangle$ and $|V\rangle$ states.

```{code-cell} ipython3
def Rp(theta):
    return Qobj([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]).tidyup()
```

```{code-cell} ipython3
Rp(pi/2)
```

```{code-cell} ipython3
V == Rp(pi/2)*H
```

## 3) Using your $\hat{R}_p(\theta)$ operator, verify the operator properties described in Sections 4.1 and 4.2. Specifically, verify Eqns. 4.5, 4.6, 4.7, 4.16, 4.18, 4.22, and 4.27

```{code-cell} ipython3

```

## Example: similarity transform
The following defines a function that creates a similarity transform matrix. It takes the two old basis vectors and the two new basis vectors.

```{code-cell} ipython3
def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])
```

```{code-cell} ipython3
Shv45 = sim_transform(H,V,P45,M45)  # as found in Example 4.A.1, Eq. 4.A.10.
Shv45
```

```{code-cell} ipython3
Shv45 * L  # compare to Eq. 
```

## 4) Represent $\hat{P}_H$ in the ±45 basis.
Check your answer against Eqns. 4.A.17 and 4.72

```{code-cell} ipython3
Shv45*Ph*Shv45.dag()
```

```{code-cell} ipython3

```
