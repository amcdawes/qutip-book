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

## Chapter 7 - Angular Momentum and Rotation

```{code-cell} ipython3
from numpy import sqrt, pi, exp, angle
from qutip import *
```

Our usual spin operators (spin-1/2)

```{code-cell} ipython3
pz = basis(2,0)
mz = basis(2,1)
px = 1/sqrt(2)*(pz + mz)
mx = 1/sqrt(2)*(pz - mz)
py = 1/sqrt(2)*(pz + 1j*mz)
my = 1/sqrt(2)*(pz - 1j*mz)
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()
Splus = Sx + 1j*Sy
Sminus = Sx - 1j*Sy
```

Define the spin-1 operators. We use J just to keep them apart. Could be S instead.

```{code-cell} ipython3
Jx = 1/sqrt(2)*Qobj([[0,1,0],[1,0,1],[0,1,0]])
Jy = 1/sqrt(2)*Qobj([[0,-1j,0],[1j,0,-1j],[0,1j,0]])
Jz = Qobj([[1,0,0],[0,0,0],[0,0,-1]])
Jplus = Jx + 1j*Jy
Jminus = Jx - 1j*Jy
```

```{code-cell} ipython3
Jz
```

## Rotations of spin-1/2

```{code-cell} ipython3
Rz90 = (-1j*pi/2*Sz).expm()
```

```{code-cell} ipython3
Rz90
```

```{code-cell} ipython3
Rz90*px
```

Doesn't look like example 7.4 because it's not simplified. How to check:

```{code-cell} ipython3
exp(-1j*pi/4)*py
```

 Yes, this agrees.

+++

Can also use inner product:

```{code-cell} ipython3
py.dag()*Rz90*px
```

```{code-cell} ipython3
(py.dag()*Rz90*px).norm()
```

```{code-cell} ipython3
angle(0.707 - 0.707j) == -pi/4
```

## Find the spin-1 states (the eigenstates of the corresponding matrix)
According to the postulates, the allowed values of an observable are the eigenvalues with corresponding eigenstates.

We know the matrix representation of Jx, Jy, Jz in the Z-basis so we can find all 9 states (in the Z basis). Why nine? There are three possible values $\hbar$, 0, $-\hbar$ for each of three directions.

```{code-cell} ipython3
yevals, (yd,y0,yu) = Jy.eigenstates()
zevals, (zd,z0,zu) = Jz.eigenstates()
xevals, (xd,x0,xu) = Jx.eigenstates()
xd = -xd  # fix the signs to match book
yu = -yu  # fix the signs to match book
```

```{code-cell} ipython3
y0
```

```{code-cell} ipython3
Rz90 = (-1j*pi/2*Jz).expm()
```

```{code-cell} ipython3
Rz90*x0
```

```{code-cell} ipython3
(y0.dag()*Rz90*x0).norm()
```

### 7.10 A spin-1 particle is measured to have $S_y=\hbar$. What is the probability that a subsequent measurement will yield $S_z=0$? $S_z=\hbar$? $S_z=-\hbar$?

```{code-cell} ipython3
(z0.dag()*yu).norm()**2
```

```{code-cell} ipython3
(zu.dag()*yu).norm()**2
```

```{code-cell} ipython3
(zd.dag()*yu).norm()**2
```

```{code-cell} ipython3
yu
```

```{code-cell} ipython3

```
