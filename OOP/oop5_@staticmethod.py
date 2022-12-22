# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:45:14 2022

@author: Rabia
"""
import datetime

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
    '''
    Static Methods
    They do not need to access the class data. They are self-sufficient and can work on their own.
    Since they are not attached to any class attribute, they cannot get or set the instance state or 
    class state.
    '''

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

# Static method index's is beloning to itself. For example day is equal to self in istance method or
# cls in class method.

emp_1 = Employee('Rabia', 'Tuylek', '10000')
emp_2 = Employee('Elmas', 'Tuylek', '20000')

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))



