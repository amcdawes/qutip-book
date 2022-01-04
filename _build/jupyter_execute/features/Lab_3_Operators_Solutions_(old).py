#!/usr/bin/env python
# coding: utf-8

# # Lab 3: Operators
# An overview of operator properties

# In[1]:


import matplotlib.pyplot as plt
from numpy import sqrt,cos,sin,pi,arange
from qutip import *


# In[2]:


H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])


# ## Example 1: the outer product and the projection operator

# We already have the $|H\rangle$ state represented as a vector in the HV basis, so the $\hat{P}_H$ operator is the outer product $|H\rangle\langle H|$:

# In[3]:


Ph = H*H.dag()
Ph


# Same with the $\hat{P}_V$ operator:

# In[4]:


Pv = V*V.dag()
Pv


# ## 1) Verify Eq. 4.38 for the HV basis states. Repeat for the 45, and ± basis

# In[ ]:





# ## 2) Represent the $\hat{R}_p(\theta)$ operator in the HV basis and verify your representation by operating on $|H\rangle$ and $|V\rangle$ states.

# In[5]:


def Rp(theta):
    return Qobj([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]).tidyup()


# In[6]:


Rp(pi/2)


# In[7]:


V == Rp(pi/2)*H


# ## 3) Using your $\hat{R}_p(\theta)$ operator, verify the operator properties described in Sections 4.1 and 4.2. Specifically, verify Eqns. 4.5, 4.6, 4.7, 4.16, 4.18, 4.22, and 4.27

# In[ ]:





# ## Example: similarity transform
# The following defines a function that creates a similarity transform matrix. It takes the two old basis vectors and the two new basis vectors.

# In[8]:


def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])


# In[9]:


Shv45 = sim_transform(H,V,P45,M45)  # as found in Example 4.A.1, Eq. 4.A.10.
Shv45


# In[10]:


Shv45 * L  # compare to Eq. 


# ## 4) Represent $\hat{P}_H$ in the ±45 basis.
# Check your answer against Eqns. 4.A.17 and 4.72

# In[11]:


Shv45*Ph*Shv45.dag()


# In[ ]:




