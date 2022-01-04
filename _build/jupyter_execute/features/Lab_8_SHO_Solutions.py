#!/usr/bin/env python
# coding: utf-8

# # Lab 8 - Simple Harmonic Oscillator states
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


# In[7]:


psi


# In[8]:


a.dag()*psi


# In[9]:


a.dag()*basis(N,2) == sqrt(3)*basis(N,3)


# ## Problem 12.5 and 12.6:
# These are simple, just view the matrix representation of the operators

# In[10]:


a


# In[11]:


a.dag()


# ## Problem 12.7:
# First, define $\hat{X}$ and $\hat{P}$ operators

# In[12]:


X = 1/2 * (a + a.dag())
P = 1/2j * (a - a.dag())


# In[13]:


psi = 1/sqrt(2)*(basis(N,1)+basis(N,2))
ex = psi.dag()*X*psi
exq = psi.dag()*X*X*psi
ep = psi.dag()*P*psi
epq = psi.dag()*P*P*psi


# In[14]:


deltaX = sqrt(exq[0][0][0] - ex[0][0][0]**2)
deltaP = sqrt(epq[0][0][0] - ep[0][0][0]**2)


# In[15]:


deltaX * deltaP * 2 # compare to uncertainty relation (ΔxΔp >= 1/2)
# the factor of two is to convert from the unitless version of the operator


# Alternatively, we can find the indeterminacy bound for ΔX and ΔP (the unitless operators): $$\Delta X \Delta P \geq \frac{1}{2}\left|\left\langle \left[\hat{X},\hat{P}\right] \right\rangle\right|$$

# In[16]:


1/2*(psi.dag()*commutator(X,P)*psi).norm()


# Which is also satisfied by the calculated value (1.41 > 0.25)

# ## Problem 12.8:

# In[17]:


psi = 1/sqrt(2)*(basis(N,2)+basis(N,4))
ex = psi.dag()*X*psi
exq = psi.dag()*X*X*psi
ep = psi.dag()*P*psi
epq = psi.dag()*P*P*psi


# In[18]:


deltaX = sqrt(exq[0][0][0] - ex[0][0][0]**2)
deltaP = sqrt(epq[0][0][0] - ep[0][0][0]**2)


# In[19]:


deltaX * deltaP * 2 # to compare to book solution which uses the full x and p operators with units


# In[ ]:




