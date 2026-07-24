import numpy as np
# 1-D Array
arr = np.array([1,2,3,4,5])
print(arr)

print(type(arr))  # Output: <class 'numpy.ndarray'>
print(arr.shape)  # Output: (5,)  (1D array with 5 elements)
print(arr.ndim)   # Output: 1 (1D array)
#indexing
print(arr[2])
print(arr[4])
#slicing
print(arr[1:4])

# 2-D Array
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)
print(type(arr2))
print(arr2.ndim)
print(arr2.shape)

#indexing
print(arr2[1,3])
print(arr2[0,2])
print(arr2[0,1])

#slicing
print(arr2[0:1,2:3])
print(arr2[: , 1: 4])

# 3-D Array
arr3 = np.array([
    [
        [1,2,3,4],
        [6,7,8,9]
     ],
     [
        [11,12,13,14],
        [15,16,17,18]
      ]

])
print(arr3)
print(type(arr3))
print(arr3.ndim)
print(arr3.shape)

#Indexing..
print(arr3[1,1,3])
print(arr3[0,0,3])
print(arr3[1,0,1])

#Slicing..
print(arr3[0,: , : ])
print(arr3[1,: , : ])
print(arr3[1,0:3 ,0 :2])
print(arr3[1,0:1 ,2 :3])
