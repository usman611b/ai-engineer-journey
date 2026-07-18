# Day 05 – Session 02
# Strings in Python
""""Next Topic: Strings

Why Strings?

If you become a:

Backend Developer ✅
AI Engineer ✅
Data Scientist ✅
Automation Engineer ✅

You'll manipulate text every single day.

Examples:

User names
Emails
Passwords
Chat messages
API responses
LLM prompts
AI outputs
JSON
Logs

Strings are everywhere."""

"""Session Plan
Session 1 — String Basics
✅ What is a String?
✅ Creating Strings
✅ Indexing
✅ Negative Indexing
✅ Slicing
✅ String Immutability

Session 2 — String Methods

upper()
lower()
title()
capitalize()
strip()
replace()
find()
count()
startswith()
endswith()

Session 3 — Splitting & Joining

split()
join()

Session 4 — Formatting

f-strings
format()

Session 5 — Mini Project

Password Validator
Email Validator
Username Checker"""

#What is a String?

# A string is a sequence of characters used to store text.
name = "Usman"
print(name)
"""Here:

U s m a n

Each letter is a character.

Together they form a string."""

#Just like Lists...
#Remember this?

fruits = ["Apple", "Banana", "Mango"]

#A list stores multiple separate values.

#A string stores multiple characters as one value.

#Example:

name = "Usman"


#Internally, Python sees:

#Index : 0 1 2 3 4
#Value : U s m a n

#So strings also support indexing.

# Why strings are immutable while lists are mutable.
"""The main reason is efficiency and safety"""

"""Imagine a passport number.

AB123456

Can you erase one character and make it:

AB923456

❌ No.

If you need a different passport number, you issue a new passport.

Strings work the same way.

Lists are like a notebook.

You can erase:

Apple

and write

Mango

at the same position."""

#String Slicing
#Slicing is a way to extract a portion of a string.

name = "Usman"
#Index : 0 1 2 3 4
print(name[0:3])  # Output: "Usm"

print(name[1:])  # Output: "sman"

print(name[:4])  # Output: "Usma"

print(name[:])  # Output: "Usman"


# String Methods
# Think of string methods as tools that help us manipulate text without changing the original string.

#1️⃣ upper() (Converts all characters in the string to uppercase.)
name = "Usman"
print(name.upper())  # Output: "USMAN"

#2️⃣ lower() (Converts all characters in the string to lowercase.)
name = "Usman"
print(name.lower())  # Output: "usman"

#3️⃣ title() (Capitalizes the first letter of each word in the string.)
sentence = "hello world"
print(sentence.title())  # Output: "Hello World"

#4️⃣ capitalize() (Capitalizes the first letter of the string and makes all other letters lowercase.)
sentence = "hello world"
print(sentence.capitalize())  # Output: "Hello world"

#5️⃣ strip() (Removes leading and trailing whitespace from the string.)
text = "   Hello World   "
print(text.strip())  # Output: "Hello World"

#6️⃣ replace() (Replaces a specified substring with another substring.)
text = "Hello World"
print(text.replace("World", "Python"))  # Output: "Hello Python"    

#7️⃣ find() (Returns the index of the first occurrence of a specified substring. Returns -1 if not found.)
text = "Hello World"
print(text.find("World"))  # Output: 6

#8️⃣ count() (Returns the number of occurrences of a specified substring.)
text = "Hello World"
print(text.count("o"))  # Output: 2

#9️⃣ startswith() (Checks if the string starts with a specified substring. Returns True or False.)
text = "Hello World"
print(text.startswith("Hello"))  # Output: True
print(text.startswith("World"))  # Output: False

#🔟 endswith() (Checks if the string ends with a specified substring. Returns True or False.)   
text = "Hello World"
print(text.endswith("World"))  # Output: True
print(text.endswith("Hello"))  # Output: False

# find() - (It returns the index of the first occurrence of a substring)

text = "Hello Python"
print(text.find("Python")) # Output is 6 
print(text.find("java")) # if not fount  Output is -1




name = " Usman  is a  boy "

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.strip())
print(name.replace("Usman" , "Ali"))
print(name.endswith("Usman"))
print(name.strip().startswith("Usman"))
