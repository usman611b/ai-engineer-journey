import numpy as np

#----------------------------------------------------------

# Next Topic: flatten() vs ravel()
#flatten() and ravel() are both used to convert a multi-dimensional array into a 1D array, but they have some differences in terms of memory usage and behavior.

#flatten() creates a new copy of the array and returns a 1D array, 
# while ravel() returns a flattened view of the original array whenever possible. 
# If the original array is contiguous in memory, ravel() will return a view; otherwise, it will return a copy.

arr = np.array([[1, 2, 3], [4, 5, 6]])
# Using flatten()
flat_arr = arr.flatten()
print(flat_arr)  # Output: [1 2 3 4 5 6]

flat_arr[0] = 10
print(flat_arr)  # Output: [10  2  3  4  5  6]
print(arr)  # Output: [[1 2 3] [4 5 6]]  (Original array remains unchanged)


# Using ravel()
raveled_arr = arr.ravel()
print(raveled_arr)  # Output: [1 2 3 4 5 6]
raveled_arr[0] = 10
print(raveled_arr)  # Output: [10  2  3  4  5  6]
print(arr)  # Output: [[10  2  3] [4 5 6]]  (Original array is modified because ravel() returns a view)
print(raveled_arr)  # Output: [10 2 3 4 5 6]

"""flatten() returns a new copy of the array, so changes do not affect the original. 
ravel() returns a view whenever possible, sharing the same memory with the original array, 
so modifying the returned array usually modifies the original as well. ravel() is generally more memory-efficient."""

#-----------------------------------------------------------

# Topic: Transpose (.T)
# Transpose is a common operation in linear algebra and data manipulation.
# It Convert Rows into Columns and Columns into Rows.

arr = np.array([[1, 2, 3], [4, 5, 6]])
# Original array
print(arr) # Output: [[1 2 3] [4 5 6]]
print(arr.shape) # Output: (2, 3)

# Transposed array
print(arr.T) # Output: [[1 4] [2 5] [3 6]]
print(arr.T.shape) # Output: (3, 2)

#-------------------------------------------------------------

#Topic: vstack() and hstack() combining arrays vertically and horizontally.
#vstack() is used to stack arrays vertically (row-wise), 
#while hstack() is used to stack arrays horizontally (column-wise).

#Example of vstack():
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Stack vertically
result = np.vstack((a, b))
print(result)  # Output: [[1 2 3] [4 5 6]]

a = np.array([[1, 2], [3, 4]]) # shape (2, 2)
b = np.array([[5, 6], [7, 8]]) # shape (2, 2)
result = np.vstack((a, b))
print(result)  # Output: [[1 2] [3 4] [5 6] [7 8]]  shape (4, 2) no change in the number of columns, but the number of rows has increased.

a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # shape (2, 2, 2)
b3 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]) # shape (2, 2, 2)
result = np.vstack((a3, b3))
print(result)  # Output: [[[ 1  2] [ 3  4]] [[ 5  6] [ 7  8]] [[ 9 10] [11 12]] [[13 14] [15 16]]] shape (4, 2, 2) no change in the number of columns, but the number of rows has increased.


#in vstack(), the arrays are stacked on top of each other, 
# creating a new array with more rows.but the number of columns must be the same for all arrays being stacked.

a = np.array([1, 2, 3]) # shape (3,)    
b = np.array([4, 5, 6]) # shape (3,)
# Example of hstack():
# Stack horizontally
result = np.hstack((a, b))
print(result)  # Output: [1 2 3 4 5 6]  
# The arrays are stacked side by side, creating a new array with more columns.
# The number of rows must be the same for all arrays being stacked.

a2 = np.array([[1, 2], [3, 4]]) # shape (2, 2)
b2 = np.array([[5, 6], [7, 8]]) # shape (2, 2)

result = np.hstack((a2, b2))
print(result)  # Output: [[1 2 5 6] [3 4 7 8]] shape (2, 4) no change in the number of rows, but the number of columns has increased.

a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # shape (2, 2, 2)
b3 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]) # shape (2, 2, 2)
result = np.hstack((a3, b3))    
print(result)  # Output: [[[ 1  2] [ 3  4] [ 9 10] [11 12]] [[ 5  6] [ 7  8] [13 14] [15 16]]] shape (2, 2, 4) no change in the number of rows, but the number of columns has increased.


#--------------------------------------------------------------------
# Splitting Arrays
# NumPy provides functions to split arrays into multiple sub-arrays.
# The main functions for splitting arrays are split(), hsplit(), and vsplit().

#split() is a general function that can split an array into multiple sub-arrays along a specified axis.
#hsplit() is used to split an array horizontally (column-wise).
#vsplit() is used to split an array vertically (row-wise).

#Example of split():
arr = np.array([1, 2, 3, 4, 5,  6])
sub_arrays = np.split(arr, 3)
print(sub_arrays)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]

#Example of hsplit():
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
sub_arrays_h = np.hsplit(arr2d, 2)
print(sub_arrays_h)  # Output: [array([[1, 2], [5, 6]]), array([[3, 4], [7, 8]])]

#Example of vsplit():
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
sub_arrays_v = np.vsplit(arr2d, 2)  
print(sub_arrays_v)  # Output: [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
sub_arrays_v3d = np.vsplit(arr3d, 2)    
print(sub_arrays_v3d)  # Output: [array([[[1, 2], [3, 4]]]), array([[[5, 6], [7, 8]]])]

sub_arrays_h3d = np.hsplit(arr3d, 2)
print(sub_arrays_h3d)  # Output: [array([[[1, 2], [5, 6]]]), array([[[3, 4], [7, 8]]])]


#--------------------------------------------------------------------------

# Boolean Indexing
# Boolean indexing is a powerful feature in NumPy that allows you to select elements from an array
# based on a condition. Instead of using integer indices, you use boolean values (True or False) to filter the array.


#Instead of selecting data by position (index), we select data by condition.
#Normal indexing:

arr = np.array([10,20,30,40])

print(arr[2])

#Output: 30

#Boolean indexing:

arr = np.array([10,20,30,40])

print(arr[arr > 20])

#Output: [30 40]

#Selected by condition. 

#How does it work?
#Suppose

arr = np.array([10,20,30,40,50])
#Now

result = arr > 25
print(result)  # Output: [False False True True True]

#This is called a Boolean Mask.
#Visualization:

"""Values

10   20   30   40   50

Condition (>25)

 F    F    T    T    T

Now use it:

arr[arr > 25]

NumPy keeps only the True values.

Result

[30 40 50]"""


#Example of Boolean Indexing:
a = np.array([1, 2, 3, 4, 5])
# Create a boolean mask where the condition is True for elements greater than 3
mask = a > 3
print(mask)  # Output: [False False False  True  True]

arr = np.array([5,15,25,35])

print(arr[arr < 20]) # Output: [ 5 15]

arr = np.array([10,20,30,20])

print(arr[arr != 20]) # Output: [10 30]

# Multiple Conditions
arr = np.array([5,10,15,20,25,30])
print(arr[(arr > 10) & (arr < 30)])  # Output: [15 20 25]

print(arr[(arr < 10) | (arr > 25)]) # Output: [ 5 30]

print(arr[~(arr > 20)]) # Output: [ 5 10 15 20]


#Boolean Indexing on 2D Arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Select elements greater than 5
print(arr2d[arr2d > 5])  # Output: [6 7 8 9]

"""Why AI Engineers Use This

Imagine a dataset of ages:

ages = np.array([12,18,25,16,30,40])

Adults only:

adults = ages[ages >= 18]

Result

[18 25 30 40]

Or image processing:

image[image > 200]

Gets all bright pixels.

Or removing missing values:

data[data != -1]

Boolean indexing is everywhere in AI."""

"""Important Rule

Never use Python's and or or with NumPy arrays.

❌ Wrong

arr[arr > 10 and arr < 20]

Use:

&
|
~

Correct:

arr[(arr > 10) & (arr < 20)]"""


#----------------------------------------------------------

# Conditional Selection
#📚 np.where()
#Think of it as Python's if-else for entire arrays.

#Without NumPy:

marks = [40, 70, 85, 30]

for mark in marks:
    if mark >= 50:
        print("Pass")
    else:
        print("Fail")

#Lots of code

#With NumPy:
marks = np.array([40, 70, 85, 30])
result = np.where(marks >= 50, "Pass", "Fail")
print(result)  # Output: ['Fail' 'Pass' 'Pass' 'Fail']

#Syntax: np.where(condition, value_if_true, value_if_false)

#Example:
arr = np.array([10,20,30,40])

result = np.where(arr > 20, "Big", "Small")

print(result)  # Output: ['Small' 'Small' 'Big' 'Big']

#Example 2:
arr = np.array([5,10,15,20])

result = np.where(arr > 10, 100, arr) # Replace values greater than 10 with 100, otherwise keep the original value.

print(result)  # Output: [  5  10 100 100]

#Example 3:
arr = np.array([-5,4,-2,7,8])

result = np.where(arr < 0, 0, arr)

print(result)  # Output: [0 4 0 7 8] very useful in AI for replacing negative values with 0.

#Example 4:
arr = np.array([10,20,30])

new = np.where(arr > 15, 999, arr)

print(arr)  # Output: [10 20 30]
print(new)  # Output: [ 10 999 999]  (Original array remains unchanged, a new array is created.)

#🤖 Real AI Example

#Imagine pixel values:

pixels = np.array([30,150,220,80,255])

#Convert bright pixels to white.

binary = np.where(pixels > 127, 255, 0)

print(binary) # Output: [  0 255 255   0 255]

#This is exactly how simple image thresholding works.

#2D Example:
image = np.array([[10, 200, 30], [150, 20, 250], [60, 180, 90]])
binary_image = np.where(image > 127, 255, 0)
print(binary_image) # Output: [[  0 255   0]
                     #          [255   0 255]
                     #          [  0 255   0]]

#example 3D:
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
result = np.where(arr3d > 4, "High", "Low")
print(result)  # Output: [[['Low' 'Low'] 
#                         ['Low' 'Low']] 
#                       
#                        [['High' 'High']
#                         ['High' 'High']]]

#-----------------------------------------------------------

# 📚 np.any() and np.all()
# np.any() checks if any element in the array satisfies a condition, while np.all() checks if all elements satisfy a condition.

# 1️⃣ np.any()
#Meaning : Returns True if at least ONE element is True.

#Think: "Is any element True?"

a = np.array([False, False, True, False])
print(np.any(a))  # Output: True

a = np.array([False, False, False]) # NO True elements
print(np.any(a))  # Output: False

a = np.array([1, 2, 3, 4])
print(np.any(a > 3))  # Output: True (At least one element is greater than 3)


#2️⃣ np.all()

#Meaning : Returns True only if EVERY element is True.

#Think : "Are all elements True?"

a = np.array([True, True, True])
print(np.all(a))  # Output: True

a = np.array([True, False, True])
print(np.all(a))  # Output: False (Not all elements are True)

a = np.array([5, 10, 15])
print(np.all(a > 0))  # Output: True (All elements are greater than 0)

a = np.array([5, 10, 15])
print(np.all(a > 10))  # Output: False (Not all elements are greater than 10)






