"""
DAY 21 — SESSION 01: OPTIMIZATION FUNDAMENTALS
================================================

LEARNING GOAL
-------------
Understand what optimization means, why neural-network training is an
optimization problem, how gradients and optimizers have different jobs, and
how one gradient-descent update reduces a simple loss.

1. WHAT IS OPTIMIZATION?
------------------------
Optimization means finding input values that make a function as small (a
minimum) or as large (a maximum) as possible. In machine learning we normally
minimize a loss function:

    minimize L(w)

Here L is the loss and w represents every trainable weight and bias. A neural
network may have millions of parameters, but the goal remains simple: find the
parameter values that make predictions produce the smallest loss.

Training is therefore not mysterious:

    choose parameters -> predict -> measure loss -> calculate gradients
    -> update parameters -> repeat

2. VALLEY INTUITION
-------------------
Imagine standing on a mountain in darkness and trying to reach the bottom:

    current location       = current parameters
    height                 = current loss
    local slope            = gradient
    length of one step     = learning rate
    walking strategy       = optimizer
    bottom of the valley   = minimum loss

The gradient points in the direction of steepest INCREASE. To reduce loss, we
move in the opposite direction:

    w_new = w_old - learning_rate * gradient

3. BACKPROPAGATION IS NOT THE OPTIMIZER
---------------------------------------
These jobs are related but different:

* Backpropagation calculates dL/dw for every parameter.
* The optimizer uses those gradients to decide parameter updates.

In our XOR network:

    loss.backward()             # calculate gradients
    p.data -= lr * p.grad       # optimize parameters

The second line was already vanilla gradient descent.

4. WORKED EXAMPLE: L(w) = w^2
--------------------------------
The minimum is w=0 because squares cannot be negative and L(0)=0.

Derivative:

    dL/dw = 2w

Start with w=5 and learning_rate=0.1:

    current loss = 5^2 = 25
    gradient     = 2(5) = 10
    update       = 0.1(10) = 1
    new weight   = 5 - 1 = 4
    new loss     = 4^2 = 16

Loss fell from 25 to 16. Repeat from w=4:

    gradient   = 2(4) = 8
    new weight = 4 - 0.1(8) = 3.2
    new loss   = 3.2^2 = 10.24

The sequence moves toward zero:

    weights: 5 -> 4 -> 3.2 -> 2.56 -> ... -> 0
    losses: 25 -> 16 -> 10.24 -> 6.5536 -> ... -> 0

5. WHY THE SIGN WORKS AUTOMATICALLY
-----------------------------------
At w=5 the gradient is +10, so subtracting it moves left toward zero. At w=-5
the gradient is -10:

    w_new = -5 - 0.1(-10) = -4

Subtracting a negative number moves right toward zero. The same formula handles
both sides of the valley.

6. MULTIPLE PARAMETERS
----------------------
For L(x,y), the gradient is a vector:

    gradient L = [dL/dx, dL/dy]

Each parameter is updated using its own partial derivative:

    x_new = x - lr * dL/dx
    y_new = y - lr * dL/dy

This scales to millions of parameters; vectorized libraries perform all the
updates efficiently.

COMMON MISUNDERSTANDINGS
------------------------
* Loss tells how wrong the model is; it is not the gradient.
* Gradient tells local direction and steepness; it is not a new weight.
* A gradient does not reveal the whole landscape, only the local slope.
* Optimization lowers training loss; good generalization also depends on data,
  model design, regularization, and validation.
"""


def loss(weight):
    """The simple convex test loss L(w)=w^2."""
    return weight ** 2


def gradient(weight):
    """Derivative dL/dw=2w."""
    return 2 * weight


def gradient_descent(start=5.0, learning_rate=0.1, steps=8):
    """Run GD and retain values so every update can be inspected."""
    weight = float(start)
    history = []
    for step in range(steps + 1):
        current_loss = loss(weight)
        current_gradient = gradient(weight)
        history.append((step, weight, current_loss, current_gradient))
        weight = weight - learning_rate * current_gradient
    return history


if __name__ == "__main__":
    print("step | weight    | loss      | gradient")
    print("-" * 45)
    for step, weight, value, grad in gradient_descent():
        print(f"{step:>4} | {weight:>9.5f} | {value:>9.5f} | {grad:>9.5f}")

