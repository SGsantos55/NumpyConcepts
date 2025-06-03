#choose a random number from the list
import numpy as np
my_list=[5,6,7,1,2,3]
print(np.random.choice(my_list))

#from the numpy array
c=np.arange(1,49,1)
print(np.random.choice(c))

arr=np.array([[[2,3],[4,5]],[[4,7],[9,1]]])

print(np.shape(arr))
print(arr)

# print(np.random.choice(arr)) valid only for 1 -d array