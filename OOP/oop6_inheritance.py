# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:11:01 2022

@author: Rabia
"""

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
        
    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
        return        

#Inherit from the created Class --> Employee

class Developer(Employee):
    pass
  
  
emp_1 = Employee('Rabia', 'Tuylek', 10000)
emp_2 = Employee('Elmas', 'Tuylek', 20000)

emp_3 = Developer('Rabia', 'Tuylek', 10000)
emp_4 = Developer('Elmas', 'Tuylek', 20000)

print(emp_1.email)
print(emp_2.email)
print(emp_3.email)
print(emp_4.email)

print(help(Developer))