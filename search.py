import numpy as np
arr1=np.array([6,4,5,9,8,1])
x=np.where(arr1%2==0)
print(x)#return tuples
#if we wants only the index of the even numbers in the array
print(x[0])
#to actually print the even numbers of the array
print(arr1[x[0]])
#alternatives
my_list=[]

my_list=arr1%2==0
print(my_list) 
print('even numbers in arr1 are',arr1[my_list])          