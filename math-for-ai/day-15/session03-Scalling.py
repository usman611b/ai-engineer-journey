# ============================================================
# Lesson 3 - Matrix Transformations
# Part 3.1 - Scaling Matrix
# ============================================================

"""
SCALING MATRIX

A scaling transformation changes the LENGTH of vectors.

It stretches or shrinks the coordinate axes.

Golden Rule

Columns = transformed basis vectors.

Example

Stretch x-axis by 2

e₁ → (2,0)

Stretch y-axis by 3

e₂ → (0,3)

Place them as columns

| 2  0 |
| 0  3 |

This is the scaling matrix.

Important

A scaling matrix does NOT rotate.

A scaling matrix does NOT shear.

It only changes the size of the coordinate axes.
"""

"""🤯 Do you see the pattern?
This is the biggest lesson so far.
Identity

↓

Where do the basis vectors go?

↓

Matrix

-------------------------

Rotation

↓

Where do the basis vectors go?

↓

Matrix

-------------------------

Scaling

↓

Where do the basis vectors go?

↓

Matrix
Every linear transformation is built the same way.
Just ask:
"Where does e₁ go?"

"Where does e₂ go?"

Put those answers as the columns.
Done.


🧠 Mentor Secret

This is exactly how I think.

When I see a matrix like

| 4  2 |
| 1  5 |



I don't immediately think:
"Multiply rows and columns."

I think:
"Interesting... e₁ is sent to (4,2), and e₂ is sent to (1,5)."

Everything else follows from that."""

"""
                     BEFORE SCALING
               ┌───────────────────────┐
               │  A = (2, 1)           │
               │  B = (0, 2)           │
               └──────────┬────────────┘
                          │
                          ▼
                SCALING MATRIX (S)
               ┌───────────────────────┐
               │      [ 2x    0  ]     │
               │  S = [          ]     │ 
               │      [ 0   0.5y ]     │
               └──────────┬────────────┘
                          │
          x' = 2x         │        y' = 0.5y
                          ▼
                     AFTER SCALING
               ┌───────────────────────┐
               │  A' = (4, 0.5)        │
               │  B' = (0, 1)          │
               └───────────────────────┘
"""