#Modules:
""""Why do we need modules?
Modules are a way to organize code into separate files.
This makes it easier to manage and reuse code.

Example:

print(math.pi)  
Output:
3.141592653589793

so we need to import the math module first.
import math

print(math.pi)
Output:
3.141592653589793

so what is math module?
The math module is a built-in Python module that provides mathematical functions and constants.

which are some of the functions and constants in math module?
that help us to perform mathematical operations like trigonometry, logarithms, and more.


So what is a module in Python?
A module is simply a file containing Python code (functions, classes, variables, etc.) 
that can be imported and used in other Python programs.
"""

"""A module is simply:

A Python file (.py) that contains reusable code.

For example:

Suppose you have this file:"""

#calculator.py
#(This is a simple calculator module that contains two functions: add and subtract.)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#This file is called a module.
#------------------------------------------------------------------
# Now you create another file:

#main.py

#Instead of writing add() and subtract() again...

#ou simply import them.

#import calculator  Now you can use:

"""print(calculator.add(5, 3))

Output:  8
"""

# There are Different Ways to Import 
#1- import module_name (import the entire module)

"""import calculator  


print(calculator.add(5, 3))  # Output: 8
print(calculator.subtract(5, 3))  # Output: 2

"""
#2- from module_name import function_name (import specific functions from the module)

"""from calculator import add, subtract

print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
"""

#3- from module_name import * (import all functions from the module)
"""from calculator import *

print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
"""

#4- import module_name as alias (import the module with an alias)
#Why use an alias?
#Sometimes module names can be long or conflict with other names in your code.  
#Using an alias makes it easier to reference the module and shorter to Write.    
#For example:
"""import calculator as calc

print(calc.add(5, 3))  # Output: 8
print(calc.subtract(5, 3))  # Output: 2

"""
