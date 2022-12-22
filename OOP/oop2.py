# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:30:03 2022

@author: Rabia
"""

#classes and instances

#instance method
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
        
        
    

emp_1 = Employee('Rabia', 'Tuylek', '10000')
emp_2 = Employee('Elmas', 'Tuylek', '20000')

print(emp_1.email)
new = Employee.fullname(emp_1)
print(new)
print(emp_1.pay)