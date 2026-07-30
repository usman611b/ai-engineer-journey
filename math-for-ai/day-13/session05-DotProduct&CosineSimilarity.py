
#Dot Product (The Language of Similarity)
#The dot product measures how much two vectors point in the same direction.

"""The dot product is a way to measure how similar two vectors are.
❌ It doesn't measure distance.

❌ It doesn't measure magnitude alone.

✅ It measures alignment.
"""

"""Imagine Two People Walking

Suppose you are walking.

Your direction

        ↑

Your friend

        ↑

Both walking in the same direction.

They're highly similar.

Now

You

↑

Friend

→

One walks north.

One walks east.

Almost unrelated.

Now

You

↑

Friend

↓


Completely opposite.

This is exactly what the dot product tells us."""

#Another Example
"""Think About Wind 🌬️

Imagine you're riding a bicycle.

The wind blows.

Case 1

Wind behind you.

Wind →

You →

Easy.

The wind helps.

(Large positive dot product.)

Case 2
Wind ↑

You →

The wind doesn't help.It doesn't stop you.

(Dot product    ≈ 0 )

Case 3
Wind ←

You →

The wind fights you.

(Negative dot product.)

This is the intuition.

The dot product asks:

"Are these two vectors working together?"""


#The Formula
"""
Now the math.

For two vectors

a = [a₁,a₂]

b = [b₁,b₂]

Dot Product

a·b = a₁×b₁ + a₂×b₂

Example

a = [2,3]

b = [4,5]

Calculate

2×4 + 3×5 = 8+15 = 23

Dot product = 23

But What Does 23 Mean?

Absolutely nothing...

by itself.

The value only makes sense when compared with other vectors.

The important thing is

Large Positive

↓

Very Similar

Near Zero

↓

Unrelated

Negative

↓

Opposite

Visual Intuition
Same Direction
      ↗

      ↗

Large Positive

Perpendicular
↑

→

Zero

Opposite
↑

↓


Negative

Why Does AI Love Dot Products?

Suppose

Cat

↓

[0.2
0.8
0.4]

Dog

↓

[0.3
0.9
0.5]

Car

↓

[0.9
0.1
0.2]

Now ask

Which is more similar to Cat?

The computer computes

Cat · Dog

Cat · Car

Whichever dot product is larger

↓

More similar.

That's literally semantic search."""
#Example

cat = [0.2, 0.8, 0.4]
dog = [0.3, 0.9, 0.5]
car = [0.9, 0.1, 0.2]

dot_cat_dog = sum(c * d for c, d in zip(cat, dog))
dot_cat_car = sum(c * d for c, d in zip(cat, car))

print(f"Dot Product of Cat and Dog: {dot_cat_dog}")  # Output: Dot Product of Cat and Dog: 0.74
print(f"Dot Product of Cat and Car: {dot_cat_car}")  # Output: Dot Product of Cat and Car: 0.38

#So the computer concludes that Cat is more similar to Dog than to Car based on the high positive dot product values.

"""ChatGPT

Your prompt

↓

Embedding Vector

↓

Dot Product

↓

Relevant Knowledge
-------------------------------------------
RAG

Question

↓

Embedding

↓

Dot Product

↓

Most Similar Chunks

↓

LLM
---------------------------------------
Transformers

This is HUGE.

Inside every transformer

(Q)

Query

↓

Dot Product

↓

(K)

Key

↓

Attention Score

The famous equation  Q · Kᵀ is simply thousands of dot products.

Attention is literally "Which word is most similar to the current word?" using dot products."""

"""Every recommendation system is basically asking one question:

"Which vector is most aligned with this vector?"

Netflix

↓

Movies with highest dot product.

Spotify

↓

Songs with highest dot product.

Amazon

↓

Products with highest dot product.

ChatGPT

↓

Tokens with highest attention scores.

All because of one operation.

The dot product.

a · b = a₁×b₁ + a₂×b₂ + ... + aₙ×bₙ

Same direction:      a · b > 0  (similar)
Perpendicular:       a · b = 0  (unrelated)
Opposite direction:  a · b < 0  (dissimilar)
"""

#--------------------------------------------------------
"""⚠ Now Here Comes the Problem

Suppose

A = [1000,1000]

and

B = [1000,1000]

Dot Product

↓

Very Huge

Now

C = [2,2]

and

D = [2,2]

They point in exactly the same direction.

But

their dot product is much smaller.

Why?

Because

dot product depends on BOTH:

Direction ✅
Magnitude ✅

Sometimes in AI...

We don't care about magnitude.

We only care about

Direction

Because direction represents meaning.

Example

Imagine

Person A

studies

10 hours

Person B

studies

5 hours

Both study

Computer Science

AI

Math

Programming

Same interests.

One just studies longer.

Should we call them different?

No.

Their direction is the same.

Only magnitude changed.

This is exactly why AI uses

⭐ Cosine Similarity

instead of raw dot product.

Cosine Similarity removes the effect of magnitude and only measures direction.

It answers

"Are these two vectors pointing in the same direction?"

That's why OpenAI Embeddings, Sentence Transformers, FAISS, Pinecone, ChromaDB, Weaviate, Milvus, and almost every vector database uses cosine similarity by default."""

#_____________________________________________________________________

#Cosine Similarity
#Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space. 
# It is defined as the cosine of the angle between the two vectors, which can be computed using the dot product and the magnitudes of the vectors.

#Cosine similarity measures the similarity of two vectors using only their direction, not their magnitude.

#Step 1 — The Problem with Dot Product
"""
Let's revisit yesterday.

Suppose we have

Person A Studies

Python
AI
Math

10 hours/day

Embedding

[10
20
30]

Person B

Studies exactly the same subjects

But only

5 hours/day

Embedding

[5
10
15]

Notice something.

The second vector is simply

Half

of the first.

They point in exactly the same direction.

They have exactly the same interests.

Only the amount changed.

Dot Product Says

First vector

[10
20
30]

Second

[5
10
15]

Dot product

↓

Huge number

Now compare

[1
2
3]

and

[1
2
3]

Dot product

↓

Much smaller.

But...

These vectors represent exactly the same meaning!

So why should one similarity be larger?

That's the weakness of the dot product.

It is affected by

Direction ✅
Magnitude ✅

Sometimes we only want

Direction."""

#Example
Student_A = [10, 20, 30]  # Represents hours spent on subjects
Student_B = [5, 10, 15]    # Represents hours spent on subjects

# Calculate dot product
dot_product = sum(a * b for a, b in zip(Student_A, Student_B))
print(f"Dot Product of Student A and B: {dot_product}")  # Output: Dot Product of Student A and B: 700

#So even though Student A and B have the same interests, the dot product is large due to the difference in magnitude. This is where cosine similarity comes in to measure only the direction of the vectors.
#Now we will calculate the cosine similarity to see how it reflects the similarity in direction regardless of magnitude.

#Cosine Similarity Formula

cosine_similarity = dot_product / ((sum(a ** 2 for a in Student_A) ** 0.5) * (sum(b ** 2 for b in Student_B) ** 0.5))
print(f"Cosine Similarity of Student A and B: {cosine_similarity}") #Output: Cosine Similarity of Student A and B: 1.0
#Now we can see that the cosine similarity is 1.0, indicating that the two vectors are pointing in the same direction, despite their different magnitudes. This demonstrates how cosine similarity effectively captures the similarity in direction between two vectors.

#------------------------------------
#Now example of Dissimilar Vectors
Student_C = [10, 20, 30]  # Represents hours spent on subjects
Student_D = [30, 20, 10]  # Represents hours spent on subjects in reverse order

# Calculate dot product
dot_product_cd = sum(c * d for c, d in zip(Student_C, Student_D))
print(f"Dot Product of Student C and D: {dot_product_cd}")  # Output: Dot Product of Student C and D: 1400

# Calculate magnitudes
magnitude_c = sum(c ** 2 for c in Student_C) ** 0.5
magnitude_d = sum(d ** 2 for d in Student_D) ** 0.5

# Calculate cosine similarity
cosine_similarity_cd = dot_product_cd / (magnitude_c * magnitude_d)
print(f"Cosine Similarity of Student C and D: {cosine_similarity_cd}")  # Output: Cosine Similarity of Student C and D: 0.9999999999999998

#Now we can see that the cosine similarity is very close to 1.0, indicating that the two vectors are still pointing in a similar direction, even though their order of components is reversed. This shows that cosine similarity captures the overall direction of the vectors rather than their specific arrangement.

#------------------------------------
#Now example of Opposite Vectors
Student_E = [10, 20, 30]  # Represents hours spent on subjects
Student_F = [-10, -20, -30]  # Represents hours spent on subjects in the opposite direction

# Calculate dot product
dot_product_ef = sum(e * f for e, f in zip(Student_E, Student_F))
print(f"Dot Product of Student E and F: {dot_product_ef}")  #Output: Dot Product of Student E and F: -1400
# Calculate magnitudes
magnitude_e = sum(e ** 2 for e in Student_E) ** 0.5
magnitude_f = sum(f ** 2 for f in Student_F) ** 0.5
# Calculate cosine similarity
cosine_similarity_ef = dot_product_ef / (magnitude_e * magnitude_f)
print(f"Cosine Similarity of Student E and F: {cosine_similarity_ef}")  # Output: Cosine Similarity of Student E and F: -1.0
#Now we can see that the cosine similarity is -1.0, indicating that the two vectors are pointing in exactly opposite directions. This demonstrates how cosine similarity effectively captures the relationship between vectors, showing that they are dissimilar in direction despite having the same magnitude.


#Another Example
"""Step 2 — Imagine Shadows

Imagine a flashlight.

You shine it onto the floor.

The shadow depends on the angle.

      Vector A
          ↗

        ☀

----------------

Now another vector

      Vector B
          ↗

Their shadows overlap almost perfectly.

Very similar.

Now

A

↑


B

→

The shadows don't overlap.

Not similar.

Cosine similarity only asks

How much do the directions overlap?

It completely ignores

How long the arrows are."""

#Step 3 — The Formula
"""Cosine Similarity=   A⋅B /  ∣A∣∣B|

Where:
Look carefully.

Top ->>> Dot Product

Bottom --->>> Magnitude of A  ×  Magnitude of B

The denominator removes the effect of vector length.

Only direction remains."""


#Why Embeddings Use Cosine Similarity
"""

Suppose

Cat

Embedding

[0.3
0.7
0.5]

Another model produces

[3
7
5]

This vector is

10× larger.

Meaning?

Exactly the same.

Dot product changes.

Cosine similarity

↓

Still

1

Because direction never changed.

That's why embeddings almost always use cosine similarity.
"""

cat = [0.3, 0.7, 0.5]
another_model = [3, 7, 5]

dot_product = sum(c * a for c, a in zip(cat, another_model)) # output: Dot Product of Cat and Another Model: 5.9
magnitude_cat = sum(c ** 2 for c in cat) ** 0.5 # output: Magnitude of Cat: 0.8770960202020245
magnitude_another = sum(a ** 2 for a in another_model) ** 0.5 # output: Magnitude of Another Model: 8.770960202020245

cosine_similarity = dot_product / (magnitude_cat * magnitude_another)
print(f"Cosine Similarity of Cat and Another Model: {cosine_similarity}")#Output: Cosine Similarity of Cat and Another Model: 1.0

"""
Google Search

Query

↓

Embedding

↓

Cosine Similarity

↓

Millions of pages

↓

Most relevant pages.

ChatGPT

Prompt

↓

Embedding

↓

Cosine Similarity

↓

Relevant knowledge.

RAG

Question

↓

Embedding

↓

Vector Database

↓

Cosine Similarity

↓

Top chunks.

Spotify

Your listening history

↓

Preference Vector

↓

Cosine Similarity

↓

Songs.

Netflix

Movie Embeddings

↓

Cosine Similarity

↓

Recommendations."""

"""🧠 Mentor's Golden Rule

I want you to remember these two sentences forever.

Dot Product :

Measures similarity using direction + magnitude.

Cosine Similarity :

Measures similarity using direction only.

That's one of the most important distinctions in AI."""




