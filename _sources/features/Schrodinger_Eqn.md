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

# Schrodinger Equation

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
%pylab inline
from qutip import *
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
pz = Qobj([[1],[0]])
mz = Qobj([[0],[1]])
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()
```

Schrödinger solver

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
H = -0.2*sigmaz()
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
e_list = 0.5*sigmax()  # list of expectation values to calculate
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
t_list = linspace(0,100,1000)  # list of times to evaluate
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
psi = px  # initial state
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
result = sesolve(H, psi, t_list, e_list)
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
plot(result.expect[0])
```

$<\hat{S}_x>$ average oscillates - this is QM "precession"

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
result2 = sesolve(H, pz, t_list, e_list)
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
plot(result2.expect[0])
```

Sx averages to zero at all times for a +Z state in a Bz field.
