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

# Quantum states
Useful for working examples and problems with photon quantum states. You may notice some similarity to the Jones Calculus ;-)

```{code-cell} ipython3
from numpy import sqrt
from qutip import *
```

These are the polarization states:

```{code-cell} ipython3
H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
```

Devices:

HWP - Half-wave plate axis at $\theta$ to the horizontal

LP - Linear polarizer, axis at $\theta$

QWP - Quarter-wave plate, axis at $\theta$

Note, these are functions so you need to call them with a specific value of theta.

```{code-cell} ipython3
def HWP(theta):
    return Qobj([[cos(2*theta),sin(2*theta)],[sin(2*theta),-cos(2*theta)]]).tidyup()
```

```{code-cell} ipython3
def LP(theta):
    return Qobj([[cos(theta)**2,cos(theta)*sin(theta)],[sin(theta)*cos(theta),sin(theta)**2]]).tidyup()
```

```{code-cell} ipython3
def QWP(theta):
    return Qobj([[cos(theta)**2 + 1j*sin(theta)**2,
                 (1-1j)*sin(theta)*cos(theta)],
                [(1-1j)*sin(theta)*cos(theta),
                 sin(theta)**2 + 1j*cos(theta)**2]]).tidyup()
```

## Example 1) Check that the $|H\rangle$ state is normalized

```{code-cell} ipython3
H.dag()*H
```

```{code-cell} ipython3
psi = Qobj([[1+1j], [2-1j]])
psi
```

```{code-cell} ipython3
psi.dag()
```

```{code-cell} ipython3
psi.dag().dag()
```

### 1) verify that the $|V\rangle$ state is normalized

```{code-cell} ipython3
V.dag()*V
```

```{code-cell} ipython3
V.norm()
```

### 2) Verify that the $|H\rangle$ and $|V\rangle$ states are orthogonal. Repeat for the other pairs of states.

```{code-cell} ipython3
H.dag()*V
```

### 3) Find the horizontal component $c_H$ of the state $\psi = \frac{1}{\sqrt{5}}|H\rangle + \frac{2}{\sqrt{5}}|V\rangle$

```{code-cell} ipython3
psi = 1/sqrt(5)*H + (1 + 2j)*V
psi
```

### 4) Verify Eq. (3.18) 

```{code-cell} ipython3

```
