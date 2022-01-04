#!/usr/bin/env python
# coding: utf-8

# # Lab 2: Quantum States
# Useful for working examples and problems with photon quantum states. You may notice some similarity to the Jones Calculus ;-)

# In[1]:


from numpy import sqrt,cos,sin
from qutip import *


# These are the polarization states:

# In[2]:


H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])


# In[3]:


V


# Devices:
# 
# HWP - Half-wave plate axis at $\theta$ to the horizontal
# 
# LP - Linear polarizer, axis at $\theta$
# 
# QWP - Quarter-wave plate, axis at $\theta$
# 
# Note, these are functions so you need to call them with a specific value of theta.

# In[4]:


def HWP(theta):
    return Qobj([[cos(2*theta),sin(2*theta)],[sin(2*theta),-cos(2*theta)]]).tidyup()


# In[5]:


def LP(theta):
    return Qobj([[cos(theta)**2,cos(theta)*sin(theta)],[sin(theta)*cos(theta),sin(theta)**2]]).tidyup()


# In[6]:


def QWP(theta):
    return Qobj([[cos(theta)**2 + 1j*sin(theta)**2,
                 (1-1j)*sin(theta)*cos(theta)],
                [(1-1j)*sin(theta)*cos(theta),
                 sin(theta)**2 + 1j*cos(theta)**2]]).tidyup()


# ## Example 1) Check that the $|H\rangle$ state is normalized

# In[7]:


H.dag()*H


# In[8]:


get_ipython().run_line_magic('pinfo', 'Qobj')


# In[9]:


psi = Qobj([[1+1j],[2-1j]])


# In[10]:


psi.dag()


# In[11]:


psi.dag().dag()


# ## 1) verify that the $|V\rangle$ state is normalized

# ## 2) Verify that the $|H\rangle$ and $|V\rangle$ states are orthogonal. Repeat for the other pairs of states.

# ## 3) Find the horiztonal component $c_H$ of the state $\psi = \frac{1}{\sqrt{5}}|H\rangle + \frac{2}{\sqrt{5}}|V\rangle$

# ## 4) Verify Eq. (3.18) 

# In[ ]:




