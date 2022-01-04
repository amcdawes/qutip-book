#!/usr/bin/env python
# coding: utf-8

# # Ch 8 - Examples

# In[1]:


from numpy import sqrt
from qutip import *


# In[2]:


H = Qobj([[1],[0]])
V = Qobj([[0],[1]])


# ## Example 8.A.1:

# In[3]:


psi = 1/sqrt(2)*tensor(H,H) + 1/sqrt(2)*tensor(V,V)
psi


# In[4]:


rho_ent = psi*psi.dag()


# In[5]:


(rho_ent*rho_ent).tr()


# In[6]:


rho_mix = 0.5*tensor(H,H)*tensor(H,H).dag() + 0.5*tensor(V,V)*tensor(V,V).dag()


# In[7]:


(rho_mix*rho_mix).tr()


# ## Example 8.A.2

# Remember the 45 states:

# In[8]:


P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])


# Create the projection operator for $|+45,+45\rangle$

# In[9]:


Proj_4545 = tensor(P45,P45)*tensor(P45,P45).dag()


# In[10]:


(Proj_4545*rho_mix).tr()


# Create projection operator for $|+45\rangle_i$

# In[11]:


Proj_45i = tensor(qeye(2),P45)*tensor(qeye(2),P45).dag()


# In[12]:


(Proj_45i*rho_mix).tr()


# In[13]:


0.25/0.5


# ### Extend the example for the pure (superposition) state

# In[14]:


(Proj_4545*rho_ent).tr() / (Proj_45i*rho_ent).tr()


# The photons are entanlged and therefore show perfect correlation even in the +45 measurements.
