#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2017年11月9日
Python元组学习
注意：元组中的元素不能修改，元组用的是圆括号
@author: Yiwan
'''
# 定义元素
tup1 = ('physical','chemistry',1997,20000)
tup2 = (1,2,3,4,5,6,7)
tup3 = "a","b","c","d"
tup4 = ()       # 空元组
tup5 = (50,)    #创建一个元组时要在第一个元素后添加逗号
print tup1,tup2,tup3,tup4,tup5

# 访问元组
print "tup1[0]: ", tup1[0]
print "tup2[1:5]", tup2[1:5]

# 修改元组,不可以修改元组但可以连接元组
tup1 = (12,34,56)
tup2 = ("abc","xyz")

#以下修改元素操作是非法的
#tup1[0] = 100

#创建一个新的元组
tup3 = tup1 + tup2
print tup3

# 删除元组，但元组中的元素不能删除
tup = ('physical','chemistry',1997,20000)

print tup
del tup
print "After deleting tup: "
#print tup

# 元组运算符
print len((1,2,3))
print (1,2,3) + (4,5,6)
print ("Hi!",) * 4
print 3 in (1,2,3)
for x in (1,2,3): print x

# 元组索引截取
L = ('spam','Spam','SPAM!')
print L[2]
print L[-2]
print L[1:]

# 无关闭分隔符，任意无符号的对象，以逗号隔开，默认为元组
print 'abc',-4.24e93,18+6.6j,'xyz';
x,y = 1,2
print "Value of x, y: ", x, y

# 元组内置函数
print cmp((1,2),(1,2,3))
print cmp((1,2,3),(1,2,3))
print cmp((1,2,3),(1,2))
print cmp(('x','y','z'),('a','b','c'))
print len((1,2,3,4,56,7,))
print max((2,3,4,56,7,8))
print min((2,34,5,6,7,8))
print tuple([2,3,45,6,7,8,9])


