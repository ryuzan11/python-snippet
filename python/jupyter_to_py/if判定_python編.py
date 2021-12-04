#!/usr/bin/env python
# coding: utf-8

# In[20]:


# アンパック内の空文字の扱い

def convert_dict(app_number=None, service_type=None):
    
    print(type(app_number), app_number)
    print(type(service_type), service_type)
    
    app_number = app_number if app_number else None
    service_type = service_type if service_type else  None
    
    print('1', type(app_number))
    print('2', type(service_type))

    return app_number, service_type

dict_for_unpack = {
    "app_number": "あ",
    "service_type": ""
} 

print(type(dict_for_unpack.get('app_number')))
print(type(dict_for_unpack.get('service_type')))

app_numebr, service_type = convert_dict(**dict_for_unpack)

print(app_numebr)
print(service_type)


# In[21]:


# リスト型で何もない場合の判定
empty_list = []

print('true' if empty_list else 'false')


# In[2]:


# 空文字とNoneのnot判定

none_sample = None
empty_sample = ''

if not (none_sample or empty_sample):
    print('true')


# In[5]:


empty_sample = ''

if not empty_sample:
    print('true')

if not none_sample:
    print('true')


# In[ ]:




