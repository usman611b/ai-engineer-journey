#📚 Lesson 8 — Linear Independence

"""This is one of the most important concepts in Machine Learning because it explains:

Why redundant features hurt models.
Why multicollinearity happens.
Why PCA removes dimensions.
Why LoRA uses low-rank matrices.
Why some matrices cannot be inverted."""

"""🧠 One Sentence Intuition

A set of vectors is linearly independent if every vector contributes new information.

Or even simpler:

Every vector should teach us something new."""

"""Let's Forget Mathematics First

Imagine you have three books.

Book 1
Python Programming
Book 2
Machine Learning
Book 3
Deep Learning

Each teaches something different.

These books are

Independent

because removing one loses information.

Now another example.

Book 1

Python Programming

Book 2

Python Programming

Book 3

Python Programming

Do you learn anything new from Book 2?

❌ No.

Book 3?

❌ No.

Only one book was enough.

This is dependence."""

#Ai Anology:
"""Suppose your dataset has these features.

Age

Height

Weight

Nice.

Every feature gives new information.

Now someone adds

Height in Inches

But

Height in Inches

=

Height in Centimeters / 2.54

Is this new information?

❌ No.

It's exactly the same information.

The model already knows height.

This feature is

Linearly Dependent"""

#Mathematical Definition

#No vector can be written as a combination of the other vectors.
"""Vectors are linearly independent if no vector in the set can be written as a combination of the others. 
If v1, v2, v3 are independent, they span a 3D space. If one is a combination of the others, they only span a plane.

Why it matters for AI: your feature matrix should have linearly independent columns. If two features are perfectly correlated (linearly dependent), 
the model cannot distinguish their effects. This causes multicollinearity in regression -- the weight matrix becomes unstable, and small input changes produce wild output swings.

Concrete example:

v1 = [1, 0, 0] linearly independent
v2 = [0, 1, 0] linearly independent
v3 = [2, 1, 0]   # v3 = 2*v1 + v2  linearly dependent on v1 and v2

v1 and v2 are independent -- neither is a scalar multiple or combination of the other. But v3 = 2*v1 + v2, so {v1, v2, v3} is a dependent set. 
These three vectors all lie in the xy-plane. No matter how you combine them, you cannot reach [0, 0, 1]. You have three vectors but only two dimensions of freedom.

In a dataset: if feature_3 = 2*feature_1 + feature_2, adding feature_3 gives the model zero new information. 
Worse, it makes the normal equations singular -- there is no unique solution for the weights.


"""

#What does "Combination" mean?
"""
Combination simply means : 

Multiply

+

Add

Example

v₁ = [1,0]

v₂ = [0,1]

Can we make

[1,1]

using them?

Yes.

1×v₁ + 1×v₂ = [1,1]

We just created a new vector."""

#Example 2

A = [1,0]
B = [2,0]

"""
By Row reduction, we can see that B is just 2×A. So they are linearly dependent.
If we have a dataset with two features, A and B, and B is just 2× A, then the model cannot distinguish their effects. The weight matrix becomes singular, and small input changes produce wild output swings. This is multicollinearity.

"""

"""We can simply calculate the Linearly independency by Row Reduction  After solving the matrix, if we have a row of zeros, then the columns are linearly dependent. If we have no rows of zeros, then the columns are linearly independent.
if the rank of the matrix is equal to the number of columns, then the columns are linearly independent. If the rank is less than the number of columns, then there is linear dependence.
"""

# Code Implementation
import numpy as np

A = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

rank = np.linalg.matrix_rank(A) # This function computes the rank of the matrix A, 
#which is the maximum number of linearly independent column vectors in the matrix. 
# The rank is a measure of the "non-degenerateness" of the system of linear equations represented by the matrix. 
# If the rank is equal to the number of columns, it indicates that all columns are linearly independent. 
# If the rank is less than the number of columns, it indicates that there is linear dependence among the columns.

print("Rank:", rank)
print("Number of vectors:", A.shape[1])

if rank == A.shape[1]:
    print("✅ Linearly Independent")
else:
    print("❌ Linearly Dependent")
