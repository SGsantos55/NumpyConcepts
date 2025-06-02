import numpy as np
list=[2,3,4,5]
#convert list as numpy array
sg=np.array(list)
p=np.array([3,4,5,6,7,9,1])
print(sg)
print(p)
#counts the number of elements in array
print(sg.shape)
san=np.arange(5)#create list of array [0,1,2,3,4]
print(san)
#limit in arange
print(np.arange(2,16,2))
#zeros single dimension
print(np.zeros(8))
#multi dimension zeros
print(np.zeros((2,3)))#2 rows and 3 columns

print(np.zeros((2,2,3)))# 2 depths layer, 2 rows and 3 columns
#full
print(np.full((3),5))
#multidimentional full
print(np.full((2,3,4),7))




