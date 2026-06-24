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

# Lab 2 - Quantum States, SOLUTIONS
Useful for working examples and problems with photon quantum states. You may notice some similarity to the Jones Calculus ;-)

```{code-cell} ipython3
import numpy as np
from qutip import *
```

These are the polarization states:

```{code-cell} ipython3
H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/np.sqrt(2)],[1/np.sqrt(2)]])
M45 = Qobj([[1/np.sqrt(2)],[-1/np.sqrt(2)]])
R = Qobj([[1/np.sqrt(2)],[-1j/np.sqrt(2)]])
L = Qobj([[1/np.sqrt(2)],[1j/np.sqrt(2)]])
```

```{code-cell} ipython3
V
```

```{code-cell} ipython3
Hbra = H.dag()
```

```{code-cell} ipython3
Hbra*V
```

Devices:

HWP - Half-wave plate axis at $\theta$ to the horizontal

LP - Linear polarizer, axis at $\theta$

QWP - Quarter-wave plate, axis at $\theta$

Note, these are functions so you need to call them with a specific value of theta.

```{code-cell} ipython3
def HWP(theta):
    return Qobj([[np.cos(2*theta),np.sin(2*theta)],[np.sin(2*theta),-np.cos(2*theta)]]).tidyup()
```

```{code-cell} ipython3
def LP(theta):
    return Qobj([[np.cos(theta)**2,np.cos(theta)*np.sin(theta)],[np.sin(theta)*np.cos(theta),np.sin(theta)**2]]).tidyup()
```

```{code-cell} ipython3
def QWP(theta):
    return Qobj([[np.cos(theta)**2 + 1j*np.sin(theta)**2,
                 (1-1j)*np.sin(theta)*np.cos(theta)],
                [(1-1j)*np.sin(theta)*np.cos(theta),
                 np.sin(theta)**2 + 1j*np.cos(theta)**2]]).tidyup()
```

```{code-cell} ipython3
QWP(np.pi/4)
```

## Example 1) Check that the $|H\rangle$ state is normalized

```{code-cell} ipython3
H.dag()*H
```

To show more information on an object, use the question mark after the function or object:

```{code-cell} ipython3
np.sin?
```

### Example 2) Converting from ket to bra:

```{code-cell} ipython3
psi = Qobj([[1+1j],[2-1j]])
psi
```

```{code-cell} ipython3
psi.dag()
```

```{code-cell} ipython3
psi.dag().dag()
```

the `.dag()` python method computes the "daggar" or the complex transpose.

+++

## 1) Is `psi` normalized? If not, find the normalization constant and confirm that constant normalizes `psi`.

```{code-cell} ipython3
psi.dag()*psi
```

```{code-cell} ipython3
psi_norm = psi*np.sqrt(1/7)
```

```{code-cell} ipython3
psi_norm.dag() * psi_norm
```

## 2) Verify that the $|V\rangle$ state is normalized

```{code-cell} ipython3
V.dag()*V
```

## 3) Verify that the $|H\rangle$ and $|V\rangle$ states are orthogonal. Repeat for the other pairs of states.

```{code-cell} ipython3
H.dag()*V
```

```{code-cell} ipython3
L.dag()*R
```

```{code-cell} ipython3
P45.dag()*M45
```

## 4) Calculate the horizontal component $c_H$ of the state $\psi = \frac{1}{\sqrt{5}}|H\rangle + \frac{2}{\sqrt{5}}|V\rangle$

```{code-cell} ipython3
psi = 1/np.sqrt(5)*H + 2/np.sqrt(5)*V
psi
```

```{code-cell} ipython3
psi2 = Qobj([[1/np.sqrt(5)],[2/np.sqrt(5)]])
psi2
```

```{code-cell} ipython3
H.dag()*psi
```

## 5) Verify Eq. (3.18), $P(H||45\rangle)=\frac{1}{2},$ (which states "The probability that a photon prepared in the +45 state will leave a PA_HV in the Horizontal state is one half.")

```{code-cell} ipython3
expect(H*H.dag(),P45)
```

```{code-cell} ipython3
np.conjugate(H.dag()*P45) * (H.dag()*P45)
```

## 6) Demonstrate that a half-wave plate at 45-degrees converts $|H\rangle$ to $|V\rangle$

```{code-cell} ipython3
HWP(np.radians(45)) * H
```

```{code-cell} ipython3
HWP(np.pi/4) * H == V
```

## 7) Re-create Figure 3.9 by plotting the probability P(+45) vs phase φ

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
plt.plot([1,2,3,2,3,4])
```

```{code-cell} ipython3
phi_list = np.linspace(0,8*np.pi,num=100)
```

```{code-cell} ipython3
plt.plot(phi_list,np.sin(phi_list))
```

```{code-cell} ipython3
sin_list = [np.sin(p) for p in phi_list] # notes 
```

```{code-cell} ipython3
plt.plot(phi_list,sin_list)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3
def psi(phi):
    return 1/np.sqrt(2)*(H + np.exp(1j*phi)*V)
```

```{code-cell} ipython3
answer = [expect(M45*M45.dag(),psi(phi)) for phi in phi_list]
```

```{code-cell} ipython3
plt.plot(phi_list/np.pi,answer,"-o")
plt.xlabel("$\\phi$")
plt.ylabel("P(-45)")
```

```{code-cell} ipython3

```
