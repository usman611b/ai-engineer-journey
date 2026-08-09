"""
Lesson 4: Calculus for Machine Learning
=======================================

These notes contain only the concepts covered so far in today's lesson.

Main idea
---------
A derivative tells us the local slope of a function: how quickly its output
changes when its input changes by a small amount. In other words, it is a
local rate of change.

For the function:

    f(x) = x**2

the derivative is:

    f'(x) = 2*x

At x = 3:

    f'(3) = 2*3 = 6

The local slope is 6. Near x = 3, increasing x slightly causes f(x) to
increase at a rate described by this slope.

At x = 0:

    f'(0) = 2*0 = 0

The graph is flat at x = 0. For f(x) = x**2, this is also the minimum.

Derivative meanings
-------------------
- Positive derivative: increasing the input locally increases the output.
- Negative derivative: increasing the input locally decreases the output.
- Zero derivative: the function is locally flat at that point.

AI interpretation
-----------------
In machine learning, we can think of a derivative as measuring the
sensitivity of the loss to a change in a weight:

    How much will the loss change if this weight changes slightly?

The derivative of the loss with respect to a weight is called its gradient
in the examples from this lesson.

Gradient descent
----------------
The goal is to reduce the loss. The derivative points in the direction in
which the function increases, so gradient descent moves in the opposite
direction.

The update rule is:

    w_new = w_old - learning_rate * gradient

The minus sign makes the weight move opposite the gradient.

Learning rate
-------------
The learning rate controls the size of each update:

- A learning rate that is too small makes learning very slow.
- A learning rate that is too large can jump past the minimum, called
  overshooting.
- A learning rate of zero prevents all weight updates, so no learning occurs.

Gradient descent repeats the update many times. As f(x) = x**2 approaches its
minimum at x = 0, x approaches zero, the gradient approaches zero, and the
loss approaches zero.
"""


def square(x):
    """Return f(x) = x^2, used as the loss function in today's examples."""
    return x**2


def square_derivative(x):
    """Return the analytical derivative f'(x) = 2x."""
    return 2 * x


def derivative_examples():
    """Show the derivative of f(x) = x^2 at x = 3 and x = 0."""
    print("DERIVATIVE AS LOCAL SLOPE / RATE OF CHANGE")

    for x in (3, 0):
        loss = square(x)
        derivative = square_derivative(x)
        print(f"x = {x}, f(x) = {loss}, f'(x) = {derivative}")

    print("At x = 3, the local slope is 6.")
    print("At x = 0, the derivative is 0 and the function is flat.\n")


def derivative_sign_meanings():
    """Demonstrate positive, negative, and zero derivative meanings."""
    print("POSITIVE, NEGATIVE, AND ZERO DERIVATIVES")

    for x in (3, -3, 0):
        gradient = square_derivative(x)

        if gradient > 0:
            meaning = "positive: increasing x locally increases f(x)"
        elif gradient < 0:
            meaning = "negative: increasing x locally decreases f(x)"
        else:
            meaning = "zero: the function is locally flat"

        print(f"At x = {x}, derivative = {gradient} -> {meaning}")

    print()


def one_gradient_descent_update(weight, gradient, learning_rate):
    """Apply the gradient descent update rule once."""
    return weight - learning_rate * gradient


def update_rule_examples():
    """Show normal, oversized, and zero-learning-rate updates."""
    print("GRADIENT DESCENT UPDATE RULE")
    print("w_new = w_old - learning_rate * gradient")

    weight = 5
    gradient = 10

    learning_rate = 0.1
    new_weight = one_gradient_descent_update(weight, gradient, learning_rate)
    print(
        f"w = {weight}, gradient = {gradient}, lr = {learning_rate} "
        f"-> w_new = {new_weight:g}"
    )
    print("The weight moves from 5 to 4, toward the minimum at 0.")

    learning_rate = 2
    new_weight = one_gradient_descent_update(weight, gradient, learning_rate)
    print(
        f"w = {weight}, gradient = {gradient}, lr = {learning_rate} "
        f"-> w_new = {new_weight:g}"
    )
    print("The weight jumps from 5 to -15: the large step overshoots 0.")

    learning_rate = 0
    new_weight = one_gradient_descent_update(weight, gradient, learning_rate)
    print(
        f"w = {weight}, gradient = {gradient}, lr = {learning_rate} "
        f"-> w_new = {new_weight:g}"
    )
    print("The weight stays the same, the loss stays the same, and nothing is learned.\n")


def zero_gradient_example():
    """Show that a zero gradient produces no update."""
    print("ZERO GRADIENT")

    weight = 0
    gradient = square_derivative(weight)
    learning_rate = 0.1
    new_weight = one_gradient_descent_update(weight, gradient, learning_rate)

    print(f"w = {weight}, gradient = {gradient}, lr = {learning_rate}")
    print(f"w_new = {new_weight:g}")
    print("Because the gradient is zero, the update is zero and the weight does not move.\n")


def repeated_gradient_descent():
    """
    Run the manual f(x) = x^2 example.

    Start with x = 5 and learning rate = 0.1:

        x = 5.00, gradient = 10.0 -> new x = 4.00
        x = 4.00, gradient =  8.0 -> new x = 3.20
        x = 3.20, gradient =  6.4 -> new x = 2.56

    Each repetition recalculates the gradient using the current x and then
    performs another update.
    """
    print("REPEATED GRADIENT DESCENT ON f(x) = x^2")

    x = 5.0
    learning_rate = 0.1

    print("step | old x | gradient | loss before | new x | loss after")
    print("-----|-------|----------|-------------|-------|-----------")

    for step in range(1, 4):
        old_x = x
        gradient = square_derivative(old_x)
        loss_before = square(old_x)
        x = one_gradient_descent_update(old_x, gradient, learning_rate)
        loss_after = square(x)

        print(
            f"{step:>4} | {old_x:>5.2f} | {gradient:>8.2f} | "
            f"{loss_before:>11.4f} | {x:>5.2f} | {loss_after:>9.4f}"
        )

    print("\nThe updates are: 5 -> 4 -> 3.2 -> 2.56")
    print("The corresponding gradients are: 10, 8, and 6.4")
    print("With more repetitions, x, the gradient, and the loss approach zero.\n")


def main():
    """Run all mini-examples from today's lesson."""
    derivative_examples()
    derivative_sign_meanings()
    update_rule_examples()
    zero_gradient_example()
    repeated_gradient_descent()

    # Next up: numerical derivatives versus analytical derivatives.


if __name__ == "__main__":
    main()
