#!/usr/bin/env python
# coding: utf-8

# In[2]:


# keyに数値が入ることの確認
# JSONオブジェクトのkeyにintを設定すると、フロントでは文字列として受け取ることになる

sample1 = {
    1: "one",
    2: "two",
    3: "three"
}

for i in sample1.keys():
    print(type(i))


# In[2]:


# valueの真偽値の挙動確認

sample2 = {
    "one": True,
    "two": False,
    "three": True
}

for i in sample2.values():
    print(type(i))
    print(i)


# In[2]:


# keyに真偽値が入るか

sample2 = {
    True:　"one",
    False:　"two",
    True: "three"
}


# In[5]:


sample3_dict = {
    'aaa': 'abc',
    'bbb': None
}

sample4_dict = {
    'ccc': 'ccc',
    'bbb': 'sample',
    **sample3_dict
}

print(sample3_dict)
print(sample4_dict)

sample3_dict = {**sample3_dict, **sample4_dict}

print(sample3_dict)


# In[6]:


# getメソッドに第二引数を渡した場合
print(sample1.get(0, 0))


# In[2]:


import json

aaa = json.dumps({'aaa': 'abc'})
bbb = json.dumps({})

print(aaa)
print(bbb)


# In[ ]:




