"""
Topic 1: Variables
What is a Variable?

Think of a variable as a labeled box that stores a value.

Imagine you have a box labeled age.

Syntax
age = 22

Here:

age → variable name
= → assignment operator
22 → value

Notice that = means assign, not equal to like in mathematics.

PRACTICE : 1

Create variables for:

Your name
Age
University
Semester
CGPA
Dream Job

Print them.
"""

my_name = "Usman Ali"
my_age = 21
my_university = "Lahore Garrison University"
my_semester = 6
my_CGPA = 3.3
my_dream_job = "Ai Engineer"

print ("My name is :" , my_name)
print ("My age is : ", my_age)
print ("My university is : ", my_university)
print ("My semester is : ", my_semester)
print ("My CGPA is : ", my_CGPA)
print ("My dream job is : ", my_dream_job)

"""
Topic 2: Data Types
Everything in Python is an object with a type.
The most common types you'll use are:

INTEGERS: Whole numbers, positive or negative, without decimals, of unlimited length. Example: 1, 100, -3

age = 22
marks = 100

FLOAT: Floating point numbers, positive or negative, containing one or more decimals. Example: 1.0, -3.14, 2.5e2
pi = 3.14
cost = 49.99
temperature = -273.15

STRING: A sequence of characters, enclosed in single or double quotes. Example: 'Hello', "World", '123'
name = "Usman Ali"
city = 'Lahore'

BOOLEAN: A data type with two possible values: True or False. Example: True, False
is_student = True
is_graduated = False

Checking Data Types

Python provides the built-in type() function.

age = 22

print(type(age))

Output:

<class 'int'>

Practice: 2
Create variables of each type and print both the value and its type.

Example output:

22
<class 'int'>

3.2
<class 'float'>

Usman
<class 'str'>

True
<class 'bool'>
"""
#practice 2

my_age = 22
print(my_age)
print(type(my_age))

my_cgpa = 3.3
print(my_cgpa)
print(type(my_cgpa))

name = "Usman Ali"
print(name)
print(type(name))

is_student= True
print(is_student)
print (type(is_student))

"""
Topic 3: User Input
Programs become useful when they interact with users.
Use input():
name = input("What is your name? ")
print("Hello, " + name + "!")

Important: input() always returns a string.

age = input("Enter age: ")
print(age)
print(type(age))

If you enter:
22
Output:
22
<class 'str'>

If you need to convert it to another type, use int(), float(), etc.

Topic 4: Type Casting

Because input() returns a string, you often need to convert it.

age = int(input("Enter age: "))

Now age is an integer.

Practice 3

Ask the user for:

Name
Age
Height
CGPA

Then print them along with their data types.

"""
#practice 3
name = input("Enter your name : ")
age = int(input("Enter your Age :"))
height = float(input("Enter your height : "))
cgpa = float(input("Enter your CGPA : "))

print("Name : " , name )
print (type(name))

print ("Age :" , age)
print (type(age))

print ("Height : " , height)
print (type(height))

print ("CGPA : " , cgpa)
print (type(cgpa))

"""
Topic 5: Operators

Operators perform actions on values.

+
-
*
/
//
%
**
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

What do these mean?
/ → Normal division

10 / 3 = 3.3333

// → Floor division

10 // 3 = 3

% → Remainder

10 % 3 = 1

** → Power

2 ** 5 = 32

Practice 4

Take two numbers from the user.

Print:

Sum
Difference
Product
Division
Floor Division
Modulus
Power
"""

#practice 4
num1 = int(input("Enter number 1 :"))
num2 = int (input("Enter number 2 : "))

print ("SUM : ", num1 + num2 )
print ( "Difference : " , num1 - num2 )
print ( "Product : " , num1 * num2 )
print ( "Division : " , num1 / num2 )
print ( "Floor Division : " , num1 // num2 )
print ( "Modulus : " , num1 % num2 )
print ( "Power : " , num1 ** num2 )


"""
Mini Challenge (No Help)

Build a program that asks for:

Name
University
Semester
CGPA

And prints a nicely formatted summary,
"""
#Challenge

name = input("Enter your name :")
university = input ("Enter your University name : ")
semester = int (input("Enter your Semester : "))
cgpa = float(input("Enter your CGPA : "))   

print ( "--------------Student Information ----------------")

print ("Name : " , name )
print ( "Unicersity : " , university )
print ("Semester : " , semester )
print ("CGPA : " , cgpa)

print ("----------------------------------------------------")

"""
Practice Questions :
Convert Celsius to Fahrenheit.
Convert Fahrenheit to Celsius.
Calculate the area of a rectangle.
Calculate the area of a circle.
Swap two variables without using a third variable.
"""
celcius = float(input("Enter the temoerature in Celsius :  "))
fahrenheit = (celcius * 1.8 ) + 32
print ("Temperature in Fahrenheit : " , fahrenheit)

fahrenheit = float(input("Enter the temperature in Fahrenheit :  "))
celcius = (fahrenheit - 32 ) * 0.5556
print ("Temperature in Celsius : " , celcius)

lenght = float(input("Enter the length of rectangle : "))
width = float(input("Enter the width of rectangle : ")) 
rectangle = lenght * width
print ("Area of rectangle : " , rectangle)

radius = float(input("Enter the radius of circle : "))
area = 3.14 * radius * radius
print ("Area of circle : " , area)

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)
