#!/usr/bin/env python
# coding: utf-8

# In[11]:


# class Test:
#     def __init__(self, word):
#         self.output_word = word
        
#     def __repr__(self):
#         return self.output_word

# test_instance = Test('output')
# print(test_instance)


# In[24]:


class Sample:
    def __init__(self, a_list):
        self.my_list = a_list
        
#     def __repr__(self):
#         return ','.join(self.my_list)
        
    def add(self, word):
        self.my_list.append(word)
        

sample = Sample(['aaa', 'bbb', 'ccc'])
sample.add('ddd')

print(sample)


# In[25]:


print(sample)


# In[ ]:




