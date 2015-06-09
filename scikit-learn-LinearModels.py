#!/usr/bin/python
#coding=utf-8
print 'python-learn!'
# print '学习！'
# #raw_input("\nPress the enter key to exit.")
# counter = 100 # 赋值整型变量
# miles = 1000.0 # 浮点型
# name = "John" # 字符串

# print counter
# print miles
# print name

# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']

# print list # 输出完整列表
# print list[0] # 输出列表的第一个元素
# print list[1:3] # 输出第二个至第三个的元素 
# print list[2:] # 输出从第三个开始至列表末尾的所有元素
# print tinylist * 2 # 输出列表两次
# print list + tinylist # 打印组合的列表

# dict = {}
# dict['one'] = "This is one"#key=>value
# dict[2] = "This is two"

# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


# print dict['one'] # 输出键为'one' 的值
# print dict[2] # 输出键为 2 的值
# print tinydict # 输出完整的字典
# print tinydict.keys() # 输出所有键
# print tinydict.values() # 输出所有值

#mydic = {}
#mydic['first'] = "first in dic";
#print mydic;

# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # Second Example
#    print 'Current fruit :', fruit

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
# print "dict['Name']: ", dict['Name'];
# print "dict['Age']: ", dict['Age'];

#import time;  # This is required to include time module.

# ticks = time.time()
# print "Number of ticks since 12:00am, January 1, 1970:", ticks

#函数调用，引用
import myfoo
# myfoo.printMychar("kong")
# thecurr = myfoo.appChar("the original char over!")
# print thecurr

# temp = myfoo.appSelf(thecurr)
# print temp
# print thecurr

# try:
# 	myfoo.appSelf()
# except:
# 	print "this is exception"
# 	#traceback.print_exc()

# a,b = myfoo.data()
# print a,b

print myfoo.Employee.empCount
emp1 = myfoo.Employee("Zara", 2000)
print myfoo.Employee.empCount
emp1.displayCount()
emp1.displayEmployee()

emp2 = myfoo.Employee("kong", 20000)
emp1.displayCount()

# print "Employee.__doc__:", myfoo.Employee.__doc__
# print "Employee.__name__:", myfoo.Employee.__name__
# print "Employee.__module__:", myfoo.Employee.__module__
# print "Employee.__bases__:", myfoo.Employee.__bases__
# print "Employee.__dict__:", myfoo.Employee.__dict__