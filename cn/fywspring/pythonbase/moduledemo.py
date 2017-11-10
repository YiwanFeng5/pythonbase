#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日
PYthon的模块学习
所谓Python搞得模块其实就是以.py结尾的文件，其中
包含了对象的定义和一些Python的语句
@author: Yiwan
'''

# 导入(import)自定义的mymodule.py模块
import mymodule

# 调用自定义模块中函数
mymodule.print_func("Runoob")

# 只导入模块中部分函数
from mymodule import print_func

# 导入指定模块中的所有
from mymodule import *

# Python 搜索路径
# 当前路径
# PYTHONPAYH
# 默认路径
# 设置PYTHONPATH环境变量
# set PYTHONPATH=python的lib目录

# 命名空间和作用域
Money = 2000
def AddMoney():
    "想改正代码就取消以下注释,否则UnboundLocalError"
    global Money
    Money = Money +1

print Money
AddMoney()
print Money

# dir函数
import math

content = dir(math)
print content

# globas()和locals()函数
# 返回的都是字典，可以使用keys()获取名字

# reload()函数重新加载模块，默认只加载一次

# Python 中的包
# 每个包下都有__init__.py文件，空的，用来表示包