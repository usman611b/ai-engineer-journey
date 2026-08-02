"""Vectors, Matrices & Operations
Every neural network is just matrix multiplication with extra steps.

Type: Build Languages: Python, Julia Prerequisites: Phase 1, Lesson 01 (Linear Algebra Intuition) Time: ~60 minutes

Learning Objectives
Build a Matrix class with element-wise operations, matrix multiplication, transpose, determinant, and inverse
Distinguish element-wise multiplication from matrix multiplication and explain when each applies
Implement a single dense neural network layer (relu(W @ x + b)) using only the from-scratch Matrix class
Explain broadcasting rules and how bias addition works in neural network frameworks
The Problem
You want to build a neural network. You read the code and see this:

output = activation(weights @ input + bias)

That @ is matrix multiplication. The weights are a matrix. The input is a vector. If you do not know what those operations do, this line is magic. 
If you do know, it is the entire forward pass of a layer in three operations.

Every image your model processes is a matrix of pixel values. Every word embedding is a vector. 
Every layer of every neural network is a matrix transformation. 
You cannot build AI systems without being fluent in matrix operations the same way you cannot write code without understanding variables.

This lesson builds that fluency from scratch.

The Concept
Vectors: ordered lists of numbers
A vector is a list of numbers with a direction and magnitude. In AI, vectors represent data points, features, or parameters.

v = [3, 4]        -- a 2D vector
w = [1, 0, -2]    -- a 3D vector
A 2D vector [3, 4] points to coordinates (3, 4) on a plane. Its length (magnitude) is 5 (the 3-4-5 triangle).

Matrices: grids of numbers
A matrix is a 2D grid. Rows and columns. An m x n matrix has m rows and n columns.

A = | 1  2  3 |     -- 2x3 matrix (2 rows, 3 columns)
    | 4  5  6 |
In neural networks, weight matrices transform input vectors into output vectors. A layer with 784 inputs and 128 outputs uses a 128x784 weight matrix.

Why shapes matter
Matrix multiplication has a strict rule: (m x n) @ (n x p) = (m x p). The inner dimensions must match.

(128 x 784) @ (784 x 1) = (128 x 1)
  weights       input       output

Inner dimensions: 784 = 784  -- valid
If you get a shape mismatch error in PyTorch, this is why.

The operations map:
-----------------------------------------------------------------------
Operation	        What it does	        Neural network use
---------------------------------------------------------------------------
Addition	        Element-wise combine	Adding bias to output
Scalar multiply	    Scale every element	    Learning rate * gradients
Matrix multiply	    Transform vectors	    Layer forward pass
Transpose	        Flip rows and columns	Backpropagation
Determinant	        Single number summary   Checking invertibility
Inverse	            Undo a transformation	 Solving linear systems
Identity	        Do-nothing matrix	     Initialization, residual connections


Element-wise vs matrix multiplication:
This distinction trips up beginners constantly.

Element-wise: multiply matching positions. Both matrices must be the same shape.

| 1  2 |   | 5  6 |   | 5  12 |
| 3  4 | * | 7  8 | = | 21 32 |
Matrix multiplication: dot products of rows and columns. Inner dimensions must match.

| 1  2 |   | 5  6 |   | 1*5+2*7  1*6+2*8 |   | 19  22 |
| 3  4 | @ | 7  8 | = | 3*5+4*7  3*6+4*8 | = | 43  50 |
Different operations, different results, different rules.

Broadcasting
When you add a bias vector to a matrix of outputs, the shapes do not match. Broadcasting stretches the smaller array to fit.

| 1  2  3 |   +   [10, 20, 30]
| 4  5  6 |

Broadcasting stretches the vector across rows:

| 1  2  3 |   | 10  20  30 |   | 11  22  33 |
| 4  5  6 | + | 10  20  30 | = | 14  25  36 |
Every modern framework does this automatically. Understanding it prevents confusion when shapes seem wrong but the code runs.

vector-projection

"""
class Matrix:
    def __init__(self , data):
        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0]) if self.data else 0
        self.shape = (self.rows , self.cols)

    def __repr__(self):
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix({self.shape}):\n  {rows_str}"

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def scalar_multiply(self, scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def elementwise_multiply(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        return Matrix([
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def matmul(self , other):
        if self.cols != other.rows:
            raise ValueError("Incompatible matrix dimensions")
        return Matrix([
            
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            
            for i in range(self.rows)
        ])
    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

#how it Works :

A = Matrix([[1, 2, 3], [4, 5, 6]])
B = Matrix([[7, 8, 9], [10, 11, 12]])
C = Matrix([[1, 2],[3, 4],[5 , 6]])
added_matrix = A + B
print(added_matrix)  # Output: Matrix((2, 3)):  
print(A)
print(B)
print(C)
matrix_mul = A.matmul(C)
print(matrix_mul)
print(A.transpose())


#Connect to neural networks
import random
import random

inputs = Matrix([[0.5], [0.8], [0.2]])
weights = Matrix([
    [random.uniform(-1, 1) for _ in range(3)]
    for _ in range(2)
])
bias = Matrix([[0.1], [0.1]])

def relu_matrix(m):
    return Matrix([[max(0, val) for val in row] for row in m.data])

pre_activation = weights.matmul(inputs) + bias
output = relu_matrix(pre_activation)

print(f"Input shape: {inputs.shape}")
print(f"Weight shape: {weights.shape}")
print(f"Output shape: {output.shape}")
print(f"Output: {output.data}")

#This is a single dense layer: output = relu(W @ x + b). Every dense layer in every neural network does exactly this.

#Now we can use it by Numpy
#NumPy does everything above in fewer lines and orders of magnitude faster.

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A + B =\n", A + B)
print("A * B (element-wise) =\n", A * B)
print("A @ B (matrix multiply) =\n", A @ B)
print("A^T =\n", A.T)
print("det(A) =", np.linalg.det(A))
print("A^-1 =\n", np.linalg.inv(A))
print("I =\n", np.eye(2))

inputs = np.random.randn(3, 1)
weights = np.random.randn(2, 3)
bias = np.array([[0.1], [0.1]])
output = np.maximum(0, weights @ inputs + bias)

print(f"\nNeural network layer: {weights.shape} @ {inputs.shape} = {output.shape}")
print(f"Output:\n{output}")


#Broadcasting in NumPy:

matrix = np.array([[1, 2, 3], [4, 5, 6]])
bias = np.array([10, 20, 30])
print(matrix + bias)

"""NumPy automatically broadcasts the 1D bias across both rows. This is how bias addition works in every neural network framework."""

"""Key Terms

Term	            What people say	                                     What it actually means
-------------------------------------------------------------------------------------------------------------------------------------------------------
Vector	            "An arrow"	An ordered list of numbers.             In AI: a point in high-dimensional space.

Matrix	            "A table of numbers"	                            A linear transformation. It maps vectors from one space to another.

Matrix multiply	    "Just multiply the numbers"	                        Dot products between every row of the first matrix and every column of the second. Order matters.

Transpose	        "Flip it"	                                        Swap rows and columns. Turns an m x n matrix into n x m. Critical in backpropagation.

Determinant	        "Some number from the matrix"	                    Measures how much the matrix scales area (2D) or volume (3D). Zero means the transformation crushes a dimension.

Inverse	            "Undo the matrix"	                                The matrix that reverses the transformation. Only exists when the determinant is not zero.

Identity matrix	    "The boring matrix"	                                The matrix equivalent of multiplying by 1. Used in residual connections (ResNets).

Broadcasting	    "Magic shape fixing"	                            Stretching a smaller array to match a larger one by repeating along missing dimensions.

Element-wise	    "Regular multiplication"	                        Multiply matching positions. Both arrays must have the same shape (or be broadcastable)."""