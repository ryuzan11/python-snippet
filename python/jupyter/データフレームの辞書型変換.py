#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time

test_df = pd.read_csv('テストデータ_4列.csv')
test_df


# In[6]:


column_list = ['col1', 'col2', 'col3', 'col4']

def test_apply_sample1(index, dict):
    info = dict.get(index)
    for i in column_list:
        aaa = '{}_sample'.format(info.get(i))

start = time.time()

aaa = test_df[['col1', 'col2']]
print(aaa.head())

index_test_df = test_df.set_index('index')

test_dict = index_test_df.to_dict(orient='index')

test_df['index'].apply(test_apply_sample1, dict=test_dict)

print(time.time() - start)


# In[12]:


# エラーにはならず、{}で返ってくる

sample2 = {
    'app_type': [1, 2, 3, None, 1, 2, 3, None, 1, 2, 3, None,  1, 2],
    'app_way': [1, 2, None, 1, 2, None, 1, 2, 1, 2, None, 1 ,2, None]
}

df = pd.DataFrame(sample2)
df2 = df[(df['app_type'] == 4) & (df['app_way'] == 4)]
df_dict = df2.set_index(['app_type']).to_dict(orient='index')
df_dict


# In[13]:


# getメソッドに第二引数を渡した場合の挙動

sample_dict1 = pd.DataFrame({
    'col3': [1,2,3,4,1,2,3,4],
    'col4': [4,5,6,7,4,5,6,7]
})

sample_dict2 = {
    4: 'ok'
}

sample_dict1['sample_column1'] = sample_dict1['col3'].apply(sample_dict2.get, args=('0', ))
sample_dict1['sample_column2'] = sample_dict1['col4'].apply(sample_dict2.get, args=('0', ))
sample_dict1

# help(sample_dict.get)
# test_df['sample_column1'] = test_df['col4'].apply(sample_dict.get, default='0')
# test_df['sample_column2'] = test_df['col3'].apply(sample_dict.get, default='0')


# In[ ]:




