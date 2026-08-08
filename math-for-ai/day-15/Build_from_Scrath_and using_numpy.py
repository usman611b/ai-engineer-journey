
import math 
#Matrix Transformation Functions from Scratch

def rotation_matrix(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    
    return [[c, -s], 
            [s, c]]

def scaling_matrix(sx, sy):
    return [[sx, 0], 
            [0, sy]]

def Sheering_matrix(shx, shy):
    return [[1, shx], 
            [shy, 1]]

def reflection_matrix(axis='x'):
    if axis == 'x':
        return [[1, 0], 
                [0, -1]]
    elif axis == 'y':
        return [[-1, 0], 
                [0, 1]]
    else:
        raise ValueError("Axis must be 'x' or 'y'.")

def vec_matmul(matrix , vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]

def mat_mul(a , b):
    row_a = len(a)
    col_b = len(b[0])
    col_a = len(a[0])

    return[
        [sum(a[i][k] * b[k][j] for k in range(col_a)) for j in range(col_b)]
        for i in range(row_a)
    ]


R = reflection_matrix('x')  # Reflect across the x-axis
print("Reflection Matrix (X-axis):")
for row in R:
    print(row)

R = reflection_matrix('y')  # Reflect across the y-axis
print("Reflection Matrix (Y-axis):")
for row in R:
    print(row)


S = scaling_matrix(2, 3)  # Scale x by 2 and y by 3
print("Scaling Matrix:")
for row in S:
    print(row)

H = Sheering_matrix(0.5, 0.5)  # Shear x by 0.5 and y by 0.5
print("Shearing Matrix:")
for row in H:
    print(row)

R = rotation_matrix(math.pi / 2 )  # 90 degrees in radians
R_180 = rotation_matrix(math.pi) # 180 degree in radian
print("Rotation Matrix for 90 degrees:")
for row in R:
    print(row)

Point = [1.0 , 0.0]
rotated = vec_matmul(R , Point)
print("Rotated matrix [1.0 , 0.0 ] : into " , rotated)

rotated_180 = vec_matmul(R_180 , Point)
print("Rotated matrix [1.0 , 0.0 ] : into " , rotated_180)

scaled = vec_matmul(S , [1.0 , 1.0] )
print("Scaling (1,1) by (2 ,3 ) to  : ",  scaled) 

sheared = vec_matmul(Sheering_matrix(1 , 0 ) ,[1.0,1.0] )
print("Shearing  (1,1) by (1, 0) where kx = 1 to : " ,sheared)

sheared = vec_matmul(Sheering_matrix(0 , 1 ) ,[1.0,1.0] )
print("Shearing (1,1) by (0, 1) where ky = 1 to : " ,sheared)

reflection = vec_matmul(reflection_matrix('x') , [1.0 ,1.0] )
print("Reflection (1,1) along x axis " , reflection)

reflection = vec_matmul(reflection_matrix('y') , [1.0 ,1.0] )
print("Reflection (1,1) along y axis " , reflection)

#Composition of Transformations
#Example: Rotate 90 degrees and then scale by (2,3)

R = rotation_matrix(math.pi / 2)  # 90 degrees in radians
S = scaling_matrix(2, 3)  # Scale x by 2 and y by 3

# First rotate, then scale
rotate_then_scale = mat_mul(S, R)
scale_then_rotate = mat_mul(R, S)

result1 = vec_matmul(rotate_then_scale, [1.0, 0.0])
result2 = vec_matmul(scale_then_rotate, [1.0, 0.0])

print("Result of rotating then scaling (1,0):", result1)
print("Result of scaling then rotating (1,0):", result2)
print(f"Are the two results equal? {result1 == result2}")


#-------------------------------------------------
#Now by using numpy
import numpy as np
thetha = np.pi / 2  # 90 degrees in radians
R = np.array([[np.cos(thetha), -np.sin(thetha)],
                [np.sin(thetha), np.cos(thetha)]])
Rotated = R @ np.array([1.0, 0.0])
print("Rotated matrix [1.0 , 0.0 ] : into " , Rotated)

Scaling = np.array([[2, 0],
                    [0, 3]])
Scaled = Scaling @ np.array([1.0, 1.0])
print("Scaled matrix [1.0 , 1.0 ] : into " , Scaled)

Reflection = np.array([[1, 0],
                       [0, -1]])
print("Reflection matrix [1.0 , 1.0 ] : into " , Reflection @ np.array([1.0, 1.0]))

Sheering = np.array([[1, 1],
                     [0, 1]])
print("Sheering matrix [1.0 , 1.0 ] : into " , Sheering @ np.array([1.0, 1.0]))

#Composition of Transformations using numpy
#Example: Rotate 90 degrees and then scale by (2,3)
R = np.array([[np.cos(thetha), -np.sin(thetha)],
                [np.sin(thetha), np.cos(thetha)]])
S = np.array([[2, 0],
              [0, 3]])
rotate_then_scale = S @ R
scale_then_rotate = R @ S
result1 = rotate_then_scale @ np.array([1.0, 0.0])
result2 = scale_then_rotate @ np.array([1.0, 0.0])

print("Result of rotating then scaling (1,0):", result1)
print("Result of scaling then rotating (1,0):", result2)
print(f"Are the two results equal? {np.allclose(result1, result2)}")

#-------------------------------------------------
