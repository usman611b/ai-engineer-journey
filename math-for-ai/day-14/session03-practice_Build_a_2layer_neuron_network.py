#Practice:
"""Build a two-layer network. Using only your Matrix class (no NumPy), 
create a two-layer neural network: input (3) -> hidden (4) -> output (2). 
Initialize random weights, run a forward pass,,, , and verify all shapes are correct."""
from session01_Matrix_Operations import Matrix, relu_matrix
import random

inputs = Matrix([[0.5], [0.8], [0.2]])  # Shape: (3, 1)
weights_1 = Matrix([[random.uniform(-1, 1) for _ in range(3)] for _ in range(4)])  # Shape: (4, 3)
bias_1 = Matrix([[random.uniform(-1, 1)] for _ in range(4)])  # Shape: (4, 1)

hidden_pre = weights_1.matmul(inputs) + bias_1  # Shape: (4, 1)
hidden = relu_matrix(hidden_pre)  # Shape: (4, 1)


weights_2 = Matrix([[random.uniform(-1, 1) for _ in range(4)] for _ in range(2)])  # Shape: (2, 4)
bias_2 = Matrix([[random.uniform(-1, 1)] for _ in range(2)])  # Shape: (2, 1)
output_pre = weights_2.matmul(hidden) + bias_2  # Shape: (2, 1)
output = relu_matrix(output_pre)  # Shape: (2, 1)   

print(f"Input shape: {inputs.shape}")
print(f"Hidden layer shape: {hidden.shape}")
print(f"Output shape: {output.shape}")
print(f"Output: {output.data}")

#-----------------------------------------
"""This is what we learned so far and build it apply  it
Neural Netwok whay we buod 
"""
