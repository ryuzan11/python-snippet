#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

dict_data1 = {
    'a': ["2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01"],
    'b': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01'],
    'c': ['2100-01-01', '2100-01-01', '2100-01-01', '2100-01-01', '2100-01-01', '2100-01-01']
}

dict_df1 = pd.DataFrame(dict_data1)

dict_df1['a'] = pd.to_datetime(dict_df1['a'])
dict_df1['b'] =pd.to_datetime(dict_df1['b'])
dict_df1['c'] =pd.to_datetime(dict_df1['c'])

print(dict_df1.dtypes)
dict_df1


# In[5]:


def convert_tmp(column):
    print(column.dtype)
    
dict_df1['a'].dtype
    
# dict_df1.apply(convert_tmp)


# In[ ]:


## cはそのままで上書きできるか検証　→ 全て上書きされcは消えた

dict_data2 = {
    'a': ["2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01"],
    'b': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01']
}

dict_df2 = pd.DataFrame(dict_data2)

dict_df2['a'] = dict_df2['a'].apply(lambda x: 'abc')
dict_df2['b'] = dict_df2['b'].apply(lambda x: 'def')

dict_df1 = dict_df2

print(dict_df1)


# In[32]:


dict_data3 = {
    'a': ["2018-01-01", "", "2018-01-01", "2018-01-01", "2018-01-01", "2018-01-01"],
    'b': ['2021-01-01', '2021-01-01', None, '2021-01-01', '2021-01-01', '2021-01-01'],
    'c': ['2100-01-01', '2100-01-01', '2100-01-01', None, '2100-01-01', '2100-01-01']
}

dict_df3 = pd.DataFrame(dict_data3)


def convert_hyphen(column):
    print(column.dtype)
    if column.name in ['a', 'b']:
        return column.str.replace('-', '/')
    
    return column


dict_df3 = dict_df3.apply(convert_hyphen)

dict_df3


# In[ ]:


# dict_df4 = dict_df3[['a', 'b']]

# print(dict_df4.dtypes)

# dict_df4 = dict_df4.replace('-', '/', regex=True)

# dict_df3.update(dict_df4)


# dict_df3

