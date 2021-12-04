#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import pytz

# jstのタイムゾーンを取得
JST = pytz.timezone("Asia/Tokyo")

# jstで今の日付を取得
now_jst_datetime = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))


target_date_str = '20210519'
# strptimeの第二引数にdatetime型にしたい文字列の型を指定
target_date_datetime = datetime.datetime.strptime(target_date_str, '%Y%m%d')
# datetime型の日付をjstで取得
target_date_jst_datetime = JST.localize(target_date_datetime)

print('now => {}'.format(now_jst_datetime))
print('target date => {}'.format(target_date_jst_datetime))

if now_jst_datetime < target_date_jst_datetime:
    print('true')


# In[21]:


JST = pytz.timezone("Asia/Tokyo")

yesterday_jst_datetime = datetime.datetime.now(pytz.timezone('Asia/Tokyo')) -  datetime.timedelta(days=1)

target_date_str = '20210518'
target_date_datetime = datetime.datetime.strptime(target_date_str, '%Y%m%d')
target_date_jst_datetime = JST.localize(target_date_datetime)

print('yesterday => {}'.format(yesterday_jst_datetime))
print('target date => {}'.format(target_date_jst_datetime))

if yesterday_jst_datetime >= target_date_jst_datetime:
    print('ok')
    print('1')
    
if yesterday_jst_datetime < target_date_jst_datetime:
    print('error')
    print('2')
    
if yesterday_jst_datetime == target_date_jst_datetime:
    print('3')


# In[ ]:




