#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月7日
Python中各种循环语句的使用
while
for
嵌套
break
continue
pass
@author: Yiwan
'''
from itertools import count

# while (判断条件):
#     循环体

# 理解while的循环过程
numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0: even.append(number)
    else: odd.append(number)
print "even: ",even
print "odd:  ",odd

# 输出0~8
count = 0
while count < 9: 
    print 'The count is: ',count
    count = count + 1
print "Good Bye!"

# continue和break在while中的用法

i = 1
while i < 10:
    i += 1
    if i%2 > 0:         #非双数时跳出输出
        continue
    print i             #输出双数2、4、6、8。10

i = 1
while 1:                #循环条件为必定成立
    print i             # 输出1~10
    i += 1
    if i > 10:          #当i大于10时跳出循环
        break

# 无限循环

# var = 1
# while var == 1:         # 该条件永远true，循环将无限执行下去
#     num = raw_input("Enter a number: ")
#     print "You Entered: ",num
# print "Good Bye!"

# while...false的使用

count = 0
while count < 5:
    print count, " is less than 5"
    count = count + 1
else:
    print count, " is not less than 5"
    
#若循环体只有一句可以一行写
# flag = 1
# while flag: print 'Given flag is really true!'
# print "Good Bye!"


# for 循环一个列表或者字符串
# for iterating_var in sequence:
#     statements(s)

for letter in 'Python':         # 第一个实例
    print '当前字母：',letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:            # 第二个实例
    print '当前水果：', fruit
    
print "Good Bye!"

# 通过序列的索引来迭代
for index in range(len(fruits)):        #len()返回序列的长度，range()返回一个序列的数
    print '当前水果：',fruits[index]
    
print "Goob Bye!"

# for...else
for num in range(10,20):        #迭代10到20之间的数字
    for i in range(2,num):      #根据因子迭代
        if num%i == 0:          #确定第一个因子
            j = num/i           #计算第二个因子        
            print '%d 等于 %d * %d' % (num,i,j)
            break
    else:
        print num,'是一个质数'

# for 嵌套
# for iterating_var in sequence:
#     for iterating_var in sequence:
#         statements(s)
#     statements(s)

# while 嵌套
# while expression:
#     while expression:
#         statement(s)
#     statement(s)

# 也可以while中嵌套for，for中嵌套while

i = 2
while i< 100:
    j = 2
    while j <= (i/j):
        if not(i%j): break
        j = j +1
    if j > i/j: print i," 是素数"
    i = i + 1
print "Good Bye!"

# break语句
for letter in 'Python':     # 第一个实例
    if letter == 'h':
        break
    print '当前字母：',letter

var = 10
while var > 0:
    print '当前变量值：',var
    var = var - 1
    if var == 5:        # 当前变量var等于5时退出循环
        break
print "Good Bye!"

# continue 的使用
for letter in 'Python':     # 第一个实例
    if letter == 'h':
        continue
    print '当前字母：',letter

var = 10                    # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值：',var
print "Good Bye!" 

# pass是占位语句，没有含义
# 输出 Python的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是  pass 块'
    print '当前字母：',letter
print "Good Bye!"