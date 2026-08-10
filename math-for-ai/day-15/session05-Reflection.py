# ============================================================
# Lesson 3 - Matrix Transformations
# Part 5 - Reflection Matrix
# ============================================================

"""
REFLECTION MATRIX

Reflection flips space across a mirror line.

Golden Rule

Columns = transformed basis vectors.

--------------------------------------------------

Reflection across the Y-axis

Rule

x changes sign

y stays the same

e₁ = (1,0)

↓

(-1,0)

e₂ = (0,1)

↓

(0,1)

Matrix

|-1   0|
| 0   1|


"""
diagram = r"""
                 BEFORE REFLECTION (Y-AXIS)
           ┌─────────────────────────────┐
           │  A = (2, 3)                 │
           │  B = (-1, 4)                │
           └────────────┬────────────────┘
                        │
                        ▼
              REFLECTION MATRIX (Y-AXIS)
           ┌─────────────────────────────┐
           │      [-1   0 ]              │
           │ Ry = [       ]              │
           │      [ 0   1 ]              │
           └────────────┬────────────────┘
                        │
              x' = -x   │    y' = y
                        ▼
                AFTER REFLECTION
           ┌─────────────────────────────┐
           │  A' = (-2, 3)               │
           │  B' = (1, 4)                │
           └─────────────────────────────┘
"""

print(diagram)
"""
--------------------------------------------------

Reflection across the X-axis

Rule

x stays the same

y changes sign

e₁ = (1,0)

↓

(1,0)

e₂ = (0,1)

↓

(0,-1)

Matrix

|1   0|
|0  -1|



"""
diagram = r"""
                 BEFORE REFLECTION (X-AXIS)
           ┌─────────────────────────────┐
           │  A = (2, 3)                 │
           │  B = (-1, 4)                │
           └────────────┬────────────────┘
                        │
                        ▼
              REFLECTION MATRIX (X-AXIS)
           ┌─────────────────────────────┐
           │      [ 1   0 ]              │
           │ Rx = [       ]              │
           │      [ 0  -1 ]              │
           └────────────┬────────────────┘
                        │
               x' = x   │    y' = -y
                        ▼
                AFTER REFLECTION
           ┌─────────────────────────────┐
           │  A' = (2, -3)               │
           │  B' = (-1, -4)              │
           └─────────────────────────────┘
"""

print(diagram)
"""

--------------------------------------------------

Important

Reflection changes orientation.

It is different from rotation.

A reflection cannot be achieved by rotation alone.
"""