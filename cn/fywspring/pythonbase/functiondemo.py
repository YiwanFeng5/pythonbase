#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月9日
Python函数相关
@author: Yiwan
'''

# 定义函数
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

# def functionname( parameters ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]


def printme(string_you):
    print string_you
    return

# 函数的调用

printme('你好')
printme('世界')

# list和dict可以改变，当参数传递时候，方法内改变，方法外也会改变
# strings,tuples和numbers是不可改变对象，传参只传值，在函数内部改变不会改变外部的值

def ChangeInt(a):
    a = 10
    
b = 2
ChangeInt(b)
print b #结果是2

# 传可变对象
def changename(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print "函数内取值：", mylist
    return

# 调用changename函数
mylist = [10,20,30]
changename(mylist)
print "函数外取值：",mylist

# 参数
# 以下是调用函数时可使用的正式参数类型：
# 必备参数
# 关键字参数
# 默认参数
# 不定长参数

# 必备参数
def printstr(my_string):
    "打印任何传入的字符串"
    print my_string
    return 
# 调用printme函数
#printstr()  #出错TypeError: printstr() takes exactly 1 argument (0 given)

# 关键字参数
def printStr(str):
    "打印任何传入的字符串"
    print str
    return

# 调用printStr函数
printStr(str = "My string")

def printUser(name,age):
    "打印传入的字符串"
    print "Name: ", name
    print "Age: ", age
    return 

#调用printUser函数
printUser(age=50, name='miki')

# 缺省参数
def printInfo(name,age=35):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age: ", age
    return

#调用printInfo函数
printInfo(age=50,name='miki')
printInfo(name='miki')


# 不定长参数
def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print "输出："
    print arg1
    for var in vartuple:
        print var
    return 

# 调用printinfo函数
printinfo(10)
printinfo(70,60,50)


# 匿名函数
# python 使用 lambda 来创建匿名函数。
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# 语法
# lambda函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression

# 可写函数说明
sumresult = lambda arg1,arg2:arg1+arg2

# 调用sumresult函数
print "相加后的值为：",sumresult(10,20)
print "相加后的值为：",sumresult(20,20)

# 加法
def sum_opt(arg1,arg2):
    # 返回2个参数的和
    total = arg1 + arg2
    print "函数内：",total
    return total

# 调用 sum_op函数
print sum_opt(10, 20)

total = 0 #这是一个全局变量

def sum_option(arg1,arg2):
    #返回2个参数的和
    total = arg1 + arg2 # total在这里是局部变量
    print "函数内是局部变量：",total
    return total

#调用sum_option函数
print "函数外是全局变量：",total




























