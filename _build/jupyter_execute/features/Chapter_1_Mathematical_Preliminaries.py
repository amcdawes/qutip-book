#!/usr/bin/env python
# coding: utf-8

# # Chapter 1: Mathematical Preliminaries
# ## 1.1 Probability
# ### 1.1.1 Moments of Measured Data

# Arrays of data, and their average and sum in python

# In[1]:


import matplotlib.pyplot as plt
from numpy import array, sin, sqrt, dot, outer
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


x = array([1,2,3])


# In[3]:


x.sum()


# In[4]:


x.mean()


# The formal definition (and to make sure we match with the book) is to take the sum and divide by the number of items in the sample:

# In[5]:


x.sum()/len(x)


# #### Higher order moments
# Operate on the sample, python does this element-by-element, then do the same thing as above:

# In[6]:


x**2


# In[7]:


(x**2).sum() # Note the parenthesis!


# In[8]:


(x**2).sum()/len(x)


# #### It works for functions too:

# In[9]:


sin(x)


# In[10]:


sin(x).sum()/len(x)


# #### Variance

# In[11]:


x.var()  # Variance


# In[12]:


x.std()  # Standard Deviation


# In[13]:


x.std()**2 == x.var()  # Related by a square root


# ### Example 1.1

# In[14]:


x_m = array([9,5,25,23,10,22,8,8,21,20])


# In[15]:


x_m.mean()


# In[16]:


(x_m**2).sum()/len(x_m)


# In[17]:


sqrt(281.3 - (15.1)**2)


# In[18]:


x_m.std()


# Close enough!

# ### 1.1.2 Probability

# #### Example 1.2

# In[19]:


n, bins, patches = plt.hist(x_m,bins=7)


# The hist function has several possible arguments, we use bins=7 to match the example.

# In[20]:


n/10.0*array([6,9,12,15,18,21,24])  # counts times each bin-center value


# In[21]:


sum(_)


# In[22]:


n/10.0*array([6,9,12,15,18,21,24])**2  # counts times each bin-center value


# In[23]:


sum(_)


# ## 1.2 Linear Algebra
# ### 1.2.1 Vectors and Basis sets
# We'll use the qutip library, even though this is all just linear algebra:

# In[24]:


rvec = array([1,2])  # A row vector


# In[25]:


rvec


# In[26]:


cvec = array([[1],[2]])  # A column vector


# In[27]:


cvec


# In[28]:


cvec*rvec # Actually the outer product:


# In[29]:


dot(rvec,cvec)


# In[30]:


outer(cvec,rvec)


# However, try running
# ```
# dot(cvec,rvec)
# ```
# it won't work (think about why not!)

# 
