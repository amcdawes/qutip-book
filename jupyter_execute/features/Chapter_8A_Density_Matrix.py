from numpy import sqrt
from qutip import *

H = Qobj([[1],[0]])
V = Qobj([[0],[1]])

## Example 8.A.1:

psi = 1/sqrt(2)*tensor(H,H) + 1/sqrt(2)*tensor(V,V)
psi

rho_ent = psi*psi.dag()

(rho_ent*rho_ent).tr()

rho_mix = 0.5*tensor(H,H)*tensor(H,H).dag() + 0.5*tensor(V,V)*tensor(V,V).dag()

(rho_mix*rho_mix).tr()

## Example 8.A.2

Remember the 45 states:

P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])

Create the projection operator for $|+45,+45\rangle$

Proj_4545 = tensor(P45,P45)*tensor(P45,P45).dag()

(Proj_4545*rho_mix).tr()

Create projection operator for $|+45\rangle_i$

Proj_45i = tensor(qeye(2),P45)*tensor(qeye(2),P45).dag()

(Proj_45i*rho_mix).tr()

0.25/0.5

### Extend the example for the pure (superposition) state

(Proj_4545*rho_ent).tr() / (Proj_45i*rho_ent).tr()

The photons are entanlged and therefore show perfect correlation even in the +45 measurements.