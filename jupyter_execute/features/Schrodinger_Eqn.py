%pylab inline
from qutip import *

pz = Qobj([[1],[0]])
mz = Qobj([[0],[1]])
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()

Schrödinger solver

H = -0.2*sigmaz()

e_list = 0.5*sigmax()  # list of expectation values to calculate

t_list = linspace(0,100,1000)  # list of times to evaluate

psi = px  # initial state

result = sesolve(H, psi, t_list, e_list)

plot(result.expect[0])

$<\hat{S}_x>$ average oscillates - this is QM "precession"

result2 = sesolve(H, pz, t_list, e_list)

plot(result2.expect[0])

Sx averages to zero at all times for a +Z state in a Bz field.