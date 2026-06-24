---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Measurement simulation
A way to simulate data from measurements of a specific quantum state.

Start with standard imports:

```{code-cell} ipython3
import matplotlib.pyplot as plt
from numpy import sqrt,pi,cos,sin,arange,random,real,imag
from qutip import *
%matplotlib inline
```

Define several standard states, these are photon polarization states:

```{code-cell} ipython3
H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
```

```{code-cell} ipython3
# Define the Phv measurement operator:
Phv = H*H.dag() - V*V.dag()
Phv
```

Define a quantum state: $$|\psi\rangle = \frac{1}{\sqrt{5}} |H\rangle + \frac{2}{\sqrt{5}} |V\rangle$$

```{code-cell} ipython3
psi = 1/sqrt(5)*H + 2/sqrt(5)*V
psi
```

```{code-cell} ipython3
# The function to generate a mock data set:
def simulateData(state,oper,size=10000):
    """Generate a simulated data set given a state and measurement operator.
    
    state -> the prepared state
    oper -> the measurement operator
    
    Example:
    H = Qobj([[1],[0]])
    V = Qobj([[0],[1]])
    psi = 1/sqrt(5)*H + 2/sqrt(5)*V
    Phv = H*H.dag() - V*V.dag()
    data = simulateData(psi,Phv)
    
    will generate 10000 values in the data array that obey the probability defined in the state.
    """
    A = basis(2,0)
    B = basis(2,1)
    allowed_results = [A.dag()*oper*A, B.dag()*oper*B]
    probability_amps = [A.dag()*state, B.dag()*state]
    pvals = [abs(pa.conjugate()*pa) for pa in probability_amps]
    data = random.choice(allowed_results,size=size,p=pvals)
    return data
```

```{code-cell} ipython3
data = simulateData(psi,Phv)
```

```{code-cell} ipython3
print("Variance: ",data.var())
print("Mean: ",data.mean())
```

```{code-cell} ipython3
plt.hist(real(data))
```
