#!/usr/bin/python    
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月6日
Python运算符有：
    算数运算符：+ - * 、 % **（幂运算） //（取整运算）
    比较（关系运算符）：== != <> > < >= <=
    赋值运算符：+= -= *= /= %= **= //=
    逻辑运算符：and or not
    位运算符：& | ^ ~ << >>
    成员运算符：in     not in
    身份运算符：is    is not
    运算符优先级：
    #头文件一定要在注释之前，头文件后面也不能添加注释
@author: Yiwan
'''
#算数运算符：+ - * 、 % **（幂运算） //（取整运算）
from __builtin__ import int
a = 21
b = 10
c = 0

c = a + b
print a, " + ", b, " = ",c

c = a - b
print a, " - ", b, " = ",c

c = a * b
print a, " * ", b, " = ",c

c = a / b
print a, " / ", b, " = ",c

c = a % b
print a, " % ", b, " = ",c

#修改变量a、b、c
a = 2
b = 3
c = a ** b
print a, " **  ", b, " = ",c

a = 10
b = 5
c = a // b
print a, " // ", b, " = ",c

###注意在python2.x里面，整数除以整数，只能得到整数结果，如果想要得到小数部分，把其中一个改成浮点数即可
print "1 / 2 = ",1/2
print "1.0 / 2 = ",1.0/2
print "1 / float(2) = ",1/float(2)

#比较运算符：== != <> > < >= <=（1为真0为假）
a = 21
b = 10
c = 0

if (a == b):
    print "1",a, " == ", b
else:
    print "1",a, " != ", b
    
if (a != b):
    print "2",a, " != ",b
else:
    print "2",a, " == ",b
    
if (a <> b):
    print "3", a, " <> ", b
else:
    print "3", a, " == ", b
    
if (a < b):
    print "4", a, " < ", b
else:
    print "4", a, " >= ", b
    
if (a > b):
    print "5", a, " > ", b
else:
    print "5", a, " <= ", b

#修改变量a和变量b的值
a = 5
b = 20
if ( a <= b):
    print "6", a, " <= ", b
else:
    print "6", a, " > ", b

if (a >= b):
    print "7", a, " >= ", b
else:
    print "7", a, " < ", b                    

#赋值运算：+= -= *= /= %= **= //=
a = 21
b = 10
c = 0

c = a + b
print a," + ", b, " = ",c
c += a
print " += ", c
c -= a
print " -= ", c
c *= a
print " *= ", c
c /= a
print " /= ", c

c = 2
c %= a
print " %= ", c
c **= a
print " **= ", c
c //= a
print " //= ", c


'''
    将一个十进制整数转换为二进制字符串
'''
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def getBit(x):
    flag = False
    if (x < 0):         #如果是负数，先转换为正数
        flag = True
        x = abs(x)
    result_bits = ""
    while (x / 2 >= 0):
        if (x/2 == 0):
            result_bits += str(1);
            break
        result_bits += str(x % 2)
        x /= 2
    result_bits = result_bits[::-1]         #反转
    zero_count = 8-result_bits.__len__()    #补零位数
    while (zero_count > 0):
        zero_count -= 1
        result_bits = str(0) + result_bits
    if (flag):
        result_bits.replace("1", "0");
    return result_bits

#位运算符：& | ^ ~ << >>
a = 60      #00111100
b = 13      #00001101
c = 0

c = a & b
print a," & ",b," = ",c,"==>",getBit(c)

c = a | b
print a," | ",b," = ",c,"==>",getBit(c)

c = a ^ b
print a," ^ ",b," = ",c,"==>",getBit(c)

c = ~a
print "~",a," = ",c,"==>",getBit(c)

c = a << 2
print a," << ",2," = ",c,"==>",getBit(c)

c = a >> 2
print a," >> ",2," = ",c,"==>",getBit(c)

#逻辑运算符：and or not
a = 10
b = 20

if (a and b):
    print "1 - 变量a和变量b都为true"
else:
    print "1 - 变量a和变量b有一个不为true"
    
if (a or b):
    print "2 - 变量a和变量b至少有一个为true"
else:
    print "2 - 变量a和变量b都为false"
    
#修改变量a的值
a = 0
if (a and b):
    print "3 - 变量a和变量b都为true"
else:
    print "3 - 变量a和变量b有一个不为true"

if (a or b):
    print "4 - 变量a和变量b至少有一个为true"
else:
    print "4 - 变量a和变量b都为false"
    
if not(a and b):
    print "5 - 变量a和变量b至少有一个是false"
else:
    print "5 - 变量a和变量b都为true"
    
#成员运算符：in    not in
a = 10
b = 20
testlist =  [1,2,3,4,5]

if (a in testlist):
    print "变量a在列表testlist中存在"
else:
    print "变量a不在列表testlist中"

if (b not in testlist):
    print "变量b不在给定的列表testlist中"
else:
    print "变量b在给定的列表testlist中"

#修改变量a的值
a = 2
if (a in testlist):
    print "变量a在给定的列表testlist中"
else:
    print "变量a不在给定的列表testlist中"
    
#身份运算符：is    is not
a = 20
b = 20

if (a is b):
    print "1 - a和b有相同的标识"
else:
    print "1 - a和b没有相同的标识"

if (a is not b):
    print "2 - a和b没有相同的标识"
else:
    print "2 - a和b有相同的标识"

#修改变量b的值
b = 30

if (a is b):
    print "3 - a和b有相同的标识"
else:
    print "3 - a和b没有相同的标识"

if (a is not b):
    print "4 - a和b没有相同的标识"
else:
    print "4 - a和b有相同的标识"
    
###    is 和 == 的区别：
###    is 用于判断两个变量引用对象是否为同一个
###    == 用于判断引用变量的值是否相等
a = [1,2,3]
b = a
print b is a 
print b == a
b = a[:]
print b is a
print b == a

#################运算符优先级#####################################################
# **                          指数 (最高优先级)
# ~ + -                       按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //                    乘，除，取模和取整除
# + -                         加法减法
# >> <<                       右移，左移运算符
# &                           位 'AND'
# ^ |                         位运算符
# <= < > >=                   比较运算符
# <> == !=                    等于运算符
# = %= /= //= -= += *= **=    赋值运算符
# is is not                   身份运算符
# in not in                   成员运算符
# not or and                  逻辑运算符
###############################################################################

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a+b)*c/d       #(30*15)/5
print "(",a,"+",b,")","*",c,"/",d," = ",e

e = ((a+b)*c)/d       #(30*15)/5
print "((",a,"+",b,")","*",c,")/",d," = ",e

e = (a+b)*(c/d)       #(30*15)/5
print "(",a,"+",b,")","*(",c,"/",d,") = ",e

e = a+(b*c)/d       #(30*15)/5
print a,"+(",b,"*",c,")/",d," = ",e
