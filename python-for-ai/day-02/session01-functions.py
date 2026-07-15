"""
===============================================================================
                            AI ENGINEER JOURNEY
-------------------------------------------------------------------------------
Day        : 02
Session    : 01
Topic      : Functions
Author     : Usman Ali

Description:
This session covers Python Functions from first principles.
Instead of memorizing syntax, the focus is on understanding why
functions exist, how Python executes them, and how they help us
write reusable and maintainable software.
----------------------

===============================================================================
"""

# =============================================================================
# 1. WHY FUNCTIONS?
# =============================================================================

"""
Problem:
Without functions, we repeat the same logic many times.

Solution:
Write the logic once and reuse it whenever needed.

Key Idea:
Functions improve:
- Reusability
- Readability
- Maintainability
"""

# Example
def greet():
    print("Hello AI Engineer")

greet()


# =============================================================================
# Practice 01 : Function Definition & Function Call
# =============================================================================

"""
Question:
What is the difference between defining a function and calling a function?

My Understanding:

• Function Definition:
  Stores the instructions in memory.

• Function Call:
  Executes those stored instructions.

Mentor Note:
Definition ≠ Execution
"""

def welcome():
    print("Welcome!")

welcome()


# =============================================================================
# 2. PARAMETERS & ARGUMENTS
# =============================================================================

"""
Parameter:
A placeholder that receives a value.

Argument:
The actual value passed while calling the function.

My Logic:

Instead of creating separate functions for every person,

greet_ali()
greet_usman()
greet_sara()

we create one reusable function.

Reason:
The parameter allows us to change the value whenever we call it.
"""

def greet(name):
    print(f"Hello {name}")

greet("Usman")


# =============================================================================
# Practice 02 : Positional Arguments
# =============================================================================

"""
Question:
Why does add(4,5) assign 4 to 'a' and 5 to 'b'?

My Answer:

Python matches arguments according to their position.

First Argument  → First Parameter
Second Argument → Second Parameter

Mentor Feedback:
Correct.
Python follows position, not meaning.
"""

def add(a, b):
    print(a + b)

add(4, 5)


# =============================================================================
# 3. print() vs return()
# =============================================================================

"""
print()

Displays the result on the screen.

return()

Sends the result back to the caller.

My Understanding:

print() only shows the value.

return() allows us to store the value in another variable
and use it later.
"""

def multiply(a, b):
    return a * b

result = multiply(5, 6)

print(result)


# =============================================================================
# Practice 03 : My Explanation
# =============================================================================

"""
My Answer:

When a function returns a value,

Python sends that value back to the place where
the function was called.

Example:

result = multiply(5,6)

The returned value is stored inside 'result'.

This allows us to reuse the value later.
"""


# =============================================================================
# 4. DEFAULT PARAMETERS
# =============================================================================

"""
Purpose:

Avoid writing the same common value again and again.

Example:

If every student speaks English,

language="English"

can be used as a default value.
"""

def introduce(name, language="English"):
    print(name, "-", language)

introduce("Usman")
introduce("Ali", "Urdu")


# =============================================================================
# 5. KEYWORD ARGUMENTS
# =============================================================================

"""
Why Keyword Arguments?

My Answer:

They improve readability.

Instead of remembering parameter positions,
we explicitly mention each parameter.
"""

def student(name, age, cgpa):
    print(name)
    print(age)
    print(cgpa)

student(
    name="Usman",
    age=22,
    cgpa=3.25
)


# =============================================================================
# 6. LOCAL vs GLOBAL VARIABLES
# =============================================================================

"""
Office Analogy

Notebook
→ Local Variable

Whiteboard
→ Global Variable

My Logic:

Notebook:
Only one employee can access it.

Whiteboard:
Everyone can see it.

Exactly the same concept applies in Python.
"""

name = "Usman"

def change_name():
    name = "Ali"
    print(name)

change_name()

print(name)


# =============================================================================
# Practice 04 : Predict the Output
# =============================================================================

"""
Question

name = "Usman"

def change():
    name = "Ali"
    print(name)

change()

print(name)

My Prediction:

Output

Ali
Usman

Reason:

Inside the function,
Python uses the local variable.

Outside the function,
Python uses the global variable.
"""


# =============================================================================
# 7. SOFTWARE DESIGN
# =============================================================================

"""
Mini Project

AI Student Portal

Instead of writing one large function,

I designed separate responsibilities.

Functions:

display_menu()

check_grade()

check_scholarship()

study_recommendation()

main()

Mentor Lesson:

One Function
↓

One Responsibility
"""


# =============================================================================
# SESSION REFLECTION
# =============================================================================

"""
Today's Biggest Learning

✓ Functions exist to reduce repetition.

✓ Parameters make functions reusable.

✓ Arguments provide actual values.

✓ return() sends values back to the caller.

✓ Default parameters reduce repetitive code.

✓ Keyword arguments improve readability.

✓ Python searches Local Scope before Global Scope.

✓ Before writing code,
  think about the responsibility of each function.


"""