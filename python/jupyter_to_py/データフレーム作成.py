#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


randam_df = pd.DataFrame(np.random.randn(10000,6), columns=list('ABCDEF'))

print(len(randam_df))


# In[9]:


dict_data = {
    'app_type': [1, 2, 3, None, 1, 2, 3, None, 1, 2, 3, None,  1, 2],
    'app_way': ['web', 'agent', None, 'web', 'agent', None, 'web', 'agent', 'web', 'agent',  None,'web', 'agent', None],
    'import_cd': [1, 2, 3, 11, 12, 13, None, 1, 2, 3, 11, 12, 13, None],
    'status_cd': [None, 380, 410, 250, None, 380, 410, 250, None, 380, None, 380, 410, 250]
}

dict_df = pd.DataFrame(dict_data)
print(len(dict_df))


# In[10]:


test_df = pd.read_csv('テストデータ_4列.csv')
test_df.head()


# In[ ]:




