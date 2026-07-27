import numpy as np
#📚 Sorting & Unique Values
#1- np.sort()
#Sorts the elements of an array in ascending order.

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_arr = np.sort(arr)
print(sorted_arr)

#2D array sorting
arr2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_arr2d = np.sort(arr2d, axis=1)  # Sort along rows
print(sorted_arr2d)

arr2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_arr2d = np.sort(arr2d, axis=0)  # Sort along columns
print(sorted_arr2d)


#2- np.unique()
#Returns the unique elements of an array.

unique_arr = np.unique(arr)
print(unique_arr)

arr = np.array([ "apple", "banana", "apple", "orange", "banana"])
unique_arr = np.unique(arr)
print(unique_arr)

#2D array unique values
arr2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
unique_arr2d = np.unique(arr2d)
print(unique_arr2d)



#3- np.argsort()
#Returns the indices that would sort an array.

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
indices = np.argsort(arr)
print(indices)

#2D array argsort
arr2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
indices2d = np.argsort(arr2d, axis=1)  # Sort along rows
print(indices2d)

#-----------------------------------------------------------

#Mathematical Functions

#📚 1. np.sqrt() — Square Root
arr = np.array([4, 9, 16, 25])
sqrt_arr = np.sqrt(arr)
print(sqrt_arr)  # Output: [2. 3. 4. 5.]

#📚 2. np.exp() — Exponential
arr = np.array([1, 2, 3])
exp_arr = np.exp(arr)
print(exp_arr)  # Output: [ 2.71828183  7.3890561  20.08553692]

#📚 3. np.log() — Natural Logarithm
arr = np.array([1, 2, 3])
log_arr = np.log(arr)
print(log_arr)  # Output: [0.         0.69314718 1.09861229]

#📚 4. np.square() — Square Every Element
arr = np.array([1, 2, 3])
square_arr = np.square(arr)
print(square_arr)  # Output: [1 4 9]

#📚 5. np.power() — Raise Elements to a Power
arr = np.array([1, 2, 3])
power_arr = np.power(arr, 3)  # Raise each element to the power of 3
print(power_arr)  # Output: [ 1  8 27]

#📚 6. np.abs() — Absolute Value
arr = np.array([-1, -2, 3])
abs_arr = np.abs(arr)
print(abs_arr)  # Output: [1 2 3]

#📚 7. np.round() — Round Elements
arr = np.array([1.2, 2.7, 3.1])
round_arr = np.round(arr)
print(round_arr)  # Output: [1. 3. 3.]

#📚 8. np.floor() — Floor of Elements
arr = np.array([1.2, 2.7, 3.1])
floor_arr = np.floor(arr)
print(floor_arr)  # Output: [1. 2. 3.]

#📚 9. np.ceil() — Ceiling of Elements
arr = np.array([1.2, 2.7, 3.1])
ceil_arr = np.ceil(arr)
print(ceil_arr)  # Output: [2. 3. 4.]

#📚 10. Trigonometric Functions
arr = np.array([0, np.pi/2, np.pi])
sin_arr = np.sin(arr)
print(sin_arr)  # Output: [0. 1. 0.]

cos_arr = np.cos(arr)
print(cos_arr)  # Output: [ 1.  0. -1.]

tan_arr = np.tan(arr)
print(tan_arr)  # Output: [ 0.  1.2246468e-16 -1.2246468e-16] (approximately 0, 0, 0 due to floating-point precision)

#📚 11. np.clip()
#Limits the values in an array to a specified range.
arr = np.array([1, 2, 3, 4, 5])
clipped_arr = np.clip(arr, 2, 4)  # Limit values to be between 2 and 4
print(clipped_arr)  # Output: [2 2 3 4 4]
#Very common in image processing.

#📚 12. np.maximum() and np.minimum()
#Element-wise maximum and minimum of two arrays.
arr1 = np.array([1, 4, 3])
arr2 = np.array([2, 1, 5])
max_arr = np.maximum(arr1, arr2)
min_arr = np.minimum(arr1, arr2)
print(max_arr)  # Output: [2 4 5]
print(min_arr)  # Output: [1 1 3]

#------------------------------------------------------------

#📚 Copy vs View
"""🤔 Why do we need this?

Suppose you have an array:

import numpy as np

arr = np.array([10,20,30,40])

Now you want another variable.

Question:

If you modify the new variable...

👉 Should the original array also change?

Sometimes YES → View

Sometimes NO → Copy

This is where view() and copy() come in."""

#🟢 1. View
"""
A view shares the same memory as the original array.

Think of it like two windows looking at the same room.

Original Array
       │
       ▼
  [10 20 30 40]
       ▲
       │
     View"""

arr = np.array([10,20,30,40])

view_arr = arr.view()

view_arr[0] = 999

print(view_arr) #Output: [999  20  30  40]
print(arr) #Output: [999  20  30  40] (Original array is also changed)


#🔴 2. Copy
"""
A copy creates completely new memory.

Think of it like photocopying a document.

Original

[10 20 30]

      ❌

Copy

[10 20 30]

Completely independent."""

arr = np.array([10,20,30,40])
copy_arr = arr.copy()
copy_arr[0] = 999
print(copy_arr) #Output: [999  20  30  40]
print(arr) #Output: [10 20 30 40] (Original array is unchanged)

#Example of when to use view() vs copy():
"""
Use view() when you want to create a new reference to the same data, saving memory.
Use copy() when you want to create an independent copy of the data.
"""
