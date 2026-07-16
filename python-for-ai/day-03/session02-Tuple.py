# Session 02 - Tuple

"""
Imagine you're building a university system.

Some data changes:

Student List

Students can:

Join
Leave
Update names

➡️ Use List.

Now think about:

Days of Week

Monday
Tuesday
Wednesday
...

Should someone accidentally change:

Monday → Pizza

😂 Obviously not.

Some data should never change.

Python says:

"Use a Tuple."
"""
"""Tuple is a collection of items which is ordered and unchangeable.
   In Python tuples are written with round brackets ().
   
   Notice:

List → [ ]
Tuple → ( )
   """

# Tuple Concepts
"""
1. Ordered
2. Unchangeable
3. Allow Duplicates
"""
colors = ("Red", "Green", "Blue")

print(colors[1])

numbers = (10,20,30)

print(numbers[-1])

days = ("Mon","Tue","Wed")

for day in days:
    print(day)

# 1️⃣ Packing
# Packing is the process of assigning multiple values to a single variable.
# Example:
student = "Usman", 21, "CS"
print(student)

"""
Did I use parentheses?

❌ No.

But Python automatically creates:
"""
# Unpacking
# Unpacking is the process of extracting values from a tuple and assigning them to separate variables.
# Example:

student = ("Usman", 21, "CS")

#Instead of writing:
name = student[0]
age = student[1]
department = student[2]

# Python lets us do:
name, age, department = student
print(name)
print(age)
print(department)

# 3️⃣ Tuple Methods

#Tuples have only 2 methods.

# count() - Returns the number of times a specified value occurs in a tuple
fruits = ("apple", "banana", "cherry", "apple")
print(fruits.count("apple"))
# index() - Searches the tuple for a specified value and returns the position of where it was found
print(fruits.index("banana"))


"""📊 Tuple vs List
Feature	            List  Tuple
Mutable      	    ✅	❌
Add Elements	    ✅	❌
Remove Elements	    ✅	❌
Update Elements	    ✅	❌
Indexing            ✅	✅
Looping     	    ✅	✅
Slicing	            ✅	✅
Memory Efficient    ❌	✅ (slightly)
Best For	    Changing Data	Fixed Data"""


"""🧠 The Rule I Want You to Remember Forever

Don't ask:

"Is this data important?"

Ask:

"Will this data change?"

If it changes →

✅ List

If it should remain fixed →

✅ Tuple

That simple question will guide you correctly most of the time"""