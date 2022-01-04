#!/usr/bin/env python
# coding: utf-8

# # Lab 3: Operators
# An overview of operator properties

# In[1]:


import matplotlib.pyplot as plt
from numpy import sqrt,cos,sin,arange,pi
from qutip import *
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])


# ## Example 1: the outer product and the projection operator

# We already have the $|H\rangle$ state represented as a vector in the HV basis, so the $\hat{P}_H$ operator is the outer product $|H\rangle\langle H|$ (a ket then a bra):

# In[3]:


H


# In[4]:


Ph = H*H.dag()
Ph


# Same with the $\hat{P}_V$ operator:

# In[5]:


Pv = V*V.dag()
Pv


# ## Example 2: Verify Eq. 4.38 for the HV basis states. Repeat for the ±45, and LR basis

# In[6]:


identity(2)


# In[7]:


Ph + Pv == identity(2)


# In[8]:


P45*P45.dag()


# In[9]:


M45*M45.dag()


# In[10]:


P45*P45.dag() + M45*M45.dag()


# In[11]:


L*L.dag()


# In[12]:


R*R.dag()


# In[13]:


L*L.dag() + R*R.dag()


# ## Example 3: Represent the $\hat{R}_p(\theta)$ operator in the HV basis and verify your representation by operating on $|H\rangle$ and $|V\rangle$ states. Use the following template function definition.

# In[14]:


def Rp(theta):
    return Qobj([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]).tidyup()


# In[15]:


Rp(pi/2)


# In[16]:


V==Rp(pi/2)*H


# In[17]:


# Solution Goes Here


# ## 1) Using the $\hat{R}_p(\theta)$ operator, verify the operator properties described in Sections 4.1 and 4.2. Specifically, verify Eqns. 4.6, 4.7, 4.16, 4.18, 4.22, and 4.27

# In[18]:


# Solution Goes Here


# ## Example: the similarity transform
# The following defines a function that creates a similarity transform matrix. It takes the two old basis vectors and the two new basis vectors as arguments. To apply the transform, simply multiply the matrix onto the state vector or ooperator matrix. Following the examples below, explore this transform.

# In[19]:


def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])


# We can define a similarity transform that converts from $HV\rightarrow \pm 45$

# In[20]:


Shv45 = sim_transform(H,V,P45,M45)  # as found in Example 4.A.1, Eq. 4.A.10.
Shv45


# In[21]:


Shv45 * H  # compare to Eq. 4.A.12


# ## 4) Use the similarity transform to represent $|V\rangle$ in the ±45 basis

# In[ ]:





# ## 5) Represent $\hat{P}_H$ in the ±45 basis.
# Check your answer against Eqns. 4.A.17 and 4.72

# In[ ]:





# ## 6) Represent $\hat{P}_V$ in the ±45 basis.

# In[ ]:




