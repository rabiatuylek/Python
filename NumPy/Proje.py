# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:20:38 2020

@author: RABİA TÜYLEK 090170153
"""
import numpy as np
import scipy.linalg 
from scipy import linalg
import matplotlib.pyplot as plot

n1=np.array([1.0, 0.0, 0.0, 1.0])
n1_column=n1.reshape((4,1))
n1_matris= n1_column* (1./2.**0.5)
N1=n1_matris* n1_matris.transpose()

n2=np.array([0.0, 1.0, 1.0, 0.0])
n2_column=n2.reshape((4,1))
n2_matris= n2_column*(1.0/2.0**0.5)
N2=n2_matris* n2_matris.transpose()

I=np.eye(4)
G= I-(N1+N2)
R= I-(2*G)
print("Gramm Schmit")
print(G)
print("R is : ")
print(R)
# for eigenvalue , eigenvector
print("----------------------")
[eigenvalues,eigenvectors]=np.linalg.eigh(R)
print("eigenvalues are ")
print(eigenvalues)
print("------------")
print("eigenvectors are")
print(eigenvectors)
print("eigenvalues and eigenvectors are founded")

#Md matrice
Wo=1.0
M1= np.array([-3.0, 2.0, 0.0, 0.0])
M2=np.array([2/5, -1.0, 3/5, 0.0])
M3=np.array([0.0, 3/5, -1.0, 2/5])
M4=np.array([0.0, 0.0, 2.0, -3.0])
Md=(np.array([M1,M2,M3,M4]))*Wo
print("Md is not symmetric.")
print(Md)
print("Md and R are commute.")
# multiple Md and  R matrices
matris1=[[0 for a in range(4)] for b in range(4)]
for i in range(len(Md)):
    for j in range(len(R[0])):
        for k in range(len(R)):
            matris1[i][j] += Md[i][k]*R[k][j]
            

matris2=[[0 for a in range(4)] for b in range(4)]
for i in range(len(R)):
    for j in range(len(Md[0])):
        for k in range(len(Md)):
            matris2[i][j] += R[i][k]*Md[k][j]
            
carpim= [[matris1[i][j] - matris2[i][j] for j in range(len(matris1[0]))] 
for i in range(len(matris1))]   

for carpim_sonucu in carpim:
    print(carpim_sonucu)

# for V1 matrice
print("V1 matrisi :")
Va_=np.array([1.0, 0.0, -1.0, 0.0])
Vb_=np.array([0.0, -1.0, 0.0, -1.0])
Vc_=np.array([0.0, 1.0, 0.0, -1.0])
Vd_=np.array([-1.0, 0.0, -1.0, 0.0])
V1_=(np.array([Va_,Vb_,Vc_,Vd_]))*(2.0**-0.5)
V1=V1_.reshape((4,4))
V1_trans=V1.transpose()

print(V1)
print("-------------------------")
print("V1 matrisi Transposu : ")
V1_trans=V1.transpose()
print(V1_trans)

print("Md' matrice : ")
matris1=[[0 for a in range(4)] for b in range(4)]
for i in range(len(V1_trans)):
    for j in range(len(Md[0])):
        for k in range(len(Md)):
            matris1[i][j] += V1_trans[i][k]*Md[k][j]
            

matris3=[[0 for a in range(4)] for b in range(4)]
for i in range(len(matris1)):
    for j in range(len(V1[0])):
        for k in range(len(V1)):
            matris3[i][j] += matris1[i][k]*V1[k][j]

for Md_ussu in matris3:
    print(Md_ussu)

print("\n")
print("eigenvalues and eigenvectors of V2 matris :")
(Eigenvalue, Eigenvector) = np.linalg.eig(matris3)

print("\n Eigenvalues:" , Eigenvalue,)
print(" \n Eigenvectors:", Eigenvector)
print("\n")

V2=Eigenvector
print("V2 matrice : ")
print(V2)
V2_inverse=linalg.inv(V2)
print("Inverse of V2 : ")
print(V2_inverse)

#to find lamda(diagonal matrice) 
print(" Diagonal Matrice : ")
mat1=[[0 for a in range(4)] for b in range(4)]
for i in range(len(V2_inverse)):
    for j in range(len(matris3[0])):
        for k in range(len(matris3)):
            mat1[i][j] += V2_inverse[i][k]*matris3[k][j]
            

mat2=[[0 for a in range(4)] for b in range(4)]
for i in range(len(mat1)):
    for j in range(len(V2[0])):
        for k in range(len(V2)):
            mat2[i][j] += mat1[i][k]*V2[k][j]

for diagonal in mat2:
    print(diagonal)

print("\n")
print("eigenvectors of Md")
mul1=[[0 for a in range(4)] for b in range(4)]
for i in range(len(V1)):
    for j in range(len(V2[0])):
        for k in range(len(V2)):
            mul1[i][j] += V1[i][k]*V2[k][j]

for eig_Md in mul1:
     print(eig_Md)       

e_1=np.array([-0.69, 0.148, -0.148, 0.690])
eigh_1=e_1.reshape((4,1))
eigh_t1=eigh_1.transpose()
e_2=np.array([0.516, 0.4737, -0.4737, -0.5161])
eigh_2=e_2.reshape((4,1))
eigh_t2=eigh_2.transpose()
e_3=np.array([0.7, -0.09687, -0.09687, 0.7])
eigh_3=e_3.reshape((4,1))
eigh_t3=eigh_3.transpose()
e_4=np.array([0.403, 0.580, 0.580, 0.403])
eigh_4=e_4.reshape((4,1))
eigh_t4=eigh_4.transpose()
eigh=np.array([eigh_1, eigh_2, eigh_3, eigh_4])

#özvektörleri birbirleriyle çarparken ilikinin transposunu aldım ki matris
#çarpımı yapabileyim.
print("-------------------------------------------")
print("\n")
print("Md is not orthogonal matrice.")

print("multiple eigenvector 1 and eigenvector 2 ")
c1_2=np.matmul(eigh_t1,eigh_2)
print(c1_2)

print("multiple eigenvector 1 and eigenvector 3 ")
c1_3=np.matmul(eigh_t1,eigh_3)
print(c1_3)

print("multiple eigenvector 1 and eigenvector 4 ")
c1_4=np.matmul(eigh_t1,eigh_4)
print(c1_4)

print("multiple eigenvector 2 and eigenvector 3 ")
c2_3=np.matmul(eigh_t2,eigh_3)
print(c2_3)

print("multiple eigenvector 3 and eigenvector 4 ")
c3_4=np.matmul(eigh_t3,eigh_4)
print(c3_4)

print("multiple eigenvector 2 and eigenvector 4 ")
c2_4=np.matmul(eigh_t2,eigh_4)
print(c2_4)


print("multiple eigenvector 1 and eigenvector 1 ")
c1_1=np.matmul(eigh_t1,eigh_1)
print(c1_1)


print("multiple eigenvector 2 and eigenvector 2 ")
c2_2=np.matmul(eigh_t2,eigh_2)
print(c2_2)


print("multiple eigenvector 3 and eigenvector 3 ")
c3_3=np.matmul(eigh_t3,eigh_3)
print(c3_3)


print("multiple eigenvector 4 and eigenvector 4 ")
c4_4=np.matmul(eigh_t4,eigh_4)
print(c4_4)

m=1.0
m1=m
m2=5*m
m3=5*m
m4=m

z1=np.array([m1,0,0,0])
z2=np.array([0,m2,0,0])
z3=np.array([0,0,m3,0])
z4=np.array([0,0,0,m4])
Z=np.array([z1,z2,z3,z4])

#K matrice     
m=1.0
w0=1.0

k1=m*(w0**2)
k2=2*m*(w0**2)
k3=3*m*(w0**2)
k4=2*m*(w0**2)
k5=m*(w0**2)

k1=np.array([-k1-k2, k2, 0.0, 0.0])
k2=np.array([k2, -k2-k3, k3, 0.0])
k3=np.array([0.0, k3, -k3-k4, k4])
k4=np.array([0.0, 0.0, k4, -k4-k5])
K=np.array([k1,k2,k3,k4])
print("K matrisi")
print(K)
print("\n")

(e__value, e__vector)=scipy.linalg.eigh(K,Z)
v0=np.array(e__vector[:,0])
v1=np.array(e__vector[:,1])
v2=np.array(e__vector[:,2])
v3=np.array(e__vector[:,3])
print("Eigenvalues :")
print(e__value)
print("Eigenvectors :")
print(e__vector)
print('Other orthogonality situations')

for i in range(4):
 for j in range(4):
     n=0.0
     for k in range(4):
         n+=Z[k,k]*e__vector[k,i]*e__vector[k,j] 
     print('i=',i,' j=',j,' ',n)
 
wi_1= -3.43578167
wi_2= -3.27797338
wi_3= -1.16421833
wi_4= -0.12202662

vi_1=np.array([-0.63567201, 0.13850711, -0.13850711, 0.63567201])
vi1=vi_1.reshape((4,1))
vi1_t=vi1.transpose()

vi_2=np.array([0.67524838, -0.09385054, -0.09385054, 0.67524838])
vi2=vi_2.reshape((4,1))
vi2_t=vi2.transpose()

vi_3=np.array([-0.3097113, -0.28428117, 0.28428117,  0.3097113])
vi3=vi_3.reshape((4,1))
vi3_t=vi3.transpose()

vi_4=np.array([-0.20985619, -0.30198026, -0.30198026, -0.20985619])
vi4=vi_4.reshape((4,1))
vi4_t=vi4.transpose()

x0=1.0
F0=m*(w0**2)*x0
W_maks=np.abs(wi_1)
W=2*W_maks

Force=np.array([0.0, 0.0, 1.0, 0.0])
Force*=F0
x1=np.dot(v0,Force)/(e__value[0]**2-W**2)*v0[0]
x1+=np.dot(v1,Force)/(e__value[1]**2-W**2)*v1[0]
x1+=np.dot(v2,Force)/(e__value[2]**2-W**2)*v2[0]
x1+=np.dot(v3,Force)/(e__value[3]**2-W**2)*v3[0]
print("x1")
print(x1)
x2=np.dot(v0,Force)/(e__value[0]**2-W**2)*v0[1]
x2+=np.dot(v1,Force)/(e__value[1]**2-W**2)*v1[1]
x2+=np.dot(v2,Force)/(e__value[2]**2-W**2)*v2[1]
x2+=np.dot(v3,Force)/(e__value[3]**2-W**2)*v3[1]
print("x2")
print(x2)

x3=np.dot(v0,Force)/(e__value[0]**2-W**2)*v0[2]
x3+=np.dot(v1,Force)/(e__value[1]**2-W**2)*v1[2]
x3+=np.dot(v2,Force)/(e__value[2]**2-W**2)*v2[2]
x3+=np.dot(v3,Force)/(e__value[3]**2-W**2)*v3[2]
print("x3")
print(x3)

x4=np.dot(v0,Force)/(e__value[0]**2-W**2)*v0[3]
x4+=np.dot(v1,Force)/(e__value[1]**2-W**2)*v1[3]
x4+=np.dot(v2,Force)/(e__value[2]**2-W**2)*v2[3]
x4+=np.dot(v3,Force)/(e__value[3]**2-W**2)*v3[3]
print("x4")
print(x4)

t=np.linspace(0.0,12.,400)
plot.plot(t,x3*np.sin(W*t),t,x4*np.sin(W*t))
plot.show()













     


          


    






