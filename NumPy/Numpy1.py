# -*- coding: utf-8 -*-
"""
@author: Rabia Tüylek
"""

import numpy as np
array = np.array([1,2,3,4])
print("one dimensional array : ", array)

array2= np.array([[1,2],[3,4]])
print("two dimensional array : ","\n", array2)
print("\n")
# the dimensions can be printed out using .shape property
print("shape of array : ",(array.shape))
print("shape of array2 : ",(array2.shape))
print("\n")
# the types for all matrices are same
print(type(array))
print(type(array2))
#lists can be converted to NumPy arrays as well 
python_list = [1,2,3,4,5]
numpy_array = np.array(python_list)
print(python_list)
print(numpy_array)
print(" python list has type : " ,(type(python_list)))
print("numpy_array has  type : " ,(type(numpy_array)))
("\n")
# different types of nd arrays
a1 = np.zeros((4,4))
print(a1)
a2 = np.ones((5,5))
print(a2)
# birim mmatris
a3 = np.eye(4)
print(a3)
# specific number
a4 = np.full((4,4), fill_value= 400)
print(a4)
a5 = np.random.randn(4,4)
a5_T = a5.T
print("a5 matrice : " ,a5)
print("transpoze of a5 matrice : " ,a5_T)













