#📚 Session 3 – Building Our Own Vector Class
class Vector:
    def __init__(self , coordinates):
        self.coordinates = list(coordinates)
        self.dimension = len(coordinates)

    def __add__(self, other): # it is a special method that is used to define the behavior of the addition operator (+) for objects of the class. When you use the + operator between two instances of the Vector class, this method is called to perform the addition.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])
    def __sub__(self, other): # it is a special method that is used to define the behavior of the subtraction operator (-) for objects of the class. When you use the - operator between two instances of the Vector class, this method is called to perform the subtraction.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])
    def dot(self, other): # it is a method that calculates the dot product of two vectors. The dot product is a mathematical operation that takes two equal-length sequences of numbers (vectors) and returns a single number. It is calculated by multiplying corresponding elements of the vectors and summing the results.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))
    def magnitude(self): # it is a method that calculates the magnitude (or length) of the vector. The magnitude of a vector is a measure of how long the vector is, and it is calculated using the Pythagorean theorem. For a vector with coordinates (x1, x2, ..., xn), the magnitude is given by the square root of the sum of the squares of its components.
        return sum(a ** 2 for a in self.coordinates) ** 0.5
    def normalize(self): # it is a method that returns a unit vector in the same direction as the original vector. A unit vector has a magnitude of 1. To normalize a vector, you divide each of its components by its magnitude. This method first calculates the magnitude of the vector and then creates a new Vector instance with the normalized coordinates.
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize the zero vector.")
        return Vector([a / mag for a in self.coordinates])
    def cosine_similarity(self, other): # it is a method that calculates the cosine similarity between two vectors. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space. It is defined as the cosine of the angle between the two vectors, which can be computed using the dot product and the magnitudes of the vectors.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for cosine similarity.")
        return self.dot(other) / (self.magnitude() * other.magnitude())
    def __repr__(self): # it is a special method that is used to define how an object should be represented as a string. When you print an object or use the repr() function on it, this method is called to get the string representation of the object.
        return f"Vector({self.coordinates})"
    
v = Vector([6 , 8])
v2 = Vector([4, 5])
print(v.dimension)    # Output: 2
print(type(v))  # Output: <class '__main__.Vector'>
print(v) # Output: Vector([6, 8])
print(v2) # Output: Vector([4, 5])

print(v.dot(v2))  # Output: 64
print(v.magnitude())  # Output: 10.0
print(v.normalize())  # Output: Vector([0.6, 0.8])
print(v + v2)  # Output: Vector([10, 13])
print(v - v2)  # Output: Vector([2, 3])
print(v.cosine_similarity(v2))  # Output: 0.96

class Matrix:
    def __init__(self, rows):
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))
#This runs a matrix-vector multiplication, where each element of the resulting vector is computed as the dot product of the corresponding row of the matrix and the vector.
    def __matmul__(self, other): #
        if isinstance(other, Vector):
            return Vector([
                sum(self.rows[i][j] * other.coordinates[j] for j in range(self.shape[1]))
                for i in range(self.shape[0])
            ]) 
#this method first checks if the other object is an instance of the Vector class. If it is, it performs matrix-vector multiplication. If the other object is an instance of the Matrix class, it performs matrix-matrix multiplication. The resulting matrix is constructed by calculating the dot product of each row of the first matrix with each column of the second matrix.
        rows = []
        for i in range(self.shape[0]):
            row = []
            for j in range(other.shape[1]):
                row.append(sum(
                    self.rows[i][k] * other.rows[k][j]
                    for k in range(self.shape[1])
                ))
            rows.append(row)
        return Matrix(rows)

    def transpose(self):
        return Matrix([
            [self.rows[j][i] for j in range(self.shape[0])]
            for i in range(self.shape[1])
        ])

    def __repr__(self):
        return f"Matrix({self.rows})"


rotation_90 = Matrix([[0, -1], [1, 0]])
rotation_180 = Matrix([[-1, 0], [0, -1]])
rotation_270 = Matrix([[0, 1], [-1, 0]])
rotation_360 = Matrix([[1, 0], [0, 1]])
point = Vector([7, 5])

matrix = Matrix([[1, 2], [3, 4]])
rotated_90 = rotation_90 @ matrix
rotated_180 = rotation_180 @ matrix
rotated_270 = rotation_270 @ matrix
rotated_360 = rotation_360 @ matrix
print(f"Original Matrix: {matrix}")
print(f"Transpose of matrix {matrix}: {matrix.transpose()}")
print(f"Rotated 90°: {rotated_90}")

rotated_90 = rotation_90 @ point
rotated_180 = rotation_180 @ point
rotated_270 = rotation_270 @ point
rotated_360 = rotation_360 @ point
print(f"Original: {point}")
print(f"Rotated 90°: {rotated_90}")
print(f"Rotated 180°: {rotated_180}")
print(f"Rotated 270°: {rotated_270}")
print(f"Rotated 360°: {rotated_360}")




# now all these by using Numpy  Library 

import numpy as np

matrix_a = np.array([[0 , -1], [1, 0]])
vector_b = np.array([5, 6])

result = matrix_a @ vector_b
print(f"Result of matrix-vector multiplication: {result}")  # Output: [6, 5]


matrix_c = np.array([[4 , 7], [9 , 4]])
result = matrix_a @ matrix_c

print(f"Result of matrix-matrix multiplication: {result}")

#Transpose of a matrix
matrix_d = np.array([[1, 2], [3, 4]])
print(f"Original Matrix: {matrix_d}")
transposed_matrix = np.transpose(matrix_d)
print(f"Transposed Matrix: {transposed_matrix}")


#-------------------------------------------------

import random

random.seed(42)
weights = Matrix([[random.gauss(0, 0.1) for _ in range(3)] for _ in range(2)])
input_vector = Vector([1.0, 0.5, -0.3])

output = weights @ input_vector
print(f"Input (3D): {input_vector}")
print(f"Output (2D): {output}")
print("This is what a neural network layer does -- matrix multiplication.")