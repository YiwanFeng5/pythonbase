#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月7日
Python中List相关操作
@author: Yiwan
'''
from urllib import unquote
list1 = ['python','java',1997,2008]
list2 = [1,2,3,4,5,6,7]
list3 = ["a","b","c","d"]

#访问列表
print "list1[0]: ", list1[0]
print "list2[1:5]: ",list2[1:5]

# 更新列表
print 'Value availabe at index 2: ',
print list1[2]
list1[2] = 2007
print "New value availabe at index 2: ",
print list1[2]

# 删除列表中元素
print list1
del list1[2]
print "After deleting value at index 2: ",
print list1

# Python列表脚本操作符len(list),+,*,in,for...in
print len([1,2,3])
print [1,2,3] + [4,5,6]
print ["Hi!"] * 4
print 3 in [1,2,3]
for x in [1,2,3]: print x,

# Python 列表截取
print list3[2]#第三个
print list2[-2]#从右数第二个
print list2[1:]#从第二个到最末尾

# Python列表函数和方法
print cmp([1,2,3], [3])
print len(list2)
print max(list2)
print min(list2)
print list((1,2,3))

print list1.append(2017),list1
print [1,2,3,4,5,67,8,7,6,53,4,5,6].count(6)
list3.extend(['e','f','g'])
print list3
print list3.index('e', )
list3.insert(4, 'E')#指定索引前插入
print list3
print list3.pop(),list3.pop(-3)
list3.remove('b')
print list3
list3.reverse()
print list3
list4 = [7,4,72,0,5,17,21,58,54,75,6,2,48]
list4.sort(cmp=None, key=None, reverse=True)
print list4

import urllib
s='%E5%B9%BF%E5%B7%9E'
s=unquote(s)
print(s)