#Gram-Schmidt Process:
"""Converting any set of independent vectors into an orthonormal basis. Orthonormal means every vector has length 1 and every pair is perpendicular."""

"""First, Why Do We Need Gram-Schmidt?

Imagine you have these vectors.

v₁ ↗

v₂ ↗↗

v₃ ↖

They are independent.

That's good.

But they are messy.

They are

Different lengths
Different angles
Not perpendicular

Like this:

          v₂
         /
        /
       /
      /
     /
v₁  /
   /
  /
 O-------------->


This is perfectly valid.

But computers prefer something much cleaner.

They want this

        ↑ u₂

        |

        |

        |

--------O--------> u₁

Notice

Perfectly perpendicular (90°)
Length = 1
Easy to calculate
So Gram-Schmidt Does Only One Job

It converts messy independent vectors into clean perpendicular unit vectors.

Nothing more.

Think Like Cleaning Your Room

Imagine your room.

Books

Laptop

Shoes

Bottle

Bag


Everything is useful.

But messy.

Gram-Schmidt doesn't throw anything away.

It simply organizes everything neatly.

After cleaning

Books

Bookshelf

Laptop

Desk

Shoes

Shoe Rack

Same things.

Better organized.

Mathematical Meaning

Suppose

v₁

v₂

v₃

These are your original vectors.

Gram-Schmidt produces

u₁

u₂

u₃

where

Every u has length 1.
Every pair is perpendicular.
What Doesn't Change?

This is VERY important.

Gram-Schmidt

❌ does NOT change the space.

The span stays exactly the same.

Before

Span(v₁,v₂,v₃)

After

Span(u₁,u₂,u₃)

They are identical.

It only changes how we represent the space, not the space itself.

Why AI Uses Gram-Schmidt

You don't need the mathematics yet.

Just know these applications.

AI Area	Why Gram-Schmidt Helps
QR Decomposition	Built using Gram-Schmidt
Least Squares	Solves regression more stably
PCA	Uses orthogonal directions
Numerical Computing	Reduces calculation errors
Eigenvalue Algorithms	QR Algorithm starts here
Simple Analogy

Imagine you have three rulers.

/

//

\

All point in different directions.

Gram-Schmidt straightens them into

    |
    |
____|____

⊙ (out of page in 3D)

Everything becomes perfectly organized.

The Whole Algorithm (No Math Yet)

It always follows these three steps:

Step 1

Take the first vector.

Normalize it.

↓

Make its length = 1.

Step 2

Take the second vector.

Remove the part that points toward the first vector (using projection, which you already know).

Normalize it.

Step 3

Take the third vector.

Remove the parts pointing toward both previous vectors.

Normalize it.

Done.

🧠 One Sentence for Your Notes

Gram-Schmidt is an algorithm that converts a set of linearly independent vectors into an orthonormal basis while preserving the same span.

Where:

Ortho = Perpendicular (90°)
Normal = Length = 1
Basis = Minimum vectors needed to represent the space"""

"""The algorithm:

Take the first vector, normalize it
Take the second vector, subtract its projection onto the first, normalize
Take the third vector, subtract its projections onto all previous vectors, normalize
Repeat for remaining vectors
Input:  v1, v2, v3, ... (linearly independent)

u1 = v1 / |v1|

w2 = v2 - (v2 dot u1) * u1
u2 = w2 / |w2|

w3 = v3 - (v3 dot u1) * u1 - (v3 dot u2) * u2
u3 = w3 / |w3|

Output: u1, u2, u3, ... (orthonormal basis)
This is how QR decomposition works internally. Q is the orthonormal basis, R captures the projection coefficients. QR decomposition is used in:

Solving linear systems (more stable than Gaussian elimination)
Computing eigenvalues (QR algorithm)
Least-squares regression (the standard numerical method)"""

#Code Implementation of Gram-Schmidt Process
#Code is in the file math-for-ai/day-13/session07-Build-matrices-own-class.py


