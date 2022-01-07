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

# Ch 8 - Examples

```{code-cell} ipython3
from numpy import sqrt
from qutip import *
```

```{code-cell} ipython3
H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
```

## Example 8.A.1:

```{code-cell} ipython3
psi = 1/sqrt(2)*tensor(H,H) + 1/sqrt(2)*tensor(V,V)
psi
```

```{code-cell} ipython3
rho_ent = psi*psi.dag()
```

```{code-cell} ipython3
(rho_ent*rho_ent).tr()
```

```{code-cell} ipython3
rho_mix = 0.5*tensor(H,H)*tensor(H,H).dag() + 0.5*tensor(V,V)*tensor(V,V).dag()
```

```{code-cell} ipython3
(rho_mix*rho_mix).tr()
```

## Example 8.A.2

+++

Remember the 45 states:

```{code-cell} ipython3
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
```

Create the projection operator for $|+45,+45\rangle$

```{code-cell} ipython3
Proj_4545 = tensor(P45,P45)*tensor(P45,P45).dag()
```

```{code-cell} ipython3
(Proj_4545*rho_mix).tr()
```

Create projection operator for $|+45\rangle_i$

```{code-cell} ipython3
Proj_45i = tensor(qeye(2),P45)*tensor(qeye(2),P45).dag()
```

```{code-cell} ipython3
(Proj_45i*rho_mix).tr()
```

```{code-cell} ipython3
0.25/0.5
```

### Extend the example for the pure (superposition) state

```{code-cell} ipython3
(Proj_4545*rho_ent).tr() / (Proj_45i*rho_ent).tr()
```

The photons are entanlged and therefore show perfect correlation even in the +45 measurements.
