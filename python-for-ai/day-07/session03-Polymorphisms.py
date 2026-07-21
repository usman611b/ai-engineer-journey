
# ===========================================================
#                  POLYMORPHISM IN PYTHON
#                 Mentor Notes for Usman
# ===========================================================

"""
Poly = Many
Morph = Forms

Polymorphism means:
One interface (same method call)
Many different behaviors.

Think:

Teacher asks:
    "Introduce yourself"

Ali    -> I am Ali
Ahmed  -> I am Ahmed
Usman  -> I am Usman

Same question.
Different answers.

THAT is polymorphism.
"""

# -----------------------------------------------------------
# WHY DO WE NEED POLYMORPHISM?
# -----------------------------------------------------------

"""
Without polymorphism:

dog.sound()
cat.sound()
lion.sound()

Every object is handled separately.

With polymorphism:

for animal in animals:
    animal.sound()

One method call.
Different results.
Cleaner code.
"""

# -----------------------------------------------------------
# STEP 1 : Parent Class
# -----------------------------------------------------------

class Animal:

    def sound(self):
        print("Animal makes a sound")


# -----------------------------------------------------------
# STEP 2 : Method Overriding
# -----------------------------------------------------------

class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


class Lion(Animal):

    def sound(self):
        print("Lion roars")

"""
Up to this point we are doing METHOD OVERRIDING.

Each child class creates its own implementation of sound().
"""

print("\n--- Individual Calls ---")
Dog().sound()
Cat().sound()
Lion().sound()

# -----------------------------------------------------------
# STEP 3 : REAL POLYMORPHISM
# -----------------------------------------------------------

print("\n--- Polymorphism ---")

animals = [Dog(), Cat(), Lion()]

for animal in animals:
    animal.sound()

"""
Question:

How many times did we write

animal.sound()

Only ONE.

How many outputs?

Three.

Dog -> Bark
Cat -> Meow
Lion -> Roar

This is POLYMORPHISM.
"""

# -----------------------------------------------------------
# PYTHON THINKS LIKE THIS
# -----------------------------------------------------------

"""
animal.sound()

Iteration 1

animal = Dog()

↓

Dog has sound() ?

YES

↓

Run Dog.sound()

----------------------------

Iteration 2

animal = Cat()

↓

Cat has sound() ?

YES

↓

Run Cat.sound()

----------------------------

Iteration 3

animal = Lion()

↓

Lion has sound() ?

YES

↓

Run Lion.sound()
"""

# -----------------------------------------------------------
# ANOTHER EXAMPLE
# -----------------------------------------------------------

class Employee:

    def work(self):
        print("Employee works")


class Developer(Employee):

    def work(self):
        print("Writing Python Code")


class Manager(Employee):

    def work(self):
        print("Managing Team")


class Designer(Employee):

    def work(self):
        print("Designing UI")


print("\n--- Employee Example ---")

employees = [
    Developer(),
    Manager(),
    Designer()
]

for emp in employees:
    emp.work()

# -----------------------------------------------------------
# PAYMENT EXAMPLE
# -----------------------------------------------------------

class Payment:

    def pay(self):
        pass


class JazzCash(Payment):

    def pay(self):
        print("Paid using JazzCash")


class EasyPaisa(Payment):

    def pay(self):
        print("Paid using EasyPaisa")


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


print("\n--- Payment Example ---")

payments = [
    JazzCash(),
    EasyPaisa(),
    CreditCard()
]

for payment in payments:
    payment.pay()

# -----------------------------------------------------------
# SHAPE EXAMPLE
# -----------------------------------------------------------

class Shape:

    def draw(self):
        print("Drawing Shape")


class Circle(Shape):

    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle")


print("\n--- Shape Example ---")

shapes = [
    Circle(),
    Rectangle()
]

for shape in shapes:
    shape.draw()

# -----------------------------------------------------------
# DIFFERENCE
# -----------------------------------------------------------

"""
METHOD OVERRIDING

Child creates a new implementation.

Example

Dog.sound()

Cat.sound()

Lion.sound()

------------------------------------

POLYMORPHISM

Uses those implementations.

Example

for animal in animals:
    animal.sound()

Same method.

Different behavior.
"""

# -----------------------------------------------------------
# WHY POLYMORPHISM?
# -----------------------------------------------------------

"""
Advantages

1. Cleaner Code

2. Less if/else

Instead of

if animal == Dog:
    ...

if animal == Cat:
    ...

Simply

animal.sound()

3. Easy to add new classes

Tomorrow

Cow()

Just override sound()

No need to change existing loop.

4. Easy Maintenance

5. Better Software Design
"""

# -----------------------------------------------------------
# INTERVIEW DEFINITIONS
# -----------------------------------------------------------

"""
Q. What is Polymorphism?

Polymorphism is the ability of different objects
to respond differently to the same method call.

--------------------------------------


Q - Why we need it ?
We use polymorphism so we don't have to keep changing our code every time a new class is added.

or

We use polymorphism to write one piece of code that works with many different objects.

That's the biggest benefit.

with just this lineof code 
animal = [Dog(), Cat(), Lion()]
for animal in animals:
    animal.sound()

as amany as classes we add it works with all of them.

rather than writing 100 if else statements for 100 classes.
example
dog.sound()
cat.sound()
lion.sound()
that's not a good way to write code.


Q. Difference between Overriding and Polymorphism?

Overriding:
Creates different implementations.

Polymorphism:
Uses those implementations through one interface.

---------------------------------

Q. Can Polymorphism exist without Inheritance?

The most common runtime polymorphism in Python
comes from inheritance + method overriding.

"""

# -----------------------------------------------------------
# MEMORY TRICK
# -----------------------------------------------------------

"""
Inheritance

IS A

Dog IS AN Animal

------------------------

Composition

HAS A

Car HAS AN Engine

------------------------

Overriding

Create different behavior.

------------------------

Polymorphism

Use ONE method call.

animal.sound()

Different objects

Different outputs.
"""

# -----------------------------------------------------------
# PRACTICE
# -----------------------------------------------------------

"""
1. Vehicle

Car

Bike

Airplane

Override move()

Use

for vehicle in vehicles:

    vehicle.move()

--------------------------------

2. Notification

Email

SMS

PushNotification

Override send()

Use one loop.

--------------------------------

3. Animal

Cow

Horse

Elephant

Override sound()

Use one loop.

"""

print("\nCongratulations! You finished Polymorphism.")
