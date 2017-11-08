#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017�?11�?7�?
Numbers(数字)相关
数据类型是不允许改变的，这就意味�?如果改变Number数据类型的�?�，将会重新分配内存空间
var1 = 1
var2 = 10
del var1,var2   #删除这两个对象的引用

Python 支持的四种不同的数�?�类�?
整形(int)
长整�?(long integers)
浮点�?(floating point real values)
复数(complex numbers)

int              long           float              complex
10            51924361L          0.0               3.14j
100           -0x19323L         15.20              45.j
-786            0122L            -21.9             9.322e-36j
080    0xDEFABCECBDAECBFBAEl    32.3+e18          .876j
-0490    535633629843L          -90.               -.6545+0J
-0x260    -052318172735L      -32.54e100            3e+26J
0x69    -4721885298529L        70.2-E12            4.53e-7j

@author: Yiwan
'''
# 
# int(x [,base ])         将x转换为一个整�?  
# long(x [,base ])        将x转换为一个长整数  
# float(x )               将x转换到一个浮点数  
# complex(real [,imag ])  创建�?个复�?  
# str(x )                 将对�? x 转换为字符串  
# repr(x )                将对�? x 转换为表达式字符�?  
# eval(str )              用来计算在字符串中的有效Python表达�?,并返回一个对�?  
# tuple(s )               将序�? s 转换为一个元�?  
# list(s )                将序�? s 转换为一个列�?  
# chr(x )                 将一个整数转换为�?个字�?  
# unichr(x )              将一个整数转换为Unicode字符  
# ord(x )                 将一个字符转换为它的整数�?  
# hex(x )                 将一个整数转换为�?个十六进制字符串  
# oct(x )                 将一个整数转换为�?个八进制字符�?  
from math import ceil
import math
from random import choice
import random


# 数学函数
print "abs(-10) = ", abs(-10)               # 取绝对�??
print "ceil(4.1) = ",ceil(4.1)              # 返回数字的上入整�?
print "cmp(2,3) = ",cmp(2, 3),";cmp(2,2)"," = ",cmp(2, 2),";cmp(3,2)"," = ",cmp(3, 2)               # 比较两个数大�?,< -1,== 0,> 1
print "exp(1) = ",math.exp(1)               # e的一次幂
print  "fabs(-10) = ",math.fabs(-10)        # 去绝对�?�，返回浮点�?
print "floor(4.9) = ",math.floor(4.9)       # 向下舍去，返回浮点数
print "log(100,10) = ",math.log(100,10)     # log(底数,指数),返回浮点�?
print "log10(100) = ",math.log10(100)       # log(10,指数),返回浮点�?
print "max(1,2,3,4,5,6) = ",max(1,2,3,4,5,6)   # 返回给定参数中的�?大�?�，参数可以是一个序�?
print "min([2,3,4,5,6]) = ",min([2,3,4,5,6])   # 返回给定参数中的�?小�?�，参数可以是一个序�?
print "modf(-3.14159) = ",math.modf(-3.14159)  # 返回�?个tuple,其中包含整数部分和小数部分，符号都与给定值相同，且都是浮点数
print "pow(2,3) = ",math.pow(2, 3)          # 2�?3次幂
print "round(3.1415926) = ",round(3.1415926,2)# 四舍五入，保�?3位小�?
print "sqrt(100) = ",math.sqrt(100)         # 取平方根，返回浮点数

# Python中随机函�?

print random.choice(range(10))            # 0~9中随机挑选一个整�?
print random.randrange(0,100,2)           # 0~100中随机�?�取�?个数，缺省步长为1，此处为2
print random.random()                     # 生成0~1之间的小�?
# random.seed(100)
print random.random()                     #保证random每次生成的数都一样，默认random中seed是Python自己选的，每次都不一�?
test_list = [2,3,4,5,6,7,8]
random.shuffle(test_list)                 # 随机打乱序列
print test_list
print random.uniform(2,5)                   #随机生成2~5之间的实�?

# Python中三角函�?
print math.acos(0)          # 反余弦参数只能是-1~1之间
print math.asin(1)          # 反正弦同�?
print math.atan(1)          # 反正�?
print math.atan2(0.6, 1)    # 计算指定点的反正切�??
print math.sin(math.pi/2)   #计算正弦�?
print math.cos(math.pi)     # 计算余弦�?
print math.tan(math.pi/4)   # 计算正切�?
print math.hypot(2, 5)      # 返回欧几里得范数sqrt(x*x+y*y)
print math.degrees(math.pi) # 弧度转角�?
print math.radians(90)      # 角度转弧�?

# Python中数学常�?
print math.pi
print math.e