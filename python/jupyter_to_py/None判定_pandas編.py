#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

sample = {
    'app_type': [1, 2, 3, None, 1, 2, 3, None, 1, 2, 3, None,  1, 2],
    'app_way': [1, 2, None, 1, 2, None, 1, 2, 1, 2, None, 1 ,2, None],
    'import_cd': [1, 2, 3, 11, 12, 13, None, 1, 2, 3, 11, 12, 13, None],
    'status_cd': [None, 380, 410, 250, None, 380, 410, 250, None, 380, None, 380, 410, 250]
}

df = pd.DataFrame(sample)
df.head()


# In[12]:


# 参考までにただのNone同士の比較はTrueになる
print(None == None)
print(None is None)


# In[13]:


# NaN同士の比較はFalseになる
# Not a Number
# Not a Time(NaT)はどうなる？
ccc = df['app_way']  == df['import_cd']
ccc


# - 参考：https://estuarine.jp/2017/09/extract_rows_with_nan/

# In[18]:


nan_df1 = df.isnull()
print(nan_df1.head())


# In[17]:


nan_df1 = df['app_type'].isnull()
print(nan_df1.head())


# ## 1, 12行目が消える

# In[20]:


# Nanがない行が削除される
nan2_df = df[df.isnull().any(axis=1)]
print(nan2_df.head())


# In[22]:


print(df.isnull().any())


# In[9]:


def ccc(a, b, c):
    try:
        print(jjj(a))

        print(jjj(b))
        
        print(c)
    except  Exception as e:
        return e
    
def jjj(d):
    return d / 10

def abab(a, b, c):
    try:
        print(a)
        
        print(b / 10)
        
        print(c / 80)
    except Exception as e:
        return e
    
a = 2
b = 'gjo'
c = 'aowei'

# result = abab(a, b, c)

# result

result2 = ccc(a, b, c)
result2


# In[ ]:




