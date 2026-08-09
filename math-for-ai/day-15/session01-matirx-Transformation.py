#Session 1 — What does “matrix transformation” actually mean?
"""# ============================================================
# Lesson 3 - Matrix Transformations (Part 1)
# Topic: Column Picture of a Matrix
# ============================================================
==========================
BIG IDEA
==========================

A matrix is NOT just a table of numbers.

A matrix is a TRANSFORMATION MACHINE.

Its job is to take every vector (point) in space and
transform (move) it into a new position.

                Input Vector
                     │
                     ▼
            +----------------+
            |     Matrix     |
            | Transformation |
            |    Machine     |
            +----------------+
                     │
                     ▼
                New Vector


==========================
STANDARD BASIS VECTORS
==========================

Every vector in 2D is built from two basis vectors.

e1 = [1]
     [0]

e2 = [0]
     [1]

These define our coordinate system.


==========================
THE MOST IMPORTANT IDEA
==========================

The COLUMNS of a matrix tell us where the basis vectors
move after the transformation.

Example:

        |2  1|
A =     |3  4|

Column 1 = [2]
           [3]

Column 2 = [1]
           [4]

This means

e1 -----> (2,3)

e2 -----> (1,4)

The matrix is literally describing where each basis
vector ends up after the transformation.

So a matrix is completely determined by where it sends
the basis vectors.


==========================
COLUMN PICTURE
==========================

Suppose

A = |5  2|
    |1  7|

Without doing multiplication we immediately know

e1 -----> (5,1)

e2 -----> (2,7)

because

First Column  = image of e1
Second Column = image of e2


==========================
HOW EVERY VECTOR IS TRANSFORMED
==========================

Every vector can be written as a combination of basis vectors.

Example

v = [3]
    [2]

can be written as

v = 3e1 + 2e2

Since

e1 -----> First Column

e2 -----> Second Column

then

A(v)

=

3 × (First Column)

+

2 × (Second Column)

Example

A = |4  1|
    |2  5|

Columns

c1 = (4,2)

c2 = (1,5)

Transform

v = (2,3)

Instead of row-column multiplication we think

2 × c1 + 3 × c2

=

2 × (4,2)

+

3 × (1,5)

=

(8,4)

+

(3,15)

=

(11,19)

This gives exactly the same answer as normal
matrix multiplication.


==========================
IDENTITY MATRIX
==========================

Identity Matrix

I = |1  0|
    |0  1|

Columns are

e1 = (1,0)

e2 = (0,1)

So

e1 -----> e1

e2 -----> e2

Nothing changes.

Identity transformation means every vector stays
where it already is.


==========================
IMPORTANT OBSERVATION
==========================

A matrix is NOT built from basis vectors.

Instead,

its COLUMNS ARE the transformed basis vectors.

This is the key intuition behind matrix transformations.


==========================
GOLDEN FORMULA
==========================

If

        | c1  c2 |

is a matrix,

and

x = [a]
    [b]

then

Ax

=

a(c1)

+

b(c2)

This is called the COLUMN PICTURE of matrix multiplication.


==========================
AI CONNECTION
==========================

A neural network weight matrix does exactly the same thing.

Instead of thinking

"Matrix × Vector"

think

"The weight matrix creates a NEW coordinate system."

Each column of the weight matrix represents a learned
feature direction.

Every layer transforms the input into a new feature space.


==========================
ONE-LINE MEMORY
==========================

"A matrix is a transformation machine.
Its columns are the transformed basis vectors,
telling us where each basis vector moves in space."

-----------------------------------------------
"""


