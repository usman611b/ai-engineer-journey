#OOP Pillar #2 — Inheritance

#🏢 Imagine You Work at Google
"""Google has employees.

Every employee has:

Name
Age
Salary

Now Google has different types of employees.

Developer , Manager , Designer ,HR

Question.

Should we write

class Developer

and again write

Name

Age

Salary

?

Then for Manager again?

Name

Age

Salary

Again?

For Designer?

Again?

😵

This Is Called
Code Duplication

Imagine

class Developer:

    name

    age

    salary

and

class Manager:

    name

    age

    salary

Same code.

Again.

Again.

Again."""

"""Because if tomorrow

Google says

Every employee now also has

Employee ID

Now you must edit

Developer

Manager

Designer

HR

...

100 classes."""

#The Better Idea
"""Instead of writing the same code again and again, we can write a base class called Employee."""
from dbm.ndbm import library


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

"""Now

Developer --> doesn't need to rewrite them.

Manager --->doesn't need to rewrite them."""

"""                 Employee

          Name

          Age

          Salary

          /      |      \

         /       |       \

Developer  Manager  Designer 

Notice something?

Developer IS AN Employee.

Manager IS AN Employee.

Designer IS AN Employee.

⭐ The Golden Rule of Inheritance

Whenever you hear

IS A

Think

Inheritance.

Examples:

Dog IS AN Animal

Cat IS AN Animal

Car IS A Vehicle

Bike IS A Vehicle

Teacher IS AN Employee

Developer IS AN Employee

Inheritance.

When NOT to Use Inheritance

Suppose

Car

Engine

Question.

Is

Engine IS A Car?

😂

No.

Car HAS AN Engine.

Not

IS A.

This is composition, not inheritance.

We'll study it much later.

⭐ Real-Life Examples
Correct
Lion IS AN Animal

Inheritance.

Correct
Apple IS A Fruit

Inheritance.

Wrong
Wheel IS A Car

❌

No.

Wheel is part of a car.

Wrong
Keyboard IS A Laptop

No.
"""
#Inheritance in Python
"""Inheritance allows us to reuse existing code instead of writing the same code again.

Inheritance allows a child class to reuse the attributes and methods of a parent class. 
It reduces code duplication, improves maintainability, and models real-world "is-a" relationships.
"""


# Code 
class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    pass  # Dog inherits from Animal, so it has access to eat() and sleep() methods

dog1 = Dog()
dog1.eat()  # Output: Eating
dog1.sleep()  # Output: Sleeping

"""Dog inherits from Animal. Since eat() is already defined in the parent class, 
the Dog object can directly use it without rewriting the method. 
Python first looks inside the Dog class, and if it doesn't find the method there, 
it searches the parent class (Animal)."""

"""Dog

↓

Do I have eat()?

↓

No

↓

Go to Animal

↓

Found

↓

Run it"""

class Cat(Animal):
    pass  # Cat inherits from Animal, so it has access to eat() and sleep() methods

cat1 = Cat()
cat1.eat()  # Output: Eating
cat1.sleep()  # Output: Sleeping

"""same as for cat reuse is the main advantage of inheritance."""

#Suppose we want :
"""Dog

↓

eat()

↓

"Dog is eating meat"""
"""Question...

Should we go to the Animal class and change it?

❌ NO.

Because then

Cat

Lion

Elephant

Cow

all change too.

We only want Dog to behave differently."""

#This is called  -->>> Method Overriding
class Dog(Animal):

    def eat(self):
        print("Dog is eating meat")

dog2 = Dog()
dog2.eat()  # Output: Dog is eating meat (overridden method)
dog2.sleep()  # Output: Sleeping (inherited from Animal)

"""Dog just overrides the eat() method from the Animal class.The sleep() method is still inherited from the Animal class, so it behaves the same way as before."""
"""This is one of the MOST IMPORTANT rules in OOP

The child class only replaces the methods it overrides. Everything else is still inherited from the parent."""

#Method Overriding

#Definition (Interview)

#Method Overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")
    
    def debug(self):
        print("Fixing bugs")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

emp = Employee()
emp.work()  # Output: Employee is working

dev = Developer()
mgr = Manager()
dev.work()  # Output: Developer is writing code
dev.debug()  # Output: Fixing bugs
mgr.work()  # Output: Manager is managing the team

"""Difference between Inheritance and Overriding?

Inheritance--->> Child gets methods from parent.

Method Overriding ---->> Child replaces one inherited method with its own implementation."""

# Suppose we want both methods like this:
# when we call work() :Both the parent and child methods should run.
# Output: Developer is writing code
# Output: Employee is working

#We can do this by using super() function.

class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def work(self):

        super().work()  # Call the parent class method

        print("Developer is writing code")

        print("Writing Python code")

dev = Developer()
dev.work()
# Output:
# Employee is working
# Developer is writing code
# Writing Python code

"""Why?

Because --->> super() means -->> "Go to my parent class.

super().work() means -->> "Go to my parent class and run the work() method from there.
 ANd then come back here and continue running the rest of the code in this method."""
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()

dog.sound()

"""
Dog

↓

Found sound()

↓

Run Dog.sound()

↓

super().sound()

↓

Go to Animal

↓

Run Animal.sound()

↓

Return to Dog.sound()

↓

print("Dog barks")

↓

Finished

"super() calls the parent method from inside the child method.
 After the parent method finishes, the child method continues executing."
"""
#Composition vs Inheritance
"""Composition is a design principle where one class contains an instance of another class,
 allowing for code reuse and flexibility. Inheritance, on the other hand,
establishes an "is-a" relationship between classes, enabling a child class to
inherit attributes and methods from a parent class. While inheritance promotes
code reuse through hierarchical relationships, composition emphasizes building 
complex objects by combining simpler ones, offering greater flexibility and reducing tight coupling between classes."""

class Engine:

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")


class Car:

    def __init__(self, brand, horsepower):
        self.brand = brand

        # Composition
        self.engine = Engine(horsepower)

    def start_car(self):
        print(f"{self.brand} is starting...")
        self.engine.start()


# Create object
car1 = Car("Toyota", 180)

# Start the car
car1.start_car()

# Output:
# Toyota is starting...
# Engine with 180 HP started.

"""Q: When should we use Inheritance?

Use inheritance when there is an "IS A" relationship and the child class 
should inherit the behavior and attributes of the parent class.

Q: When should we use Composition?

Use composition when there is a "HAS A" relationship and one object contains 
or uses another object as one of its parts."""


class Book:
    def __init__(self , name):
        self.name = name 

    def display(self):
        print(f"{self.name} is book in this library!")

class Library:
    def __init__(self ,  lib_name , name ):
        self.lib_name = lib_name
        self.book = Book(name)
    
    def display_lib(self):
        print(f"{self.lib_name} is our library name ")
        self.book.display()

lib = Library("OOP " , "LGU ")
lib.display_lib() 
