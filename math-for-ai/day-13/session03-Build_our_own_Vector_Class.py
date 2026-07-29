#📚 Session 3 – Building Our Own Vector Class
class Vector:
    def __init__(self , coordinates):
        self.coordinates = list(coordinates)
        self.dimension = len(coordinates)

    def __add__(self, other): # it is a special method that is used to define the behavior of the addition operator (+) for objects of the class. When you use the + operator between two instances of the Vector class, this method is called to perform the addition.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])
    def __sub__(self, other): # it is a special method that is used to define the behavior of the subtraction operator (-) for objects of the class. When you use the - operator between two instances of the Vector class, this method is called to perform the subtraction.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])
    def dot(self, other): # it is a method that calculates the dot product of two vectors. The dot product is a mathematical operation that takes two equal-length sequences of numbers (vectors) and returns a single number. It is calculated by multiplying corresponding elements of the vectors and summing the results.
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))
    def magnitude(self): # it is a method that calculates the magnitude (or length) of the vector. The magnitude of a vector is a measure of how long the vector is, and it is calculated using the Pythagorean theorem. For a vector with coordinates (x1, x2, ..., xn), the magnitude is given by the square root of the sum of the squares of its components.
        return sum(a ** 2 for a in self.coordinates) ** 0.5
    def normalize(self): # it is a method that returns a unit vector in the same direction as the original vector. A unit vector has a magnitude of 1. To normalize a vector, you divide each of its components by its magnitude. This method first calculates the magnitude of the vector and then creates a new Vector instance with the normalized coordinates.
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize the zero vector.")
        return Vector([a / mag for a in self.coordinates])
     
    def __repr__(self): # it is a special method that is used to define how an object should be represented as a string. When you print an object or use the repr() function on it, this method is called to get the string representation of the object.
        return f"Vector({self.coordinates})"
    
v = Vector([6 , 8])
v2 = Vector([4, 5])
print(v.dimension)    # Output: 2
print(type(v))  # Output: <class '__main__.Vector'>
print(v) # Output: Vector([6, 8])
print(v2) # Output: Vector([4, 5])

print(v.dot(v2))  # Output: 64
print(v.magnitude())  # Output: 10.0
print(v.normalize())  # Output: Vector([0.6, 0.8])

