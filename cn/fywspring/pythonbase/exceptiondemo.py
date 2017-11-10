#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python 的异常处理
@author: Yiwan
'''
# 异常处理
try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常！！！")
except IOError:
    print "Error: 没有找到文件或者读取文件失败！"
else:
    print "内容写入文件成功"
    fh.close()


# try-finally
try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常！！！")
finally:
    print "Error: 没有找到文件或者读取文件失败！"

# 以上也可以写成
try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"

# 异常的参数
def temp_convert(var):
    try:
        return int(var)
    except ValueError,Argument:
        print "参数没有包含数字\n",Argument

# 调用函数
temp_convert("xyz")


# 可以使用raise语句触发一个异常，并且之后的语句不再运行
# def functionName(level):
#     if level < 1:
#         raise Exception("Invalid level!",level)
#         # 触发异常后，后面的代码就不会执行了
# 
# try:
#     functionName(0) #触发异常
# except "Invalid level!":
#     print 1
# else:
#     print 2


# 用户自定义异常
class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg
        
try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args





