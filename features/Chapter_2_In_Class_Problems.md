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

+++ {"nteract": {"transient": {"deleting": false}}}

# Chapter 2: in-class problems

+++ {"nteract": {"transient": {"deleting": false}}}

## 2.3 Find the eigenvalues and vectors of J$_\theta$ for $\theta$=45

```{code-cell} ipython3
from qutip import *
from numpy import cos, sin, pi, deg2rad
```

```{code-cell} ipython3
qm = Qobj([[cos(pi/4)**2,cos(pi/4)*sin(pi/4)],[cos(pi/4)*sin(pi/4),sin(pi/4)**2]])
```

```{code-cell} ipython3
qm
```

```{code-cell} ipython3
qm.eigenstates()
```

```{code-cell} ipython3
from numpy import sqrt, exp
1/sqrt(2)
```

```{code-cell} ipython3
phi = 1.5
Jphi = Qobj([[exp(1j)*phi,0],[0,1]])
Jphi 
```

```{code-cell} ipython3
hvec = Qobj([[1],[0]])
hvec
```

```{code-cell} ipython3
vvec = Qobj([[0],[1]])
vvec
```

```{code-cell} ipython3
Jphi*hvec
```

```{code-cell} ipython3
Jphi*vvec
```

```{code-cell} ipython3

```
