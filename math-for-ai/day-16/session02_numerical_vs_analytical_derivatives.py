"""
Lesson 5: Numerical vs Analytical Derivatives
=============================================

This file contains only the concepts covered so far in this lesson.

We use the function:

    f(x) = x**2

Its derivative is:

    f'(x) = 2*x

There are two ways discussed so far to find its derivative:

1. Analytical differentiation
2. Numerical differentiation


Analytical derivative
----------------------------------------
An analytical derivative uses a derivative formula found with calculus.

For f(x) = x**2:

    f'(x) = 2*x

At x = 3:

    f'(3) = 2*3 = 6

At x = 5:

    f'(5) = 2*5 = 10

This gives the exact derivative for this function.


Numerical derivative: forward difference
----------------------------------------
Suppose we do not use the derivative formula. We can estimate the derivative
by comparing the function at x and at a nearby point x + h:

    f'(x) approximately equals (f(x + h) - f(x)) / h

Here, h is a small change in x.

The calculation asks:

    If x increases by a tiny amount, how much does f(x) change?

For x = 5 and h = 0.001, the estimate is approximately 10.001. The exact
analytical derivative is 10.


What happens when h gets smaller?
---------------------------------
In the examples covered, making h smaller moves the numerical estimate closer
to the exact derivative:

    h = 0.1       -> approximately 10.1
    h = 0.01      -> approximately 10.01
    h = 0.001     -> approximately 10.001
    h = 0.000001  -> approximately 10.000001

As h approaches zero, the estimate approaches 10.

However, computers have limited numerical precision. If h becomes excessively
small, rounding errors can make the estimate worse. Therefore, h should be
small, but not unbelievably small.


Analytical versus numerical
---------------------------
- The analytical method uses a derived formula such as 2*x.
- The numerical method evaluates the function at nearby points.
- The analytical result is exact for this example.
- The numerical result is an approximation and depends on h.
- Numerical differentiation is useful when we do not have the derivative
  formula or when we want to check a derivative.
- The analytical calculation is usually more accurate and is fast once the
  formula is known.
- Numerical differentiation needs additional function evaluations.


Numerical derivative: central difference
----------------------------------------
Instead of using only x and x + h, central difference uses a nearby point on
each side of x:

    x - h  <-  x  ->  x + h

Its formula is:

    f'(x) approximately equals (f(x + h) - f(x - h)) / (2*h)

We divide by 2*h because the distance between the two points is:

    (x + h) - (x - h) = 2*h

For x = 5 and h = 0.001, the two points are 4.999 and 5.001. Their distance
is 0.002, which equals 2*h.

Because the interval is centered around x, errors from the two sides can
balance each other. Central difference therefore usually gives a better
estimate than forward difference. For f(x) = x**2 in this example, it gives
approximately 10.
"""


def f(x):
    """Return f(x) = x^2, the function used throughout this lesson."""
    return x**2


def analytical_derivative(x):
    """Return the exact derivative f'(x) = 2x."""
    return 2 * x


def forward_difference(x, h):
    """Estimate the derivative using x and the nearby point x + h."""
    return (f(x + h) - f(x)) / h


def central_difference(x, h):
    """Estimate the derivative using the nearby points x - h and x + h."""
    return (f(x + h) - f(x - h)) / (2 * h)


def analytical_examples():
    """Show exact analytical derivatives at x = 3 and x = 5."""
    print("ANALYTICAL DERIVATIVES")

    for x in (3, 5):
        derivative = analytical_derivative(x)
        print(f"At x = {x}: f'(x) = 2 * {x} = {derivative}")

    print()


def forward_difference_example():
    """Compare the analytical result with a forward numerical estimate."""
    print("FORWARD NUMERICAL DIFFERENCE")

    x = 5
    h = 0.001
    exact = analytical_derivative(x)
    estimate = forward_difference(x, h)

    print(f"x = {x}")
    print(f"h = {h}")
    print(f"Exact analytical derivative: {exact}")
    print(f"Forward numerical estimate: {estimate}")
    print("The estimate is close to 10, but it is not exact.\n")


def h_size_examples():
    """Show how the forward estimate changes as h becomes smaller."""
    print("EFFECT OF MAKING h SMALLER")

    x = 5
    exact = analytical_derivative(x)

    print(f"Exact derivative at x = {x}: {exact}")
    print("h          | forward estimate")
    print("-----------|-----------------")

    for h in (0.1, 0.01, 0.001, 0.000001):
        estimate = forward_difference(x, h)
        print(f"{h:<10g} | {estimate:.9f}")

    print("The estimates move closer to 10 as h gets smaller.")
    print("An excessively small h can eventually cause computer rounding errors.\n")


def central_difference_example():
    """Compare forward difference with the centered, two-sided estimate."""
    print("CENTRAL DIFFERENCE")

    x = 5
    h = 0.001
    left_point = x - h
    right_point = x + h
    distance = right_point - left_point

    exact = analytical_derivative(x)
    forward = forward_difference(x, h)
    central = central_difference(x, h)

    print(f"Left point, x - h: {left_point}")
    print(f"Right point, x + h: {right_point}")
    print(f"Distance between the points: {distance:.3f} = 2 * h")
    print(f"Exact analytical derivative: {exact}")
    print(f"Forward difference: {forward}")
    print(f"Central difference: {central}")
    print("Central difference uses nearby points on both sides of x.")


def main():
    """Run all examples covered so far in Lesson 5."""
    analytical_examples()
    forward_difference_example()
    h_size_examples()
    central_difference_example()

    # Next up: connecting these ideas to automatic differentiation.


if __name__ == "__main__":
    main()
