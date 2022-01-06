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

# Gaussian Wavepackets

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
import numpy as np
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
def Gaussian(x, chi, sigma):
    return 1/(sigma*sqrt(2*np.pi)) * np.exp(-(x - chi)**2/(2*sigma**2))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
%pylab inline
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
x = arange(0,10,0.1)
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
plot(x,Gaussian(x,5,0.5))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
import scipy.integrate as integ
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
integ.quad?
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
integ.quad(Gaussian, -numpy.inf, numpy.inf, (5,5))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
def eipx_Gaussian(x,p,chi,sigma):
    return np.exp(1j*p*x)*Gaussian(x,chi,sigma)
    
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
def psip(p):
    result = scipy.integrate.quad(eipx_Gaussian,-numpy.inf,numpy.inf,(p,5,0.5))
    return result[0]
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
plot?
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---

```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
psip(0)
```

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
z = symbols('z')
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
integrate(Gaussian(z,5,0.5),(z,-oo,oo))
```

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---

```
