"""
Welcome to Session 2.

This is one of the most important sessions because every AI application uses conditional statements.

Think about it:


ChatGPT deciding whether to call a tool.
An AI agent checking if a user is authenticated.
A RAG system deciding whether to search a vector database.
A website deciding if a password is correct.

All of these rely on conditions.
"""
#Session 2: Conditional Statements

"""
Goal:
By the end of this session, you'll be able to:

Write complex decision-making logic.
Build login systems.
Validate user input.
Think like a programmer instead of memorizing syntax.

Before We Start

Imagine this scenario.

You're building an AI chatbot.

A user asks:

"Summarize my PDF."

Before your program does anything, it needs to ask itself:

Did the user upload a PDF?

YES → Summarize it

NO → Ask the user to upload one.

That's exactly what an if statement does.
"""

#Topic 1 — Comparison Operators
"""
==
!=
>
<
>=
<=
"""
age = 20
print(age > 18) # True
print(age < 18) 

print(age < 25) # True
print(10 == 10)# True
print(10 != 5)# True

#Topic 2 — if Statement

age = 20

if age >= 18:
    print("Adult")
"""
Notice the colon.

Notice the indentation.

Python uses indentation to know which code belongs to the if.
"""
marks = 85

if marks >= 50:
    print("Pass")

#Topic 3 — if-else Statement
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

"""
Practice Questions :

Write programs for:

1-Voting eligibility
2-Driving license eligibility
3-Even or Odd
4-Positive or Negative
"""
#Practice 1: Voting Eligibility
age = int(input("Enter your Age : "))

if age >=18:
    print("you are Eligiblle for vote:")
else:
    print("you are not eligible for vote:")

#Practice 2: Driving License Eligibility
age = int(input("Enter your Age : "))

if age >= 18:
    print("you are eligible for driving license:")
else:
    print("you are not eligible for driving license:")

#Practice 3: Even or Odd

num = int(input("enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Even number")       
    else:
        print("Odd number")
else:
    print("Please enter a positive number.")

#practice 4: Positive or Negative
num = int(input("enter a numbwer : "))
if num > 0:
    print ("Positive Number ")
else:
    print("Negative Number")


# Topic 4 — if-elif-else
# When there are multiple possibilities.
marks = 81

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("Fail")

# Topic 5 — Nested if

age = 21
has_id = True

if age >= 18:

    if has_id:
        print("Entry Allowed")

    else:
        print("Bring your ID")

else:
    print("Too Young")

# Topic 6 — Logical Operators
# and (Both conditions must be true)

age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome")

# or (At least one condition must be true)

is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access Granted")

# not (Reverses the value )

is_authenticated = False
if not is_authenticated:
    print("Please log in")

"""
Mini Challenge 1

Ask the user:

Age?

If

18 or above

Print

Eligible to Vote

Otherwise

Not Eligible
"""
age = int (input("Enter your age : "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

"""
Mini Challenge 2

Take username and password.

Correct values:

Username: admin

Password: python123

If both match:

Login Successful

Else

Invalid Credentials
"""

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == 'admin' and password == 'python123':
    print("Login Successful")
else:
    print("Invalid Credentials")
"""
Mini Challenge 3

ATM System

Ask:

Balance

Withdraw Amount

If amount is greater than balance:

Insufficient Balance

Else

Transaction Successful

Remaining Balance: ...
"""
balance = 1000
withdrawal_amount = int(input("Enter the amount to withdraw: "))

if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f"Withdrawal successful. New balance: {balance}")
else:
    print("Insufficient funds. Withdrawal denied.")

pdf = input("Have you uploaded a PDF? (yes/no): ").strip().lower()
if pdf == "yes":
    print("Summarizing your PDF...")
else:
    print("Please upload a PDF to summarize.")


"""
Practice Questions (20)
Easy
1-Check if a number is positive.
2-Check if a number is even.
3-Check voting eligibility.
4-Check if a student passed.
5-Check whether a number is greater than 100.
6-Check if two numbers are equal.
7-Check if a password is correct.
8-Compare two numbers.
9-Find the larger of two numbers.
10-Check whether a character is uppercase or lowercase.
Medium
11-Largest of three numbers.
12-Grade Calculator.
13-ATM Withdrawal.
14-Login System.
15-Age Category (Child/Teen/Adult/Senior).
16-Leap Year Checker.
17-Electricity Bill Calculator (simple slab logic).
18-BMI Category (Underweight/Normal/Overweight/Obese).
19-Movie Ticket Eligibility (age + payment).
20-Scholarship Eligibility (CGPA + attendance).
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}. ")
else:
    print(f"{num2} is greater than {num1}. ")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")

characters = input("Enter a character: ")
if characters.isupper():
    print("The character is uppercase.")
else:
    print("The character is lowercase.")

age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

unit = int(input("Enter the number of electricity units consumed: "))
if unit <= 100:
    bill = unit * 5
elif unit <= 200:
    bill = 100 * 5 + (unit - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (unit - 200) * 10
print(f"Your electricity bill is: Rs. {bill}")

print("===== LGU Student Portal =====")
print("#1. Check Result")
print("#2. Check Scholarship Eligibility")
print("#3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    marks = int(input("Enter your marks: "))
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C" 
    else:
        grade = "F"
    print(f"Your grade is: {grade}")


elif choice == 2:
    cgpa = float(input("Enter your CGPA : "))
    attendance = float(input("Enter your attendance percentage : "))    

    if cgpa >= 3.5 and attendance >= 85:
        print("Congratulations! You are eligible for the scholarship.")
    else:
        print("Sorry, you are not eligible for the scholarship.")
elif choice == 3:
    print("Exiting the portal. Have a great day!")
else:
    print("Invalid choice. Please select a valid option.")
