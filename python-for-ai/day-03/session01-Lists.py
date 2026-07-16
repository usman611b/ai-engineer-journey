# 📅 Day 03
# Session 01 — Lists
"""
🎓 Final Summary — Python Lists


📌 List Fundamentals
✅ Why lists exist
✅ Creating lists
✅ Storing collections of data

📌 Accessing Data
✅ Positive indexing
✅ Negative indexing
✅ Zero-based indexing

📌 Updating Data
✅ Mutable lists
✅ Updating elements

📌 Adding Data
✅ append()
✅ insert()
✅ extend()

📌 Removing Data

✅ remove()
✅ pop()
✅ del

📌 Utility Operations
✅ len()
✅ in
✅ not in
✅ sort()
✅ reverse()
✅ copy()

📌 Iteration
✅ for loop
✅ range()
✅ for i in range(len(...))

"""
"""
Many beginners think:

"Today we're learning Lists."

❌ Wrong.

Today we're learning:

How computers store and manage collections of data.

Lists are just Python's tool for doing that.
"""

#🌍 Real AI Examples
"""


Imagine you're building ChatGPT.

One user asks:

"Hello"

Another asks:

"Summarize this PDF"

Another asks:

"Translate this."

Can we store all these messages in one variable?

message = "Hello"

❌ No.

We need something that can store many values together.

That's why lists exist.

Another example.

Suppose you're training an AI model.

You have:

Image1
Image2
Image3
Image4
Image5
...
100000 Images

Will you create?

image1
image2
image3
...
image100000

😂 Impossible.

Instead:

images = [...]

One variable.

Thousands of values.
"""

#🧠 Question 1 (Think Like an Engineer)

"""


Suppose Python didn't have lists.

How would you store marks of 100 students?

Don't think about syntax.

Think about the problem.

What difficulties would you face?

Imagine you're working at Google.

Your manager says:

"We have 2 million users."

Will you create?

user1
user2
user3
...
user2000000

😂 Impossible.

Even 100 variables are painful.

2 million is unimaginable.

Let's identify the real engineering problems.

Without lists:

❌ Problem 1 — Too Many Variables
student1 = 90
student2 = 85
student3 = 92
...
student100 = 88

Imagine writing this every day.

❌ Problem 2 — Difficult to Process

Suppose I ask:

Calculate the average marks.

Without lists, what would you do?

(student1 + student2 + student3 + ... + student100) / 100

Terrible.

Now imagine 10,000 students.

❌ Problem 3 — Difficult to Loop

Yesterday we learned loops.

How would Python loop over:

student1
student2
student3
...

It can't.

A loop needs one collection to iterate over.

That's exactly what a list provides.

❌ Problem 4 — Difficult to Update

Suppose student #57 changes marks.

How do you know where student57 is?

Now imagine 50,000 students.

❌ Problem 5 — Hard to Organize

You mentioned something I liked:

"Two campuses."

Excellent.

Imagine:

Lahore Campus
1000 Students

Karachi Campus
1200 Students

Islamabad Campus
800 Students

Instead of thousands of variables, we can organize data into collections.

This idea scales to millions of records.
"""
# 🧠 Question 2
"""
Which is better?

Option A
student1 = 90
student2 = 85
student3 = 78
...
student100 = 91

or

Option B
students = [90, 85, 78, ..., 91]

Don't just say:

"Because it's easier."

Explain why.

What engineering problems does Option B solve?

Option B is better because it stores multiple related values inside a single variable
 instead of creating hundreds of separate variables. This makes the data easier 
 to organize, process, update, and maintain. It also allows us to use loops 
 and many built-in Python operations efficiently. As the amount of data grows 
 from 100 records to thousands or millions, the program remains scalable and much
 easier to manage.

"""
# 🧠 Question 3

"""

Yesterday we learned:

Function → One Task
Module → Collection of Related Functions

Now tell me...

What do you think a List is?

Don't search.

Don't guess syntax.

Just use your own reasoning.

A List is a data structure that stores a collection of related values 
in a single variable, allowing them to be organized, processed, updated,
 and accessed efficiently.

Function → One Task
Module → Collection of Related Functions
List → Collection of Related Values

"""

"""
Yet you've already understood why lists exist.

This is exactly how I want to teach you.

First understand the problem.

Then appreciate the solution.

Finally learn the syntax.

Most tutorials do it backwards.
"""

"""
Today I officially introduce you to one of the most important terms in Computer Science.
"""
#  Data Structure
"""
A data structure is simply:

A way of organizing data so that it can be stored, managed, and processed efficiently.

Read that again.

It doesn't say "List."

It doesn't say "Dictionary."

It says:

A way of organizing data.

Lists are one example.

Soon we'll learn:

1-List
2-Tuple
3-Set
4-Dictionary

All of them are Data Structures.
"""
# Topic 1 — Creating a List

students = [90, 85, 78, 91]

"""Lists Can Store Different Data Types"""

data = [10, "Usman", 3.14, True]
print(data)

"""Lists Can Store Other Lists

bcz 

Because a list element can be anything:

Integer ✅
String ✅
Float ✅
Boolean ✅
Another List ✅

This is called a Nested List.
"""

students = [
    ["Usman", 90],
    ["Ali", 85],
    ["Ahmed", 95]
]
"""
.

🌍 Real AI Example

Imagine you're building a Student AI System.

Instead of:

student1_name
student1_marks

student2_name
student2_marks

You can store everything like this:

students = [
    ["Usman", 90],
    ["Ali", 85],
    ["Ahmed", 95]
]

Later, an AI model can process this structured data much more easily.
"""

# Topic 2 — Indexing

"""
Before I teach you the syntax, I want you to think.

Imagine a bookshelf.

Books:

Python
C++
Java
JavaScript

Now I ask you:

"Give me the third book."

You immediately know where to look.

Why?

Because every book has a position.

Lists work the same way.

Every element has a position, called an Index.
"""

fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits[0]  # Apple
"""
Most beginners think:

Apple  → 1
Banana → 2
Mango  → 3
Orange → 4

❌ But Python doesn't think that way.

Python starts counting from 0.

Index

0 → Apple
1 → Banana
2 → Mango
3 → Orange
"""
# Topic 3 — Negative Indexing

"""
Think of a Train
                 Positive Index

                 0     1      2      3

              ┌──────┬──────┬──────┬──────┐
fruits =      │Apple │Banana│Mango │Orange│
              └──────┴──────┴──────┴──────┘

                -4     -3     -2     -1

                 Negative Index

Notice something interesting?

Positive indexing starts from the front.

Negative indexing starts from the back.
"""

"""
Without negative indexing, you'd first calculate:"""

messages[len(messages)-1]

"""
That's more work.

Python lets you simply write:

"""

messages[-1]

"""Much cleaner.
"""
"""
🌍 AI Engineering Connection

Imagine ChatGPT stores conversation history.

Message1
Message2
Message3
...
Latest Message

If we want only the newest message, we don't need to know how many messages exist.

We simply access:

conversation[-1]

This pattern appears constantly in:

AI chat history
Logs
Latest predictions
Recent transactions

"""
# Topic 4 — Accessing & Modifying List Elements
"""
Mutable

A mutable object is something that can be changed after it is created.

Lists are mutable.
"""
marks = [85, 90, 78, 92]

marks[1] = 95

print(marks)

# Topic 5 — Adding Elements to a List

"""Method 1 — append()
it adds a single element to the end of the list."""

marks = [85, 90, 78, 92]
marks.append(88)
print(marks)

"""Method 2 — insert()
it adds a single element at a specific index."""

marks = [85, 90, 78, 92]
marks.insert(2, 95)
print(marks)

# Topic 6 — Removing Elements from a List
# Method 1 — remove()
""" it removes the first occurrence of a specific value from the list."""
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

# Method 2 — pop()
""" it removes the last element from the list and returns it."""
fruits = ["Apple", "Banana", "Mango"]
last_fruit = fruits.pop()

""" it also removes an element at a specific index and returns it."""
fruits = ["Apple", "Banana", "Mango"]
specific_fruit = fruits.pop(1)
print(specific_fruit)

# Method 3 — del
""" it removes an element at a specific index without returning it."""
fruits = ["Apple", "Banana", "Mango"]
del fruits[1]
print(fruits)

"""and it also can delete the entire list."""
numbers = [10,20,30]

del numbers

""""""
# Topic 7 — len()

"""Think First

Imagine you're building a university portal.

The teacher asks:

"How many students are enrolled?"

Would you count manually?

Usman
Ali
Ahmed
Hamza
...

❌ No.

Python already knows the size of the list.

That's why len() exists."""

students = ["Usman", "Ali", "Ahmed"]

print(len(students))

# Topic 8 — in and not in
"""
Think First

Imagine you're building a university portal.

The teacher asks:

"Is Usman enrolled in the course?"

Would you manually check the list?

❌ No.

Python can quickly check for you.

That's why 'in' and 'not in' exist."""

students = ["Usman", "Ali", "Ahmed"]

print("Usman" in students)  # True
print("Sarah" not in students)  # True

# Topic 3 — Looping Through Lists

"""
Imagine you're building a university portal.
Imagine 10,000 students.

students = [
    "Usman",
    "Ali",
    ...
]

Would you do:

print(students[0])
print(students[1])
print(students[2])

10,000 times?

😂 Impossible.

Instead
"""

students = ["Usman", "Ali", "Ahmed"]

for student in students:
    print(student)

# Topic 4 — range()

"""
The `range()` function generates a sequence of numbers,
 which is often used with a `for` loop to iterate over a list by index.
"""

students = ["Usman", "Ali", "Ahmed"]

for i in range(len(students)):
    print(students[i])

students = ["Usman","Ali","Ahmed"]

print(len(students))

students = ["Usman","Ali","Ahmed"]

print("Ali" in students)

# Topic 6 — extend()

"""it adds multiple elements to the end of the list."""

"""Imagine two campuses."""

campus_a = ["Usman", "Ali"]
campus_b = ["Ahmed", "Hamza"]
"""
The university merges both campuses.

Should we add students one by one?
"""

campus_a.append("Ahmed")
campus_a.append("Hamza")

"""
❌ Too much work.

Instead:
"""
campus_a.extend(campus_b)

#Result:

["Usman", "Ali", "Ahmed", "Hamza"]
"""Difference
append()

Adds ONE element.

extend()

Adds ALL elements from another iterable."""

# Topic 7 — sort()

"""it sorts the list in ascending order by default."""
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

# Topic 9 — copy()

"""it creates a shallow copy of the list."""
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)

"""Now there are two separate lists.

Changing one won't affect the other.

We'll explore why later when we study memory and references.

For now, just remember:

copy() creates another independent list.
"""

# Topic 10 — clear()

"""it removes all elements from the list."""
students = ["Usman", "Ali", "Ahmed"]
students.clear()
print(students)  # []

# List Slicing

"""
List slicing allows you to extract a portion of a list.
The syntax is: list[start:stop:step]
"""

students = ["Usman", "Ali", "Ahmed", "Hamza"]

# Extract the first two students
print(students[0:2])

# Extract all students except the first one
print(students[1:4])

# Extract every second student
print(students[::2])

# Extract the last two students
print(students[-2:])

# from index 2 to the end
print(students[2:])

print(numbers[:3])
"""
This will output: [10, 20, 30] why because the slice numbers[:3] means "start from the beginning of the list and go up to, but not including, index 3." 
"""


# count()

"""It returns the number of occurrences of an element in the list."""
numbers = [1, 2, 3, 2, 4, 2]
print(numbers.count(2))  # Output: 3

# index()

"""It returns the index of the first occurrence of an element in the list."""
numbers = [1, 2, 3, 2, 4, 2]
print(numbers.index(2))  # Output: 1

numbers = [10,20,30,40,50]

