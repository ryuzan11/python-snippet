#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

def request():
    r_get = requests.get('https://github.com/timeline.json')
    # data,headers,timeout
    r_post = requests.post("http://httpbin.org/post")
    
    print(r_get.text, '\n')
    print(r_get.encoding, '\n')
    print(r_get.content, '\n')
    print(r_get.json(), '\n')
    print(r_get.raw, '\n')
    print('post\n')
    print(r_post.text, '\n')
    print(r_post.text.split(','))
    
request()


# In[ ]:




