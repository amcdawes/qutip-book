#!/usr/bin/env python
# coding: utf-8

# # Gaussian Wavepackets (using Sympy)

# In[1]:


from sympy import *


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


def Gaussian(x, alpha, beta):
    return 1/(beta*sqrt(pi)) * exp(-(x - alpha)**2/(beta**2))


# In[4]:


x,p,a,b = symbols('x p a b')


# In[5]:


plot(Gaussian(x,5,0.5))


# In[6]:


integrate(Gaussian(x,5,0.5),(x,-oo,oo))


# In[7]:


def eipx_Gaussian(x,p,alpha,beta):
    return exp(1j*p*x)*Gaussian(x,alpha,beta)


# In[8]:


def psip(p):
    result = integrate(eipx_Gaussian,(p,-oo,oo))
    return result[0]


# In[9]:


eipx_Gaussian(2,1,2,3)


# In[10]:


integrate(eipx_Gaussian(x,p,a,b),(p,-oo,oo),conds='none')


# In[ ]:




