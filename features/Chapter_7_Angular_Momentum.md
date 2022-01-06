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

# Chapter 7: Angular Momentum

We'll use $\hbar=1$ for numerical results, this is fairly standard practice, but can be tricky to remember.

```{code-cell} ipython3
from numpy import sin,cos,pi,sqrt
from qutip import *
```

```{code-cell} ipython3
pz = Qobj([[1],[0]])
mz = Qobj([[0],[1]])
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()
Splus = Sx + 1j*Sy
Sminus = Sx - 1j*Sy
```

```{code-cell} ipython3
Splus*mz
```

```{code-cell} ipython3
Splus*pz
```

```{code-cell} ipython3
Sminus*pz
```

```{code-cell} ipython3
Sminus*mz
```

```{code-cell} ipython3
Splus
```

```{code-cell} ipython3
Sminus
```

```{code-cell} ipython3

```
