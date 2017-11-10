#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
Python文件I/O相关操作

@author: Yiwan
'''
from __builtin__ import str
from twisted import positioning

# 最简单的输出语句print
print "Python是一个非常棒的语言，不是吗","enen"

# 读取键盘输入
# raw_input()
str_me = raw_input("请输入：")
print "您输入的内容是：",str_me
# input(),不仅可以实现以上功能，还可以接受一个表达式，计算返回结果
str_me = input("请输入：")
print "您输入的结果是：",str_me

# 打开和关闭文件，可以使用file对象操作文件
#open()打开或创建一个文件函数
# file object = open(file_name [, access_mode][, buffering])
# 各个参数的细节如下：
# file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
# access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

# 不同模式打开文件的完全列表：
# 模式    描述
# r    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+    打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+    以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# File对象的属性

# 属性                                               描述
# file.closed       返回true如果文件已被关闭，否则返回false。
# file.mode         返回被打开文件的访问模式。
# file.name         返回文件的名称。
# file.softspace    如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

fo = open("foo.txt","wb")
print "文件名：",fo.name
print "是否已经关闭：",fo.closed
print "访问模式：",fo.mode
print "末尾是否强制追加空格：",fo.softspace

# close()方法
fo.close()

# write()方法，不会再结尾添加\n
fo = open("foo.txt","wb")
fo.write("www.baidu.com!\nVery good site!\n")
fo.close()

# read()方法
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读到的内容是：", str
fo.close()

# 文件定位
# tell()返回文件内的当前位置
# seek(要移动的字节数,[0,1,2])方法可以指定文件位置0开头1当前2结尾

fo = open("foo.txt", "r+")
str = fo.read(10)
print "读到的内容是：", str

# 查找当前位置
position = fo.tell()
print "当前文件位置：", position

#  把指针再次重新定位到文件头
position = fo.seek(0,0);
str = fo.read(10)
print "重新读到的内容是：", str

fo.close()

# 重命名和删除文件，使用os对象，使用前要导入

import os
# 重命名文件test1.txt到test2.txt
os.rename("test1.txt", "test2.txt")

# 删除文件
os.remove("text2.txt")

# Python里面的目录
# 创建目录test
os.mkdir("test")
# 改变当前目录
os.chdir("/home/newdir")
# 显示当前工作目录
os.getcwd()
# 删除目录
os.rmdir("/tmp/test")

















