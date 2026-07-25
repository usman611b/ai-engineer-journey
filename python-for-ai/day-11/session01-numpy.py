# ==========================================================

# NumPy Complete Notes (Day 11)

# Author: Usman Ali

# AI Engineer Journey

# ==========================================================

"""
NumPy (Numerical Python)

NumPy is the foundation of almost every AI, Machine Learning,
Deep Learning and Data Science library.

Libraries built on NumPy:

• Pandas
• Scikit-Learn
• OpenCV
• TensorFlow
• PyTorch
• Hugging Face

If Python is the language,
NumPy is the mathematics engine behind AI.

---

## WHY DO WE NEED NUMPY?

Python Lists

✔ Easy to use
✔ Flexible

But

❌ Slow
❌ More memory usage
❌ Not optimized for numerical computation

NumPy Arrays

✔ Faster
✔ Less memory
✔ Mathematical operations
✔ Multi-dimensional arrays
✔ Foundation of AI

---

## INSTALLATION

Install NumPy

```
pip install numpy
```

Verify installation

```
python -c "import numpy; print(numpy.__version__)"
```

---

## IMPORTING NUMPY

Industry Standard

import numpy as np

We use "np" because it is the standard alias.

Just like

import pandas as pd
import matplotlib.pyplot as plt

=========================================================

1. CREATING ARRAYS
   =========================================================
   """

import numpy as np

# 1D Array

one_d = np.array([10, 20, 30, 40, 50])

print("1D Array")
print(one_d)

"""
Output

[10 20 30 40 50]
"""

# 2D Array

two_d = np.array([
[1,2,3],
[4,5,6]
])

print(two_d)

"""
1 2 3
4 5 6
"""

# 3D Array

three_d = np.array([
[
[1,2],
[3,4]
],
[
[5,6],
[7,8]
]
])

print(three_d)

# ==========================================================

# 2. ndarray

# ==========================================================

"""
Every NumPy array is an object of type

numpy.ndarray

ndarray means

N-Dimensional Array
"""

print(type(one_d))

# ==========================================================

# 3. SHAPE

# ==========================================================

"""
shape tells us

How many elements exist in every dimension.

Examples

(5,)      -> 5 elements

(2,3)     -> 2 rows
3 columns

(2,2,2)   -> 2 matrices
2 rows
2 columns
"""

print(one_d.shape)
print(two_d.shape)
print(three_d.shape)

# ==========================================================

# 4. NDIM

# ==========================================================

"""
ndim tells us

How many dimensions the array has.

1D

[1 2 3]

ndim = 1

---

2D

1 2
3 4

ndim = 2

---

3D

Matrix
Matrix

ndim = 3
"""

print(one_d.ndim)
print(two_d.ndim)
print(three_d.ndim)

# ==========================================================

# 5. DTYPE

# ==========================================================

"""
dtype means

Data Type

NumPy stores every element with a fixed datatype.

Why?

✔ Faster computation

✔ Less memory

✔ GPU compatibility

Common AI datatypes

int64

float64

float32

uint8 (Images)

float16 (Large AI Models)

bfloat16 (Modern LLMs)
"""

arr1 = np.array([1,2,3])

arr2 = np.array([1.5,2.7,3.9])

arr3 = np.array([1,2,3],dtype=np.float32)

print(arr1.dtype)

print(arr2.dtype)

print(arr3.dtype)

# ==========================================================

# 6. INDEXING

# ==========================================================

"""
Accessing elements.

1D

array[index]

2D

array[row,column]

3D

array[matrix,row,column]
"""

# 1D

print(one_d[0])

print(one_d[2])

print(one_d[-1])

# 2D

print(two_d[0,0])

print(two_d[1,2])

print(two_d[0,1])

# 3D

print(three_d[1,1,1])

print(three_d[0,0,1])

print(three_d[1,0,0])

# ==========================================================

# 7. SLICING

# ==========================================================

"""
1D

array[start:end]

Example

"""

print(one_d[1:4])

"""
Output

20 30 40

---

2D

array[rows,columns]

:

means

Take everything.
"""

# Entire second column

print(two_d[:,1])

# Entire first row

print(two_d[0,:])

# Multiple rows and columns

print(two_d[0:2,1:3])

## """

"""3D

array[matrix,row,column]"""
"""

# First Matrix

print(three_d[0,:,:])

# Second Matrix

print(three_d[1,:,:])

# Slice

print(three_d[1,0:2,0:2])

# ==========================================================

# VISUALIZATION

# ==========================================================

""""""
1D

[10 20 30 40 50]

Shape

(5,)

ndim

1

---

2D

1 2 3
4 5 6

Shape

(2,3)

ndim

2

---

3D

Matrix 1

1 2
3 4

Matrix 2

5 6
7 8

Shape

(2,2,2)

ndim

3
"""

#Vectorization
# IT is the ability of NumPy to perform operations on entire arrays without the need for explicit loops.
# unlike Python lists, NumPy arrays allow for element-wise operations, which means that you can perform mathematical operations on entire arrays at once, rather than having to loop through each element individually.

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])
result = arr1 + arr2
print(result)  # Output: [11 22 33 44 55]

result = arr1 * arr2
print(result)  # Output: [ 10  40  90 160

#If we want to multiply each element of arr1 by 10, we can do it like this at once without using a loop:
result = arr1 * 10
print(result)  # Output: [10 20 30 40 50]

result = arr1 ** 2
print(result)  # Output: [ 1  4  9 16 25]

result = np.sqrt(arr1)
print(result)  # Output: [1.         1.41421356 1.73205081 2.         2.23606798]   

#Broadcasting
#Why do we need broadcasting?
# Broadcasting is a powerful feature in NumPy that allows for operations between arrays of different shapes and sizes. 
# It enables NumPy to perform element-wise operations on arrays that do not have the same dimensions, 
# by automatically expanding the smaller array to match the shape of the larger array.

#Suppose you have:
arr = np.array([10, 20, 30, 40])

#We already know:
arr + 10 # Output: [20 30 40 50]

#Question:  👉 How did NumPy add 10 to every element without a for loop?

#Internally, it uses broadcasting. Instead of creating a new array:

#[10, 10, 10, 10]  ---->>>> NumPy pretends it exists and performs the operation efficiently.

# This saves both memory and time.


#Example 1: Scalar Broadcasting
arr = np.array([1, 2, 3, 4])
#You want to add 5 to every element of arr.
result = arr + 5
print(result)  # Output: [6 7 8 9]

#Visually, NumPy treats it as:
# [1, 2, 3, 4]
#[1 2 3 4]
#   +
#   5
#
#   ↓

#[1 2 3 4]
#   +
#[5 5 5 5]
#
#   ↓

#[6 7 8 9]

# The second array is never actually created. but that second array is never physically allocated in memory.

#Example 2: Multiplication

arr = np.array([2, 4, 6])
result = arr * 3
print(result)  # Output: [ 6 12 18]

#Visually, NumPy treats it as:
# [2, 4, 6]
#   *
#   3
#
#   ↓

# [2, 4, 6]
#   *
#[3 3 3]
#
#   ↓

#[6 12 18]


#Example 3: Broadcasting with 1D Arrays

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])         

result = a + b
print(result)  # Output: [11 22 33]
#Visually, NumPy treats it as:
# [1, 2, 3]
#[10, 20, 30] this is the same shape as a, so no broadcasting is needed.
#   +
#   ↓

#[11 22 33]

#Example 4: Broadcasting with 2D Arrays
#If you have a 2D array and a 1D array, NumPy will broadcast the 1D array across the rows of the 2D array.
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)  # Output: [[11 22 33] [14 25 36]]
#Visually, NumPy treats it as:
# [[1, 2, 3],
#  [4, 5, 6]]
#[10, 20, 30]
#   +
#   ↓

# [[11, 22, 33],
#  [14, 25, 36]]

#Example 5: Broadcasting with Different Shapes
#If the shapes are not compatible, NumPy will raise an error.
#Suppose you have:
a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20, 30])  # This has a different shape and cannot be broadcasted with a.

result = a + b  # This will raise a ValueError: operands could not be broadcast together with shapes (2,2) (3,)
print(result)  # Output: ValueError: operands could not be broadcast together with shapes (2,2) (3,)

#So, broadcasting is a powerful feature that allows NumPy to perform operations on arrays of different shapes and sizes, making it easier to work with data without the need for explicit loops or reshaping.
#So how broadcasting works is that NumPy automatically expands the smaller array to match the shape of the larger array, allowing for element-wise operations to be performed efficiently.
#So how we solve by br0dcasting by code:
#Remember the rule of broadcasting:
#1. If the arrays have a different number of dimensions, the shape of the smaller-dimensional array is padded with ones on its leading (left) side.
#2. If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
#3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised.
#So, to make the shapes compatible, we can reshape b to be a 2D array with shape (3, 1) instead of (3,). This way, it can be broadcasted across the rows of a.
#Here's how you can do it:
#code:
a = np.array([[1, 2], [3, 4] , [5, 6]]) #Shape (3, 2)
b = np.array([10, 20, 30]).reshape(3, 1)  # Reshape b to be a 2D array with shape (3, 1)
result = a + b
#so now the shapes are: 3 = 3 and 2 vs 1, so b can be broadcasted across the rows of a.
print(result)  # Output: [[11 12]
                #          [23 24]]
                #          [35 36]]

#Visually, NumPy treats it as:
# [[1, 2],
#  [3, 4],
#  [5, 6]]
#   +
# [[10],    
#  [20], so now b has been reshaped to a 2D array with shape (3, 1), which can be broadcasted across the rows of a.
#  [30]]
#  ↓

# [[11, 12],
#  [23, 24],
#  [35, 36]]


"""The Actual Broadcasting Rule

When comparing dimensions:

Starting from the rightmost dimension, two dimensions are compatible if:

They are equal.
One of them is 1.

Otherwise:

❌ Broadcasting fails.

Example 1

Shapes:

(2,3)

(3,)

Compare from the right:

3 == 3 ✅

2 vs (missing)

Missing is treated like 1.

2 vs 1 ✅

Works.

Example 2

Shapes:

(2,1)

(3,)

Compare:

1 vs 3

One dimension is 1 ✅

2 vs missing

Missing becomes 1

2 vs 1 ✅

Works.

Example 3

Shapes:

(3,)

(2,)

Compare:

3 vs 2

Neither equals the other.

Neither is 1.

❌ Error"""

"""A
(3,4)

+

(4,)

Work or Error?

B
(5,1)

+

(5,)

Work or Error?

C
(2,3)

+

(3,1)

Work or Error?

D (Boss Level 😄)
(4,1,3)

+

(   5,3)

Work or Error?"""


"""A
(3,4)

+

(4,)

You answered: ❌ Error

Correct Answer:

✅ Works

Why?

(3,4)

(4,)

NumPy treats (4,) as:

(1,4)

Compare:

4 vs 4  ✅

3 vs 1  ✅

Broadcasting succeeds.

Visualization:

1 2 3 4
5 6 7 8
9 10 11 12

+

10 20 30 40

↓

11 22 33 44
15 26 37 48
19 30 41 52
B
(5,1)

+

(5,)

You answered: ✅ Works

Correct.

Let's see why.

(5,1)

(5,)

becomes

(5,1)

(1,5)

Compare

1 vs 5  ✅

5 vs 1  ✅

Result shape:

(5,5)

This surprises many people.

Example:

1
2
3
4
5

+

10 20 30 40 50

becomes

11 21 31 41 51
12 22 32 42 52
13 23 33 43 53
14 24 34 44 54
15 25 35 45 55
C
(2,3)

+

(3,1)

You answered:

❌ Error

Correct.

Compare:

(2,3)

(3,1)

Right

3 vs 1

✅

Left

2 vs 3

❌

Neither equals.

Neither is 1.

Broadcasting fails.

D
(4,1,3)

+

(5,3)

You answered

❌ Error

Correct.

NumPy first expands

(5,3)

to

(1,5,3)

Now compare

(4,1,3)

(1,5,3)
3 vs 3 ✅

1 vs 5 ✅

4 vs 1 ✅

Wait…

This is the interesting part.

It actually WORKS, not an error.

The result shape is

(4,5,3)

This is why I called it the boss level question. 😄

The Trick

Whenever one array has fewer dimensions:

NumPy automatically puts 1s on the LEFT, not the right.

Example

(5,3)

↓

(1,5,3)

That's the part that confuses almost everyone at first."""

#--------------------------------------------------------------------------------------------

#Aggregation Functions
#What are Aggregation Functions?

#Aggregation functions take many values and return one summarized value.

#Examples:
#instead of manually doing this:
# 10 +20 + 30 + 40 + 50 = 150

#We can use NumPy's aggregation functions to do this in one line of code.
a = np.array([10, 20, 30, 40, 50])
#Sum
result = np.sum(a)
print(result)  # Output: 150

"""Think of them as functions that answer questions like:

What is the total?
What is the average?
What is the largest value?
What is the smallest value?
Where is the largest value?"""

#for 1D arrays, these functions are straightforward. For example, np.sum(a) returns the sum of all elements in the array a.
#For 2D arrays, we can specify the axis along which to perform the aggregation.

#For 1D :
#np.sum(a)  # Sum of all elements
#Maximum and Minimum
result = np.max(a)
result = np.min(a)

#For Mean and Median
result = np.mean(a)
result = np.median(a)

#For argmax and argmin
result = np.argmax(a)  # Index of the maximum value
result = np.argmin(a)  # Index of the minimum value

#For standard deviation and variance
result = np.std(a)  # Standard deviation
result = np.var(a)  # Variance

#For 2D arrays, we can specify the axis along which to perform the aggregation.

b = np.array([[1, 2, 3], [4, 5, 6]])
# 2 rows and 3 columns

"""        Columns
      C0  C1  C2
      ↓   ↓   ↓
R0 → 1  2  3
R1 → 4  5  6"""
#Sum along axis 0 (columns)
result = np.sum(b, axis=0)  # Output: [5 7 9] Sum of each column 
print(result)
#Sum along axis 1 (rows)
result = np.sum(b, axis=1)  # Output: [ 6 15 ] sum of each row
print(result)

#Maximum and Minimum along axis 0 (columns)
result = np.max(b, axis=0)  # Output: [4 5 6] Maximum of each column
print(result)
result = np.min(b, axis=1)  # Output: [1 4] Minimum of each row
print(result)   

#Mean and Median along axis 0 (columns)
result = np.mean(b, axis=0)  # Output: [2.5 3.5 4.5] Mean of each column
print(result)
result = np.median(b, axis=1)  # Output: [2. 5.] Median of each row
print(result)

#Argmax and Argmin along axis 0 (columns)
result = np.argmax(b, axis=0)  # Output: [1 1 1] Index of the maximum value in each column
print(result)
result = np.argmin(b, axis=1)  # Output: [0 0] Index of the minimum value in each row
print(result)

#Standard Deviation and Variance along axis 0 (columns)
result = np.std(b, axis=0)  # Output: [1.5 1.5 1.5] Standard deviation of each column
print(result)
result = np.var(b, axis=1)  # Output: [0.66666667 0.66666667] Variance of each row
print(result)

#-----------------------------------------------------

#Reshaping Arrays
#Reshaping means changing the shape of an array without changing its data.  
#For example, you can convert a 1D array into a 2D array or vice versa.
#The reshape() function is used to change the shape of an array.

a = np.array([1, 2, 3, 4, 5, 6])
#Reshape to 2D array with 2 rows and 3 columns
result = a.reshape(2, 3)
print(result)

#Reshape to 1D array
result = result.reshape(6)
print(result)

# Reshape to 3D array with 1 matrix, 2 rows, and 3 columns
result = a.reshape(1, 2, 3)
print(result)

a2 = np.array([[1, 2, 3], [4, 5, 6]])
#Reshape to 1D array    
result = a2.reshape(6)
print(result)

result = a2.reshape(3, 2)
print(result)

result = a2.reshape(2, 3, 1)
print(result)

a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#Reshape to 2D array with 4 rows and 2 columns
result = a3.reshape(4, 2)
print(result)

result = a3.reshape(2, 4)
print(result)

result = a3.reshape(8)
print(result)

# 🔥 One Super Useful Feature (-1)

# The -1 in the reshape function means "infer the dimension from the other dimensions"
# For example, if you have a 1D array with 6 elements and you want to reshape it to a 2D array with 2 rows, you can use -1 for the number of columns:
result = a.reshape(2, -1)
print(result)

# Or if you want to reshape it to a 3D array with 2 matrices, each with 3 rows and 2 columns:
result = a.reshape(2, 3, -1)
print(result)

"""Whenever you see -1, think:

"NumPy, you calculate this dimension for me."

Example:

12 elements

reshape(3,-1)

↓

3 × ? = 12

↓

? = 4

Very simple. --->>> becomes (3 , 4)

"""
