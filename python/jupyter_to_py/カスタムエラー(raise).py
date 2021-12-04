#!/usr/bin/env python
# coding: utf-8

# In[1]:


def custom_value_error():
    try:
        raise ValueError('値エラー')
    except ValueError as e:
        print(type(e))
        print(e)
    except ZeroDivisionError as e:
        print(type(e))
        print(e)
    except Exception as e:
        print(type(e))
        print(e)
    print('last')
        
def custom_zero_error():
    try:
        raise ZeroDivisionError('演算0エラー')
    except ValueError as e:
        print(type(e))
        print(e)
    except ZeroDivisionError as e:
        print(type(e))
        print(e)
    except Exception as e:
        print(type(e))
        print(e)
    print('last')
        
def custom_except_error():
    try:
        raise Exception('大半エラー')
    except ValueError as e:
        print(type(e))
        print(e)
    except ZeroDivisionError as e:
        print(type(e))
        print(e)
    except Exception as e:
        print(type(e))
        print(e)
    print('last')
        
custom_value_error()
custom_zero_error()
custom_except_error()


# In[ ]:




