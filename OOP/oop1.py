# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:09:12 2022

@author: Rabia
"""

#classes and instances

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return ('{} {} {}'.format(self.first, self.last, self.pay))
        
        
    

emp_1 = Employee('Rabia', 'Tuylek', '10000')
emp_2 = Employee('Elmas', 'Tuylek', '20000')
# we understand that different memories
#print(emp_1)
#print(emp_2)

print(emp_1.fullname())
print(emp_1.email)

print(emp_2.fullname())
print(emp_2.email)
