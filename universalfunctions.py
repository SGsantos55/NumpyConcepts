import numpy as np
arr=np.array([-2,-1,5,6,7,3,4])
print(np.sqrt(arr))
print(np.zeros((2,5)))
print(np.absolute(arr))

#exponents
print(np.exp(arr))
#max and min
print("the maximum number in array is ",np.max(arr))
print("the minimum number in array is ",np.min(arr))

#sign
print(np.sign(arr))#return -1 for negetive numbers and 1 for positive numbers
#sign cos,sin,log
print(np.sin(arr))
print(np.log(arr))