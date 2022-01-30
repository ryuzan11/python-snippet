#!/usr/bin/env python
# coding: utf-8

# In[6]:


sample_dict = {
  0: "a",
   1: "aaa",
   2: "bbb",
   3: "ccc",
   4: "ddd" 
}

sample_list = ["aaa", "bbb", "ccc", "ddd"]


# In[7]:


sasa = list(v for k, v in sample_dict.items() if k != 0)
print(sasa)


# In[19]:


# リスト内包表記

in_list = [i for i in sample_dict.values()]

print(in_list)

in_list2 = list(i for i in sample_dict.values())

print(in_list2)


# In[5]:


# ifで条件分岐したリスト内包表記

in_list_if = [value for key, value in sample_dict.items() if key % 2 == 0]

print(in_list_if)


# In[7]:


# 三項演算子を使用したリスト内包表記

in_list_ternary_operator = ['even'  if key % 2 == 0 else 'odd' for key, value in sample_dict.items()]

print(in_list_ternary_operator)


# In[10]:


# enumerateを使ったリスト内包表記

in_list_enumerate_list = [{'key': i, 'value': value} for i, value in enumerate(sample_list)]

print(in_list_enumerate_list)

# 仕組み不明(辞書型でenumerate)
in_list_enumerate_dict = [{'key': i, 'value': s_dict} for i, s_dict in enumerate(sample_dict)]

print(in_list_enumerate_dict)


# In[11]:


# 集合内包表記（Set comprehensions）
# 順番が変わっている？

in_set = {v for v in sample_list}

print(in_set)


# In[18]:


# 辞書内包表記（Dict comprehensions）

in_dict = {k: v for k, v in sample_dict.items()}

print(in_dict)


# In[ ]:




