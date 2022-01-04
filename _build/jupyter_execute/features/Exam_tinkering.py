#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
from qutip import *


# In[2]:


e = Qobj([[2,1],[1,2]])
e


# In[3]:


e.eigenstates()


# In[4]:


pz = Qobj([[1],[0]])
mz = Qobj([[0],[1]])
px = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
mx = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
py = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])
my = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()


# In[5]:


psi = 1/sqrt(5)*py + 1/sqrt(5)*px + 1/sqrt(3)*pz
psi.norm()


# In[6]:


psi.dag()*e*psi


# In[7]:


psi.dag()*e*e*psi


# In[8]:


7.66 - 2.6**2


# In[ ]:




