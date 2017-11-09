#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月9日
Python字典操作
键值对形式用冒号分割
键值对与键值对之间用逗号分割
在花括号中
键不可变
@author: Yiwan
'''

# 定义一个字典
# d = {key1: value1,key2: value2}
dict1 = {'Alice': '2341','Beth': '9102','Cecil': '3258'}
dict2 = {'abc',456}
dict3 = {'abc': 123, 98.6: 37}
print dict1,dict2,dict3

# 访问字典里的值,如果访问没有定义的键,会报错
dict4 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict4['Name']: ",dict4['Name']
print "dict4['Age']: ",dict4['Age']

# 修改字典
dict4['Age'] = 8        #修改指定键名的值
dict4['School'] = "DSP School"     # 如果没有指定的键名，会创建新的键，并指定值
print "dict4['Age']: ", dict4['Age']
print "dict[School']: ", dict4['School']

# 删除字典元素
del dict4['Name']   # 删除键是'Name'的条目
dict4.clear()        # 清空字典所有条目
del dict4;          # 删除字典
#字典不存在会出现异常
# print "dict4['Age']: ", dict4['Age']

# 字典的特性
#字典值可以没有限制的取任何python对象
#既可以是标准对象，也可以是用户自定义的，但是键不行
# 1) 不允许同一个键出现两次，创建时如果同一个键被赋值两次，后一个值会被记住
dict5 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict4['Name']: ", dict5['Name']

# 2) 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
# dict6 = {['name']: 'Zara','Age': 7}     # 报错unhasnbale
# print "dict['Name']: ", dict['Name']

# 字典的内置函数和方法
print cmp({'Name': 'zhan'},{'Name': 'zhang'})
print len({'Name':'zhang','Age':7})
print str(dict1)
print type(dict1)

print dict1.clear()     # 清空指定字典中元素
print dict3.copy()      # 返回指定字典的浅复制
print dict.fromkeys(('a','b','c'),1) # 创建一个新的字典，用tuple中每一个元素做键，1做值
print dict5.get('abc')  # 获取指定键的值,没有找到就返回None
print dict5.has_key('Name') #判断指定键在字典中是否存在，存在返回True
print dict5.items() #以列表返回可遍历的（键，值）元组数组
print dict5.keys()  #返回字典中键组成的序列
print dict5.setdefault('addr') # 和get类似
dict6 = {'Name': 'Zara', 'Age': 7}
dict6.update({'Sex': 'female'})
print dict6
print dict5.values()    # 返回字典中所有的值组成的列表
print dict.pop('Name')  # 删除字典给定的键对应的值，并返回该值
print dict5.popitem()   #随机返回并删除字典中的一对键值








