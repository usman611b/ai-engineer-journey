# 📅 Day 02 — Session 02
# 🎯 Topic: Modules & Imports
"""This is a small topic, but it's extremely important because every AI project uses it.

Example:
import numpy as np
import pandas as pd
import torch
import tensorflow as tf
from fastapi import FastAPI

You can't build AI applications without understanding imports.
"""

# .🧠 Question 1 (Think First)
"""Imagine you write this in one file:"""

def add(a, b):
    return a + b
"""Now you create another Python file."""

"""Question:

Can the second file use the add() function directly?

Imagine:

calculator.py

def add(a, b):
    return a + b

main.py

print(add(5, 3))

How does main.py know that add() exists?

It doesn't.

Python only knows the code inside the current file unless you explicitly tell it to load another file.

That's exactly why import exists.

So your complete reasoning should be:

Each Python file has its own namespace. Another file cannot automatically access functions
 from a different file. We need to import that file first so Python knows where to find the function.

"""
# 🧠 Question 2
"""


Imagine a company has:

Project/

calculator.py

main.py

The add() function is inside calculator.py.

Why would engineers put add() in a separate file instead of writing everything inside main.py?

Imagine this:

main.py

2000 lines

Everything is inside one file.

😵 Nightmare.

Instead:

calculator.py

Contains:

add()
subtract()
multiply()
student.py

Contains:

check_grade()
scholarship()
main.py

Contains:

Only the program flow.

Now your answer becomes:

We separate code into different files to organize the project
, improve readability, make the code reusable,
 and make maintenance easier
"""
# Topic 1: Importing Multiple Functions
"""Suppose calculator.py contains:"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

"""
instead of writing:

from calculator import add
from calculator import subtract
from calculator import multiply

python allows you to write:

from calculator import add, subtract, multiply


"""
print(add(5, 3))
print(subtract(10, 4))
print(multiply(2, 6))

# Topic 2: Aliases (as)
"""Sometimes module names are long."""

"""
Example:

import numpy

Instead of writing:

numpy.array(...)
numpy.zeros(...)
numpy.ones(...)

Developers write:

import numpy as np

Now:

np.array(...)
np.zeros(...)

Same module.

Shorter name.
"""

#Topic 3: Built-in Modules
"""Python already gives us many modules"""

import math
import random
import datetime

print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.datetime.now())

"""
🧠 The Big Picture

Notice the pattern over the last two sessions:

Yesterday:

Repeated code

↓

Functions

Today:

Repeated functions

↓

Modules

Soon:

Repeated modules

↓

Packages

Then:

Repeated packages

↓

Libraries

Then:

Repeated libraries

↓

Frameworks

Software engineering is always about organizing and reusing code at a larger scale.
"""
# So the real reasoning is:
# Module vs Function

"""


We divide a large project into multiple modules because each module has one responsibility. This keeps the project organized, easier to read, easier to maintain, and allows different developers to work on different parts without interfering with each other.

Notice the difference?

Function → One task.
Module (file) → One related area of responsibility.
🧠 One sentence you'll remember

I want you to memorize this engineering principle:

A function should do one job. A module should group related jobs.

Examples:

math.py
├── add()
├── subtract()
├── multiply()

One module.

Many related functions.

pdf_reader.py
├── open_pdf()
├── extract_text()
├── get_pages()

One module.

Many related functions.
"""
# The Engineering Hierarchy
"""

1️⃣ Function

A function performs one specific task.

Example:

def extract_text():
    ...

One job.

Extract text.

Nothing else.

2️⃣ Module (.py file)

A module groups related functions (and sometimes classes and variables) that share the same responsibility.

Example:

pdf_reader.py

contains

open_pdf()

extract_text()

count_pages()

close_pdf()

All are related to PDF handling.

One responsibility.

3️⃣ Package (Folder)

A package groups related modules.

Example:

document_processing/
│
├── pdf_reader.py
├── word_reader.py
├── image_reader.py

Everything is about document processing.

Project
│
├── Package
│     │
│     ├── Module
│     │      │
│     │      ├── Function
│     │      ├── Function
│     │      └── Function
│     │
│     └── Module
│            │
│            ├── Function
│            └── Function
│
└── Package
"""