# Exception Handling
# Why do we need exception handling?
# Exception handling allows us to gracefully handle errors that may occur during program execution.
# It prevents the program from crashing and provides a better user experience.

#💡 The Problem

#Without Exception Handling:

"""
Start Program
      ↓
User enters wrong input
      ↓
💥 Program crashes"""

#With Exception Handling:

"""Start Program
      ↓
User enters wrong input
      ↓
Show friendly message
      ↓
Program keeps running"""

# The try Block

try:
    age = int(input("Enter age: "))
    print(age)
except:
    print("Invalid input!")

#Output: if user enters a non-integer value, it will print "Invalid input!" instead of crashing the program.

# A more specific example:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    name = "Usman"
    print(name[10])
except IndexError:
    print("Error: Index out of bounds.")

dic = {"name": "Usman"}

try:
    print(dic["age"])
except KeyError:
    print("Error: Key not found.")

#File Handling with Exception Handling
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")


# Explaining the code:
# The `try` block contains the code that might raise an exception.
# The `except` block(s) handle specific exceptions that may occur.

#why we use except ValueError and except ZeroDivisionError instead of a generic except:

"""Suppose there is another bug in your program unrelated to int().

A plain except: will hide that bug too, making debugging harder."""

# So it's better to catch specific exceptions to avoid masking other bugs.
#That why we use except ValueError and except ZeroDivisionError instead of a generic except.

# Concept: else

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result is: {result}")

# The `else` block runs only if no exceptions were raised in the `try` block.


# Finally Concept: finally

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

#The finally always runs, regardless of whether an exception occurred or not.
#  It is often used for cleanup actions, such as closing files or releasing resources.


 
   