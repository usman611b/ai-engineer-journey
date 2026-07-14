# Session 3 – Loops
"""
First Principle (Very Important)
Ask Yourself:

Why did loops even get invented?

Imagine there were no loops.

You want to print:


    Welcome

10 times.

You would have to write:

print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")

Now imagine:

Reading 10,000 records
Processing 5,000 PDFs
Training on 1 million images
Sending emails to 20,000 users

Impossible without loops.

"""
# AI Example
"""Imagine you're building a chatbot.The user sends 100 messages."""
# Without loops:
"""
process(message1)
process(message2)
process(message3)

"""

# With loops:
"""
for message in messages:
    process(message)

"""
# Topic 1 — for Loop
# A for loop is used when you know (Number of iterations) a collection or a sequence .

for i in range(5):
    print(i)

# Topic 2 — Understanding range()
# It has three forms:
# 1. range(stop)
range(5)
""" Produces: 0, 1, 2, 3, 4 """
""" Meaning: Start at 0, stop before 5 """

# 2. range(start, stop)
range(2, 5)
""" Produces: 2, 3, 4 """
""" Meaning: Start at 2, stop before 5 """

# 3. range(start, stop, step)
range(0, 10, 2)
""" Produces: 0, 2, 4, 6, 8 """
""" Meaning: Start at 0, stop before 10, step by 2 """

# Reverse Counting
range(10, 0, -1)
""" Produces: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 """
""" Meaning: Start at 10, stop before 0, step by -1 """

""""Practice 1 """
for i in range(6):
    print(i)
""" Output: 0, 1, 2, 3, 4, 5 """

for i in range(3, 8):
    print(i)
""" Output: 3, 4, 5, 6, 7 """

for i in range(2, 12, 3):
    print(i)
""" Output: 2, 5, 8, 11 """

# Topic 3 — Using the Loop Variable
"""The loop variable is the variable that takes the value of the item inside
 the sequence on each iteration.and changes its value with each iteration."""


for i in range(5):
    print("Iteration:", i)

""" Output:
Iteration: 0 
Iteration: 1
Iteration: 2 
Iteration: 3
Iteration: 4
"""

# Topic 4 — while Loop
"""A while loop is used when you don't know the number of iterations in advance.
It continues to execute as long as the condition is True."""

count = 1

while count <= 5:
    print(count)
    count += 1
""" Output:
1
2
3
4
5
"""
""""
When to use while

Use while when you don't know in advance how many times the loop should run.

Examples:

1-Keep asking for a password until it's correct.
2-Keep reading user input until they type exit.
3-Keep retrying an API call until it succeeds (with limits)."""

# Topic 5 — Infinite Loops
while True:
    print("Hello")

# Topic 6 — break
"""break immediately exits the loop."""

for i in range(10):
    if i == 5:
        break

    print(i)

""" Output:
0
1
2
3
4
"""
# Topic 7 — continue

"""continue skip the current iteration and immediately 
jumps to the next iteration of the loop."""

for i in range(6):
    if i == 3:
        continue

    print(i)

""" Output:
0
1
2
The number 3 is skipped. due to the continue statement.
4
5
"""
# Topic 8 — pass

"""pass is a null statement in Python. It does nothing when executed."""

for i in range(5):
    pass

# Real AI Example
"""Imagine processing uploaded documents."""
documents = ["cv.pdf" , "notes.pdf" , "image.png"]

for doc in documents:
    if not doc.endswith("pdf"):
        continue
    print(f"Processing {doc}...")

"""
The program skips files that aren't PDFs.

That's a practical use of continue.
"""

"""---------------------------------------------------------------------"""
for i in range(1,21):
    print(i)

     
for i in range (2 , 50):
    if i % 2 == 0:
        print(i)
    else:
        continue

for i  in range (2 , 50 , 2):
    print(i)
num = 0
for i in range(1 , 101):
    num += i

print(num)

ask = input("Enter the password")

while ask != 'python123':
    ask = input("Enter the password")
print("Your password is correct")

num  = int(input("Enter the number for Multiplication table"))

for i in range(1 , 11):
    print(f" {num} * {i}  =  {num * i} " )

# Number Guessing Game

num = 27

guess = int(input("Enter your Guess"))
while guess != num:
    if guess > num:
        print("Guess Too High")
        guess = int(input(" Try Again ,Enter your Guess"))
    elif guess < num:
        print("Guess Too Low")
        guess = int(input("Try Again , Enter your Guess"))
print("Congratulations! You guessed the correct number.")
   

