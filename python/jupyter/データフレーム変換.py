#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

sample = {
    'app_type': [1, 2, 3, None, 1, 2, 3, None],
    'app_way': [1, 2, None, 1, 2, None, 1, 2],
    'import_cd': [1, 2, 3, 11, 12, 13, None, 1],
    'status_cd': [None, 380, 410, 250, None, 380, 410, 250]
}
df = pd.DataFrame(sample)


# In[4]:


bool_df = df['app_type'] == df['app_way']


# In[9]:


# applyでgetメソッドを指定すると、どう動くのか

print(df['app_type'])

convert_app_type_dict = {
    1: "aaa",
    2: "bbb",
    3: "ccc",
    None: "やばい"
}

sample_df = df['app_type'].apply(convert_app_type_dict.get)
print(sample_df)


# In[4]:


# 新しい行
df['new_way'] = bool_df.apply(lambda x: 1 if x else 0)
df.head()


# In[5]:


# 既存行
df['app_type'] = bool_df.apply(lambda x: 1 if x else 0)
df.head()


# In[6]:


def abc(row):
    app_type = row['app_type']
    app_way = row['app_way']
    
    if app_type == app_way:
        return 1
    return 0
    
int_method = df.apply(abc, axis=1)
int_method.head()


# In[7]:


int_lambda = df.apply(lambda x: 1 if x['app_type'] == x['app_way'] else 0, axis=1)
int_lambda.head()


# In[8]:


# loc使用
df.loc[~bool_df, 'import_cd'] = 'False'
df.head()


# In[9]:


# whereで新しいseriesを作成
convert_not_false = df['import_cd'].where(df['import_cd'] == 'False', 'False以外を置換')
convert_not_false.head()


# In[10]:


# maskで新しいseriesを作成
convert_false = df['import_cd'].mask(df['import_cd'] == 'False', 'Falseを置換')
convert_false.head()


# In[11]:


# maskでdataframeの列を変換
df['import_cd'] = df['import_cd'].mask(df['import_cd'] == 'False', 'Falseを置換')
df.head()


# In[17]:


# assign使用
new_df = df.assign(new_way=df['status_cd'])
new_df.head()


# In[21]:


# assign使用2
# applyでメソッド使用
# 既存データフレームを上書き
def sample_assign(cd):
    if cd == 1:
        return '1でした'
    
    if cd == 0:
        return '0でした'
    
    return 'その他'

convert_new_way_df= df.assign(new_way=df['new_way'].apply(sample_assign))
print(df.head())
print(convert_new_way_df.head())


# In[50]:


# app_typeが0のデータのみ抽出
filter_df = df[df['app_type'] == 0]
filter_df.head()


# In[51]:


aaa = {
    0: 'aaa'
}

# Warnig発生
filter_df['app_type'] = filter_df['app_type'].apply(lambda x: aaa.get(x))
filter_df


# In[52]:


aaa = {
    'aaa': 0
}

# seriesで取得できる
filter_df = filter_df['app_type'].apply(lambda x: aaa.get(x))
filter_df


# In[54]:


# dataframeが空の場合でもエラーにはならない
sample_df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'height' : [1.66, 1.68, 1.70, 1.72, 1.75],
    'weight'    : [50, 55, 65, 75, 80]    
})


def calc_shape(x):
    bmi = x.weight / (x.height ** 2)
    if bmi >= 25:
        return("Overweight")
    elif bmi >= 18.5:
        return("Normal")
    else:
        return("Thin")
    
sample2_df = sample_df[sample_df["name"] == "Foo"]
print(sample2_df)

sample2_df["name"] = sample2_df.apply(lambda x: calc_shape(x), axis=1)
sample2_df


# In[ ]:




