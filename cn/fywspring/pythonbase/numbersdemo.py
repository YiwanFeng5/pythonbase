#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月7日
Numbers(数字)相关
数据类型是不允许改变的，这就意味着如果改变Number数据类型的值，将会重新分配内存空间
var1 = 1
var2 = 10
del var1,var2   #删除这两个对象的引用

Python 支持的四种不同的数值类型
整形(int)
长整型(long integers)
浮点型(floating point real values)
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
# int(x [,base ])         将x转换为一个整数  
# long(x [,base ])        将x转换为一个长整数  
# float(x )               将x转换到一个浮点数  
# complex(real [,imag ])  创建一个复数  
# str(x )                 将对象 x 转换为字符串  
# repr(x )                将对象 x 转换为表达式字符串  
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
# tuple(s )               将序列 s 转换为一个元组  
# list(s )                将序列 s 转换为一个列表  
# chr(x )                 将一个整数转换为一个字符  
# unichr(x )              将一个整数转换为Unicode字符  
# ord(x )                 将一个字符转换为它的整数值  
# hex(x )                 将一个整数转换为一个十六进制字符串  
# oct(x )                 将一个整数转换为一个八进制字符串  
from math import ceil
import math
from random import choice
import random



# 数学函数
print "abs(-10) = ", abs(-10)               # 取绝对值
print "ceil(4.1) = ",ceil(4.1)              # 返回数字的上入整数
print "cmp(2,3) = ",cmp(2, 3),";cmp(2,2)"," = ",cmp(2, 2),";cmp(3,2)"," = ",cmp(3, 2)               # 比较两个数大小,< -1,== 0,> 1
print "exp(1) = ",math.exp(1)               # e的一次幂
print  "fabs(-10) = ",math.fabs(-10)        # 去绝对值，返回浮点数
print "floor(4.9) = ",math.floor(4.9)       # 向下舍去，返回浮点数
print "log(100,10) = ",math.log(100,10)     # log(底数,指数),返回浮点数
print "log10(100) = ",math.log10(100)       # log(10,指数),返回浮点数
print "max(1,2,3,4,5,6) = ",max(1,2,3,4,5,6)   # 返回给定参数中的最大值，参数可以是一个序列
print "min([2,3,4,5,6]) = ",min([2,3,4,5,6])   # 返回给定参数中的最小值，参数可以是一个序列
print "modf(-3.14159) = ",math.modf(-3.14159)  # 返回一个tuple,其中包含整数部分和小数部分，符号都与给定值相同，且都是浮点数
print "pow(2,3) = ",math.pow(2, 3)          # 2的3次幂
print "round(3.1415926) = ",round(3.1415926,2)# 四舍五入，保留3位小数
print "sqrt(100) = ",math.sqrt(100)         # 取平方根，返回浮点数

# Python中随机函数

print random.choice(range(10))            # 0~9中随机挑选一个整数
print random.randrange(0,100,2)           # 0~100中随机选取一个数，缺省步长为1，此处为2
print random.random()                     # 生成0~1之间的小数
# random.seed(100)
print random.random()                     #保证random每次生成的数都一样，默认random中seed是Python自己选的，每次都不一样
test_list = [2,3,4,5,6,7,8]
random.shuffle(test_list)                 # 随机打乱序列
print test_list
print random.uniform(2,5)                   #随机生成2~5之间的实数

# Python中三角函数
print math.acos(0)          # 反余弦参数只能是-1~1之间
print math.asin(1)          # 反正弦同上
print math.atan(1)          # 反正切
print math.atan2(0.6, 1)    # 计算指定点的反正切值
print math.sin(math.pi/2)   #计算正弦值
print math.cos(math.pi)     # 计算余弦值
print math.tan(math.pi/4)   # 计算正切值
print math.hypot(2, 5)      # 返回欧几里得范数sqrt(x*x+y*y)
print math.degrees(math.pi) # 弧度转角度
print math.radians(90)      # 角度转弧度

# Python中数学常量
print math.pi
print math.e