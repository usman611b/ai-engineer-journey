#📅 Day 04 – Session 02
#📘 Dictionary in Python
"""
This is one of the most important data structures in Python.

You'll use it in:

🌐 APIs
📄 JSON
🤖 AI
🧠 Machine Learning
⚡ FastAPI
🗄️ Databases
🔗 LangChain
🤖 OpenAI API responses
"""

#Step 1 — Why Do Dictionaries Exist?
"""
Imagine we want to store a student's information."""

#With a List:

student = ["Usman", 21, "BSCS", 3.20]

#Now I ask you:
"""
What is the student's CGPA?

You'd have to remember:"""

student[3]

"""
What does index 3 represent?

Name?
Age?
Department?
CGPA?

It's not obvious.

As the program grows, this becomes difficult to maintain.
"""
#Python's Solution

#Instead of using indexes, use meaningful names (keys) where keys are descriptive which represent the data they store.

student = {
    "name": "Usman",
    "age": 21,
    "department": "BSCS",
    "cgpa": 3.20
}

# Now we don't remember index 3.
#We simply write:

student["cgpa"]

#Much clearer.

"""
List answers:

"What is stored at position 3?"

Dictionary answers:

"Give me the value for the key cgpa."

That's why dictionaries exist."""

#Dictionary Syntax

students = {
    "name" : "Usman",
    "age" : 21,
    "department" : "BSCS",
    "cgpa" : 3.20
}

print(students)  # Output: {"name": "Usman", "age": 21, "department": "BSCS", "cgpa": 3.20}
print(students["name"])  # Output: "Usman"

#Topic 2 — Accessing Values

student = {
    "name": "Usman",
    "age": 21,
    "cgpa": 3.20
}
print(student["name"])  # Output: "Usman"
print(student["age"])   # Output: 21
print(student["cgpa"])  # Output: 3.20  

#⚠️ Important Difference
#What happens if the key doesn't exist?

print(student["department"])  # Raises KeyError

#Python provides a safer way:
print(student.get("department"))  # Output: None
print(student.get("department", "Key not found"))  # Output: "Key not found"

#🧠 Engineering Rule
"""
Use [] when you're 100% sure the key exists.
Use .get() when you're not sure.

Exactly like:

remove() vs discard() in Sets.
"""

"""Sets
remove()   ❌ Error if missing
discard()  ✅ Safe

Today:

Dictionaries
student["age"]        ❌ Error if missing
student.get("age")    ✅ Safe"""

# 🚀 Topic 3 — Adding & Updating Dictionary Values

student = {
    "name" : "Usman",
    "age" : 21,
    "cgpa" : 3.20
}

# Adding a new key-value pair
student["department"] = "BSCS"

# Updating an existing value
student["age"] = 22
student["cgpa"] = 3.50

print(student)  # Output: {"name": "Usman", "age": 22, "department": "BSCS", "cgpa": 3.50}

"""The same syntax does two different things.

If the key doesn't exist → it adds it.
If the key already exists → it updates the value."""

"""Lists
append()     → Add
list[i] = x  → Update

Dictionaries
dict[key] = value

This one statement handles both:

Add a new key
Update an existing key"""

#Topic — Removing Items
#1️⃣ pop(key)
student = {
    "name": "Usman",
    "age": 21,
    "cgpa": 3.20
}

age = student.pop("age")
"""age contains = 21
👉 pop() removes and returns the value"""

#2️⃣ del

del student["cgpa"]

"""Removes the key-value pair.

Unlike pop(), it doesn't return the removed value."""

#3️⃣ clear()

student.clear() # output = {} Everything is removed.

"""Use del:  when you simply want to remove a key-value pair and don't need its value anymore.
Use pop():  when you want to remove the key and also use the removed value later."""

# Topic 4 — Looping Through Dictionaries

student = {
    "name": "Usman",
    "age": 21,
    "department": "BSCS",
    "cgpa": 3.20
}

#Method 1 — Loop Through Keys (Default)

for key in student:
    print(key)

#Method 2 — Get Values Using Keys
for key in student:
    print(key ," : ", student[key])

#Method 3 — keys()
for key in student.keys():
    print(key)

#Method 4 — values()
for value in student.values():
    print(value)

#Method 5 — items() Most proffesional way , and used 
for key , value in student.items():
    print(key , " : " , value)










