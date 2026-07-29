#📚 Lesson 1 – Session 2
#Vectors: The Language of AI

"""🎯 Learning Objectives

By the end of this session, you'll be able to answer:

What is a scalar?
What is a vector?
Why is a vector more than just a Python list?
Why do AI models use vectors?
What is magnitude?
What is direction?
Why do dimensions matter?
"""
#Step 1 — What is a Scalar?
"""Scalars are single numbers.
Examples:

5
10
-3
99
3.14

These are all scalars.
They only tell us "how much.

Real-Life Examples

Your age = 20

Temperature = 38°C

Weight = 70 kg

Salary = $500

Notice something? -->>> All of these answer one question:

How much?

They do not tell us direction."""

age = 20
temperature = 38
height = 5.8

#Each variable stores one value. --->>> That is a scalar.

#📌 Remember : A scalar only has magnitude (size).It has no direction.

#----------------------------------------------------

#Step 2 — Then Why Isn't a Scalar Enough?
"""Scalars are great for answering "how much" questions.

But what if we want to answer "in which direction" or "in how many dimensions"?
Imagine I tell you

Walk

10 km

Question:

Where?

North?

South?

East?

West?

Impossible to know.

A scalar cannot tell direction.
"""
#Step 3 — Enter the Vector
#A vector is a quantity with both magnitude and direction.

"""Google Maps Example

Instead of

10 km

I now tell you

10 km

North-East

Now you know

how far
where

That is a vector.

-----(Geometry)----

Imagine a graph.

          y
          ↑
      4   |
      3   |
      2   |       ● (3,2)
      1   |
──────────┼────────────────→ x
          1   2   3   4

This point is

(3,2)

That is a vector.
Why?

Because it tells us

Move --->>> 3 units Right

then --->>> 2 units  Up

Now we know both

1-magnitude
2-direction
"""

#Python Representation
#A vector is simply

v = [3, 2]

#Looks like a list.

#But...

#📌 Mentor's Addition

#This is NOT just a Python list.

#It represents

#Position in Space that we see in the graph above.

#That changes everything.

#Example:
"""SUppose we have :"""
cat = [1.2, 3.5]
dog = [1.4, 3.7]
car = [9.5, 0.4]

"""These are not a random list of numbers. They represent positions or locations in AI's space."""
"""Imagine

Cat

↓

[0.18,-0.62,0.41,...768 numbers]

That entire list is ONE VECTOR."""

#Question

"""Why not use

Cat = 5

Because

one number

↓

one dimension

↓

cannot represent complex meaning."""
#----------------------------------------------

#Step 4 — Dimensions
#This is one of the most important concepts.

#1D Vector
"""
------------●----------------

0     1    2    3    4

Example

[2]

Only one coordinate.

Lives on a line."""

#2D Vector
"""
2D Vector
        y
        ↑

        ●

──────────────→ x

Example

[3,2]

Lives on a plane.

2D vector [3, 2]:

x	y	Point
3	2	The vector points from origin (0,0) to (3, 2) on the plane
"""

#3D Vector
"""
3D Vector

        y
        ↑

        ●    


──────────────→ x
       /   
      / 
     ● z

Example

[3,2,5]

Lives in space.  
        """

#nD Vector
"""
nD Vector
n-Dimensional Vector

We cannot draw

768 dimensions.

But mathematically

[0.12,0.55,...768 values]

is still ONE VECTOR."""

"""📌 AI Connection

Every word

↓

768-dimensional vector

Every image

↓

Thousands or millions of dimensions

Every user

↓

Preference vector

Everything

↓

Vector"""

#Step 5 — Magnitude
#Magnitude is the length of a vector.

"""Imagine two arrows.

Arrow A---->

Arrow B-------------->

Which is longer? Arrow B.

That length is called Magnitude

Example:

Vector = (3,4)

Length =5

We haven't learned the formula yet. whicj we'll learn how to calculate.
Formula:
magnitude = √(x² + y²)

step 1: Square each component: 3² = 9, 4² = 16
step 2: Add the squares: 9 + 16 = 25
step 3: Take the square root: √25 = 5

result: The magnitude of the vector (3, 4) is 5.

For now Think

Magnitude = Length


"""
# What is normalization?
"""What is normalization?
One Sentence : Normalization changes the vector's length to exactly 1 without changing its direction.

Notice something important.

It changes the magnitude.

It does NOT change the direction.

Visual Intuition

Suppose we have

      •

     /

    /

   /

  /

 O

Length = 5

Now normalize it.

   •

  /

 /

O

Length = 1

Still pointing the SAME direction.

Only shorter.

Why Do We Need to Normalize a Vector?
Imagine these two vectors.

Cat

↓

[300,400]

and

Tiger

↓

[3,4]

Are they pointing in the same direction?

YES.

One is simply much longer.

If we compare them without normalization,

the larger numbers dominate.

Normalization removes the effect of size.

Only direction remains.

This is why cosine similarity works.

Why we need to normalize a vector?
Normalization is important because it allows us to compare vectors of different magnitudes on a common scale.

Example:
Vector A = (3, 4)
Vector B = (6, 8)
Both vectors point in the same direction, but Vector B is twice as long as Vector A.

So, we can normalize both vectors to have a magnitude of 1, which allows us to compare their directions without being influenced by their lengths.
To normalize a vector, we divide each component of the vector by its magnitude.

For example, to normalize Vector A = (3, 4):
1. Calculate the magnitude of Vector A: √(3² + 4²) = 5
2. Divide each component of Vector A by its magnitude:
3. Normalized Vector A = (3/5, 4/5) = (0.6, 0.8)
Now, both Vector A and Vector B can be compared based on their directions, as they are both unit vectors with a magnitude of 1.

"""


#Step 6 — Direction
#Direction is the way a vector  Direction points.

#Imagine two arrows.
"""Imagine

→

and

↑

Same length.

Different directions.

That means

Vectors are different."""

"""Example

[5,0]

↓

Go Right
[0,5]

↓

Go Up

Same magnitude.

Different directions."""

#Pure Python

#Let's create our first vector.

v = [3, 2]

print("Vector:", v)
print("X coordinate:", v[0])
print("Y coordinate:", v[1])

#Nothing fancy.

#Just a list.

#But now you know

#It represents a point.

#Not merely data.

"""
🧠 Mentor's Golden Rule #2

I want you to remember this forever.

A vector is not the numbers themselves. A vector is the position those numbers describe.

For example

[2,5]

Those numbers are not important by themselves.

They describe
    |
    |       •
    |      (2,5)
    |
    |____________________
            

That's the vector.


The list is merely the storage."""

#
#Cosine Similarity
"""
The Dot Product Measures Similarity
The dot product of two vectors tells you how similar they are.

a · b = a₁×b₁ + a₂×b₂ + ... + aₙ×bₙ

Same direction:      a · b > 0  (similar)
Perpendicular:       a · b = 0  (unrelated)
Opposite direction:  a · b < 0  (dissimilar)
This is literally how search engines, recommendation systems, and RAG work -- find vectors with high dot products."""


