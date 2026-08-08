# ============================================================
# Lesson 3 - Part 8 - Eigenvalues & Eigenvectors
# ============================================================

"""
EIGENVECTOR

An eigenvector is a special non-zero vector whose direction
does not change after a matrix transformation.

The vector may:

- become longer
- become shorter
- flip direction (negative eigenvalue)

But it always stays on the same line.

--------------------------------------------------

EIGENVALUE

The eigenvalue tells us how much the eigenvector
is stretched or compressed.

Example

Eigenvalue = 2

↓

The eigenvector becomes twice as long.

-----------------------------------

Eigenvalue = 0.5

↓

The eigenvector shrinks to half its length.

-----------------------------------

Eigenvalue = -3

↓

The eigenvector becomes three times longer
and flips direction.

--------------------------------------------------

Fundamental Equation

Av = λv

Meaning

Transformation of the vector

=

Scaling of the same vector

--------------------------------------------------

Interpretation

Eigenvector

↓

Special direction that survives the transformation.

Eigenvalue

↓

Stretch / shrink factor along that direction.
"""
#Finding Eigenvalues and Eigenvectors
import numpy as np

M = np.array([[2, 1], [1, 2]], dtype=float)
eigenvalues, eigenvectors = np.linalg.eig(M)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
 # What this means is that if you multiply the matrix M by an eigenvector, 
 # the result will be the same as multiplying the eigenvalue by that eigenvector. 
 # Let's verify this property for each eigenvalue and its corresponding eigenvector.
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    print(f"  M @ v{i} = {M @ v}, lambda * v{i} = {lam * v}")
