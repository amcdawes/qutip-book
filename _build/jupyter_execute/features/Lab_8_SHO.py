#!/usr/bin/env python
# coding: utf-8

# # Lab 8: Simple Harmonic Oscillator states
# Problems from Chapter 12

# In[1]:


from numpy import sqrt
from qutip import *


# ## Define the standard operators

# In[2]:


N = 10  # pick a size for our state-space
a = destroy(N)
n = a.dag()*a


# ## Problem 12.1:

# In[3]:


a*a.dag() - a.dag()*a


# ## Problem 12.2:

# In[4]:


n*a.dag() - a.dag()*n


# In[5]:


n*a.dag() - a.dag()*n == a.dag()


# ## Problem 12.3 (use n=2 as a test-case):
# To define $|2\rangle$ use the `basis(N,n)` command where `N` is the dimension of the vector, and `n` is the quantum number.

# In[6]:


psi = basis(N,2)


# In[ ]:





# ## Problem 12.5 and 12.6:
# These are simple, just view the matrix representation of the operators

# In[ ]:





# ## Problem 12.7:
# First, define $\hat{X}$ and $\hat{P}$ operators
# 
# ```
# X=
# P=
# ```

# In[7]:





# In[7]:


psi = 1/sqrt(2)*(basis(N,1)+basis(N,2))


# In[ ]:





# ## Problem 12.8:

# In[8]:


psi = 1/sqrt(2)*(basis(N,2)+basis(N,4))


# In[ ]:





# In[ ]:




