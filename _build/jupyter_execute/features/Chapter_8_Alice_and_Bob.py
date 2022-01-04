#!/usr/bin/env python
# coding: utf-8

# # Chapter 8: Local Realism
# ## with Alice and Bob

# In[1]:


from numpy import sin,cos,pi,sqrt,angle,exp,deg2rad,arange,rad2deg
import matplotlib.pyplot as plt
from qutip import *
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


H = Qobj([[1],[0]])
V = Qobj([[0],[1]])


# First define the projection operator for a state at angle $\theta$:

# In[3]:


def P(theta):
    """The projection operator for a state at angle theta"""
    theta_ket = cos(theta)*H + sin(theta)*V
    return theta_ket*theta_ket.dag()


# Create the projection operators for each of the angles, two for Alice, two for Bob

# In[4]:


Pa1 = P(deg2rad(19))
Pa2 = P(deg2rad(-35))
Pb1 = P(deg2rad(-19))
Pb2 = P(deg2rad(35))


# Create the state $\big|\psi\big\rangle = \sqrt{0.2} \big|H,H\big\rangle + \sqrt{0.8} \big|V,V\big\rangle$:

# In[5]:


psi=sqrt(0.2)*tensor(H,H) + sqrt(0.8)*tensor(V,V)


# Now, find the joint probability that Alice measures A1 and Bob measures B1. We do this by finding the expectation value of the projection operator for the joint state $\big|\theta_{A1},\theta_{B1}\big\rangle$. This is formed as the tensor product of the two appropriate projection operators. **In these tensor products, be sure to put Alice's operator first, then Bob's (just like we did for the signal and idler photons).** Each operator acts on the photon corresponding to the order in the `tensor()` function.
# 
# Notice we'll be using a new function `expect()`. This is equivalent to putting the operator in between the state bra and ket:

# In[6]:


P1 = expect(tensor(Pa1,Pb1),psi)  # joint for A1, B1 (expect 0.09)
P2 = psi.dag()*tensor(Pa1,Pb1)*psi
P1 == P2.data[0,0]  # The only difference is that we have to pull out the value 
                    # from the Qobj using the .data[0,0] method so we can compare it to result from `expect`


# In[7]:


P1


# Find the conditional probability $P(\theta_{B2}|\theta_{A1}) = \frac{P(\theta_{B2},\theta_{A1})}{P(\theta_{A1})}$

# In[8]:


# B2 conditioned on A1 (expect 1)
Prob_b2_a1 = expect(tensor(Pa1,Pb2),psi)
#(psi.dag()*tensor(Pa1,Pb2)*psi).data[0,0]   # the joint probability
Prob_a1 = expect(tensor(Pa1,qeye(2)),psi)
#(psi.dag()*tensor(Pa1,qeye(2))*psi).data[0,0]  # the singular probability
Prob_b2a1 = Prob_b2_a1 / Prob_a1  # the conditional probability
Prob_b2a1


# Find the conditional probability $P(\theta_{A2}|\theta_{B1}) = \frac{P(\theta_{A2},\theta_{B1})}{P(\theta_{B1})}$

# In[9]:


# A2 conditioned on B1 (expect 1)
# can do it all on one line:
expect(tensor(Pa2,Pb1),psi) / expect(tensor(qeye(2),Pb1),psi)


# In[10]:


expect(tensor(Pa2,Pb2),psi)  # joint for A2, B2 (classically expect 0.09, QM says 0)


# This is what we described in class.

# ### What if the state was just $|H,H\rangle$?

# In[11]:


psi2=tensor(H,H)


# In[12]:


expect(tensor(Pa1,Pb1),psi2)  # joint for A1, B1 (expect 0.09)


# In[13]:


# B2 conditioned on A1:
expect(tensor(Pa1,Pb2),psi2) / expect(tensor(Pa1,qeye(2)),psi2)


# In[14]:


# A2 conditioned on B1 
expect(tensor(Pa2,Pb1),psi2) / expect(tensor(qeye(2),Pb1),psi2)


# In[15]:


# joint for A2, B2
expect(tensor(Pa2,Pb2),psi2)


# This is harder to interpret, but we clearly have different probabilities. Finally, check if we had used a mixed state:

# ### A mixed state instead of the pure (entangled state).
# Here we have to use the density matrix (since a `ket` cannot describe a mixed state). First some background:
# QuTiP has a function that gives the density matrix from a `ket` state: `ket2dm`.

# In[16]:


rho_mix = 0.2 * ket2dm(tensor(H,H)) + 0.8 * ket2dm(tensor(V,V))
rho_mix


# In[17]:


# joint for A1, B1
expect(tensor(Pa1,Pb1),rho_mix)  


# In[18]:


# B2 conditioned on A1
expect(tensor(Pa1,Pb2),rho_mix) / expect(tensor(Pa1,qeye(2)),rho_mix)


# In[19]:


# A2 conditioned on B1
expect(tensor(Pa2,Pb1),rho_mix) / expect(tensor(Pb1,qeye(2)),rho_mix)


# In[20]:


# joint for A2, B2:
expect(tensor(Pa2,Pb2),rho_mix)  


# We see that  $P(\theta_{B2},\theta_{A2}) >  P(\theta_{B1},\theta_{A1})$ as we said in class for a state that obeys realism.

# ### Now repeat with the pure state but using density matrix techniques.
# This isn't going to tell us anything new, but it shows how to work with the density matrix if you already know the `ket` state.

# In[21]:


rho_pure = ket2dm(psi)  # convert from a ket to a density matrix (dm)
rho_pure


# The calculations are actually the same in QuTiP, the `expect` function takes either a `ket` state or a density matrix.

# In[22]:


# joint for A1, B1
expect(tensor(Pa1,Pb1),rho_pure)  


# In[23]:


# B2 conditioned on A1
expect(tensor(Pa1,Pb2),rho_pure) / expect(tensor(Pa1,qeye(2)),rho_pure)


# In[24]:


# A2 conditioned on B1
expect(tensor(Pa2,Pb1),rho_pure) / expect(tensor(Pb1,qeye(2)),rho_pure)


# In[25]:


# joint for A2, B2:
expect(tensor(Pa2,Pb2),rho_pure)  


# These all agree (as they should).

# ### Explore the angles in more detail:
# Why these angles, 19 and 35?

# In[26]:


psi=sqrt(0.2)*tensor(H,H) + sqrt(0.8)*tensor(V,V)


# In[27]:


angles = arange(1,90,1)


# In[28]:


rads = deg2rad(angles)


# Make a list of the probability of joint measurements for a pair of angles:

# In[29]:


out = []
for r in rads:
    out.append(expect(tensor(P(-r),P(r)),psi))

plt.plot(angles,out,".") # plot in units of pi


# We see that the joint probabilities have a zero at 35˚. Now plug that in to one of the conditional probabilities and see what angle for the conditional probability gives 1:

# In[30]:


out = []
for r in rads:
    out.append(expect(tensor(P(r),P(deg2rad(35))),psi) / expect(tensor(P(r),qeye(2)),psi))

plt.plot(angles,out,".")


# So only 19 and 35 work. Now, can you derive 19 and 35 given only the state $|\psi\rangle$? Try the first plot, i.e. calculate the joint probability $P(\theta_A,\theta_B)$

# ### Solution
# Using the state, write the projection operators for a two photon state with angles $\theta_A$ and $\theta_B$. First, recall $$\big|\theta_i\big\rangle = \cos\theta_i\big|H\big\rangle + \sin\theta_i\big|V\big\rangle.$$ Next, form the two-photon state: $$\big|\theta_A,\theta_B\big\rangle = \big|\theta_A\big\rangle \otimes \big|\theta_B\big\rangle = \left(\cos\theta_A\big|H\big\rangle + \sin\theta_A\big|V\big\rangle\right) \otimes \left(\cos\theta_B\big|H\big\rangle + \sin\theta_B\big|V\big\rangle\right)$$
# which we can reduce to:
# $$=\cos\theta_A\cos\theta_B\big|H,H\big\rangle + \cos\theta_A\sin\theta_B\big|H,V\big\rangle + \sin\theta_A\cos\theta_B\big|V,H\big\rangle + \sin\theta_A\sin\theta_B\big|V,V\big\rangle.$$
# Find the probability of a joint measurement of polarizations $\theta_A$ and $\theta_B$:
# $$P(\theta_A,\theta_B) = \big|\big\langle\psi\big|\theta_A,\theta_B\big\rangle\big|^2$$
# Since $\big|\psi\big\rangle$ only has $\big|H,H\big\rangle$ and $\big|V,V\big\rangle$ terms, this probability only has two terms:
# $$P(\theta_A,\theta_B) = \left|\sqrt{0.2}\cos\theta_A\cos\theta_B + \sqrt{0.8}\sin\theta_A\sin\theta_B\right|^2$$
# Plot is shown below for $\theta_A = -\theta_B$ and it agrees perfectly with our model above.

# In[31]:


# Solution:
# For the first plot, we can show the joint probability for two angles is given by:

plt.plot(rad2deg(rads),(sqrt(0.2)*cos(-rads)*cos(rads) + sqrt(0.8)*sin(-rads)*sin(rads))**2)


# ### Challenge:
# If we change the state to $\big|\psi\big\rangle = \sqrt{0.8} \big|H,H\big\rangle + \sqrt{0.2} \big|V,V\big\rangle$, the two angles that work for this state.

# In[32]:


# Solution

psi3=sqrt(0.8)*tensor(H,H) + sqrt(0.2)*tensor(V,V)

out = []
for r in rads:
    out.append(expect(tensor(P(-r),P(r)),psi3))

plt.plot(angles,out,".") # plot in units of pi


# In[33]:


# Solution
out = []
for r in rads:
    out.append(expect(tensor(P(r),P(deg2rad(55))),psi3) / expect(tensor(P(r),qeye(2)),psi3))

plt.plot(angles,out,".")

