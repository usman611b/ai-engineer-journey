# ============================================================
# Lesson 3 - Matrix Transformations
# Part 4.1 - Shearing Matrix (X-Shear)
# ============================================================

"""
SHEARING MATRIX

A shearing transformation changes the SHAPE of an object.

It does NOT rotate the object.

It does NOT uniformly scale the object.

Instead, it slides one axis while keeping the other fixed.

Example: X-Shear

Rule

new_x = old_x + k × old_y

new_y = old_y

where k is the shear factor.

--------------------------------------------------

Golden Rule

Columns = transformed basis vectors.

For k = 1

e₁ = (1,0)

↓

(1,0)

(x-axis stays fixed)

-----------------------------------

e₂ = (0,1)

↓

(1,1)

(y-axis slides to the right)

-----------------------------------

Place them as columns

        |1  1|
Shx  =  |0  1|

--------------------------------------------------

Important

✔ Changes shape

✔ Turns rectangles into parallelograms

✔ Does NOT rotate

✔ Does NOT uniformly scale

✔ x-axis stays fixed

✔ y-axis slides
"""

"""Shearing
e₁ → unchanged

e₂ → shifted
↓
Shearing Matrix
"""

# ============================================================
# Lesson 3 - Matrix Transformations
# Part 4.2 - General X-Shear Matrix
# ============================================================

"""
GENERAL X-SHEAR MATRIX

The shear factor is k.

Rule

new_x = old_x + k × old_y

new_y = old_y

-----------------------------------

Transform the basis vectors.

e₁ = (1,0)

↓

(1,0)

-----------------------------------

e₂ = (0,1)

↓

(k,1)

-----------------------------------

Place the transformed basis vectors as columns.

          |1  k|
Shx(k) =  |0  1|

-----------------------------------

Meaning

k = 0

No shear (Identity Matrix)

k > 0

Slides the y-axis to the right.

k < 0

Slides the y-axis to the left.

-----------------------------------

Remember

A shear matrix changes the SHAPE.

It does not rotate the object.

It does not uniformly scale the object.
"""

diagram = r"""
                     BEFORE SHEAR
               ┌─────────────────────────┐
               │  A = (1, 0)             │
               │  B = (0, 1)             │
               └──────────┬──────────────┘
                          │
                          ▼
                 SHEAR MATRIX (x-axis)
               ┌─────────────────────────┐
               │      [1   k]            │
               │ Shx =[     ]            │
               │      [0   1]            │
               │      k = 1              │
               └──────────┬──────────────┘
                          │
           x' = x + ky    │      y' = y
                          ▼
                      AFTER SHEAR
               ┌─────────────────────────┐
               │  A = (1, 0)             │
               │  (unchanged)            │
               │                         │
               │  B' = (1, 1)            │
               │  (shifted right)        │
               └─────────────────────────┘
"""

print(diagram)


# ============================================================
# Lesson 3 - Matrix Transformations
# Part 4.2 - General Y-Shear Matrix
# ============================================================

"""
GENERAL Y-SHEAR MATRIX
The shear factor is k.
Rule
new_x = old_x
new_y = old_y + k × old_x

-----------------------------------
Transform the basis vectors.
e₁ = (1,0) --> (1,0)
e₂ = (0,1) --> (k,1) where k is the shear factor. k = 0 means no shear, k > 0 slides the x-axis up, and k < 0 slides the x-axis down.
-----------------------------------
Place the transformed basis vectors as columns.

          |1  0|
Shy(k) =  |k  1|

-----------------------------------
"""


diagram = r"""
                     BEFORE SHEAR
               ┌─────────────────────────┐
               │  A = (1, 0)             │
               │  B = (0, 1)             │
               └──────────┬──────────────┘
                          │
                          ▼
                 SHEAR MATRIX (y-axis)
               ┌─────────────────────────┐
               │      [1   0]            │
               │ Shy =[     ]            │
               │      [k   1]            │
               │      k = 1              │
               └──────────┬──────────────┘
                          │
           x' = x         │      y' = y + kx
                          ▼
                      AFTER SHEAR
               ┌─────────────────────────┐
               │  A = (1, 0)             │
               │  (unchanged)            │
               │                         │
               │  B' = (1, 1)            │
               │  (shifted up)           │
               └─────────────────────────┘
"""

print(diagram)
