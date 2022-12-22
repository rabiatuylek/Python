# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:38:16 2022

@author: Rabia
"""

#classes and instances

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
        

print("Inital number:", Employee.nump_of_emps)
emp_1 = Employee('Rabia', 'Tuylek', '10000')
emp_2 = Employee('Elmas', 'Tuylek', '20000')


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.__dict__)
print(emp_1.__dict__)

print("Final number:", Employee.nump_of_emps)

emp_1.decrease()
print(emp_1.pay)
print(emp_1.__dict__)