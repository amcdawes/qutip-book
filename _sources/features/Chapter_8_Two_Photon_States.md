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

# Chapter 8 - Two-photon States

```{code-cell} ipython3
from qutip import *
from numpy import sqrt
```

```{code-cell} ipython3
H = basis(2,0)
V = basis(2,1)
p45 = 1/sqrt(2)*(H + V)
m45 = 1/sqrt(2)*(H - V)
R = 1/sqrt(2)*(H - 1j*V)
L = 1/sqrt(2)*(H + 1j*V)
```

```{code-cell} ipython3
hh = tensor(H,H)
hv = tensor(H,V)
vh = tensor(V,H)
vv = tensor(V,V)
```

```{code-cell} ipython3
vv
```

```{code-cell} ipython3
# Show these are all orthogonal:
hh.dag()*hv
```

```{code-cell} ipython3
vh.dag()*hv
```

```{code-cell} ipython3
qeye(2)
```

```{code-cell} ipython3
# Example 8.1
Phv = H*H.dag() - V*V.dag() # polarization measurement
ps_hv = tensor(Phv,qeye(2))
pi_hv = tensor(qeye(2),Phv)
psi_hv = tensor(Phv,Phv)

print(ps_hv*tensor(V,p45) == -tensor(V,p45))

print(pi_hv*tensor(V,p45) == tensor(V,m45))

print(psi_hv*tensor(V,p45) == -tensor(V,m45))
```

```{code-cell} ipython3
# Example 8.2
Pvh = tensor(V,H)*tensor(V,H).dag()
expect(Pvh,tensor(R,p45))
```

```{code-cell} ipython3
# Example 8.3
Phi = tensor(qeye(2),H)*tensor(qeye(2),H).dag()
expect(Phi,tensor(R,p45))
```

```{code-cell} ipython3
# Example 8.4
state = tensor(R,p45)
expect(Pvh,state) / expect(Phi,state)
```

## Entangled states

```{code-cell} ipython3
phip = 1/sqrt(2)*(tensor(H,H) + tensor(V,V))
Phs = tensor(H,qeye(2))*tensor(H,qeye(2)).dag() 
Phi = tensor(qeye(2),H)*tensor(qeye(2),H).dag()
Phshi = tensor(H,H)*tensor(H,H).dag()

expect(Phshi,phip)/ expect(Phi,phip)
```

```{code-cell} ipython3
P_45s45i = tensor(p45,p45)*tensor(p45,p45).dag()
P_45i = tensor(qeye(2),p45)*tensor(qeye(2),p45).dag()
```

```{code-cell} ipython3
expect(P_45s45i,phip)/expect(P_45i,phip)
```

```{code-cell} ipython3

```
