#Packages:
"""A folder that contains multiple related modules."""
"""When you have multiple modules that are related to each other, you can organize them into a package."""
"""When you import a package, you can access all the modules inside it."""
"""Why we need packages?
To organize and manage large codebases, and to make it easier to reuse code across different projects."""

#Difference between a module and a package:
"""A module is a single file containing Python code, 
while a package is a folder that contains multiple related modules and a special __init__.py file."""

"""math_tools/
│
├── add.py
├── subtract.py
├── multiply.py
└── __init__.py"""

#Example of a package:
"""Real AI Example

When you write:

import sklearn

You're not importing one file.

You're importing an entire package.

Inside sklearn are many modules:

sklearn/
│
├── linear_model
├── svm
├── tree
├── preprocessing
├── metrics
└── cluster

That's why we can do things like:"""

#from sklearn.linear_model import LogisticRegression
"""Let's break it down:

sklearn → Package 📦
linear_model → Module 📄
LogisticRegression → Class 🏷️"""

"""Another Example
numpy

is actually a package.

Inside it are many modules.

Same for:

pandas
torch
transformers
tensorflow

These are all packages, not just single files."""

"""Why Packages Exist

Imagine NumPy had 10,000 functions in one file.

😵 It would be impossible to maintain.

Instead, developers organize related code into packages and modules."""

#Example of a package structure:
"""my_package/
│
├── __init__.py --- This file is required to make Python treat the directory as a package.because it can contain initialization code for the package.
├── module1.py
└── module2.py
"""

#example:
import numpy as np


np.array([1, 2, 3])  # Output: array([1, 2, 3])
np.mean([1, 2, 3])  # Output: 2.0


#-------------------------------------------------------------------------

# pip stands for "Pip Installs Packages" or "Pip Installs Python".
# pip is a package manager for Python that allows you to install and manage third-party packages and libraries that are not included in the standard library.
"""Suppose we  want to use NumPy.

Your computer only has Python installed.

If you write:

import numpy

Python says:

ModuleNotFoundError: No module named 'numpy'

🤔 Why do you think this happens?

Think conceptually.

Why doesn't Python already have NumPy?"""

"""NumPy is a third-party package, so Python doesn't include it by default. We must install it first.

You've got the concept.

Built-in vs Third-party Packages
✅ Built-in Modules (come with Python)

You can use them immediately:

import math
import random
import os
import datetime
import json

No installation needed.

📦 Third-party Packages

These are created by the Python community.

Examples:

numpy
pandas
matplotlib
scikit-learn
torch
transformers
opencv

Python doesn't ship with them because that would make Python huge, and not everyone needs every library."""

"""So What is pip?

Think of pip as Python's App Store 📱.

Just like:

Google Play installs Android apps.
App Store installs iPhone apps.

pip installs Python packages.

Example:

pip install numpy

After installation:

import numpy as np

Now it works.

Real AI Example

When we start AI, you'll install libraries like:

pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install torch
pip install transformers

This is how every AI developer sets up their environment."""

"""Most Common pip Commands

Install a package:

pip install numpy

Upgrade a package:

pip install --upgrade numpy

See installed packages:

pip list

Check package details:

pip show numpy

Uninstall a package:

pip uninstall numpy"""

# One More Important Thing
# pip install -r requirements.txt

"""A requirements.txt file contains the project's dependencies (the packages the project needs).

For example:

numpy==2.3.1
pandas==2.3.0
matplotlib==3.10.3
scikit-learn==1.7.0
torch==2.8.0
transformers==4.56.0

Notice the ==?

That specifies the exact version of each package."""

"""When you run:pip install -r requirements.txt"""
"""Why is this important?

Imagine I build an AI project and send it to another developer.

Without requirements.txt, I'd have to tell them:

Install NumPy...

Install Pandas...

Install PyTorch...

Install Transformers...

Instead, I simply send:

requirements.txt

Then others run one command:

pip install -r requirements.txt

Python installs everything automatically.

This is how almost every professional Python project works.

🧠 Real GitHub Workflow

When you download an AI project from GitHub, the first thing you'll usually do is:

git clone <repository>
cd project_folder
pip install -r requirements.txt

Now your computer has all the libraries needed to run the project."""



