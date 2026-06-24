---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.4
kernel_info:
  name: python3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

## Chapter 7 - Angular Momentum and Rotation
We'll use $\hbar=1$ for numerical results, this is standard practice, but it is important to remember.

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
Jplus = Jx + 1j*Jy # raising operator
Jminus = Jx - 1j*Jy # lowering operator
```

```{code-cell} ipython3
Jz
```

## Rotations of spin-1/2

+++

To define an exponentiated operator, we apply the `.expm()` method to the argument. So to write the rotation operator: 

$$\hat{R}_z(90^\circ) = e^{-i\frac{\pi}{2}\hat{S}_z}$$

we do the following. It looks a little odd to read since you might expect the `exp` to come first, but looks like this:

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
abs(py.dag()*Rz90*px)
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

# Fix the signs to match book:
# (if first value of eigenstate is negative, flip all signs)
states = [xd, x0, xu, yd, y0, yu, zd, z0, zu]
states = [-s if s.full()[0][0]<0 else s for s in states]
# Python doesn't change the values in the list so we have 
# to replace the old values with the new ones:
[xd, x0, xu, yd, y0, yu, zd, z0, zu] = states
```

```{code-cell} ipython3
xd
```

```{code-cell} ipython3
Rz90 = (-1j*pi/2*Jz).expm()
```

```{code-cell} ipython3
Rz90*xu == -1j*yu
```

```{code-cell} ipython3
Rz90*xu
```

```{code-cell} ipython3
yd
```

```{code-cell} ipython3
abs(y0.dag()*Rz90*x0)
```

### 7.10 A spin-1 particle is measured to have $S_y=\hbar$. What is the probability that a subsequent measurement will yield $S_z=0$? $S_z=\hbar$? $S_z=-\hbar$?

```{code-cell} ipython3
abs(z0.dag()*yu)**2
```

```{code-cell} ipython3
abs(zu.dag()*yu)**2
```

```{code-cell} ipython3
abs(zd.dag()*yu)**2
```

### 7.11 A spin-1 particle is measured to have $S_y=0$. What is the probability that a subsequent measurement will yield $S_x=-\hbar$?

```{code-cell} ipython3
abs(y0.dag()*xd)**2
```

```{code-cell} ipython3
abs(xd.dag()*y0)**2
```

### 7.13 $|\psi\rangle = \frac{1}{3}(2|1,1\rangle - i|1,0\rangle + 2|1,-1\rangle)$ Calculate expectation values of $S^2$, $S_y$, and $S_z$.

```{code-cell} ipython3
psi = (1/3)*(2*zu -1j*z0 +2*zd)
psi
```

```{code-cell} ipython3
Jsquared = Jx*Jx + Jy*Jy + Jz*Jz
Jsquared
```

```{code-cell} ipython3
psi.dag()*Jsquared*psi
```

```{code-cell} ipython3
psi.dag()*Jy*psi
```

```{code-cell} ipython3
psi.dag()*Jz*psi
```

```{code-cell} ipython3

```
