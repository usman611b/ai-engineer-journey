
import numpy as np
#🧮 NumPy Linear Algebra (np.linalg)

"""We'll cover:

✅ Determinant
✅ Inverse
✅ Transpose (Quick Review)
✅ Norm
✅ Trace"""

# 1. Determinant
#The determinant is a single number calculated from a square matrix.

arr = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(arr)    
print("Determinant:", determinant)  # ..Output: Determinant: -2.0

#Visually, it looks like this:
# Original Matrix   
# [[1, 2],
#  [3, 4]]
# Determinant = (1*4) - (2*3) = 4 - 6 = -2.0


arr2 = np.array([[2, 5], [1, 3]])
determinant2 = np.linalg.det(arr2)
print("Determinant:", determinant2)  # Output: Determinant: 1.0

arr3 = np.array([[12, 20, 23], [12, 13, 4], [5, 6, 10]])
determinant3 = np.linalg.det(arr3)
print("Determinant:", determinant3)  # Output: Determinant: -566.999999

#Visually, it looks like this:
# Original Matrix
# [[12, 20, 23],
#  [12, 13, 4],
#  [5, 6, 10]]

# Determinant = 12*(13*10 - 4*6) - 20*(12*10 - 4*5) + 23*(12*6 - 13*5)
# = 12*(130 - 24) - 20*(120 - 20) + 23*(72 - 65)
# = 12*106 - 20*100 + 23* 7
# = 1272 - 2000 + 161
# = -728 + 161
# = -567 (approximately -566.999999)


#2. Inverse
#The inverse of a matrix is a matrix that, when multiplied with the original matrix, yields the identity matrix.

arr = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(arr)
print("Inverse:\n", inverse)

#Visually, it looks like this:
# Original Matrix
# [[1, 2],
#  [3, 4]]

#Calculating the inverse using the formula for a 2x2 matrix:
# If A = [[a, b], [c, d]], then A^(-1) = (1/det(A)) * [[d, -b], [-c, a]]
# For our matrix, a=1, b=2, c=3, d=4, and det(A) = -2.0
# So, A^(-1) = (1/-2) * [[4, -2], [-3, 1]] = [[-2.0, 1.0], [1.5, -0.5]] 
# Inverse Matrix
# [[-2. ,  1. ],
#  [ 1.5, -0.5]]


print("Product of matrix and its inverse:\n", arr @ np.linalg.inv(arr)) #Verifying that the product of a matrix and its inverse yields the identity matrix.

arr3 = np.array([[12, 20, 23], [12, 13, 4], [5, 6, 10]])
inverse3 = np.linalg.inv(arr3)
print("Inverse:\n", inverse3)
print("Product of matrix and its inverse:\n", arr3 @ np.linalg.inv(arr3)) #Verifying that the product of a matrix and its inverse yields the identity matrix.


#3. Transpose
#The transpose of a matrix is obtained by flipping it over its diagonal, which means that the row and column indices are swapped.

#Visually, it looks like this:
# Original Matrix
# [[1, 2],
#  [3, 4]]
# Transpose Matrix
# [[1, 3],
#  [2, 4]]

arr = np.array([[1, 2], [3, 4]])
transpose = np.transpose(arr)
print("Transpose:\n", transpose)

arr3 = np.array([[12, 20, 23], [12, 13, 4], [5, 6, 10]])
transpose3 = np.transpose(arr3)
print("Transpose:\n", transpose3)


#4. Norm
#The norm of a matrix is a measure of its size or length. The most common norm is the Frobenius norm, which is the square root of the sum of the absolute squares of its elements.
#Norm a function that measures the length, size, or magnitude of a vector

arr = np.array([[1, 2], [3, 4]])
norm = np.linalg.norm(arr)
print("Norm:", norm)  # Output: Norm: 5.477225575051661

#Visually, it looks like this:
# norm = sqrt(1^2 + 2^2 + 3^2 + 4^2) = sqrt(1 + 4 + 9 + 16) = sqrt(30) ≈ 5.477225575051661


arr3 = np.array([[12, 20, 23], [12, 13, 4], [5, 6, 10]])
norm3 = np.linalg.norm(arr3)
print("Norm:", norm3)  # Output: Norm: 43.01162845532537

#Visually, it looks like this:  
# norm = sqrt(12^2 + 20^2 + 23^2 + 12^2 + 13^2 + 4^2 + 5^2 + 6^2 + 10^2)    
#= sqrt(144 + 400 + 529 + 144 + 169 + 16 + 25 + 36 + 100)
#= sqrt(1563) ≈ 43.01162845532537


#5. Trace
#The trace of a matrix is the sum of its diagonal elements.

arr = np.array([[1, 2], [3, 4]])
trace = np.trace(arr)
print("Trace:", trace)  # Output: Trace: 5

#Visually, it looks like this:
# Original Matrix
# [[1, 2],
#  [3, 4]]
# Trace = 1 + 4 = 5

arr3 = np.array([[12, 20, 23], [12, 13, 4], [5, 6, 10]])
trace3 = np.trace(arr3)
print("Trace:", trace3)  # Output: Trace: 35

#Visually, it looks like this:
# Original Matrix
# [[12, 20, 23],
#  [12, 13, 4],
#  [5, 6, 10]]
# Trace = 12 + 13 + 10 = 35


#Example of using multiple linear algebra operations together:
arr = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(arr)
transpose = np.transpose(arr)
norm = np.linalg.norm(arr)
trace = np.trace(arr)

print("Original Matrix:\n", arr)
print("Inverse:\n", inverse)
print("Transpose:\n", transpose)
print("Norm:", norm)
print("Trace:", trace)

#Example of using multiple linear algebra operations together on a 3x3 matrix:::
arr3 = np.array([[12, 20, 23], [12, 13, 4], [5, 6, 10]])
inverse3 = np.linalg.inv(arr3)
transpose3 = np.transpose(arr3)
norm3 = np.linalg.norm(arr3)
trace3 = np.trace(arr3)

print("Original Matrix:\n", arr3)
print("Inverse:\n", inverse3)
print("Transpose:\n", transpose3)
print("Norm:", norm3)
print("Trace:", trace3)
