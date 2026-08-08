#Apply rotation, scaling, and shearing to a unit square (corners at [0,0], [1,0], [1,1], [0,1]). 
# Print the transformed corners for each. Verify that rotation preserves distances between corners.
import numpy as np
corner = np.array([[0, 0],
                   [1, 0],
                   [1, 1],
                   [0, 1]])
R = np.array([[np.cos(np.pi/2), -np.sin(np.pi/2)],
              [np.sin(np.pi/2), np.cos(np.pi/2)]])
S = np.array([[2, 0], [0, 2]])
H = np.array([[1, 1], [0, 1]])

print("Original corners:\n", corner)
rotated_corners = corner @ R.T
scaled_corners = corner @ S.T
sheared_corners = corner @ H.T

print("Rotated corners:\n", rotated_corners)
print("Scaled corners:\n", scaled_corners)
print("Sheared corners:\n", sheared_corners)

#verify that rotation preserves distances between corners
import math

def distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2
    )
def verify_distances(corners):
    return [
        distance(corners[i], corners[j])
        for i in range(len(corners)) 
        for j in range(i + 1, len(corners))
    ]
 
original_distances = verify_distances(corner)
rotated_distances = verify_distances(rotated_corners)

print("Original distances:", original_distances)
print("Rotated distances:", rotated_distances)

#--------------------------------------------------------------

#Create a composition of three transformations (rotate 30 degrees, scale by [1.5, 0.8], shear with kx=0.3) 
# and apply it to 8 points arranged in a circle. Print before and after coordinates. 
# Compute the determinant of the composed matrix and verify it equals the product of the individual determinants.

point = np.array([[np.cos(theta), np.sin(theta)] for theta in np.linspace(0, 2 * np.pi, 8, endpoint=False)]) # what this does is create 8 points on a unit circle in the xy-plane. Each point is represented as a 2D vector [x, y], where x = cos(theta) and y = sin(theta). The np.linspace function generates 8 evenly spaced angles between 0 and 2π (not including 2π), which correspond to the angles of the points on the circle. The resulting array 'point' contains the coordinates of these 8 points.

print("Original points:\n", point)
R = np.array([[np.cos(np.pi/6), -np.sin(np.pi/6)],
              [np.sin(np.pi/6), np.cos(np.pi/6)]])
S = np.array([[1.5, 0], [0, 0.8]])
H = np.array([[1, 0.3], [0, 1]])

composed_matrix = H @ S @ R

print ("Composed transformation matrix:\n", composed_matrix)

transformed_points = point @ composed_matrix 

print("Transformed points:\n", transformed_points)

# Compute determinants
det_composed = np.linalg.det(composed_matrix)
det_individual = np.linalg.det(H) * np.linalg.det(S) * np.linalg.det(R)

print("Determinant of composed matrix:", det_composed)
print("Product of individual determinants:", det_individual)

#---------------------------------------------------------
#Find the eigenvalues of the matrix [[4, 2], [1, 3]] by hand using the characteristic equation. 
# Then verify with your from-scratch function or  with NumPy.

M = np.array([[4, 2], [1, 3]])
# Characteristic polynomial: det(M - λI) = 0
#by hand Let's compute the characteristic polynomial:
# det([[4-λ, 2], [1, 3-λ]]) = (4-λ)(3-λ) - (2)(1) = 12 - 4λ - 3λ + λ² - 2 = λ² - 7λ + 10
# So the characteristic polynomial is λ² - 7λ + 10 = 0
# Factoring: (λ - 5)(λ - 2) = 0
# Therefore, the eigenvalues are λ = 5 and λ = 2.

# For Eigenvectors, we can solve (M - λI)v = 0 for each eigenvalue.


# For λ = 5:
# (M - 5I)v = 0
# [[4-5, 2], [1, 3-5]]v = 0
# [[-1, 2], [1, -2]]v = 0
# This gives us the system of equations:
# -v1 + 2v2 = 0
# v1 - 2v2 = 0
# From the first equation: v1 = 2v2
# So an eigenvector for λ = 5 is [2, 1] (or any scalar multiple).


# For λ = 2:
# (M - 2I)v = 0
# [[4-2, 2], [1, 3-2]]v = 0
# [[2, 2], [1, 1]]v = 0
# This gives us the system of equations:
# 2v1 + 2v2 = 0
# v1 + v2 = 0
# From the first equation: v1 = -v2
# So an eigenvector for λ = 2 is [1, -1] (or any scalar multiple).



Eigenvalues = np.linalg.eigvals(M)
print("Eigenvalues of M:", Eigenvalues) # Should be [5, 2]

Eigenvectors = np.linalg.eig(M)[1]
print("Eigenvectors of M:\n", Eigenvectors) # values corresponding to eigenvalues 5 and 2 is [[0.89442719 0.4472136 ], [0.4472136 0.89442719]]
#---------------------------------------------

