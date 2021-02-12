# Chapter 8 - Two-photon States

from qutip import *
from numpy import sqrt

H = basis(2,0)
V = basis(2,1)
p45 = 1/sqrt(2)*(H + V)
m45 = 1/sqrt(2)*(H - V)
R = 1/sqrt(2)*(H - 1j*V)
L = 1/sqrt(2)*(H + 1j*V)

hh = tensor(H,H)
hv = tensor(H,V)
vh = tensor(V,H)
vv = tensor(V,V)

vv

# Show these are all orthogonal:
hh.dag()*hv

vh.dag()*hv

qeye(2)

# Example 8.1
Phv = H*H.dag() - V*V.dag() # polarization measurement
ps_hv = tensor(Phv,qeye(2))
pi_hv = tensor(qeye(2),Phv)
psi_hv = tensor(Phv,Phv)

print(ps_hv*tensor(V,p45) == -tensor(V,p45))

print(pi_hv*tensor(V,p45) == tensor(V,m45))

print(psi_hv*tensor(V,p45) == -tensor(V,m45))

# Example 8.2
Pvh = tensor(V,H)*tensor(V,H).dag()
expect(Pvh,tensor(R,p45))

# Example 8.3
Phi = tensor(qeye(2),H)*tensor(qeye(2),H).dag()
expect(Phi,tensor(R,p45))

# Example 8.4
state = tensor(R,p45)
expect(Pvh,state) / expect(Phi,state)

## Entangled states

phip = 1/sqrt(2)*(tensor(H,H) + tensor(V,V))
Phs = tensor(H,qeye(2))*tensor(H,qeye(2)).dag() 
Phi = tensor(qeye(2),H)*tensor(qeye(2),H).dag()
Phshi = tensor(H,H)*tensor(H,H).dag()

expect(Phshi,phip)/ expect(Phi,phip)

P_45s45i = tensor(p45,p45)*tensor(p45,p45).dag()
P_45i = tensor(qeye(2),p45)*tensor(qeye(2),p45).dag()

expect(P_45s45i,phip)/expect(P_45i,phip)

