#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# as eはPython3の書き方
# except節はワイルドカード
# Exceptionはシステム終了以外のすべての組み込み例外の基底クラス


# In[3]:


# 色々な例外エラー処理

def except_test():
    try:
#         raise NameError('name error')
        raise Exception('aaa')
    except (ZeroDivisionError, TypeError) as e:
        print('ZeroDivisionError, TypeError')
        print(type(e), e)
        print(type(e.args), e.args)
        print(type(e.args[0]), e.args[0])
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
        print(type(e), e)
        print(type(e.args), e.args)
        print(type(e.args[0]), e.args[0])
    except TypeError as e:
        print('TypeError')
        print(type(e), e)
        print(type(e.args), e.args)
        print(type(e.args[0]), e.args[0])
    except Exception as e:
        print('Exception')
        print(type(e), e)
        print(type(e.args), e.args)
        print(type(e.args[0]), e.args[0])
    except:
        print('Error')
    print('例外終了後')
        
except_test()


# In[10]:


# 例外をキャッチしても何も処理を行わず終了

def except_test2():
    try:
        raise
    except Exception as e:
        print(type(e), e)
        pass
    print('実行される')
        
except_test2()


# In[16]:


# exceptでエラーを拾うが、処理は中断されない

def except_test3():
    try:
        raise
    except Exception as e:
        print('try内でエラー発生')
        print(e)
        
    print('処理再開')

except_test3()


# In[17]:


# elseは例外が発生せず正常終了したあとに行う処理
# finallyは例外が発生した場合もしなかった場合も常に最後に行う処理

def except_test4(a):
    try:
        print(10 / a)
    except Exception as e:
        print(type(e), e)
    else:
        print('例外発生なし')
    finally:
        print('最後に絶対に処理')
        
except_test4('a')
# except_test4(10)


# In[2]:


# returnが使えるか
def except_test5():
   try:
       raise Exception()
   except Exception as e:
       return "a"
   
except_test5()


# In[ ]:




