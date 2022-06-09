#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

args = ['python', 'cwd_sample.py']

print(os.getcwd())

a = subprocess.run(args, cwd='sample_dir/', check=True, capture_output=True)
print(a)
print(a.stdout.decode().strip().split('\n'))
print(a.stdout.decode())

print(os.getcwd())


# In[ ]:


args = ['python', 'test_error.py']

a = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(a.stdout)
print(a.stderr)

