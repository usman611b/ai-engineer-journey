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

"""So Why Expose iter()?

Because not everything uses a for loop.

Sometimes you want control.

Imagine:

numbers = [10,20,30]

With a for loop:

for num in numbers:
    print(num)

Output:

10
20
30

It goes through everything.

You cannot stop after one element and continue later easily.

But With an Iterator...
it = iter(numbers)

print(next(it))

Output

10

Nothing else happens.

Later...

print(next(it))

Output

20

Later...

print(next(it))

Output

30

Now you control when to move forward.

Real AI Example

Imagine a dataset with

10,000,000 images

Do you want Python to load all of them?

❌ No.

Instead...

Load image 1

↓

Process it

↓

Load image 2

↓

Process it

↓

Load image 3

One at a time.

That's exactly how iterators and generators work."""

# Generators
#Now that we know about iterators, let's talk about generators.
#Imagine you have a huge dataset, and you want to process it one item at a time without loading the entire dataset into memory.
#  This is where generators come in handy.

#Example: Normal Function
def numbers():
    return [1, 2, 3, 4, 5]
result = numbers()
print(result)  # Output: [1, 2, 3, 4, 5]

#But if we have a huge dataset, this approach will consume a lot of memory.
"""But what if...

1 billion numbers

😱

Python tries to create:

[1,2,3,4,5,6,7........1000000000]

before returning.

Memory 💥"""

#Python Says...    Instead of returning everything...

# Let's return one item at a time.

#That's exactly what "yield" does.


#Normally, a function returns a value and exits. 
def numbers():
    return [1, 2, 3]

#Generators:
#But when you use "yield", the function will return a value and pause its state, allowing it to be resumed late
def numbers():
    yield 1
    yield 2
    yield 3
n = numbers()  # Create a generator object
print(next(n))  # Output: 1
print(next(n))  # Output: 2
print(next(n))  # Output: 3


#We can also use a loop to get all the values from the generator:
def numbers1():
    for i in range(1, 10):
        yield i

num = numbers1()  # Create a generator object
print(next(num))  # Output: 1
print(next(num))  # Output: 2
print(next(num))  # Output: 3

while True:
    try:
        itx = next(num)
        print(itx)
    except StopIteration:
        break




"""AI Example

Imagine you're training an AI model on 10 million images.

Do you think PyTorch loads all 10 million images into RAM?

❌ No.

It does something like:

for image in dataset:
    yield image

It loads:

Image 1

↓

Train

↓

Throw away

↓

Image 2

↓

Train

↓

Throw away

One image at a time.

That's why generators are so important in AI."""

"""A generator does not store all values in memory.

Instead, it:

Produces one value.
Pauses at yield.
Waits until next() (or a for loop) asks for the next value.
Continues from where it paused.

So instead of:

Memory

[1][2][3][4][5]...[1000000000]

It does:

Memory

[1]

↓

discard

↓

[2]

↓

discard

↓

[3]

↓

discard

Only the current value is being processed."""

def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

gen = demo()

print(next(gen)) # Output: Start returns 1 and pauses
print(next(gen)) # Output: Middle returns 2 and pauses
print(next(gen)) # This will raise StopIteration

# Generator Expressions
#Generator expressions are similar to list comprehensions, but they use parentheses instead of square brackets.

#Example: List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(type(squares))  # Output: <class 'list'>
print(squares)  # Output: [1, 4, 9, 16, 25]

#Example: Generator Expression
numbers = [1, 2, 3, 4, 5]
squares_gen = (x * x for x in numbers)
print(squares_gen)  # Output: <generator object <genexpr> at 0x7f8b8c0c1d30>
print(next(squares_gen))  # Output: 1
print(next(squares_gen))  # Output: 4
print(next(squares_gen))  # Output: 9
print(next(squares_gen))  # Output: 16
print(next(squares_gen))  # Output: 25


numbers = [1, 2, 3, 4, 5]

squares = (x**2 for x in numbers)

for num in squares:
    print(num)

#List vs Generator
"""
List Comprehension
squares = [x**2 for x in range(1000000)]

Python creates:

1,000,000 values

and stores them all in memory.

Generator Expression
squares = (x**2 for x in range(1000000))

Python creates:

Generator object

Only one value exists at a time."""

"""1. Generator Function

You write:

def numbers():
    yield 1
    yield 2
    yield 3

Here, you explicitly use yield.

2. Generator Expression

You write:

numbers = (x for x in range(1, 4))

Notice...

There is no yield.

Yet:

print(type(numbers))

Output:

<class 'generator'>

It's still a generator"""

"""So Where Is yield?

Python secretly creates it for you.

Think of this:

numbers = (x for x in range(5))

as roughly equivalent to:

def generator():
    for x in range(5):
        yield x

numbers = generator()

You don't write yield yourself because Python automatically generates that behavior behind the scenes"""
#When Should You Use Each?
#✅ Generator Expression


"""
Use it when the logic is simple:"""

(x**2 for x in range(100))

"""Short, clean, and readable."""

#✅ Generator Function
"""
Use it when the logic is more complex:"""

def process_data(data):
    for item in data:
        if item > 0:
            item = item * 2
            print("Processing:", item)
            yield item

"""You can't write that cleanly as a generator expression"""

#Difference Between Generator Function and Iterator Function

"""Generator Function

A function that uses yield to produce values one at a time. When called, it returns a generator object.

Iterator

An object that remembers its current position and returns one item at a time using next()."""
"""
A generator object is an iterator, but not every iterator is a generator.

For example:

numbers = [1, 2, 3]

it = iter(numbers)

it is an iterator, but it is not a generator.

Whereas:

def numbers():
    yield 1
    yield 2

gen = numbers()

gen is both:

✅ a generator
✅ an iterator
"""





