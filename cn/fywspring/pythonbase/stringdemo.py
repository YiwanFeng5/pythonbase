#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017�?11�?7�?
字符串操�?
@author: Yiwan
'''

# 1.字符串可以是单引号括起来的，也可以是双引�?
var1 = 'Hello World!'
var2 = "Python Runoob"
print var1,var2

# 2.访问字符串中�?
print "var1[0]", var1[0]
print "var2[1:5]", var2[1:5]

# 3.字符串更�?
print "更新字符串：",var1[:6] + 'Runoob!'

# 4.转义字符
# \(在行尾时)    续行�?
# \\    反斜杠符�?
# \'    单引�?
# \"    双引�?
# \a    响铃
# \b    �?�?(Backspace)
# \e    转义
# \000    �?
# \n    换行
# \v    纵向制表�?
# \t    横向制表�?
# \r    回车
# \f    换页
# \oyy    八进制数，yy代表的字符，例如：\o12代表换行
# \xyy    十六进制数，yy代表的字符，例如：\x0a代表换行
# \other    其它的字符以普�?�格式输�?

# 5.字符串运算符
a = "Hello"
b = "Python"
# 5.1 字符串连�? +
print a + b
# 5.2 字符串重�?
print a * 2
# 5.3 获取字符串的单个字符
print a[0]
# 5.4 获取字符串的子串
print a[0:5]
# 5.5 判断字符串是否包含指定字�?
print 'H' in a,'a' in a
# 5.6 判断字符串是否不包含指定字符
print 'H' not in a,'a' not in a
# 5.7 将转义原始化
print r'\n',R'\a'
# 5.8 字符串格式化
print "My name is %s and weight is %d kg!" % ('Zara',21)

# 6. Python中的格式化符号有�?

#      �?   �?      描述
#       %c     格式化字符及其ASCII�?
#       %s     格式化字符串
#       %d     格式化整�?
#       %u     格式化无符号整型
#       %o     格式化无符号八进制数
#       %x     格式化无符号十六进制�?
#       %X     格式化无符号十六进制数（大写�?
#       %f     格式化浮点数字，可指定小数点后的精度
#       %e     用科学计数法格式化浮点数
#       %E     作用�?%e，用科学计数法格式化浮点�?
#       %g     %f�?%e的简�?
#       %G     %f �? %E 的简�?
#       %p     用十六进制数格式化变量的地址

# 6.2格式化操作符辅助指令（在str.format()中可以使用）
# 符号    功能
# *    定义宽度或�?�小数点精度
# -    用做左对�?
# +    在正数前面显示加�?( + )
# <sp>    在正数前面显示空�?
# #    在八进制数前面显示零('0')，在十六进制前面显示'0x'或�??'0X'(取决于用的是'x'还是'X')
# 0    显示的数字前面填�?'0'而不是默认的空格
# %    '%%'输出�?个单�?�?'%'
# (var)    映射变量(字典参数)
# m.n.    m 是显示的�?小�?�宽�?,n 是小数点后的位数(如果可用的话)

# 7. Python中字符串跨行，以�?对三单引号，或�?�一对三双引�?
print '''�?
好，
�?
�?
�?
'''

# 8. Unicode字符,将字符串中可以嵌入Unicode编码
print 'Hello\u0020World!'
print u'Hello\u0020World!'

# 9. 字符串内建函�?
test_str = "你好,世界"
print test_str
print test_str.capitalize()#把首字母变成大写
print test_str.center(30)#居中左右补空�?
print test_str.count('l',3,7)#统计下标3~7，�?�l’出现的次数
print test_str.encode('base64','strict')#按照base64进行编码
print test_str.decode('UTF-8','strict')#按照UTF-8进行解码
print test_str.endswith('�?',0,6),len(test_str)#指定范围类是否以指定字符串结尾，6位长度，�?个Unicode�?3个长�?
print 'hello\tworld!'
print 'hello\tworld!'.expandtabs(3)#将\t变成空格
print 'hello world'.find('ll',1,6)#在指定区间内查找子字符串
print "{},{}".format('hello', 'world')#字符串的格式�?
print "{1} {0} {1}".format('python','java')
print "姓名：{name}, 年龄：{age}".format(name='张三',age=24)
user_info = {'name':'李四','age':23}
print "姓名：{name}, 年龄：{age}".format(**user_info)
user_infos = ['王五',34]
print "姓名：{0[0]}, 年龄：{0[1]}".format(user_infos)

# format 用对象传参数
class MyObject(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = MyObject('赵四',33)
print '姓名：{0.name}, 年龄：{0.age}'.format(user)
print '{:.2f}'.format(3.1415926)
print "hello".index('l',1,4)#和find�?样，但是index找不到会报错
print "hello123".isalnum()#至少有一个字符，并且�?有字符都是数字或者字�?
print "hello123".isalpha()#同上，但只能是字�?
print "123456".isdigit()#只包含数�?
print "hello123".islower()#都是小写字母或数�?
print " ".isspace()#是否是空�?
print "hello".istitle()#是否是标题化�?
print 'HELLO'.isupper()#是否为大�?
print "-".join(['w','o','r','l','d'])#将序列中字符�?-链接起来
print 'hello'.ljust(10)#左对�?10个长度包括字符串长度
print "HELLO".lower()#大写装小�?
print '   hello   '.lstrip()#去掉字符串左边的空格
from string import maketrans


print 'hello world'.translate(maketrans('aeiou','12345'))#映射替换
print max('hello123A')#返回字符串中�?大字�?
print min("hello123A")#和上面相�?
print 'http://www.baidu.com'.partition('://')#返回三个元素分隔符左边的，分隔符，分隔符右边�?
print 'hello world!'.replace('l', 'L',2)#替换两个
print 'hello world!'.rfind('l')#从右边开始找
print 'hello world!'.rindex('o')
print 'hello'.rjust(30)#右对齐，�?30个空�?
print 'http://www.baidu.com://www.google.com'.rpartition('://')
print '   hello    '.rstrip()#删除右边的空�?
print 'hello world hello python'.split(' ',2)#切两�?
print 'he\nllo\r\n wo\rrld!'.splitlines()#按行符切
print 'he\nllo\r\n wo\rrld!'.splitlines(True)#保留行符
print 'hello World!'.startswith('hell')
print '   hello    '.strip()#去除左右空格
print 'hello'.swapcase()#大写变小写，小写变大�?
print 'hello world'.title()#转标题，�?有单词首字母大写
print "hello world".translate(maketrans('aeiou', '12345'),'l')#将l过滤�?
print 'hello'.upper()#小写转大�?
print 'hello'.zfill(10)#补零填充





