#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月7日
主要介绍if判断语句的使用（规定非0非空为true）
@author: Yiwan
'''
# if (判断条件):
#     执行语句
# else:
#     执行语句
flag = False
name = 'Luren'
if name == 'Python':        #判断bl是否为'Python'
    flag = True             #条件成立时设置标志为真  
    print 'Welcome boss'    #并输出欢饮信息
else:
    print name              #条件不成立时输出不了名称

# if (判断条件1):
#     执行语句1
# elif (判断条件2):
#     执行语句2
# elif (判断条件3):
#     执行语句3
# else:
#     执行语句4

num = 5
if (num == 3):          #    判断num的值
    print 'Boss'
elif (num == 2):
    print 'User'
elif (num == 1):
    print 'Worker'
elif (num < 0):         #    值小于零时输出
    print 'Error'
else:
    print "Roadman"     #    条件均不成立时输出
    
#if语句多个条件
num = 9
if num >= 0 and num <= 10:      #判断值是否在0~10之间
    print 'Hello'
# 输出Hello

num = 10
if num < 0 and num >10:         #判断值是否在小于0或大于10
    print 'Hello'
else:
    print 'Undefine'            
# 书吹结果：Undefine

num = 8
#判断值是否在0~5或者10~15之间
if (num >= 0 and num <=5) or (num >=10 and num <= 15):
    print 'Hello'
else:
    print 'Undefine'
# 输出结果：Undefine

#在同一行使用if判断
var = 100
if var == 100: print '变量 var 的值为100'
print 'Good Bye!'