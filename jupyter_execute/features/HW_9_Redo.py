# HW 9.14:
A redo opportunity, to get the full problem right and study this specific Hamiltonian.

from qutip import *
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

Γ1 = 0.5
Γ2 = 0.25
α = 0.1 + 0.2j
H = Qobj([[Γ1, α, 0], [np.conj(α), Γ1, 0], [0, 0, Γ2]])
H

# Make sure this is Hermitian:
H.isherm

energies, [E1, E2, E3] = H.eigenstates()

energies

print(Γ2)
print(Γ1 + np.abs(α))
print(Γ1 - np.abs(α))

### These agree with
$\Gamma_2$ and $\Gamma_1 \pm |\alpha|$

E1

E2

E3

### Now write the state $\big|a\big\rangle$ in terms of the energy eigenstates

a = Qobj([[1],[0],[0]])
a

a.dag()*E1

a.dag()*E2

a.dag()*E3

### And write  $\big|b\big\rangle$ in terms of the energy eigenstates 

b = Qobj([[0],[1],[0]])

b.dag()*E1

b.dag()*E2

b.dag()*E3

### Solve for the time dynamics

N = 100
T = 2*np.pi/np.abs(α)   # period of oscillation
tlist = np.linspace(0,T,N)
proj_b = b.dag()*b
solution = sesolve(H, a, tlist, proj_b)

plt.plot(tlist/T,solution.expect[0],".")

### Consistent with $P(b,t) = \sin^2(|\alpha|t/\hbar)$

