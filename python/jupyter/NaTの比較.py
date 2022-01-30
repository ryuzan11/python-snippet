#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

sample = {
    'app_type': ["2021-03-11 11:11:11", "NaT"],
    'app_way': ["2021-03-11 11:11:11", "NaT"]
}

df = pd.DataFrame(sample)
df.head()


# In[17]:


app_type_date = pd.to_datetime(df['app_type'])

app_way_date = pd.to_datetime(df['app_way'])


# In[19]:


type(app_type_date[1])


# In[18]:


type(app_way_date[1])


# In[13]:


# NaT同士の判定はFalseになる
print(app_type_date == app_way_date)


# In[ ]:




