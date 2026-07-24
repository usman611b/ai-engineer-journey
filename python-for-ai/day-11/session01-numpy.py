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

