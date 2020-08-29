#numpy module

import numpy as np
import sys
import time

S=range(1000)
print(sys.getsizeof(5)*len(S))

D=np.arange(1000)                              #numpy arrays aquire less memory than a list
print(D.size*D.itemsize)
print("--------------------------------------------")


size=10000
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)
start=time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start=time.time()
result=a1+ a2
print((time.time()-start)*1000)
print("----------------------------------------------")


a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)                             #built-in functions
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
print(a)

a=a.reshape(3,2)                          #reshaping the array
print(a)
print("------------------------------------------------")
print(a[0:3])                             #to print rows from 0 to 3 includong 0th row

p=np.linspace(1,3,5)                      #it gives 5 numbers equally distant between 1 and 3
print(p)
print("-----------------------------------------------")

print(a.max())                            #gives maximum value in array
print(a.min())                            #gives minimum value in array
print(a.sum())                            #gives sum of all the elements of the array
print(np.sqrt(a))                         #square root all the elements of the array
print("-----------------------------------------------")
print(np.std(a))                          #gives standard deviation of array elements
print("-----------------------------------------------")
print(np.exp(a))                          #converts array elements to their exponential
print("-----------------------------------------------")
print(np.log(a))                          #converts array elements to their natural logarithm
print("-----------------------------------------------")
print(np.log10(a))                        #convertd array elements to their logarithm bas 10
print("-------------------------------------------")



a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])
print(a+b)
print("-----------------------------------------------")
print(a-b)
print("-----------------------------------------------")
print(a*b)
print("-----------------------------------------------")
print(a/b)
print("-----------------------------------------------")
print(np.vstack((a,b)))                 #forms vertical array
print("-----------------------------------------------")
print(np.hstack((a,b)))                 #forms horizontal array
print("-----------------------------------------------")
print(a.ravel())

