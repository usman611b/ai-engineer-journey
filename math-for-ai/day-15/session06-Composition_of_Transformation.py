# ============================================================
# Lesson 3 - Matrix Transformations
# Part 6 - Composition of Transformations
# ============================================================

"""
COMPOSITION OF TRANSFORMATIONS

Composition means applying multiple transformations one after another.

Example

Rotate

↓

Scale

is different from

Scale

↓

Rotate

--------------------------------------------------

Why?

Because every transformation changes the coordinate system
for the next transformation.

The output of the first transformation becomes
the input of the second transformation.

--------------------------------------------------

Example

Vector

(1,0)

Path 1

Rotate 90°

↓

(0,1)

↓

Scale x by 2

↓

(0,1)

-----------------------------------

Path 2

Scale x by 2

↓

(2,0)

↓

Rotate 90°

↓

(0,2)

Different final results.
(0,1) ≠ (0,2    )

Therefore,

Rotate → Scale

≠

Scale → Rotate

--------------------------------------------------

Matrix Multiplication

If

A = Rotation

B = Scaling

Then

B @ A

means

Apply A first,
then apply B.

The matrix closest to the vector
is applied FIRST.

--------------------------------------------------

Important

Matrix multiplication is NOT commutative.

A @ B ≠ B @ A

because the order of transformations matters.
"""