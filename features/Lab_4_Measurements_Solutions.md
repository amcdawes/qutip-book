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

# Lab 4 - Measurements
First our standard definitions:

```{code-cell} ipython3
import matplotlib.pyplot as plt
from numpy import sqrt,pi,cos,sin,arange,random,exp
from qutip import *
```

```{code-cell} ipython3
H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
```

```{code-cell} ipython3
def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])
```

```{code-cell} ipython3
def Delta(state, op):
    """Calculate std. dev. of an observable in a given state"""
    eO2 = state.dag()*op*op*state
    eO = state.dag()*op*state
    return sqrt(eO2.data[0,0] - (eO.data[0,0])**2)
```

### Q: Define the $\hat{\mathscr{P}}_{HV}$ operator

```{code-cell} ipython3
Phv = H*H.dag() - V*V.dag()
Phv
```

###Q: What is the expectation value $\langle \hat{\mathscr{P}}_{HV}\rangle$ for state $|\psi\rangle = \frac{1}{\sqrt{5}}|H\rangle + \frac{2}{\sqrt{5}}|V\rangle$? Interpret this result given the amplitudes in the state.

```{code-cell} ipython3
psi = 1/sqrt(5)*H + 2/sqrt(5)*V
```

```{code-cell} ipython3
psi.dag()*Phv*psi
```

### Q: What is the variance of $\mathscr{P}_{HV}$?

```{code-cell} ipython3
psi.dag()*Phv*Phv*psi
```

```{code-cell} ipython3
1.0 - (-0.6)**2
```

### Ex: Use the random function to generate a mock data set for the state $|\psi\rangle$.
    random.choice([1,-1],size=10,p=[0.2,0.8])
gives a list of 10 numbers, either 1 or -1 with the associated probability p:

```{code-cell} ipython3
data = random.choice([1, -1],size=20,p=[0.2,0.8])
```

```{code-cell} ipython3
data.mean()
```

```{code-cell} ipython3
data.var()
```

### Q: Verify the mean and variance of the mock data set match your QM predictions. How big does the set need to be for you to get ±5% agreement?

```{code-cell} ipython3
data = random.choice([1, -1],size=10000,p=[0.2,0.8])
```

```{code-cell} ipython3
data.mean()
```

```{code-cell} ipython3
data.var()
```

10,000 does pretty well for getting to the predictions. "There is no substitute for an adequate sample size."

+++

### Q: Answer problems 5.11, 5.12, 5.13, 5.14, 5.17, 5.18, 5.19 from the textbook. These are an opportunity to practice with a new operator $\hat{\mathscr{P}}_{C}$

```{code-cell} ipython3
#5.11
P_45 = P45*P45.dag() - M45*M45.dag()
```

```{code-cell} ipython3
#5.12
P_c = L*L.dag() - R*R.dag()
```

```{code-cell} ipython3
#5.13
(Phv*P_45 - P_45*Phv) == 2j * P_c
```

```{code-cell} ipython3
#5.14
(Phv*P_c - P_c*Phv) == -2j * P_45
```

```{code-cell} ipython3
#5.15
P_p45 = P45*P45.dag()
P_v = V*V.dag()
```

```{code-cell} ipython3
P_p45*P_v - P_v*P_p45
```

## 5.19 - this one is tricky, but is easier with our custom function

```{code-cell} ipython3
psi = 1/sqrt(3)*H + sqrt(2/3.0)*exp(1j*pi/3.0)*V
psi.norm()
```

```{code-cell} ipython3
Delta(psi,P_45)*Delta(psi,Phv)
```

```{code-cell} ipython3
1/2j*(psi.dag()*(Phv*P_45 - P_45*Phv)*psi).data[0,0]
```

```{code-cell} ipython3

```
