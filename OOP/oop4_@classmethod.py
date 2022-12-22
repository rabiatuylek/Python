# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:01:37 2022

@author: Rabia
"""
# self in Python holds the reference of the current working instance
#cls in Python holds the reference of the class --> @classmethod
class Employee:
    
    nump_of_emps = 0  #knit method runs every time that we create a new employee
    
    raise_amount = 2
    new_amount = 1/raise_amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
        Employee.nump_of_emps +=1
        

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)
        return
        
    def decrease(self):
        self.pay = float(self.pay * self.new_amount)
        return
    
    
    #Class method is a method which is bound to the class and not the object of the class
    @classmethod
   
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        return 
    
    @classmethod
    def from_string(cls, emp_str):
        first_, last_, pay_ = emp_str.split('-')
        cls.first_ = first_
        cls.last_ = last_
        cls.pay_ = pay_

        return cls(first_, last_, pay_)
        
    # Using cls we can access only the class data members of the current class.

emp_1 = Employee('Rabia', 'Tuylek', '10000')
emp_2 = Employee('Elmas', 'Tuylek', '20000')

str1 = 'John-Doe-7800'

Employee.set_raise_amt(2.4)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

new_emp = Employee.from_string(str1)
print(new_emp.email)
print(new_emp.pay)






