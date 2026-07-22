#Lambda Functions

# A lambda function is a small anonymous(no name) function.
# A lambda function can take any number of arguments, but can only have one expression.

#how it differs from a normal function:
#A normal function is defined using the def keyword, while a lambda function is defined using the lambda keyword.
#In Lambda function there is no return statement , and only used one time,and not reusable, while normal function can be used multiple times. 

# We can use lambda functions wherever function objects are required.for example in higher-order functions, which take other functions as arguments.like map(), filter(), and reduce().
#Lambda functions are often used when you need a simple function for a short period of time, and you don't want to define a full function with the def keyword.



from functools import reduce # for reduce() function

# Normal Function
def double(x):
    return x * 2


# Lambda Version
lambda x: x * 2

# They do the same thing.
x = lambda a : a + 10
print(x(5))  # Output: 15

y = lambda a, b : a * b
print(y(5, 6))  # Output: 30

z = lambda a, b, c : a + b + c
print(z(5, 6, 7))  # Output: 18

a = lambda s : 'a ' in s
print(a("apple"))  # Output: True

a = lambda e : e % 2 == 0
print(a(4))  # Output: True

"""If lambda and normal functions do the same thing... why learn lambda?

Excellent question.

The answer is:

Because later we'll use it with things like: in Higher-Order Functions like:

map()

filter()

sorted()

Pandas

NumPy

There, writing a whole def function every time becomes unnecessary.

Lambda makes those operations short and readable."""



#So What is the Use of Lambda Functions?
#Lambda functions are used to create small, one-time, anonymous functions in Python. 
# They are often used in situations where a simple function is needed for a short period of time,
#  such as in higher-order functions like map(), filter(), and reduce(). 
# Lambda functions can also be used to create small utility functions 
# that are not intended to be reused elsewhere in the code.

#So what is a Higher-Order Function?
#A higher-order function is a function that takes one or more functions as arguments, or returns a function as its result. 

#Example of how it usable in Higher-Order Functions in Python:

#like this is the example of a normal function that takes another function as an argument:
def square(x):
    return x * x
def transform(func, L):
    output = []
    for i in L:
        output.append(func(i))
    print(output)

L = [1, 2, 3, 4, 5]
transform(square, L)  # Output: [1, 4, 9, 16, 25]

# So we can use lambda function instead of normal function in this example like this:

def transform(func, L): # so this is a higher-order function that takes another function as an argument.
    output = []
    for i in L:
        output.append(func(i))
    print(output)

L = [1, 2, 3, 4, 5]
transform(lambda x: x ** 2, L)  # Output: [1, 4, 9, 16, 25]
transform(lambda x: x + 10, L)  # Output: [11, 12, 13, 14, 15]
transform(lambda x: x ** 3 , L)  # Output: [1, 8, 27, 64, 125]

# So instead of defining a separate function like square(), Cube() , etc we can use a lambda function directly in the transform() call.
# This makes the code shorter and more readable, especially for simple operations.

#HIGHER-ORDER FUNCTIONS
#A higher-order function is a function that takes one or more functions as arguments, or returns a function as its result.

# Map Function (higher-order function)
# The map() function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator).
#  You can convert the map object to a list or other iterable types.


#map(function, iterable)

map (lambda x: x ** 2, [1, 2, 3, 4, 5]) # Output: <map object at 0x7f8c8c8c8c8c>
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) # Output: [1, 4, 9, 16, 25]

L = [1, 2, 3, 4, 5]
list(map(lambda x: "Even " if x % 2 == 0 else "ODD ", L)) # Output: ['ODD ', 'Even ', 'ODD ', 'Even ', 'ODD ']

temps = [20, 25, 30]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps)) # Output: [68.0, 77.0, 86.0]
print(fahrenheit)

user = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

list(map(lambda x: x["name"], user)) # Output: ['Alice', 'Bob', 'Charlie']

print(list(map(lambda x: x["age"], user))) # Output: [25, 30, 35]

#Filter Function (higher-order function)
numbers = [1,2,3,4,5,6,7,8,9,10]
# We want Output: [2,4,6,8,10] (only even numbers)
# We can use the filter() function to achieve this.use effectively with lambda functions.
"""filter()

The function returns:

True

or

False

Python asks:

"Should I keep this item?"

If the function returns:

True

✅ Keep it.

If it returns:

False

❌ Throw it away."""

numbers = [1,2,3,4,5,6,7,8,9,10]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result)) #output: [2, 4, 6, 8, 10]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
result = filter(lambda x: len(x) > 5, fruits)
print(list(result)) #output: ['banana', 'cherry', 'mango']

result = filter(lambda x: x.startswith("a"), fruits)
print(list(result)) #output: ['apple']

scores = [0.92, 0.35, 0.81, 0.20, 0.99]
result = filter(lambda x: x > 0.8, scores)
print(list(result)) #output: [0.92, 0.81, 0.99] 

#Reduce Function (higher-order function)
# The reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. 
# This function is defined in the functools module. unlike map() and filter(), we need to import it before we can use it.
# The reduce() function takes two arguments: a function and an iterable. 

#Suppose we have a list of numbers and we want to find the sum of all the numbers in the list.

#If we want to find the sum of all the numbers in a list, we can use a for loop to iterate through the list and add each number together.  

numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total += num

print(total)


#  We can use the reduce() function to achieve this.

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)
print(total) # output: 15

"""[1,2,3,4,5]

↓

1 + 2

↓

3

↓

3 + 3

↓

6

↓

6 + 4

↓

10

↓

10 + 5

↓

15"""

scores = [0.92, 0.35, 0.81, 0.20, 0.99]
from functools import reduce

total = reduce(lambda a, b: a + b, scores)

average = total / len(scores)

print(average)


"""🧠 The Big Picture
map()

Question:

How should I change every item?

Returns:----

List
filter()

Question:

Which items should I keep?

Returns:

List
reduce()

Question:

How can I combine everything into ONE value?

Returns:

Single value"""


#Difference Between (map(), filter(),  reduce()) and List Comprehension why we use seperately instead of using list comprehension for all three.
"""✅ Prefer list comprehensions for creating new lists.
✅ Use map() when you already have a function that you want to apply to every item.
✅ Use filter() when its intent ("keep matching items") makes the code clearer.
✅ Use reduce() only when you genuinely need to combine many values into one result."""



