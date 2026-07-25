import numpy as np
#Array Initialization Functions
#Array can be initialized in many ways using NumPy. Here are some common array initialization functions:

#📚 1. np.zeros()
#Creates an array filled with zeros.

#1D array of zeros
zeros_1d = np.zeros(5)
print(zeros_1d)
print(zeros_1d.dtype)  # Output: float64 (default data type for zeros)

#2D array of zeros
zeros_2d = np.zeros((3, 4))
print(zeros_2d)
print(zeros_2d.dtype)  # Output: float64 (default data type for zeros)

#3D array of zeros
zeros_3d = np.zeros((2, 3, 4))
print(zeros_3d)
print(zeros_3d.dtype)  # Output: float64 (default data type for zeros)


#📚 2. np.ones()
#Creates an array filled with ones.

#1D array of ones
ones_1d = np.ones(5)
print(ones_1d)
print(ones_1d.dtype)  # Output: float64 (default data type for ones)

#2D array of ones
ones_2d = np.ones((3, 4))
print(ones_2d)
print(ones_2d.dtype)  # Output: float64 (default data type for ones)

#3D array of ones
ones_3d = np.ones((2, 3, 4))
print(ones_3d)
print(ones_3d.dtype)  # Output: float64 (default data type for ones)


#📚 3. np.full( shape, value )
#Creates an array filled with a specified value.

#1D array filled with a specific value
full_1d = np.full(5, 7)
print(full_1d)
print(full_1d.dtype)  # Output: int64 (default data type for full)

#2D array filled with a specific value
full_2d = np.full((3, 4), 8)
print(full_2d)
print(full_2d.dtype)  # Output: int64 (default data type for full)

#3D array filled with a specific value
full_3d = np.full((2, 3, 4), 9)
print(full_3d)
print(full_3d.dtype)  # Output: int64 (default data type for full)


#📚 4. np.empty()
#It does NOT initialize values. It simply allocates memory.

#1D array of uninitialized values
empty_1d = np.empty(5)
print(empty_1d)
print(empty_1d.dtype)  # Output: float64 (default data type for empty

#2D array of uninitialized values
empty_2d = np.empty((3, 4))
print(empty_2d)
print(empty_2d.dtype)  # Output: float64 (default data type for empty)

"""These are garbage values already present in memory.

⚠️ Never assume empty() contains zeros."""

"""Why use it?

It's faster because NumPy skips filling values.

Useful when you'll immediately overwrite every element."""

#Example: Creating an empty array and then filling it with values
empty_array = np.empty(5)
empty_array.fill(42)  # Fill the array with a specific value
print(empty_array)


#📚 5. np.eye()
#Creates a 2D array with ones on the diagonal and zeros elsewhere.
#Very important in Linear Algebra.

#Identity matrix
identity = np.eye(3)
print(identity)
print(identity.dtype)  # Output: float64 (default data type for eye)

identity_4x4 = np.eye(4)
print(identity_4x4)

##Identity matrix with a different data type
identity_int = np.eye(3, dtype=int)
print(identity_int)
print(identity_int.dtype)  # Output: int64 (specified data type for eye)

#📚 6. np.identity()
#Creates an identity matrix (equivalent to np.eye())

identity_matrix = np.identity(3)
print(identity_matrix)
print(identity_matrix.dtype)  # Output: float64 (default data type for identity)

"""Difference

identity() only creates square matrices.

eye() is more flexible."""


#📚 7. np.arange(start , stop , step)
#Creates an array with a range of values.

#1D array with values from 0 to 4
arange_1d = np.arange(5)
print(arange_1d)
print(arange_1d.dtype)  # Output: int64 (default data type for arange)

#1D array with values from 2 to 8 (exclusive)
arange_2d = np.arange(2, 8)
print(arange_2d)
#1D array with values from 0 to 10 (exclusive) with a step of 2
arange_step = np.arange(0, 10, 2)
print(arange_step)

##1D array with values from 10 to 1 (exclusive) with a negative step
arange_negative_step = np.arange(10, 1, -1)
print(arange_negative_step)

#2D array with values from 0 to 11 (exclusive) reshaped to (3, 4)
arange_2d_reshaped = np.arange(12).reshape(3, 4)
print(arange_2d_reshaped)

#3D array with values from 0 to 23 (exclusive) reshaped to (2, 3, 4)
arange_3d_reshaped = np.arange(24).reshape(2, 3, 4)
print(arange_3d_reshaped)


#📚 8. np.linspace(start, stop, num_of_values)
#Creates an array of evenly spaced values over a specified interval.
#Unlike arange()  The ending value is included.

linspace_1d = np.linspace(0, 10, 5)  # 5 evenly spaced values from 0 to 10
print(linspace_1d)
print(linspace_1d.dtype)  # Output: float64 (default data type for linspace)

linspace_2d = np.linspace(1, 5, 9).reshape(3, 3)  # 9 evenly spaced values from 1 to 5 reshaped to (3, 3)
print(linspace_2d)

linspace_1d_negative = np.linspace(10, 0, 5)  # 5 evenly spaced values from 10 to 0
print(linspace_1d_negative)

"""arange()

"I know the gap between values."

Example:

0, 5, 10, 15, 20

Gap = 5.

linspace()

"I know how many values I want."

Example:

Start = 0
End = 20
Need 5 numbers

NumPy calculates the spacing automatically."""

