# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:57:33 2022

@author: Rabia
"""


"""
 __repr__ 
 
it is enable to transform otomatically flat index in class format.
ıf we can want to see name, lastname, we do not need to write emp1.first just it is enough that is emp1 by using __repr__

"""


class Employee:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        return
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = float(self.pay* self.raise_amount)
        return
    
    def __repr__(self):
        return "Employee ( '{}' ,'{}', '{}')".format(self.first, self.last, self.pay)
# we use the __add__, __sub__ vb by using (self, other) for minus, plus, vb math calculations 
# These have to be belong to "other" with "self"
# they can be plus or minus with "other" index that we want to calculate
    
    def __add__ (self, other):
        result_salary = (self.pay + other.pay)
        return result_salary
    # bu tarz __x__ ifadeler sistemden görmek istediğimiz zaman içine hemen ekler x.pay yazmamıza gerek yoktur.
     
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'Employee', 60000)

print(emp1.email)
print(emp1)
print(emp1.first)
print("Total Salary: ", emp1.pay + emp2.pay)
print("Total Salary: ", emp1+ emp2)