# ============================================================
# Lesson 3 - Matrix Transformations
# Part 7 - Determinant
# ============================================================

"""
DETERMINANT

The determinant tells us what a transformation
does to AREA (2D) or VOLUME (3D).

Forget the formula.

Think geometrically.

Start with a unit square
Imagine the smallest square in the coordinate system.
Its corners are

(0,0)

(1,0)

(1,1)

(0,1)

Graphically
      y
      ↑
      │
  ■───■
  │   │
  │   │
  ■───■──────► x


This square has

Width = 1

Height = 1

Area = 1 * 1 = 1

\]This is called the unit square.
Step 2 — Apply a scaling matrix
Suppose the matrix is

 S = | 2  0 |
     | 0  3 |

You already know what this means.
Stretch x-axis by 2
Stretch y-axis by 3
The square becomes
        y
        ↑
        │
        │
  ■────────■
  │        │
  │        │
  │        │
  │        │
  ■────────■────────► x
Now
Width  2
Height  3
Area   = 2 * 3 = 6
--------------------------------------------------

|det(A)|

=

Area Scaling Factor

Examples

det = 6

↓

Area becomes 6 times larger.

----------------------------

det = 0.25

↓

Area becomes one-quarter.

----------------------------

det = 1

↓

Area is preserved.

(rotation)

----------------------------

det = 0

↓

Space collapses to a line.

Transformation is not reversible.

----------------------------

Negative determinant

The absolute value still tells us
the area scaling.

The negative sign tells us that
the orientation is flipped.

Example

det = -1

↓

Area unchanged

Orientation flipped

(reflection)

Example

det = -4

↓

Area becomes 4 times larger

Orientation flipped

--------------------------------------------------

Remember

Magnitude (|det|)

↓

Area scaling

Sign (+/-)

↓

Orientation
"""

"""
🧠 BIG IDEA
Look at these examples.
Matrix      	Area    Before	    Area After	    Determinant
Scale           (2,3)	    1	        6	            6
Scale           (2,4)	    1	        8	            8
Scale           (0.5,0.5)	1	        0.25	        0.25


Do you see the pattern?
The determinant tells you:
"How many times bigger or smaller did the transformation make the area?"


🧠 The complete meaning of determinant
Determinant     	Meaning

2	                Area doubled
0.5	                Area halved
1	                Area preserved
0	                Space collapsed to a line
-1	                Area preserved and orientation flipped
-3	                Area tripled and orientation flipped

Magnitude (|det|)

↓

How much the area changes.

4

-----------------------

Sign (-)

↓

Orientation flips.

This is a very strong foundation. Most students memorize the determinant as:
                   \[ad - bc\]
                   
                   and never know what it means.

You now understand its geometric meaning, which is much more valuable for AI.
"""