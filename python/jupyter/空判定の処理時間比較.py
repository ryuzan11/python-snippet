#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import timeit

df = pd.DataFrame(np.random.randn(10000, 4), columns=list('ABCD'))

def empty(df):
    return df.empty

def lenz(df):
    return len(df) == 0

def lenzi(df):
    return len(df.index) == 0

get_ipython().run_line_magic('timeit', 'empty(df)')
get_ipython().run_line_magic('timeit', 'lenz(df)')
get_ipython().run_line_magic('timeit', 'lenzi(df)')


# In[ ]:




