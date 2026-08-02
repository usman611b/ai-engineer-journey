import numpy as np
#Random Module
#Random module is used to generate random numbers in Python. It provides various functions to generate random numbers, select random elements from a list, shuffle elements, and more.
#Why do we need random numbers?
#Random numbers are used in various applications such as simulations, games, cryptography, and statistical

"""Imagine you're training a neural network.

Should every neuron start with weight:

0
0
0
0

❌ No.

All neurons would learn the same thing.

Instead, we initialize them randomly.

Example:

0.23
-0.54
1.11
0.07

Random numbers are also used for:

🎯 Initializing neural network weights
📊 Creating dummy datasets
🔀 Shuffling training data
🎲 Random sampling
🧪 Simulations
🤖 Machine Learning experiments"""

#📚 1. np.random.rand()
# Generates random numbers from a uniform distribution over [0, 1).

#Example:
#single random number
random_number = np.random.rand()
print(random_number)

#multiple random numbers
random_numbers = np.random.rand(5)
print(random_numbers)

#2D array of random numbers
random_array_2d = np.random.rand(3, 4)
print(random_array_2d)

#3D array of random numbers
random_array_3d = np.random.rand(2, 3, 4)
print(random_array_3d)


#📚 2. np.random.randn()
# Generates random numbers from a standard normal distribution (mean=0, std=1).
#Unlike rand() always btw (0, 1), values can be:

#Positive
#Negative
#Around zero
# Centered around zero 
#Example:
#single random number
random_number = np.random.randn()
print(random_number)

#multiple random numbers
random_numbers = np.random.randn(5) 
print(random_numbers)

#2D array of random numbers
random_array_2d = np.random.randn(3, 4)
print(random_array_2d)  

#3D array of random numbers
random_array_3d = np.random.randn(2, 3, 4)
print(random_array_3d)



#📚 3. np.random.randint(low, high=None, size=None, dtype=int)
# Generates random integers from a discrete uniform distribution.
# low: Lower boundary of the output interval.
# high: Upper boundary of the output interval.
# size: Shape of the output.
# dtype: Data type of the output.

#Number is btw low (inclusive) and high (exclusive).

#Example:
#single random integer
random_integer = np.random.randint(1, 10)
print(random_integer)

#multiple random integers
random_integers = np.random.randint(1, 10, 5)
print(random_integers)

#2D array of random integers
random_array_2d = np.random.randint(1, 10, (3, 4))
print(random_array_2d)

#3D array of random integers
random_array_3d = np.random.randint(1, 10, (2, 3, 4))
print(random_array_3d)


#📚 4. np.random.choice(a, size=None, replace=True, p=None )
# Generates a random sample from a given 1-D array.
# a: 1-D array-like or int. If an int, the random sample is generated from np.arange(a).
# size: Output shape. If the given shape is, e.g., (m, n), then m * n samples are drawn.
# replace: Whether the sample is with or without replacement.
# p: The probabilities associated with each entry in a. If not given, the sample assumes a uniform distribution over all entries in a.

#Example:
#single random choice
choices = np.random.choice([1, 2, 3, 4, 5], size=1)
print(choices)

fruits = ['apple', 'banana', 'cherry', 'date']
#single random choice from a list of fruits
choice = np.random.choice(fruits, size=1)
print(choice)

#multiple random choices
choices = np.random.choice([1, 2, 3, 4, 5], size=3)
print(choices)

choices = np.random.choice(fruits, size=3)
print(choices)

#2D array of random choices
choices = np.random.choice([1, 2, 3, 4, 5], size=(2, 3))
print(choices)

choices = np.random.choice(fruits, size=(2, 3))
print(choices)

#3D array of random choices
choices = np.random.choice([1, 2, 3, 4, 5], size=(2, 3, 4))
print(choices)

choices = np.random.choice(fruits, size=(2, 3, 4))
print(choices)


#📚 5. np.random.seed()
# Sets the seed for the random number generator.
# This ensures that the same sequence of random numbers is generated each time the code is run.

np.random.seed(42)
random_numbers = np.random.randn(5)
print(random_numbers)

# The same seed will produce the same sequence of random numbers
np.random.seed(42)
random_numbers = np.random.randn(5)
print(random_numbers)

#2D array of random numbers
np.random.seed(42)
random_array_2d = np.random.rand(3, 4)
print(random_array_2d)

# The same seed will produce the same sequence of random numbers
np.random.seed(42)
random_array_2d = np.random.rand(3, 4)
print(random_array_2d)

#3D array of random numbers
np.random.seed(42)
random_array_3d = np.random.rand(2, 3, 4)
print(random_array_3d)

# The same seed will produce the same sequence of random numbers
np.random.seed(42)
random_array_3d = np.random.rand(2, 3, 4)
print(random_array_3d)


#📚 6. np.random.shuffle()
# Shuffles the elements of an array in place.
#Shuffles the original array.

#Example:
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
np.random.shuffle(arr)
print("Shuffled array:", arr)

arr2d =np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:", arr2d)
np.random.shuffle(arr2d)
print("Shuffled 2D array:", arr2d)

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Original 3D array:", arr3d)
np.random.shuffle(arr3d)
print("Shuffled 3D array:", arr3d)


#📚 7. np.random.permutation()
# Returns a permuted sequence or array.
# Unlike shuffle(), permutation() returns a new array and does not modify the original array.

#Example:
arr = np.array([1, 2, 3, 4, 5])
permuted_arr = np.random.permutation(arr)
print("Original array:", arr)
print("Permuted array:", permuted_arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
permuted_arr2d = np.random.permutation(arr2d)
print("Original 2D array:", arr2d)
print("Permuted 2D array:", permuted_arr2d)

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
permuted_arr3d = np.random.permutation(arr3d)   
print("Original 3D array:", arr3d)
print("Permuted 3D array:", permuted_arr3d) 

#Randon Uniform Distribution
a = np.random.uniform(0, 1, 5)  # 5 random numbers between 0 and 1
print(a)

arr2d = np.random.uniform(0, 10, (3, 4))  # 3x4 array of random numbers between 0 and 10
print(arr2d)

arr3d = np.random.uniform(-5, 5, (2, 3, 4))  # 2x3x4 array of random numbers between -5 and 5
print(arr3d)