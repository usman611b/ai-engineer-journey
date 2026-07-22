#Iterables & Iterators

#Step 1 — Imagine a Box of Books 📚
#Suppose you have a shelf:
books = ["Python", "AI", "ML", "DL"]

"""Question:

Can you read all the books?  --->> ✅ Yes.

Can you read them one by one?--->>> ✅ Yes.

Python calls this an iterable."""

#Iterables:
"""Definition : An iterable is any object that can be traversed (visited) one item at a time."""

"""Examples:

list
tuple
string
set
dictionary

All of these are iterables."""

numbers = [10, 20, 30]
for num in numbers:
    print(num)
"""Output:

10
20
30

So numbers is an iterable."""

#But Here's the Real Question...

"""

When you write: --->> for num in numbers:

How does Python know:

first → 10
then → 20
then → 30

Who keeps track?---->>> The iterator."""

#Step 2 — Iterator
"""Think of an iterator like a remote control.

The iterable is the movie collection.

The iterator says:

▶ Play next

↓

10

▶ Next

↓

20

▶ Next

↓

30

▶ Next

↓

End

It remembers where you currently are."""

#Step 3 — Creating an Iterator
# We use the iter() function to create an iterator from an iterable.
numbers = [10, 20, 30]

it = iter(numbers) # Create an iterator object

"""Now:

numbers → iterable
it → iterator
"""

#Step 4 — Getting the Next Item

#We use the next() function to get the next item from the iterator.
print(next(it)) # Output: 10
print(next(it)) # Output: 20
print(next(it)) # Output: 30

"""Every time you call:

next(it)

Python remembers where it stopped."""

"""numbers

[10,20,30]
      |
      v
 iterator
      |
next()
↓
10
next()
↓
20
next()
↓
30
next()
↓
❌ StopIteration"""

# The Secret Behind for Loop

numbers = [10, 20, 30]
for num in numbers:
    print(num)

#It is actually doing this behind the scenes:
it = iter(numbers) # Create an iterator object  
while True:
    try:
        num = next(it)
        print(num)
    except StopIteration:
        break

names = ["Ali", "Usman", "Ahmed"]

it = iter(names)

print(next(it))
print(next(it))
print(next(it))

while True:
    try:
        n1 = next(it)
        print(n1)
    except StopIteration:
        break





