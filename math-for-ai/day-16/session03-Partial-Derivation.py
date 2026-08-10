"""
Lesson 4 — Calculus for Machine Learning, Part 2
================================================

These notes continue AFTER the earlier topics of derivatives and differentiation
methods. They cover learning rate, gradient descent, partial derivatives, and the
gradient vector.


1. LEARNING RATE
----------------

The learning rate (usually written as lr, alpha, or eta) controls the size of each
step an optimization algorithm takes while trying to reduce loss.

Intuition:
    Imagine walking downhill toward the lowest point of a valley.

    * A very small learning rate takes tiny, safe steps, but learning can be slow.
    * A suitable learning rate makes useful progress without jumping past the goal.
    * A very large learning rate can overshoot the minimum. Repeated overshooting
      may cause the values to bounce around or move farther away (diverge).
    * lr = 0 means the step size is zero, so the parameter never changes and the
      model cannot learn.

Example update when the current value is x = 5 and the gradient is 10:

    lr = 0.1  -> new x = 5 - 0.1(10) = 4       (useful step)
    lr = 0.01 -> new x = 5 - 0.01(10) = 4.9    (small, slow step)
    lr = 1.0  -> new x = 5 - 1.0(10) = -5      (overshoots x = 0)
    lr = 0    -> new x = 5 - 0(10) = 5         (no learning)

The best learning rate depends on the problem. It is a hyperparameter: a setting
chosen by the programmer rather than learned directly as a model weight.


2. GRADIENT DESCENT
-------------------

Gradient descent repeatedly changes parameters in the direction that reduces a
function such as a model's loss.

Update rule:

    new_parameter = old_parameter - learning_rate * gradient

or mathematically:

    x_new = x_old - lr * f'(x_old)

Why subtract? The gradient points toward the direction of greatest local increase.
Moving in the opposite direction therefore moves locally downhill.

Algorithm:

    1. Start with an initial parameter value.
    2. Calculate the gradient at that value.
    3. Multiply the gradient by the learning rate.
    4. Subtract that amount from the parameter.
    5. Repeat until the loss changes very little or another stopping rule is met.

Worked example for f(x) = x^2, starting at x = 5 with lr = 0.1:

    gradient = 2x

    Step 0: x = 5
    Step 1: gradient = 2(5) = 10
            x = 5 - 0.1(10) = 4

    Step 2: gradient = 2(4) = 8
            x = 4 - 0.1(8) = 3.2

    Step 3: gradient = 2(3.2) = 6.4
            x = 3.2 - 0.1(6.4) = 2.56

Observations:

    * x moves toward the minimum at x = 0.
    * f(x) also falls: 25 -> 16 -> 10.24 -> 6.5536.
    * Steps shrink as x approaches zero because the gradient becomes smaller.
    * Gradient descent usually approaches a minimum over multiple updates; it does
      not need to land exactly on the minimum in one step.


3. PARTIAL DERIVATIVES
----------------------

A function can depend on more than one variable. A partial derivative measures how
the output changes with respect to ONE variable while treating all other variables
as constants.

Worked example:

    f(x, y) = x^2 + 3xy + y^2

With respect to x, treat y as a constant:

    partial f / partial x
        = 2x + 3y + 0
        = 2x + 3y

Explanation:
    * x^2 becomes 2x.
    * 3xy becomes 3y because y is held constant.
    * y^2 becomes 0 because it contains no changing x.

With respect to y, treat x as a constant:

    partial f / partial y
        = 0 + 3x + 2y
        = 3x + 2y

Explanation:
    * x^2 becomes 0 because it contains no changing y.
    * 3xy becomes 3x because x is held constant.
    * y^2 becomes 2y.


4. GRADIENT VECTOR
------------------

The gradient is a vector containing all first partial derivatives:

    grad f(x, y) = [partial f / partial x, partial f / partial y]

For f(x, y) = x^2 + 3xy + y^2:

    grad f(x, y) = [2x + 3y, 3x + 2y]

At (x, y) = (1, 2):

    grad f(1, 2) = [2(1) + 3(2), 3(1) + 2(2)]
                 = [8, 7]

Interpretation:
    Near (1, 2), increasing x slightly raises f at a local rate of about 8 per
    unit, while increasing y slightly raises it at a local rate of about 7 per
    unit. The vector [8, 7] points in the direction of steepest local increase.
    To reduce f, gradient descent moves in the opposite direction, [-8, -7].

AI intuition:
    A neural network can have thousands or millions of weights. Each partial
    derivative answers, "How would the loss change if this one weight changed while
    the others were held fixed?" The gradient collects those answers:

        loss gradient = [dL/dw1, dL/dw2, ..., dL/dwn]

    Every weight is then updated at the same time:

        weights_new = weights_old - lr * loss_gradient


5. INTERPRETING GRADIENT SIGNS
------------------------------

For minimization, the update uses the NEGATIVE gradient.

If the gradient is [-5, 12]:

    x_new = x - lr(-5) = x + 5lr  -> increase x
    y_new = y - lr(12) = y - 12lr -> decrease y

So a negative gradient component makes its parameter increase during gradient
descent, while a positive component makes its parameter decrease.

Important distinction:
    The sign describes the locally useful direction for the current point. It does
    not mean a parameter must always move in that direction; the gradient may
    change after the next update.


6. KEY TAKEAWAYS
----------------

* The learning rate scales every update step.
* lr = 0 prevents learning; an excessively large lr may overshoot or diverge.
* Gradient descent follows: parameter = parameter - lr * gradient.
* A partial derivative changes one variable while holding the others constant.
* The gradient vector collects every partial derivative.
* The gradient points toward steepest local increase; negative gradient is the
  local downhill direction used for minimization.
* In machine learning, gradients tell us how to adjust many weights to reduce loss.


7. COMMON MISTAKES
------------------

* Adding the gradient when trying to minimize instead of subtracting it.
* Forgetting to multiply the gradient by the learning rate.
* Thinking lr = 0 means slow learning; it means no learning at all.
* Assuming a larger learning rate always learns faster; it may skip the minimum.
* Differentiating every variable in a partial derivative instead of holding the
  other variables constant.
* Confusing a scalar partial derivative with the full gradient vector.
* Reading a negative gradient as "decrease the parameter." Because the update
  subtracts the gradient, a negative component makes that parameter increase.
* Assuming one gradient step must reach the minimum exactly.

Run this file to see concise numerical examples of the ideas above.
"""


def gradient_descent_1d(x: float, learning_rate: float, steps: int) -> list[float]:
    """Run gradient descent on f(x) = x^2 and return every x value."""
    history = [x]
    for _ in range(steps):
        gradient = 2 * x
        x = x - learning_rate * gradient
        history.append(x)
    return history


def f(x: float, y: float) -> float:
    """Evaluate f(x, y) = x^2 + 3xy + y^2."""
    return x**2 + 3 * x * y + y**2


def gradient_f(x: float, y: float) -> tuple[float, float]:
    """Return the gradient [2x + 3y, 3x + 2y]."""
    return 2 * x + 3 * y, 3 * x + 2 * y


def apply_gradient_step(
    x: float, y: float, gradient: tuple[float, float], learning_rate: float
) -> tuple[float, float]:
    """Apply one two-variable gradient-descent update."""
    dx, dy = gradient
    return x - learning_rate * dx, y - learning_rate * dy


if __name__ == "__main__":
    print("Gradient descent on f(x) = x^2 (start=5, lr=0.1):")
    values = gradient_descent_1d(x=5.0, learning_rate=0.1, steps=3)
    for step, x_value in enumerate(values):
        print(f"  step {step}: x={x_value:g}, f(x)={x_value**2:g}")

    point = (1.0, 2.0)
    grad = gradient_f(*point)
    print(f"\nf{point} = {f(*point):g}")
    print(f"gradient at {point} = {grad}")

    signed_gradient = (-5.0, 12.0)
    updated = apply_gradient_step(1.0, 2.0, signed_gradient, learning_rate=0.1)
    print("\nSign example with gradient (-5, 12) and lr=0.1:")
    print(f"  (x, y): (1, 2) -> {updated}  (x increases, y decreases)")

    print("\nLearning-rate comparison from x=5 for one step:")
    for lr in (0.1, 0.01, 1.0, 0.0):
        new_x = gradient_descent_1d(x=5.0, learning_rate=lr, steps=1)[-1]
        print(f"  lr={lr:g}: x -> {new_x:g}")
