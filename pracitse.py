import numpy as np 
a=np.array([5,6,7,8,9,2])
print('list in array form is ', a)
#counts the numbers in array
print(a.shape)
c=np.arange(5)
print(c)
#limit in arange
print(np.arange(2,16,2))
#zeros
print(np.zeros(8))
#multidimention zeros 2-d
c=np.zeros((2,3))
print(c)
#zeros in 3-d
d=np.zeros((2,2,2))#2 depths, 2 rows and 2 columns
print(d)

#full single dimension
print(np.full((4),6))
#multidimension full
print(np.full((2,4,3),8))
#defining single dimension array
arr1=np.array([4,5,6,7])
print(arr1)
#defining 2-d array
arr2=np.array([[4,1,9,7],[8,7,6,1]])
print(arr2)
#defining 3-d array with depth 1
arr3=np.array([[[9,6,2],[1,2,4],[7,4,9]]]) #1 depth 3 rows and 3 columns.

print(arr3)
print(np.shape(arr3))
print()
# converting lists into numpy arrays
my_list=[6,3,5,1,9]
my_array=np.array(my_list)
print(my_array)

#defining 3-d array with depth layer=2
arr4=np.array([[[2,3,4,5],[2,3,4,1]],[[4,5,6,1],[7,8,9,9]]])
print(np.shape(arr4))
print()
print(arr4)