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

# Chapter 12: Simple Harmonic Oscillator
Several examples that make use of the built-in Simple Harmonic Oscillator tools:

```{code-cell} ipython3
from numpy import sqrt,linspace,exp
from qutip import *
import matplotlib.pyplot as plt
%matplotlib inline
```

```{code-cell} ipython3
N = 40 # size of the Hilbert space.
       # N needs to be large enough that matrix is not truncated
a = destroy(N)
n = a.dag()*a
```

Define a coherent state with $\alpha = 2:$

```{code-cell} ipython3
psi = coherent(N,1)
```

```{code-cell} ipython3
psi
```

Expectation value $\langle n\rangle$:

```{code-cell} ipython3
psi.dag()*n*psi
```

```{code-cell} ipython3
# Convert to a density matrix:
psi_dm = ket2dm(psi)
```

```{code-cell} ipython3
psi*psi.dag()
```

```{code-cell} ipython3
# Fock state distribution of the coherent state:
plot_fock_distribution(psi_dm)
```

Also look at other coherent states:

```{code-cell} ipython3
# With larger N and α:
plot_fock_distribution(coherent_dm(100,6))
```

And some other density matrices, like a fock-state (or n eigenstate):

```{code-cell} ipython3
# With a Fock state (number state):
plot_fock_distribution(fock_dm(20,2))
```

```{code-cell} ipython3
fock(20,2)
```

And a thermal state:

```{code-cell} ipython3
# A thermal state has decaying amplitudes
plot_fock_distribution(thermal_dm(20,2))
```

## Finally, can visualize the phasor using what is called the Wigner function:

```{code-cell} ipython3
xvec = linspace(-10,10,200) # Create an array for the phase space coordinates.
plt.imshow(wigner(coherent(40,5j)+coherent(40,-5j),xvec,xvec), extent=[-10,10,-10,10]) # contour plot of Wigner function
```

```{code-cell} ipython3
:inputHidden: false
:outputHidden: false


```

```{code-cell} ipython3

```
