#!/usr/bin/python
#coding=utf-8
def printMychar( str ):
   "print all char"
   print str;
   return;


def appChar(original):
	thecurr = original + "kong"
	return [thecurr]

def appSelf(original):
	original.append("append himself")
	return

def data():
	a = [1,2,3,4,5,6,67,8,9]
	tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
	return a,tinydict


class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary