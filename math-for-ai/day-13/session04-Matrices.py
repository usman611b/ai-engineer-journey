# What is a Matrix?
# A matrix is simply an organized collection of vectors (or numbers) arranged in rows and columns.

#Now Imagine Many Vectors

#Suppose we have

#Student A
[85, 90]
#Student B
[70, 95]
#Student C
[88, 76]

#Instead of storing them separately
student1 = [85,90]
student2 = [70,95]
student3 = [88,76]

#we organize them together.
[
 [85,90],
 [70,95],
 [88,76]
]

#This is a matrix.
"""
Visualize It
        Math   English

A         85      90

B         70      95

C         88      76

Notice something.

Each row is one vector.

Each column represents one feature."""
#Another Example

"""
Suppose

Cat -->> Weight,Height,Age

Represented as [4,30,2]

Dog [15,60,4]

Tiger [220,110,7]

Store them together

[
 [4,30,2],
 [15,60,4],
 [220,110,7]
]

That is another matrix."""

"""So What Is a Matrix?

Think of it like an Excel sheet.

Rows

↓

1 2 3

4 5 6

7 8 9

      →
   Columns

Rows go horizontally.
Columns go vertically."""

#Mathematically, a matrix is represented as:
A = [
 [1,2,3],  
 [4,5,6],
 [7,8,9]
]

#Dimensions of a Matrix

rows = len(A)
cols = len(A[0])
print(f"Rows: {rows}, Columns: {cols}")  # Output: Rows: 3, Columns: 3

shape = (rows, cols)
print(f"Shape: {shape}")  # Output: Shape: (3, 3)

#Accessing Elements in a Matrix
element = A[1][2]  # Accessing the element in the 2nd row and 3rd column (0-indexed)
print(f"Element at row 2, column 3: {element}")  # Output: Element at row 2, column 3: 6

element = A[0][1]  # Accessing the element in the 1st row and 2nd column (0-indexed)
print(f"Element at row 1, column 2: {element}")  # Output  : Element at row 1, column 2: 2

#------------------------------------------------------------------
#Matrices as Transformations
#A matrix is a machine that takes a vector as input and outputs a new transformed vector.
#A matrix is not just numbers.It does something.

"""   INPUT

      [2]
      [1]

        │
        ▼

   +--------------+
   |   MATRIX M   |
   +--------------+

        │
        ▼

      [4]
      [2]
      
      
You put a vector in.

Another vector comes out.

The matrix changed it.
      """
#A Matrix Changes Space
#Suppose you have one point.

"""Suppose you have one point.

y

3|

2|

1|       •

0|__________________

   0 1 2 3

Coordinates

(2,1)

Now apply a matrix.

The point becomes

(4,2)

Now

y

3|

2|              •

1|

0|____________________

   0 1 2 3 4

The point moved."""
"""A matrix doesn't move one point.

It moves every point.

Imagine many points.

Before

•      •

     •

  •

        •

After one matrix

       •

   •

             •

•

                  •

Everything moved together.

The entire space changed.

That's why we call it a transformation."""

#Different Matrices Do Different Jobs
#1️⃣ Scaling
"""Makes vectors longer or shorter.

Before

•

After

        •

Direction stays the same.

Magnitude changes.

"""
#Rotation
"""Rotates vectors around the origin.
Before

        •   
After

    •

Direction changes.
Magnitude stays the same.

"""
#Shearing(stretching)
"""Stretches vectors in a particular direction.
Before

+----+
|    |
|    |
+----+
After

  /----/
 /    /
/----/

Direction changes.
Magnitude changes.  
"""
#reflection
"""Flips vectors across a line.
Before

        •   
After

    •

Direction changes.
Magnitude stays the same.
"""
"""In AI, matrices ARE the model:

Neural network weights → matrices that transform input into output
Attention scores → matrices that decide what to focus on
Embeddings → matrices that map words to vectors
"""

"""This Is Why People Say

A neural network is just matrix multiplication with nonlinear activations.

Every layer is simply

Vector

↓

Matrix

↓

Vector

↓

Matrix

↓

Vector

Again and again."""

"""
🧠 Mentor Insight

This is why I said earlier:

A vector is like a point.
A matrix is like a machine that moves those points."""

#-----------------------------------------------------

#Matrix multiplication :
#Matrix multiplication is a way of combining information from a vector to create a new vector.

#Step 1 — Imagine a Recipe
"""
Suppose you're making tea.

Ingredients:

Sugar = 2 spoons

Milk = 1 cup

Represent this as a vector:

[2]
[1]

Now imagine a recipe card.

Tea Recipe

2   0

0   3

This recipe says:

Double the sugar.
Triple the milk.

The recipe card is the matrix.

The ingredients are the vector.

The result is a new vector.

The matrix didn't create new ingredients—it transformed them."""

#Step 2 — A Matrix Is Instructions
"""
Look at this matrix.

2 0

0 2

Don't see numbers.

Read it as instructions.

x → multiply by 2

y → multiply by 2

So


Input

[3]
[4]

becomes

[6]
[8]

This is scaling.

Now another matrix.

1 0

0 3

Instructions:

Keep x the same.

Triple y.

Input

[2]
[4]

Output

[2]
[12]

Only the vertical direction stretched."""

#Matrix Multiplication
Matrix = [
        [2, 0],
        [0, 3]
]
Vector = [
        [3],
        [4]
]

Result = [
        [2*3 + 0*4],  # First row of Matrix dot product 
        [0*3 + 3*4]   # Second row of Matrix dot product
]
print(f"Result of Matrix Multiplication: {Result}")  # Output: Result of Matrix Multiplication: [[6], [12]]



#---------------------------------------------------------
