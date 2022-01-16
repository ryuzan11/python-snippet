#!/usr/bin/env python
# coding: utf-8

# In[6]:


from cerberus import Validator

def cerberus_research(params):
    # バリデーションルール
    scheme = {
        'name': {
            'type': 'string',
            # オプション
            'required': False,
            'nullable': True,
            'empty': True
        },
        'id': {
            'type': 'integer',
            # 必須
            'required': True,
            'empty': False
        }
    }
    
    # バリデーションチェックのインスタンスを作成
    check_validator = Validator(scheme)
    
    # バリデーションチェックを実行
    result = check_validator.validate(params)
    
    print(result)

    
# params = {
#     'name': 'yuta',
#     'id': 0
# }

params = {
    'name': 0,
    'id': 'tests'
}

# params = {
#     'id': 0
# }

# params = {
#     'id': 'tests'
# }

# params = {
#     'name': 'yuta',
# }

cerberus_research(params)


# In[8]:





# In[3]:





# In[ ]:




