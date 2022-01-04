#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 in-class problems

# ## 2.3 Find the eigenvalues and vectors of J$_\theta$ for $\theta$=45

# In[1]:


from qutip import *
from numpy import cos, sin, pi, deg2rad


# In[2]:


qm = Qobj([[cos(pi/4)**2,cos(pi/4)*sin(pi/4)],[cos(pi/4)*sin(pi/4),sin(pi/4)**2]])


# In[3]:


qm


# In[4]:


qm.eigenstates()


# In[5]:


from numpy import sqrt, exp
1/sqrt(2)


# In[6]:


phi = 1.5
Jphi = Qobj([[exp(1j)*phi,0],[0,1]])
Jphi 


# In[7]:


hvec = Qobj([[1],[0]])
hvec


# In[8]:


vvec = Qobj([[0],[1]])
vvec


# In[9]:


Jphi*hvec


# In[10]:


Jphi*vvec


# In[ ]:




