#Topic: Virtual Environment (venv)
"""Next Topic: Virtual Environment (venv)"""
"""Why Virtual Environment?"""

"""If you become a: Backend Developer ✅
AI Engineer ✅
Data Scientist ✅
Automation Engineer ✅

You'll use Python packages every single day...
Imagine this situation

You have two AI projects.

📁 Project A

Needs:

numpy 1.26

because it's an old project.

📁 Project B

Needs:

numpy 2.3

because it's a new project.

Now suppose you install:

pip install numpy==2.3

Your computer now has:

NumPy 2.3

Great!

But then you open Project A.

😨 It crashes because it was written for NumPy 1.26.
"""

"""How to Solve This Problem?"""
"""The solution is to create a virtual environment for each project.
A virtual environment is an isolated environment that allows you to manage dependencies for each project separately.
This way, you can have different versions of the same package installed for different projects without conflicts."""

"""Computer
│
├── Project A
│      ├── Python
│      └── NumPy 1.26
│
├── Project B
│      ├── Python
│      └── NumPy 2.3
│
└── Project C
       ├── Python
       └── PyTorch 2.8"""

#How to Create a Virtual Environment?
"""To create a virtual environment, you can use the built-in venv module in Python."""

"""Step 1: Open your terminal or command prompt.
Step 2: Navigate to your project directory.
Step 3: Run the following command to create a virtual environment:
python -m venv myenv
Replace 'myenv' with the name you want for your virtual environment.
"""

"""Step 4: Activate the virtual environment.
On Windows: myenv\Scripts\activate
On macOS/Linux: source myenv/bin/activate   """

