#Determinant of a Matrix:
"""


Meaning
--------
Measures how much a matrix scales area (2D) or volume (3D).

The determinant tells whether a matrix is invertible. 
If the determinant is zero, the matrix is singular, 
meaning features are linearly dependent 
and some algorithms like the normal equation cannot compute a unique solution.

Interpretation
--------------
det > 0  -> Area/volume increases, orientation preserved.
det < 0  -> Area/volume increases, orientation flipped.
det = 0  -> Matrix collapses space (singular).

Important Property
------------------
det(A)=0
→ Matrix is NOT invertible.
→ Rows/Columns are linearly dependent.

det(A)≠0
→ Matrix is invertible.
→ Rows/Columns are linearly independent.

NumPy
------
np.linalg.det(A)

AI Uses
-------
- Check invertibility
- Linear Regression (Normal Equation)
- Feature redundancy
- Numerical stability"""
import numpy as np
#WE can compute the determinant of a matrix using NumPy's `np.linalg.det()` function. This is particularly useful in AI applications where we need to check if a matrix is invertible, which is crucial for solving systems of equations, such as in linear regression using the normal equation.
Matrix_A = np.array([[1, 2], [3, 4]])
det_A = np.linalg.det(Matrix_A)
print(f"Determinant of Matrix A: {det_A}")#Output: Determinant of Matrix A: -2.0 here the determinant is negative, indicating that the area is scaled and the orientation is flipped.

Matrix_B = np.array([[2, 3], [1, 4]])
det_B = np.linalg.det(Matrix_B)
print(f"Determinant of Matrix B: {det_B}") #Output: Determinant of Matrix B: 5.0 here the determinant is positive, indicating that the area is scaled and the orientation is preserved.

#--------------------------------------------------

#Inverse Matrix:

"""
Meaning
--------
The inverse of a matrix is a matrix that, when multiplied by the original matrix, results in the identity matrix. Not all matrices have an inverse; only square matrices with a non-zero determinant are invertible.
The inverse undoes the transformation of a matrix.

Property
--------
A(original matrix) × A⁻¹(inverse matrix) = I(identity matrix)

Identity Matrix
---------------
[[1,0],
 [0,1]]

----------------
Interpretation
--------------
If a matrix has an inverse, it means the matrix is invertible and the system of equations it represents has a unique solution.

Inverse Exists When
-------------------
det(A) ≠ 0

No Inverse When
---------------
det(A) = 0

---------------

Important Property
------------------
A matrix is invertible if and only if its determinant is non-zero.

NumPy
------
np.linalg.inv(A)

AI Uses
-------
- Solving systems of linear equations
- Computing least squares solutions
- Regularization in machine learning
"""


#Computing the inverse of a matrix using NumPy's `np.linalg.inv()` function. This is particularly useful in AI applications where we need to solve systems of linear equations or compute least squares solutions.
Matrix_C = np.array([[1, 2], [3, 4]])
inv_C = np.linalg.inv(Matrix_C)
print(f"Inverse of Matrix C:\n{inv_C}")

Matrix_D = np.array([[1, 2], [2, 4]])
inv_D = np.linalg.inv(Matrix_D)
print(f"Inverse of Matrix D:\n{inv_D}") #Output: LinAlgError: Singular matrix here the matrix is singular (determinant is zero), indicating that it does not have an inverse.
