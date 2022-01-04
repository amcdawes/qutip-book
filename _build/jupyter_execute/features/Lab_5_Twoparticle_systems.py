#!/usr/bin/env python
# coding: utf-8

# # Lab 5: Two-particle systems
# An introduction to multi-particle spaces, starting with photon polarization states. This lab answers the question: How do we describe the state of two photons?

# In[1]:


import matplotlib.pyplot as plt
from numpy import sqrt,pi,sin,cos,arange
from qutip import *


# ### The polarization states (in the HV-basis):

# In[2]:


H = basis(2,0)
V = basis(2,1)
P45 = 1/sqrt(2)*(H+V)
M45 = 1/sqrt(2)*(H-V)
L = 1/sqrt(2)*(H+1j*V)
R = 1/sqrt(2)*(H-1j*V)


# ### Define two-particle states using the `tensor()` function:
# Mathematically, we are taking the tensor product of two vectors. That product is a larger vector with twice as many entries as the individual state vectors. As long as we take the tensor products in the right order (i.e. always talking about photon 1 and photon 2 in that order) we can also make operators that act on two-photon states). In order to keep a consistent naming scheme, we'll call the first photon the **signal** photon and the second photon the **idler** photon. The names aren't particularly important but they come from the process we use in the lab:  [Spontaneous Parametric Down Conversion](https://en.wikipedia.org/wiki/Spontaneous_parametric_down-conversion) 
# 
# First, look at a generic pair of vectors and their tensor product:

# In[3]:


A = Qobj([[1],[2]])
B = Qobj([[3],[4]])
print(A)
print(B)
print(tensor(A,B))


# So we see that the tensor product has the following elements: 1\*3 = 3, 1\*4 = 4, 2\*3 = 6, 2\*4 = 8. Essentially, we distributed the multiplication of the first vector through the second vector. Using the technical terms of vector spaces, the tensor product exists in a larger Hilbert space (the number of dimensions is the product of the dimensions of the original states). See this with larger initial states: two 3-dim vectors have a tensor product in 9-dim space:

# In[4]:


C = Qobj([[1],[2],[3]])
D = Qobj([[4],[5],[6]])
print(tensor(C,D))


# Now, back to the quantum mechanics. Form the four different combinations of two photons:

# In[5]:


HH = tensor(H,H)
HV = tensor(H,V)
VH = tensor(V,H)
VV = tensor(V,V)


# In[6]:


# How do we represent HH? It is a vector with four elements.
HH


# So we interpret the state $|HH\rangle$ as the vector (1,0,0,0) in a four-dimensional space.

# Recall: The polarization measurement operator (for one photon):

# In[7]:


Phv = H*H.dag() - V*V.dag()
Phv


# Also, the identity is defined as `qeye(n)` for `n` dimensions in qutip:

# In[8]:


qeye(2)  # 2-dimensional identity


# The two-photon operator, measuring the **signal** photon, is formed with the `tensor()` function. It is the tensor product of the projection operator `Phv` and the 2-dimensional identity operator `qeye(2)`. The trick is putting them in the correct order. The first element in the tensor product acts on the signal photon, the second acts on the idler photon. So to act on only the signal photon, we create a tensor product with the projection operator first, and the identity second:

# In[9]:


Phv_s = tensor(Phv,qeye(2))
Phv_s


# It can be hard to interpret these values visually but remember it was constructed by multiplying all the terms between two matrices with only diagonal elements. It makes sense that the result is also diagonal. Also, the sign of the diagonal depends on the state of the signal photon (the first one listed). Recall the states are in the order: HH, HV, VH, VV so the first two states have H signal photons and are therefore 1, and the second two states are V signal photons so -1 for those diagonals.

# Now construct the two-photon operator that measures the idler photon:

# In[10]:


Phv_i = tensor(qeye(2),Phv)
Phv_i


# Next, construct a projection operator that projects the idler photon to H:

# In[11]:


Ph = H*H.dag()
Ph_i = tensor(qeye(2),Ph)  # Ph for idler photon


# And the same but for the signal photon:

# In[12]:


Ph_s = tensor(Ph,qeye(2))  # Ph for signal photon


# You start to see the pattern. Build these up from our earlier operators, just apply them to the specific particle by including them in the tensor product at that position.
# 
# Next we will do some example calculations.

# ### Example: find the probability of measuring a horizontal idler photon if the system is prepared in the state $|HH\rangle$

# In[13]:


HH.dag()*Ph_i*HH


# ### Example: find the probability of measuring a horizontal idler photon in the state $|\psi\rangle = |H,+45\rangle$

# In[14]:


psi = tensor(H,P45)  # the prepared state


# In[15]:


psi.dag()*Ph_i*psi


# ### Example 8.2 prob. of measuring vertical signal and horizontal idler if $|\psi\rangle = |R,+45\rangle$

# In[16]:


# First, form the prepared state:
psi = tensor(R,P45)

# Then create the projection operator for the state we are asking about:
projection = VH*VH.dag()

# Finally, calculate the probability by computing the bra-ket:
psi.dag()*projection*psi


# ## Entangled states:
# 
# A very interesting system can be set up where there are paired photons being created with unknown but correlated polarization. In this case, we can say the state is in a combination of $|HH\rangle$ and $|VV\rangle$. If either two-photon state is allowed, then the normalized state is $$\big|\phi^+\big\rangle = \frac{1}{\sqrt{2}}\big( \big|HH\big\rangle + \big|VV\big\rangle \big)$$

# In[17]:


phiPlus = 1/sqrt(2)*(HH + VV)


# In[18]:


phiPlus.dag()*Ph_i*phiPlus  # probability of measuring a horizontal idler photon:


# This is expected, because the HH state has 50% of the probability amplitude. Same for a horizontal signal photon:

# In[19]:


phiPlus.dag()*Ph_s*phiPlus  # probability of measuring a horizontal signal photon


# ## Now, find $P(H_s|H_i)$ (Example 8.5)

# In[20]:


# Projection operator for H idler and H signal:
phh = HH*HH.dag()
phiPlus.dag()*phh*phiPlus


# In[21]:


# Projection operator for H idler
Pih = tensor(qeye(2),H*H.dag())
phiPlus.dag()*Pih*phiPlus


# $P(H_s|H_i) = \frac{P(H_s,H_i)}{P(H_i)}$

# In[22]:


0.5/0.5


# Guaranteed to measure a horizontal signal photon whenever a horizontal idler photon is measured. What about vertical? Find the conditional probability of measuring a vertical signal photon if the idler photon is found to be vertical:

# In[26]:





# Now, measure a different basis (use the +45 states) to show that the photons are always found in the same polarization even when measured at a different angle:

# In[23]:


# Solution

# Probability that signal is +45 and idler +45
Pp45p45 = tensor(P45,P45) * tensor(P45,P45).dag()
phiPlus.dag()*Pp45p45*phiPlus


# In[24]:


# Solution

# Probability that the idler is +45 regardless of the signal
Pp45i = tensor(qeye(2),P45) * tensor(qeye(2),P45).dag()
phiPlus.dag()*Pp45i*phiPlus


# Finally, to really drive this odd point home, show that they are **never** found in the $\big|+45,-45\big\rangle$ state:

# In[25]:


# Solution

# Probability that they are in different 45 states:
Pp45m45 = tensor(P45,M45) * tensor(P45,M45).dag()

phiPlus.dag()*Pp45m45*phiPlus


# ## Using these states solve problems 8.2, 8.3, 8.7, 8.8

# In[ ]:




