#!/usr/bin/env python
# coding: utf-8

# # Gaussian Wavepackets

# In[1]:


import numpy as np


# In[2]:


def Gaussian(x, chi, sigma):
    return 1/(sigma*sqrt(2*np.pi)) * np.exp(-(x - chi)**2/(2*sigma**2))


# In[3]:


get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


x = arange(0,10,0.1)


# In[5]:


plot(x,Gaussian(x,5,0.5))


# In[13]:


import scipy.integrate as integ


# In[14]:


get_ipython().run_line_magic('pinfo', 'integ.quad')


# In[15]:


integ.quad(Gaussian, -numpy.inf, numpy.inf, (5,5))


# In[62]:


def eipx_Gaussian(x,p,chi,sigma):
    return np.exp(1j*p*x)*Gaussian(x,chi,sigma)
    


# In[66]:


def psip(p):
    result = scipy.integrate.quad(eipx_Gaussian,-numpy.inf,numpy.inf,(p,5,0.5))
    return result[0]


# In[94]:


get_ipython().run_line_magic('pinfo', 'plot')


# In[74]:





# In[83]:


psip(0)


# In[16]:


from sympy import *


# In[19]:


z = symbols('z')


# In[20]:


integrate(Gaussian(z,5,0.5),(z,-oo,oo))


# In[ ]:




