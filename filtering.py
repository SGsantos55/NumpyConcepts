import numpy as np
my_list=[]
arr=np.array([4,9,2,7,6,1])
for el in arr:
    if(el%2==0):
        my_list.append(True)
    else:
        my_list.append(False)
print(arr)
print(my_list)
print('after filtering the even numbers',arr[my_list])     

#Shortcuts
my_list=arr%2!=0
print(my_list)
print('odd numbers after filtering',arr[my_list])








