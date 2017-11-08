#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    第三个python程序
    变量赋�??
"""
from queuelib.tests.test_pqueue import base
from random import random


counter = 100   # 赋�?�整形变�?
miles = 1000.0  # 浮点�?
name = "John"   # 字符�?

print counter
print miles
print name

'''
    多变量赋�?
'''
a = b = c = 1;  #创建�?个整形对象，值为�?，三个变量被分配到相同的内存空间�?
print a,b,c
a,b,c = 1,2,"John"  #两个整形对象a,b�?个字符串对象c
print a,b,c

'''
    五个标准的数据类�?
    Numbers(数字)
    String(字符�?)
    List(列表)
    Tuple(元组)
    Dictionary(字典)
'''
#    数字，python支持4中数字类�?
#    int(有符号整�?),long(长整型，也可以代表八进制和十六进�?),float(浮点�?),complex(复数)
var1 = 1
var2 = 10
print var1,var2
#del var1
print var1,var2

#    字符串，以数字字母和下划线组成的�?串字�?
#    从左到右是从0�?始到长度-1
#    从右到左是从-1�?始到�?
#截取字符串语法为    [头小�?:尾下标]，下标为空就是截到尾
s = "ilovepython"
print s[1:5]
str1 = 'Hello World!'
print str1            # 输出完整字符�?
print str1[0]         # 输出字符串中第一个字�?
print str1[2:5]       # 输出字符串中第三个到第五个之间的�?有字�?
print str1[2:]        # 输出字符串从第三个开始后面所有的字符
print str1 * 2        # 输出字符串两�?
print str1 + "test"   # 输出连接后的字符�?

#    列表，和字符串差不多
mylist = ['runoob',786,2.23,'John',70.2]
tinylist = [123,'John']
print mylist
print mylist[0]
print mylist[1:3]
print mylist[2:]
print mylist * 2
print mylist + tinylist

#    元组和列表差不多，但是是用的圆括号，并且是只读的，不能二次赋�?
mytuple = ('runoob',786,2.23,'John',70.2)
tinytuple = (123,'John')
print mytuple
print mytuple[0]
print mytuple[1:3]
print mytuple[2:]
print mytuple * 2
print mytuple + tinytuple
#tuple[2] = 1000    #元组不支持修改操作，只能�?
#print tuple

#    字典，列表有序�?�字典无�?
#    字典以键取�?�，而列表是通过偏移
#    字典用{}标识，索引key对应值value
mydict = {}
mydict['one'] = "This is one"
mydict[2] = "This is two"
tinydict = {'name':'John','code':6734,'dept':'sales'}
print mydict['one']           #输出键为one的�??
print mydict[2]               #输出键为2的�??
print tinydict              #输出完整的字�?
print tinydict.keys()       #输出�?有的�?
print tinydict.values()     #输出�?有�??

'''
    数组类型转换
'''
# 将x转换为一个整�?,class int(x,base=10),其中x可以是字符串也可以是数字，base是进制，默认是十进制
print "int()不传参返回�?�为�?",
print int()

print "int(3) = ",
print int(3)

print "int(3.6) = ",
print int(3.6)

#如果带base参数的话�?12要以字符串的形式进行输入�?12为十六进�?
print "int('12',16) = ",
print int('12',16)

print "int('0xa',16) = ",
print int('0xa',16)

print "int('10',8) = ",
print int('10',8)

#将x转换成一个长整型
print "long() = ",
print long()

print "long(1) = ",
print long(1)

print "long('123') = ",
print long('123')

#将x转换成一个浮点数
print "float(1) = ",
print float(1)

print "float(112) = ",
print float(112)

print "float('123') = ",
print float('123')

#创建�?个复�?,创建�?个�?�为real+imag*j的复数，class complex(real[, imag])
#real:int,long,float或�?�字符串，imag：int,long,float，返回一个复�?
#若real为字符串，则无需指定第二个参�?

print "complex(1,2) = ",
print complex(1, 2)

print "complex(1) = ",  #real为数�?
print complex(1)

print "complex(\"1\") = ",    #当做字符串处�?
print complex("1")

print "complex(\"1+2j\") = ",    #加号两边不能有空�?
print complex("1+2j")
#将对象x转换成字符串,class str(object='')
print "str(\'RUNOOB\') = ",
print str('RUNOOB')

mydict = {'runoob': 'runoob.com','google': 'google.com'};
print str(mydict)

#将对象x转换成表达式字符�?,repr(x)
s = 'RUNOOB'
print repr(s)
print repr(dict)

#用来计算在字符串中的有效Python表达式，并返回一个对�?
#eval(expression,[,gloabls][,locals])
#expression是表达式,以字符串形式输入
#gloabls是变量作用域，全�?命名空间，如果被提供，则必须是一个字典对�?
#locals是变量作用域，局部命名空间，如果被提供，可以是任何映射对�?
#返回表达式计算结�?
x = 7
print "x*7 = ",
print eval('x*7')

print "2^2 = ",
print eval('pow(2,2)') 

print "2+2 = ",
print eval('2+2')

print eval("5+4")

#将序列转换成元组，tuple(seq)，seq为待转序�?
print tuple([1,2,3,4])
print tuple({1:2,3:4})  #针对字典，会返回字典的key组成的tuple
print tuple((1,2,3,4))  #元组会返回自�?

aList = [123,'xyz','zara','abc']
aTuple = tuple(aList)
print aTuple

#将序列转换成列表，list(seq)
aList = list(aTuple)
print aList 

#转换为可变集合，class set([iterable]),iterable可迭代对象对�?
#set()创建无序不重复元素集，可进行关系测试，删除重复数据，还可以并交差
#返回新的集合对象
x = set('runoob')
y = set('google')
print x,y       #打印显示重复的字母已经被删除
print x & y     #交集
print x | y     #并集
print x - y     #差集,从x中除去y中有�?

#创建�?个字典，dict(d)，d必须是一个序�?(key,value)元组
#dict(**kwrg),dict(mapping,**kwrg),dict(iterable,**kwrg)
#kwrg:关键字，mapping:元素的容器，iterable:可迭代对�?
print dict()                                  #创建空字�?
print dict(a='a',b='b',t='t')                 #传入关键�?
print dict(zip(['one','two','three'],[1,2,3]))#映射函数方式来创造字�?
print dict([('one',1),('two',2),('three',3)]) #可迭代对象方式创建字�?

#转换为不可变集合，class frozenset([iterable])
#返回frozenset对象，不传参默认返回空集�?
a = frozenset(range(10))        #生成�?个新的不可变集合
print a
b = frozenset('runoob')     #创建不可变集�?
print b     

#将一个整数转换为�?个字�?
#只能用在�?个range(256)内的（就�?0~255）整数作为参数，返回�?个对应的字符
#chr(i),i:可以是十进制也可以是十六进制形式的数�?
#返回值是单钱整数对应的ASCII字符
print chr(0x30),chr(0x31),chr(0x61)       #十六进制
print chr(48),chr(49),chr(97)             #十进�?

#和chr功能�?样�?�只不过返回的是Unicode字符
print unichr(97)
print unichr(98)
print unichr(99)

#将一个字符转换成�?个整数�?�，ord(c),c为接收的字符
print ord('a')
print ord('b')
print ord('c')

#将一个整数转换成�?个十六进制字符串hex(x)，x为接收的整数
print hex(10)
print hex(11)
print hex(12)
#将一个整数转换成�?个八进制字符串oct(x)，x为接收的整数
print oct(10)
print oct(20)
print oct(15)
