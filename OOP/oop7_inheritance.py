# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:28:03 2022

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
        self.pay = float(self.pay * self.raise_amount)
        return        



class Developer(Employee):      #Inherit from the created Class --> Employee
    raise_amount = 2
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #yeni bir class içine fonksiyon açarsan (inheritance) eski classın özelliklerini eklemek için super methodunu kullanmalısın.
        self.prog_lang = prog_lang

# SO IMPORTANTT !!!
# ınheritance ya aynı class özelliklerini alır YA DA
# aynı klas özelliklerini alıp kendi bir def__init__ daha açarak ya instance methodu kullanarak bir özellik daha ekler.


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):   #instance method
        super().__init__(first, last, pay)
        
        if employees == None:   # or if employees is None
            self.employees = []
        else:
            self.employees = employees
            
        return
 
    #append employee
    def add_emp(self, emp):               #instance method
        if emp not in self.employees:
            self.employees.append(emp)
        return
            
    #remove employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        return
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        return
            

emp_1 = Developer('Rabia', 'Tuylek', 10000, 'C')
emp_2 = Developer('Elmas', 'Tuylek', 20000, 'Python')

print(emp_1.email)
print(emp_1.prog_lang)



mgr_1 = Manager('Sue', 'Smith', 9000, [emp_1])

print(mgr_1.email)
mgr_1.print_emps()

print("final")
mgr_1.add_emp(emp_2)
mgr_1.remove_emp(emp_1)
mgr_1.print_emps()
