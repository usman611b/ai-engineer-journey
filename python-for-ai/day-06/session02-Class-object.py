#Class
from os import name


class Student:
    pass 
"""class is a keyword that tells Python:

"I'm creating a class  a new blueprint."""
#What is pass?
"""
Right now, our class has nothing inside it.
Python doesn't allow an empty block, so we write:
pass

It simply means:

"I'll add code here later."""

#Object
#Now we use the blueprint.
student1 = Student()
student2 = Student()

"""Student Class
      │
      ├────────► student1
      ├────────► student2
      └────────► student3
      """

# __init__() and self
#The Constructor
# __init__() is called the constructor.
"""A constructor is a special method that automatically runs when an object is created. 
It is used to initialize the object's data (attributes)."""

"""Imagine This

Toyota has a blueprint.

Car

Now they manufacture three cars.

Car 1

Color : Black
Engine : 1800cc
Owner : Ali

Car 2

Color : White
Engine : 1300cc
Owner : Ahmed

Car 3

Color : Red
Engine : 660cc
Owner : Sara

Question:

Where did these values come from?

The blueprint?

❌ No.

The blueprint only defines what every car should have.

The actual values are given when each car is created.

So how does Python know?"""

"""The Answer

When you create the object.

Like this:

student1 = Student("Usman", 21, "CS", 3.20)

Python now knows:

Name = Usman

Age = 21

Department = CS

CGPA = 3.20

Another object

student2 = Student("Ali", 20, "SE", 3.80)

Now

Name = Ali

Age = 20

Department = SE

CGPA = 3.80

Notice something?

The same class creates different students.

How?

Because every object receives different data.

So What Is __init__()?

Think of it as...

The object's birth certificate.

Whenever a new object is born...

Python automatically calls

__init__()

You never call it yourself.

Python does it for you.

Example
student1 = Student(...)

Python secretly does:

Create Object

↓

Run __init__()

↓

Store Data"""


"""def __init__

Why def?

Because...

Is __init__ a thing?

Or an action?

👉 It's an action.

So it's a function.

Inside a class, a function is called a method."""

"""only  we to understand one thing today:

When you write:

"""
class Student:
    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

students1 = Student("Usman", 21, "CS", 3.20)
print(students1.name)  # Output: Usman
print(students1.age)   # Output: 21

"""
Python automatically calls the constructor (__init__) and passes the data
 so the new object can store its own information."""

# Why we need __init __ constructor?
"""if there is no __init__ constructor we have to do this to store the data of new object:"""
student1 = Student()
student1.name = "Usman"
student1.age = 21
student1.department = "CS"
student1.cgpa = 3.20
"""But this is not a good way to store data because we have to write 4 lines of code for every new object."""

#With __init__ constructor we can store the data of new object in one line of code:
student2 = Student("Ali", 20, "SE", 3.80)

# Now we see what is Self in Python OOP.
"""Imagine This Classroom

You and your friend Ali are in the same classroom.

Teacher says:

"Write your name."

What happens?

You write:

Usman

Ali writes:

Ali

The teacher didn't have to say:

"Usman, write Usman."

"Ali, write Ali."

Each student automatically knows:

"This paper belongs to me."

self Means...

"Me."

Nothing more.

Nothing less.

self means: ----> This current object."""

#Example

student1 = Student("Usman", 21, "CS", 3.20)
student2 = Student("Ali", 20, "SE", 3.80)

#whenpython creates student1 object, it automatically passes the reference of student1 to self parameter of __init__ constructor.

"""self --> student1 """

#When python creates student2 object, it automatically passes the reference of student2 to self parameter of __init__ constructor.

"""self --> student2 """
"""So self is a reference to the current object.
"""
# Why Do We Write
"""
self.name = name
self.age = age
self.department = department
self.cgpa = cgpa
"""
"""self.name = name means:
Let's read it in English.

self.name ---> means  This object's name (like attribute it may be age, department, cgpa, etc.)

and

= name ---> means  equals the value passed in.

So if we create:

student1 = Student("Usman", 21)

Python effectively does:

student1.name = "Usman"
student1.age = 21

If we create:

student2 = Student("Ali", 20)

Python effectively does:

student2.name = "Ali"
student2.age = 20

That's why every object gets its own data.   
"""

"""The Complete Picture

Imagine:

student1 = Student("Usman", 21)
student2 = Student("Ali", 20)

Python secretly does something like this:

For student1
Create Object

↓

self → student1

↓

student1.name = "Usman"

student1.age = 21
For student2
Create Object

↓

self → student2

↓

student2.name = "Ali"

student2.age = 20

Now everything clicks:

self always points to the object currently being worked on.
self.name means this object's name.
self.age means this object's age.
🎯 Interview Question

If an interviewer asks:

What is self in Python?

A strong answer is:

self is a reference to the current object (instance) of a class. 
It allows each object to access and store its own attributes 
and call its own methods. Although it's just a parameter name by convention, 
Python programmers use self to make the code clear and consistent."""

#Complete Example of Class and Object
#step 1: Create a class
class Student:
    pass

#step2 : Add the __init__ constructor to the class
class Student:
    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

#step3 : Create objects of the class
student1 = Student("Usman", 21, "CS", 3.20)

student2 = Student("Ali", 20, "SE", 3.80)

# To access the attributes of the objects, we use dot notation:

print(student1.name)  # Output: Usman
print(student1.age)   # Output: 21
print(student1.department)  # Output: CS
print(student1.cgpa)   # Output: 3.2

print(student2.name)  # Output: Ali
print(student2.age)   # Output: 20
print(student2.department)  # Output: SE
print(student2.cgpa)   # Output: 3.8

# ⭐ Let's Add a Method
"""Earlier we learned

Functions perform actions.

Inside a class,

Functions are called

Methods

Now let's make a display method."""

class Student:

    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Department :", self.department)
        print("CGPA :", self.cgpa)

print("Student 1 Information:")
student1 = Student("Usman", 21, "CS", 3.20)
student1.display()  

#Here, we created a method called display() that prints the student's information.
#But here we also used self to access the object's attributes.

"""When we call
student1.display()

Python secretly does

Student.display(student1)

So inside the method

self → student1

Therefore

self.name ->> becomes -->> student1.name

Output: Usman"""

"""Today:

self → student1

Tomorrow:

self → student2

Then:

self → student500

The method doesn't care.

It simply says:

"Whoever called me, I'll work with that object."

That's why one method can work for thousands of objects."""

# Final Example of Class and Object
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2
    
calc = Calculator(10, 5)
print("Addition:", calc.add())        # Output: Addition: 15
print("Subtraction:", calc.subtract())  # Output: Subtraction: 5

# Instance Variable vs Local Variable:
# Instance variable is a variable that belongs to an instance of a class. It is defined inside the __init__ method and is prefixed with self. It is associated with the instance of the class and can be accessed using self.variable_name.
#It remains the same for the lifetime of the object and can be accessed by any method within the class.


# Local variable is a variable that is belong to Methods or function and is defined inside a method and is not prefixed with self. It is only accessible within that method and cannot be accessed outside of it.
#It is created when the method is called and destroyed when the method exits. It is not associated with any instance of the class and cannot be accessed by other methods within the class.

#Example of Instance Variable vs Local Variable
class Example:
    def __init__(self, value):
        self.instance_variable = value  # This is an instance variable

    def method(self):
        local_variable = 10  # This is a local variable
        print("Instance Variable:", self.instance_variable)
        print("Local Variable:", local_variable)  

# Return Value from Method
#Python methods can return values using the return statement. When a method is called, it can perform operations and return a result to the caller. The returned value can be stored in a variable or used directly in expressions.
# Example of Return Value from Method
class Student:

    def calculate(self):
        return 100

    def display(self):
        marks = self.calculate()
        print(marks)

student = Student()
student.display()  



