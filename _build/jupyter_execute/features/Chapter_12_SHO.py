#!/usr/bin/env python
# coding: utf-8

# # Chapter 12: Simple Harmonic Oscillator
# Several examples that make use of the built-in Simple Harmonic Oscillator tools:

# In[1]:


from numpy import sqrt,linspace,exp
from qutip import *
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


N = 40 # size of the Hilbert space.
       # N needs to be large enough that matrix is not truncated
a = destroy(N)
n = a.dag()*a


# Define a coherent state with $\alpha = 2:$

# In[3]:


psi = coherent(N,1)


# In[4]:


psi


# Expectation value $\langle n\rangle$:

# In[5]:


psi.dag()*n*psi


# In[6]:


# Convert to a density matrix:
psi_dm = ket2dm(psi)


# In[7]:


psi*psi.dag()


# In[8]:


# Fock state distribution of the coherent state:
plot_fock_distribution(psi_dm)


# Also look at other coherent states:

# In[9]:


# With larger N and α:
plot_fock_distribution(coherent_dm(100,6))


# And some other density matrices, like a fock-state (or n eigenstate):

# In[10]:


# With a Fock state (number state):
plot_fock_distribution(fock_dm(20,2))


# In[11]:


fock(20,2)


# And a thermal state:

# In[12]:


# A thermal state has decaying amplitudes
plot_fock_distribution(thermal_dm(20,2))


# ## Finally, can visualize the phasor using what is called the Wigner function:

# In[13]:


xvec = linspace(-10,10,200) # Create an array for the phase space coordinates.
plt.imshow(wigner(coherent(40,5j)+coherent(40,-5j),xvec,xvec), extent=[-10,10,-10,10]) # contour plot of Wigner function


# In[42]:





# In[ ]:




