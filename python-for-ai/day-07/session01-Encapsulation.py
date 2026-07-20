# OOP Pillar #1 — Encapsulation
#First we  must have to  understand WHY Encapsulation exists.

#Imagine This
#You created a Student object.

#student1 = Student("Usman",21,"CS",3.20)

"""Everything looks good.

Now imagine another programmer writes"""

# student1.cgpa = -15 (Can a student have  CGPA = -15 --->  Of course not.)

"""Another programmer writes"""

# student1.age = -5 (Can a student have age = -5 --->  Of course not.)

"""Another programmer writes"""
# student1.name = 123 (Can a student have name = 123 --->  Of course not.)

# Big Problem
"""Without Protection, any programmer can change the data of your object in a way that doesn't make sense."""
"""That is Dangerous. We need to protect the data of our object from being changed in a way that doesn't make sense."""

"""That is why Encapsulation exists.
Encapsulation is the process of protecting the data of an object from being changed in a way that and dont allow everyone to modify important data  directly.""
"""
#Before Encapsulation
"""
Student

↓

Anyone

↓

Change Anything

Dangerous."""

#After Encapsulation
"""Student

↓

Permission Check

↓

Allowed?

↓

Yes

↓

Change Data"""

# What is Encapsulation?
"""Encapsulation protects an object's data by preventing invalid or unauthorized modifications. 
It ensures that data is changed only through controlled methods where validation rules can be applied."""

"""Suppose I write

student.cgpa = 4.0

Should Python stop me?

Think carefully.

Because...

Sometimes changing CGPA is valid.

For example,

After semester results.

So...

Should Python completely block it?

🤔

No.

Instead...

Python should ask:

"Before changing the CGPA, let me check if the new value is valid."

Example:

Is CGPA >= 0 ?

YES

↓

Is CGPA <= 4 ?

YES

↓

Update

If someone writes

student.cgpa = 10

Then

10 <= 4 ?

NO

↓

Reject
⭐ This Is the Whole Purpose of Encapsulation

Not to stop changes.

But to ensure only valid changes happen.

That is a HUGE difference."""

# Now We Need One New Feature
"""How do we stop people from doing this?"""
"""We can make the attributes private by adding two underscores before their names (__cgpa). 
This way, they cannot be accessed directly from outside the class."""

#This Leads to Getters & Setters

#instead of directly accessing the attributes of an object,
# student.cgpa = -20
 
#  we use methods to get and set their values. These methods are called getters and setters.

#student.set_cgpa(3.5)  # Setter
#Setter are used to update the private data value of an attribute safely.
#Now insode the set_cgpa method, we can check if the new CGPA is valid before updating it.
#if 0 <= cgpa <= 4: ---|> then only update .


#Getters are used to retrieve the private data value of an attribute.
#student.get_cgpa()  # Getter




# CODE
# Student Class

class Student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.__cgpa = cgpa  # Private attribute

    # Getter for CGPA
    def get_cgpa(self):
        return self.__cgpa

    # Setter for CGPA
    def set_cgpa(self, new_cgpa):
        if 0 <= new_cgpa <= 4:
            self.__cgpa = new_cgpa
        else:
            print("Invalid CGPA. Must be between 0 and 4.")

# Can we do print(student.__cgpa)  # ❌ No, this will raise an AttributeError--->> bcz __cgpa is private and cannot be accessed directly from outside the class.
#that why we use getters and setters to access and modify the private attribute __cgpa safely.

student1 = Student("Usman", 21, 3.20)
print("Initial CGPA:", student1.get_cgpa())  # Using getter to access

student1.set_cgpa(3.5)  # Using setter to update
print("Updated CGPA:", student1.get_cgpa())  # Using getter to access

student1.set_cgpa(5.0)  # Attempt to set an invalid CGPA
#output: Invalid CGPA. Must be between 0 and 4.

"""Why Getter?

Answer

Because the variable is private. Getter provides controlled read access.

Why Setter?

Answer

Setter provides controlled write access. It validates the data before updating the object's private variable."""

class Bankaccount:

    def __init__(self , owner_name , balance):
        self.owner_name = owner_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    def set_deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print("Successfully deposit")
        else:
            print("Invalid Amount")
    def withdraw(self , amount):
        if amount > self.__balance:
            print("Amount is greater than your balance ")
        else:
            self.__balance -= amount
    
            
account1 = Bankaccount("Usman" , 1000) 
print(account1.get_balance())

account1.set_deposit(100)

