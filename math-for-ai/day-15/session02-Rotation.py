# ============================================================
# Lesson 3 - Matrix Transformations
# Part 2.1 - Rotation (Intuition)
# ============================================================

"""
ROTATION

A rotation transformation changes the DIRECTION (angle)
of a vector while preserving its LENGTH (magnitude).

Properties of Rotation

✔ Changes the angle (direction)
✔ Preserves the length (magnitude)
✔ Preserves distances between points
✔ Preserves the shape of objects

Example

Before Rotation

(1,0)

↓

Rotate 90°

↓

(0,1)

The vector points in a new direction,
but its length remains exactly the same.

Think of rotating an arrow around the origin.
The arrow spins, but it never stretches or shrinks.
"""

# ============================================================
# Lesson 3 - Matrix Transformations
# Part 2.2 - Building a Rotation Matrix
# ============================================================

"""
How do we build a rotation matrix?

Remember the golden rule:

"The columns of a matrix are the transformed basis vectors."

Standard basis vectors

e1 = (1,0)
e2 = (0,1)

Rotate both basis vectors 90° counterclockwise.

e1 → (0,1)

e2 → (-1,0)

Now place these transformed basis vectors as the columns
of the matrix.

First Column  = image of e1 = (0,1)

Second Column = image of e2 = (-1,0)

Rotation Matrix (90° CCW)

| 0  -1 |
| 1   0 |

We did NOT memorize this matrix.

We BUILT it by asking:

"Where do the basis vectors move?"
"""

# ============================================================
# Lesson 3 - Matrix Transformations
# Part 2.3 - Rotation Matrices from Basis Vectors
# ============================================================

"""
Instead of memorizing rotation matrices,
we can BUILD them using the basis vectors.

Golden Rule

Columns of a matrix = transformed basis vectors.

--------------------------------------------------

0° Rotation

e1 → (1,0)

e2 → (0,1)

Matrix

| 1  0 |
| 0  1 |

--------------------------------------------------

90° Counter Clockwise

e1 → (0,1)

e2 → (-1,0)

Matrix

| 0  -1 |
| 1   0 |

--------------------------------------------------

180°

e1 → (-1,0)

e2 → (0,-1)

Matrix

| -1   0 |
|  0  -1 |

--------------------------------------------------

270° Counter Clockwise

e1 → (0,-1)

e2 → (1,0)

Matrix

| 0   1 |
| -1  0 |

--------------------------------------------------

Important Idea

Every rotation matrix can be built simply by asking:

"Where do the basis vectors move?"

Then place those transformed basis vectors
as the columns of the matrix.
"""

"""Let's organize everything
Rotation        	\(e_1\) becomes 	\(e_2\) becomes	Rotation Matrix
0° (Identity)	    (1,0)	(0,1)	    [[1,0],[0,1]]
90° CCW	            (0,1)	(-1,0)	    [[0,-1],[1,0]]
180°	            (-1,0)	(0,-1)	    [[-1,0],[0,-1]]
270° CCW	        (0,-1)	(1,0)	    [[0,1],[-1,0]]
360°	            (1,0)	(0,1)	    [[1,0],[0,1]]"""

"""Imagine the basis vectors

↓

Rotate them

↓

Where does e₁ go?

↓

Where does e₂ go?

↓

Put them as columns

↓

Done!"""

# ============================================================
# Lesson 3 - Matrix Transformations
# Part 2.4 - General Rotation Matrix
# ============================================================

"""
GENERAL ROTATION MATRIX

We already know:

A matrix is a transformation machine.

The columns of a matrix are the transformed basis vectors.

--------------------------------------------------

Step 1

The first basis vector

e1 = (1,0)

starts at 0°.

After rotating by θ,

its coordinates become

(cosθ, sinθ)

So the FIRST COLUMN becomes

| cosθ |
| sinθ |

--------------------------------------------------

Step 2

The second basis vector

e2 = (0,1)

already starts at 90°.

After rotating by θ,

its angle becomes

90° + θ

Using the unit circle identities,

cos(90° + θ) = -sinθ

sin(90° + θ) =  cosθ

So the SECOND COLUMN becomes

| -sinθ |
|  cosθ |

--------------------------------------------------

Step 3

Place both transformed basis vectors as columns.

Rotation Matrix

        | cosθ   -sinθ |
R(θ) =  | sinθ    cosθ |

--------------------------------------------------

Properties

✔ Changes the direction (angle)

✔ Preserves the magnitude (length)

✔ Preserves distances

✔ Preserves shape

✔ Determinant = 1

✔ Pure rotation (no scaling or shearing)

--------------------------------------------------

Important Memory

We DO NOT memorize the rotation matrix.

We BUILD it by asking:

"Where do the basis vectors move after rotation?"
"""

import math

def rotation_matrix(theta):
    """
    Returns the 2D rotation matrix for a given angle theta (in radians).
    
    Parameters:
    theta (float): The angle of rotation in radians.
    
    Returns:
    list: A 2x2 rotation matrix.
    """
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    
    return [[cos_theta, -sin_theta],
            [sin_theta, cos_theta]]

matrix_90_deg = rotation_matrix(math.pi / 2)
print("Rotation Matrix for 90 degrees (π/2 radians):")
for row in matrix_90_deg:
    print(row)

matrix_180_deg = rotation_matrix(math.pi)
print("\nRotation Matrix for 180 degrees (π radians):")
for row in matrix_180_deg:
    print(row)

matrix_270_deg = rotation_matrix(3 * math.pi / 2)
print("\nRotation Matrix for 270 degrees (3π/2 radians):")
for row in matrix_270_deg:
    print(row)