#!/usr/bin/env python
# coding: utf-8

# In[4]:


# beforehandの引数を受け取る
def beforehand(test1, test2):
    # secondfunc関数を受け取る
    print('beforehandの引数 =>')
    print(test1)
    print(test2)
    def second(func):
        print('デコレータに組み込まれる関数(func) =>')
        print(func)
        print('argsはここでは使えない\n')
        def _wrapper(*args, **kwargs):
            print('secondfuncの引数 =>')
            print(*args)
            # ここで改行を入れると二回改行されている？
            print('\n')
            print('kwargs =>')
            print(**kwargs)
#             print('引数funcをデコレータ内で実行してみた =>')
#             # ここでfuncを実行すると、最後にNoneが出力されるぞ？
#             print(func(*args))
            func(*args)
#             response = func(*args)
            # returnで関数返さなくてもデコレータ は動く
#             return response
        return _wrapper
        print(_wrapper)
    return second


@beforehand(test1='beforehand引数1', test2='beforehand引数2\n')
def secondfunc(sample1, sample2):
    print('secondfunc内 =>')
    print(sample1)
    print(sample2)
    return

sample1 = 'secondfunc引数1'
sample2 = 'secondfunc引数2'
secondfunc(sample1, sample2)
        


# In[3]:


def a(b=0):
    if b>0:
        print('a')
        
a(b="ka")


# In[4]:


def hgt(a):
    return a, 'bbb'

b, c = hgt('何個受け取れる？')

print(b,c)

def jki(a):
    return a

d, e = jki('何個受け取れる？')

print(d, e)


# In[ ]:




