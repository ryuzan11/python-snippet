#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import time

test_df = pd.read_csv('テストデータ_4列.csv')
test_df.head()


# In[6]:


column_list = ['col1', 'col2', 'col3', 'col4']


# In[8]:


# 行全てをメソッドに渡す
def test_apply_sample2(row):
    test_index = row.get('index')
    for i in column_list:
        aaa = '{}_{}_sample'.format(test_index, row.get(i))

start = time.time()

test_df.apply(test_apply_sample2, axis='columns')

print(time.time() - start)


# In[10]:


start = time.time()

index_test_df = test_df.set_index('index')[column_list]

test_dict = index_test_df.to_dict(orient='index')

for key, value in test_dict.items():
    for i in column_list:
        aaa = '{}_{}_sample'.format(key, value.get(i))

print(time.time() - start)


# In[12]:


start = time.time()

index_test_df = test_df.set_index('index')[column_list]

test_dict = index_test_df.to_dict(orient='index')

for key in test_dict.keys():
    for i in column_list:
        aaa = '{}_{}_sample'.format(key, test_dict.get(key).get(i))

print(time.time() - start)


# In[ ]:




