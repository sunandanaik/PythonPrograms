#Using numpy library for numerical computation
import numpy as np
n1=np.array([10,20,30,40,50]) #single dim array
#n2=np.array([[10,20,30,40],[50,60,70,80,90],['a','b','c']])  #multi dim array
print(n1)
#print(n2)

# n3=np.array([1,2,3,4,5],[4,5,6,7])
# print(type(n3))
# print(n3)

#Initializing numpy array values with zeroes
n0=np.zeros((5,5)) #zeros((rowsize,colsize))
print(n0)

#initializing numpy array with the same number
n3=np.full((2,2),4)
print(n3)

n4=np.arange(51,101)
print(n4)

# for i in range(1,11):
#     print(i)

n5=np.arange(10,50,2)
print(n5)

#Initializing numpy array with random numbers
nrand=np.random.randint(1,100,10)
print(nrand)

#Checking of numpy array shapes
ns=np.array([[1,2,3],[4,5,6]])
print("Shape is:",ns.shape)


#Joining of numpy array using vstack()
n1=np.array([10,20,30])
n2=np.array([40,50,60])
print(np.vstack((n1,n2)))

#Joining of numpy array using hstack()
n1=np.array([10,20,30])
n2=np.array([40,50,60])
print(np.hstack((n1,n2)))

#Joining of numpy array using column_stack()
n1=np.array([10,20,30])
n2=np.array([40,50,60])
print(np.column_stack((n1,n2)))

#Intersecting of numpyarray
n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90])

print("Intersection:",np.intersect1d(n1,n2))

#Differencing the numpy array
n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90])

print("Difference:",np.setdiff1d(n1,n2))

#Addition of Numpy Array
n1=np.array([10,20])
n2=np.array([30,40])
print("Sum is:",np.sum([n1,n2]))

print("Addition with respect to col:",np.sum([n1,n2],axis=0))

print("Addition with respect to row:",np.sum([n1,n2],axis=1))

#Incrementing /changing array values using basic arithmetic operations
n1=np.array([10,20,30,40,50])
n1=n1-1
print(n1)

n1=np.array([10,20,30,40,50])
n1=n1*2
print(n1)

n1=np.array([10,20,30,40,50])
n1=n1/2
print(n1)

n1=np.array([10,20,30,40,50])
print("Mean is:",np.mean(n1))

print("Median is:",np.median(n1))

print("Standard Deviation is:",np.std(n1))

#Numpy Save and load
n1=np.array([10,20,30,40,50,60])
np.save('my_numpy',n1)

n2=np.load('my_numpy.npy')
print(n2)




