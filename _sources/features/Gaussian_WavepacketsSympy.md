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

# Gaussian Wavepackets (using Sympy)

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
from sympy import *
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
%matplotlib inline
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
def Gaussian(x, alpha, beta):
    return 1/(beta*sqrt(pi)) * exp(-(x - alpha)**2/(beta**2))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
x,p,a,b = symbols('x p a b')
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
plot(Gaussian(x,5,0.5))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
integrate(Gaussian(x,5,0.5),(x,-oo,oo))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
def eipx_Gaussian(x,p,alpha,beta):
    return exp(1j*p*x)*Gaussian(x,alpha,beta)
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
def psip(p):
    result = integrate(eipx_Gaussian,(p,-oo,oo))
    return result[0]
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
eipx_Gaussian(2,1,2,3)
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
integrate(eipx_Gaussian(x,p,a,b),(p,-oo,oo),conds='none')
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---

```
