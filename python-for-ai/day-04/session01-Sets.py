# Day 04 - Session 01.
# Sets in Python
"""
Why Did Python Create Sets?

Imagine Python only had Lists.
"""
courses = [
    "Python",
    "Python",
    "AI",
    "DBMS",
    "AI"
]

"""
Now suppose you want to know:

"Which unique courses has this student selected?"

With a List, you'd have to write extra logic to remove duplicates.

Python says:

"Why not create a data structure that automatically keeps only unique values?"

That data structure is a Set.
"""

"""Think of a Set Like This
📝 List

Attendance sheet:

Usman
Ali
Usman
Ahmed
Ali

Duplicates are allowed.

🎟️ Set

Entry gate to an event.

If Usman scans his ticket:

✅ Allowed

If he scans it again:

❌ Already entered.

Only one unique entry exists."""

# Set is a built-in data structure in Python that stores unique values in an unordered manner and are mutable.

# 📌 Set Properties

#✅ Unique Values
numbers = {1, 2, 3, 2, 1, 4}
print(numbers)  # Output: {1, 2, 3, 4}

#❌ No Indexing / Unordered
# print(numbers[0])  # This would raise a TypeError
"""Why?

Because Sets are unordered."""

# Creating Sets
#Method 1 (Most Common)

students = {"Usman", "Ali", "Ahmed"}
print(students)  # Output: {"Usman", "Ali", "Ahmed"}

#Method 2
#Convert a List into a Set.

courses_list = ["Python", "AI", "DBMS", "Python", "AI"]
courses_set = set(courses_list)
print(courses_set)  # Output: {"Python", "AI", "DBMS"}

"""This is very common in AI and data processing.

Example:

Imagine a dataset with 1 million email addresses.

Some emails are duplicated.

Instead of writing a loop to remove duplicates, you simply do:

unique_emails = set(emails)

Done."""

#Method 3
"""

Create an empty Set.

⚠️ This is a very common interview question.

Look at these two lines:

A = {}
B = set()

🎯 Question 4

Which one creates an empty Set?

A
B

And why do you think Python didn't use {} for an empty Set?"""

#The correct answer is:
"""

B creates an empty Set.

my_set = set()

Why not {}?

Because Python already uses {} for Dictionaries.

For example:

student = {} -> It is an empty Dictionary.

This is not a Set.

If Python also made {} an empty Set, it wouldn't know whether you wanted a Dictionary or a Set.

So Python decided:

{} → Dictionary
set() → Empty Set
Remember this interview question

What is this?

A = {}

Answer:

An empty Dictionary.

What is this?

B = set()

Answer:

An empty Set."""


# Topic 2 — Adding & Removing Elements (Set are also Mutable)
#✅ add()

students = {"Usman " , "Ali" , "Zain "}
students.add("Ahmed")
print(students)  # Output: {"Usman", "Ali", "Zain", "Ahmed"}

#Duplicate values are ignored.
students.add("Ali")
print(students)  # Output: {"Usman", "Ali", "Zain", "Ahmed"}


#❌ add() with a List or Tuple
# students.add(["Usman", "Ali"])  # This would raise a TypeError

#✅ remove()
students.remove("Ali")
print(students)  # Output: {"Usman", "Zain", "Ahmed"}

#❌ remove() with a value that doesn't exist
# students.remove("Ali")  # This would raise a KeyError

#✅ discard()
students.discard("Ali")  # No error, even if "Ali" doesn't exist

"""Engineering Rule:

Use remove() when you're sure the element exists.
Use discard() when you're not sure."""

# ✅ pop()
#Unlike Lists:
number = [10, 20, 30]
number.pop() # output: 30 (last element)

numbers = {10, 20, 30}

numbers.pop() # output: 10 (or 20 or 30, depending on the internal order)
"""
It removes and returns an arbitrary element, not the "last" one.

Why?

Because Sets are unordered."""

# ✅ clear() , i.e. remove all elements from the Set
students.clear()

#✅ del
del students  # Deletes the entire Set

# Topic 3 — Set Operations
#✅ Union

A = {"Python", "AI"}

B = {"AI", "DBMS"}

#Question: What courses are offered by both departments combined?

A | B
print(A | B)  # Output: {"Python", "AI", "DBMS"}

C = A.union(B)
print(C)  # Output: {"Python", "AI", "DBMS"}
""" Duplicates are automatically removed.
"""

#Intersection (&) 

#Question: Which course exists in both sets?

A & B
print(A & B)  # Output: {"AI"}

C = A.intersection(B)
print(C)  # Output: {"AI"}

#Difference (-)

#Question: Which courses are only in A?

A - B
print(A - B)  # Output: {"Python"}

C = A.difference(B)
print(C)  # Output: {"Python"}

#Symmetric Difference (^)

#Question: Which courses are in A or B but not both? like which courses not not common in both sets?

A ^ B
print(A ^ B)  # Output: {"Python", "DBMS"}

C = A.symmetric_difference(B)
print(C)  # Output: {"Python", "DBMS"}

#Membership : in and not in are used to check if an element exists in a Set or not.
#✅ in
#✅ not in

#Example:
A = {"Python", "AI", "DBMS"}
print("Python" in A)  # Output: True

print("Java" not in A)  # Output: True








    