#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月9日
Python时期和时间操作
time和calendar模块用于格式化日期和时间
每个时间戳都以来自1970年1月1日午夜经过了多长时间来表示
@author: Yiwan
'''

import time
from time import localtime

# time.time()
ticks = time.time()
print "当前时间戳为：", ticks

# 时间元组
# Python函数用一个元组装起来的9组数字处理时间
# 序号    字段                                        值
# 0    4位数年                              2008
# 1    月                                     1 到 12
# 2    日                                       1到31
# 3    小时                                   0到23
# 4    分钟                                    0到59
# 5    秒                               0到61 (60或61 是闰秒)
# 6    一周的第几日                    0到6 (0是周一)
# 7    一年的第几日                 1到366 (儒略历)
# 8    夏令时                         -1, 0, 1, -1是决定是否为夏令时的旗帜
# 上述也就是struct_time元组。这种结构具有如下属性：
# 序号          属性                   值
# 0    tm_year    2008
# 1    tm_mon    1 到 12
# 2    tm_mday    1 到 31
# 3    tm_hour    0 到 23
# 4    tm_min    0 到 59
# 5    tm_sec    0 到 61 (60或61 是闰秒)
# 6    tm_wday    0到6 (0是周一)
# 7    tm_yday    1 到 366(儒略历)
# 8    tm_isdst    -1, 0, 1, -1是决定是否为夏令时的旗帜

# 获取当前时间time.localtime()
# 从返回浮点数的时间方式向时间元组转换，只要浮点数传递给如localtime之类的函数
localtime_me = time.localtime(time.time())
print "本地时间为：", localtime_me

# 获取格式化的时间time.asctime()
localtime_me = time.asctime(time.localtime(time.time()))
print "本地时间为：", localtime_me

# 格式化时间time.strftime(format[,t])

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串装换为时间戳
a = "Thu Nov 09 14:11:43 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
# python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# 获取某月日历
import calendar
cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历："
print cal

print time.altzone  # 返回格林威治西部的夏令时地区的偏移秒数
print time.asctime() # 接受24个字符的字符串
print time.clock()  # 返回浮点数计算的秒数返回当前的CPU时间，用来衡量不同程序的耗时
print time.ctime(345678) # 作用相当于asctime(localtime(secs)),未给参数相当于asctime()
print time.gmtime(36000)# 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
print time.localtime()# 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）
#print time.mktime()# 接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
# time.sleep(3000)#推迟线程的运行
# print time.strftime(format)#格式化时间，参见上面
print time.time()# 返回当地时间戳
print "time.timezone: ",time.timezone
print "time.tzname: ", time.tzname

# 日历模块
print calendar.calendar(2017,w=2,l=1,c=6)#返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
print calendar.firstweekday()# 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
print calendar.isleap(2017)# 判断润年
print calendar.leapdays(1993, 2017)#判断指定两个年份之间闰年的数
print calendar.month(2017, 9,w=2,l=1)#返回指定年月的日历
print calendar.monthcalendar(2017,12)#返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
print calendar.monthrange(2017, 11)
print calendar.prcal(2017,w=2,l=1,c=6)
print calendar.prmonth(2017,10,w=2,l=1)
print calendar.setfirstweekday(3)#设置每周起始日期码
print calendar.timegm(time.localtime())
print calendar.weekday(2017, 12, 25)#返回星期码

#datetime
#pytz
#dateutil











