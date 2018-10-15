#!/user/bin/python
#-*-coding:utf-8-*-
from jiandian01 import chaxunshujuku

import logging
# logging.getLogger().setLevel(logging.INFO)
# data1 = {'b': 789, 'c': 456, 'a': 123}
# login_token_aa = "{" + '"' + "login_token" + '"' + ":" + '"' + "123" + '"' + "}"
# login_token_bb = "{" + '"' + "login_tok" + '"' + ":" + '"' + "789" + '"' + "}"
# print type(data1),type(login_token_aa)
# login_aa=eval(login_token_aa)
# login_bb=eval(login_token_bb)
# a=dict(login_aa.items()+login_bb.items())
# print type(a),a
# b=login_aa.update(login_bb)
# print b,type(b)


z=220/24
print z


# from jiandiandenglu.common.query_database import Query_database
# test1=5
# test2=3
# sql = "SELECT `price`,`give_price`,`sort` FROM `t_member_store_rule` WHERE  (  cid = 436 and status = 1 ) ORDER BY `sort`  asc"
# a=Query_database()
# c=a.query_database(sql)
# print c
#
# print c[1][0],c[1][1]
# if c[1][0]==test1 and c[1][1]==test2:
#     print "yese"
# else:
#     print "no"


# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# encode_json = json.dumps(data1)
# print type(encode_json), encode_json
#
# decode_json = json.loads(encode_json)
# print type(decode_json)
# print decode_json['a']
# print decode_json


# print"**************zheshi fengexian la **********************"
#
# sql = "SELECT price,ispay,pay_way,pay_type FROM t_pay_order WHERE order_id='22201803211002369485679821597756' "
# a=chaxunshujuku.shujuku(sql)
# print a
# print a[0],a[1],a[2],a[3]
#
# print"**************zheshi fengexian la **********************"
#
# sql="SELECT cid,role,aid,pid FROM t_sys_adminuser WHERE  username = '15868314566'"
# b=chaxunshujuku.shujuku(sql)
# cid=b[0]
# print cid
#
# sql = 'SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
# a= chaxunshujuku.shujuku(sql)
# print a
# print a[0],a[1],a[2],a[3]

# logging.info("hello world")
# from jiandian01 import chaxunshujuku
# bsql = "SELECT price,ispay,pay_way,pay_type FROM t_pay_order WHERE order_id='22201803211002369485679821597756' "
# a=chaxunshujuku.shujuku(bsql)
# print a[0],a[2]
# print  range(3)


# import time
# class Date:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#     @staticmethod
#     def now(): #用Date.now()的形式去产生实例,该实例用的是当前时间
#         t=time.localtime() #获取结构化的时间格式
#         return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回
#     @staticmethod
#     def tomorrow():#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
#         t=time.localtime(time.time()+86400)
#         return Date(t.tm_year,t.tm_mon,t.tm_mday)
#
# a=Date('1987',11,27) #自己定义时间
# b=Date.now() #采用当前时间
# c=Date.tomorrow() #采用明天的时间
#
# print(a.year,a.month,a.day)
# print(b.year,b.month,b.day)
# print(c.year,c.month,c.day)