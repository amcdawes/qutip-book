#!/usr/bin/env python
# coding: utf-8

# # Lab 4: Measurements
# First our standard definitions:

# In[1]:


import matplotlib.pyplot as plt
from numpy import sqrt,pi,cos,sin,arange,random
from qutip import *


# In[2]:


H = Qobj([[1],[0]])
V = Qobj([[0],[1]])
P45 = Qobj([[1/sqrt(2)],[1/sqrt(2)]])
M45 = Qobj([[1/sqrt(2)],[-1/sqrt(2)]])
R = Qobj([[1/sqrt(2)],[-1j/sqrt(2)]])
L = Qobj([[1/sqrt(2)],[1j/sqrt(2)]])


# In[3]:


def sim_transform(o_basis1, o_basis2, n_basis1, n_basis2):
    a = n_basis1.dag()*o_basis1
    b = n_basis1.dag()*o_basis2
    c = n_basis2.dag()*o_basis1
    d = n_basis2.dag()*o_basis2
    return Qobj([[a.data[0,0],b.data[0,0]],[c.data[0,0],d.data[0,0]]])


# ###Q: Define the $\hat{\mathscr{P}}_{HV}$ operator

# In[4]:


Phv = H*H.dag() - V*V.dag()
Phv


# ###Q: What is the expectation value $\langle \hat{\mathscr{P}}_{HV}\rangle$ for state $|\psi\rangle = \frac{1}{\sqrt{5}}|H\rangle + \frac{2}{\sqrt{5}}|V\rangle$? Interpret this result given the amplitudes in the state.

# In[5]:


psi = 1/sqrt(5)*H + 2/sqrt(5)*V


# In[6]:


psi.dag()*Phv*psi


# ###Q: What is the variance of $\mathscr{P}_{HV}$?

# In[7]:


psi.dag()*Phv*Phv*psi


# In[8]:


1- (-0.6)**2


# ###Example: Use the random function to generate a mock data set for the state $|\psi\rangle$.
#     random.choice([1,-1],size=10,p=[0.2,0.8])
# gives a list of 10 numbers, either 1 or -1 with the associated probability p:

# In[9]:


data = random.choice([1, -1],size=1000000,p=[0.2,0.8])


# ###Q: Verify the mean and variance of the mock data set match your QM predictions. How big does the set need to be for you to get ±5% agreement?

# In[10]:


data.mean()


# In[11]:


data.var()


# ###Q: Answer problems 5.11, 5.12, 5.13, 5.14, 5.17, 5.18, 5.19 from the textbook. These are an opportunity to practice with a new operator $\hat{\mathscr{P}}_{C}$

# In[12]:


P_45 = P45*P45.dag() - M45*M45.dag()


# In[13]:


P_45


# In[14]:


P_c = L*L.dag() - R*R.dag()


# In[15]:


P_c


# In[ ]:




