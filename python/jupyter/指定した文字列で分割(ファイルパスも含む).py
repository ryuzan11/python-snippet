#!/usr/bin/env python
# coding: utf-8

# In[2]:


file_path = 'dir1/dir2/dir3/dir4/sample.jpeg'

print(file_path.split('/')[0])
print(file_path.split('/')[1])
print(file_path.split('/')[-1])
print(file_path.split('/')[-2])


# In[4]:


import os


# In[5]:


basename = os.path.basename(file_path)
print(basename)


# In[6]:


dirname = os.path.dirname(file_path)
print(dirname)


# In[7]:


# ファイルの直上のフォルダ名のみを取得
subdirname = os.path.basename(os.path.dirname(file_path))
print(subdirname)


# In[9]:


root, ext = os.path.splitext(file_path)
print(root)
print(ext)


# In[ ]:




