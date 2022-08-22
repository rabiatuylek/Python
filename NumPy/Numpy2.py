# -*- coding: utf-8 -*-
"""
@author: Rabia Tüylek
"""

import numpy as np
import time 
random_array = np.random.rand(5,5)
print(random_array)
print("\n")
print("third row second column number is : ", random_array[2][1],random_array[2,1])

a = np.zeros([2,3])
print(a)
# slicing arrays [start : end], [start :end : step]
print("first three rows of first column :" , random_array[:3,0])
print("forth column : ", random_array[:,3])
print("last row 3rd, 4th, 5th columns : ", random_array[4,2:])
print("\n")

# Reshaping
b = np.random.rand(6,6)
print(b)
print("new 9x4 reshaped array : ", b.reshape(9,4))
print("new 2x18 reshaped array : ", b.reshape(2,18))
print("\n", b.shape)

# Matrix Operations
arr= np.array([[1,2],[3,4]])
print("\naddition : ","\n", arr + arr )
print("\nSubtract : ","\n", arr - arr)
print("\nMultiply : ","\n", arr*arr)
print("\nDivision : " ,"\n", arr/ arr)
print ("\nadd a scalar : ","\n", arr + 5)
print("\nadd a vector : ", "\n", arr + [7,8])

temp_arr = np.random.rand(3,4)
print("\n" ,temp_arr)
print("\nSum a with axis=0 : \n", np.sum(temp_arr,axis= 0))
print("\nSum a with axis=1 : \n", np.sum(temp_arr,axis= 1))

# Dot product 
temp_arr_transpose = temp_arr.T
dot = np.dot(temp_arr,temp_arr_transpose)
print("\nDot Product : \n", dot)


# Vectorization
rand_arr1 = np.random.rand(10,)
rand_arr2 = np.random.rand (10,)

# classical dot product
temp = 0
for i in range(10):
    temp = temp + float(rand_arr1[i]*rand_arr2[i])
    print(temp)
    

tik= time.time()
e = np.dot(rand_arr1,rand_arr2)
print("\ne: ",e)
tok= time.time()
print("multiply velocity in milliseconds is : ",tok-tik)


#Outer Product
outer = np.outer(rand_arr1, rand_arr2)
print("\n")
print("Outer product :\n ",outer)

# Elementwise Multiplication
tika=time.process_time()
mul = np.multiply(rand_arr1, rand_arr2)
toka=time.process_time()
print("\n")
print("Elementwise Multiplication \n",mul)
print("\n")
print("Elementwise Multiplication in milliseconds is : ",toka-tika)























