"""
LESSON 4 — THE CHAIN RULE FOR MACHINE LEARNING
================================================

These notes explain everything we learned about the chain rule, starting from the
basic intuition and ending with a tiny model that learns through gradient descent.


1. WHAT IS THE CHAIN RULE?
--------------------------

The chain rule is used when one function is inside another function.

Example:

    f(x) = (3x + 1)^2

This is not one operation. It is a chain of two operations:

    x  --->  u = 3x + 1  --->  f = u^2

First, x changes u. Then u changes f.

The chain rule asks:

    "How does x affect the final answer f through all the intermediate steps?"

Its formula is:

    df/dx = df/du * du/dx

In words:

    total effect = effect of the outer step * effect of the inner step

We multiply because a change is passed through every operation in the chain.


2. WHY DOES AI NEED THE CHAIN RULE?
-----------------------------------

A neural network is a long chain of operations:

    input
      -> weighted sum
      -> activation
      -> prediction
      -> loss

The network needs to answer:

    "How did each weight affect the final loss?"

The weight does not usually affect the loss in one direct step. Its effect travels
through all the intermediate operations. The chain rule connects those effects.

Example chain:

    weight -> prediction -> error -> loss

Forward pass:
    Start with the input and weight, then calculate toward the loss.

Backward pass:
    Start from the loss and multiply local derivatives backward toward the weight.

This repeated application of the chain rule is the foundation of backpropagation.


3. IMPORTANT VOCABULARY
-----------------------

Forward pass:
    Calculate intermediate values, the prediction, and the loss.

Backward pass:
    Calculate how the loss changes with respect to earlier values and weights.

Local derivative:
    The derivative for one small operation in the computation chain.

Gradient:
    The derivative of the loss with respect to a weight, or a collection of such
    derivatives when a model has many weights.

Computation graph:
    A picture or representation of values flowing through connected operations.

Backpropagation:
    Efficiently applying the chain rule backward through a computation graph.


4. EXAMPLE 1: f(x) = (3x + 1)^2
--------------------------------

Break the function into two steps:

    u = 3x + 1
    f = u^2

Find the local derivatives:

    du/dx = 3
    df/du = 2u

Use the chain rule:

    df/dx = df/du * du/dx
          = 2u * 3
          = 6u

Replace u with 3x + 1:

    df/dx = 6(3x + 1)
          = 18x + 6

At x = 2:

    u = 3(2) + 1 = 7
    df/dx = 2(7) * 3 = 42

Intuition:
    x affects u by a factor of 3. At this point, u affects f by a factor of 14.
    The total effect is 14 * 3 = 42.


5. EXAMPLE 2: u = x^2 AND f = u^3
----------------------------------

Computation chain:

    x  --->  u = x^2  --->  f = u^3

Local derivatives:

    du/dx = 2x
    df/du = 3u^2

Chain rule:

    df/dx = df/du * du/dx
          = 3u^2 * 2x
          = 6xu^2

Since u = x^2:

    df/dx = 6x(x^2)^2
          = 6x^5

We can verify this by simplifying first:

    f = (x^2)^3 = x^6
    derivative of x^6 = 6x^5

At x = 2:

    u = 2^2 = 4
    du/dx = 2(2) = 4
    df/du = 3(4^2) = 48
    df/dx = 48 * 4 = 192

Direct check:

    6(2^5) = 6(32) = 192


6. EXAMPLE 3: A WEIGHT, PREDICTION, AND SIMPLE LOSS
---------------------------------------------------

Suppose:

    p = wx
    L = p^2

where:

    x = input
    w = weight
    p = prediction
    L = loss

Computation chain:

    w  --->  p = wx  --->  L = p^2

Local derivatives:

    dp/dw = x
    dL/dp = 2p

Chain rule:

    dL/dw = dL/dp * dp/dw
          = 2p * x

Since p = wx:

    dL/dw = 2(wx)x
          = 2wx^2

Numerical example with x = 3 and w = 2:

    p = 2(3) = 6
    L = 6^2 = 36
    dL/dp = 2(6) = 12
    dp/dw = 3
    dL/dw = 12(3) = 36

With learning rate 0.01:

    w_new = w_old - learning_rate * gradient
          = 2 - 0.01(36)
          = 1.64

New prediction and loss:

    p_new = 1.64(3) = 4.92
    L_new = 4.92^2 = 24.2064

The loss fell from 36 to 24.2064.

Note:
    This simple loss pushes the prediction toward zero. A realistic supervised
    learning example includes a target value, as shown next.


7. EXAMPLE 4: SQUARED-ERROR LOSS WITH A TARGET
----------------------------------------------

This is closer to how a real model learns:

    prediction = wx
    loss = (prediction - target)^2

Break it into small operations:

    p = wx
    e = p - target
    L = e^2

Computation chain:

    w  --->  p  --->  e  --->  L

Meanings:

    p = prediction
    e = error
    L = squared loss

Local derivatives:

    dL/de = 2e
    de/dp = 1
    dp/dw = x

Chain rule:

    dL/dw = dL/de * de/dp * dp/dw
          = 2e * 1 * x
          = 2ex

Since e = wx - target:

    dL/dw = 2(wx - target)x

Numerical example:

    x = 3
    target = 9
    w = 2

Forward pass:

    p = 2(3) = 6
    e = 6 - 9 = -3
    L = (-3)^2 = 9

Backward pass:

    dL/de = 2(-3) = -6
    de/dp = 1
    dp/dw = 3
    dL/dw = -6(1)(3) = -18

Weight update with learning rate 0.01:

    w_new = 2 - 0.01(-18)
          = 2.18

The negative gradient makes the weight increase. That is useful here because the
prediction 6 is below the target 9.

After the update:

    new prediction = 2.18(3) = 6.54
    new error = 6.54 - 9 = -2.46
    new loss = (-2.46)^2 = 6.0516

The loss fell from 9 to 6.0516.


8. WHY MUST THE GRADIENT BE RECALCULATED?
-----------------------------------------

The gradient describes the slope at the CURRENT weight.

At weight 2:

    error = -3
    gradient = -18

After the weight becomes 2.18:

    error = -2.46
    gradient = 2(-2.46)(3) = -14.76

The old gradient is no longer correct because the model has moved to a new point.
Every training step therefore performs a fresh forward and backward pass:

    current weight
        -> new prediction
        -> new error and loss
        -> new gradient
        -> updated weight
        -> repeat


9. WHEN DOES TRAINING STOP?
---------------------------

Training does not always continue until the loss is exactly zero. It may stop when:

    * The loss is sufficiently small.
    * The gradient is sufficiently small.
    * The loss stops improving meaningfully.
    * A chosen number of steps or epochs has completed.

Real data often contains noise, so zero loss may be impossible or undesirable.


10. CONNECTION TO AUTOMATIC DIFFERENTIATION
--------------------------------------------

We calculated every local derivative by hand. Libraries such as PyTorch can track
the forward operations and automatically calculate these derivatives backward.

The library is not avoiding calculus. It is applying the same chain rule for us.

Manual calculation:

    dL/dw = dL/de * de/dp * dp/dw

Automatic differentiation:

    The framework records w -> p -> e -> L and multiplies the local derivatives
    during the backward pass.


11. COMMON MISTAKES
-------------------

* Adding local derivatives instead of multiplying them along a chain.
* Moving forward when calculating gradients instead of tracing backward from loss.
* Forgetting an intermediate operation, such as error = prediction - target.
* Using the old gradient after the weight has changed.
* Updating the gradient instead of updating the weight.
* Forgetting the learning rate in the update.
* Adding the gradient when minimizing instead of subtracting it.
* Expecting the loss to become exactly zero in every real problem.
* Writing mathematical names such as dL/dw as Python variables. Use a valid name
  such as weight_gradient.
* Using the mathematical multiplication style 2x in Python. Write 2 * x.


12. KEY TAKEAWAYS
-------------------------------------

* Use the chain rule when one operation feeds into another operation.
* The total derivative is the product of the local derivatives along the path.
* Neural networks are long chains of operations.
* A forward pass calculates predictions and loss.
* A backward pass applies the chain rule to calculate gradients.
* Backpropagation is the efficient repeated use of the chain rule.
* Gradient descent uses the final gradient to update each weight.
* Gradients must be recalculated after every update.
* Automatic differentiation performs this process automatically, but the underlying
  idea is still the chain rule.


RUNNABLE EXAMPLES
=================

Run this file to see each calculation in Python.
"""


# =============================================================================
# CODE EXAMPLE 1: f(x) = (3x + 1)^2
# =============================================================================

print("=" * 65)
print("EXAMPLE 1: f(x) = (3x + 1)^2")
print("=" * 65)

x = 2

# Forward pass
u = 3 * x + 1
f = u**2

# Backward pass: multiply the local derivatives.
df_du = 2 * u
du_dx = 3
df_dx = df_du * du_dx

print("x:", x)
print("u = 3x + 1:", u)
print("f = u^2:", f)
print("df/du:", df_du)
print("du/dx:", du_dx)
print("df/dx:", df_dx)


# =============================================================================
# CODE EXAMPLE 2: u = x^2, f = u^3
# =============================================================================

print("\n" + "=" * 65)
print("EXAMPLE 2: u = x^2 and f = u^3")
print("=" * 65)

x = 2

# Forward pass
u = x**2
f = u**3

# Backward pass
df_du = 3 * u**2
du_dx = 2 * x
df_dx = df_du * du_dx

print("x:", x)
print("u:", u)
print("f:", f)
print("df/du:", df_du)
print("du/dx:", du_dx)
print("df/dx using chain rule:", df_dx)
print("df/dx using 6*x^5:", 6 * x**5)


# =============================================================================
# CODE EXAMPLE 3: ONE REALISTIC TRAINING STEP
# =============================================================================

print("\n" + "=" * 65)
print("EXAMPLE 3: One training step with squared-error loss")
print("=" * 65)

x = 3
target = 9
weight = 2
learning_rate = 0.01

# Forward pass
prediction = weight * x
error = prediction - target
loss = error**2

# Backward pass using:
# dL/dw = dL/de * de/dp * dp/dw
dL_de = 2 * error
de_dp = 1
dp_dw = x
weight_gradient = dL_de * de_dp * dp_dw

# Gradient-descent update
new_weight = weight - learning_rate * weight_gradient

# Verify the new loss.
new_prediction = new_weight * x
new_error = new_prediction - target
new_loss = new_error**2

print("Old weight:", weight)
print("Old prediction:", prediction)
print("Target:", target)
print("Old error:", error)
print("Old loss:", loss)
print("Weight gradient:", weight_gradient)
print("New weight:", new_weight)
print("New prediction:", new_prediction)
print("New loss:", new_loss)


# =============================================================================
# CODE EXAMPLE 4: REPEATED TRAINING
# =============================================================================

print("\n" + "=" * 65)
print("EXAMPLE 4: Repeated training")
print("=" * 65)

x = 3
target = 9
weight = 2
learning_rate = 0.01
steps = 10

for step in range(steps):
    # Forward pass with the current weight.
    prediction = weight * x
    error = prediction - target
    loss = error**2

    # Backward pass: dL/dw = 2 * error * x.
    weight_gradient = 2 * error * x

    # Update the weight.
    weight = weight - learning_rate * weight_gradient

    print(
        "Step:", step + 1,
        "Weight:", round(weight, 6),
        "Prediction:", round(prediction, 6),
        "Loss:", round(loss, 6),
        "Gradient:", round(weight_gradient, 6),
    )


# Calculate values once more using the final updated weight.
final_prediction = weight * x
final_error = final_prediction - target
final_loss = final_error**2

print("\nFinal weight:", round(weight, 6))
print("Final prediction:", round(final_prediction, 6))
print("Final loss:", round(final_loss, 6))
print("Ideal weight is 3 because 3 * 3 = 9.")


# =============================================================================
# OPTIONAL REUSABLE FUNCTION
# =============================================================================


def train_one_weight(x, target, starting_weight, learning_rate, steps):
    """Train one weight for prediction = weight*x using squared-error loss."""
    weight = starting_weight
    history = []

    for step in range(steps):
        prediction = weight * x
        error = prediction - target
        loss = error**2
        weight_gradient = 2 * error * x

        # Save the values before performing this step's update.
        history.append(
            {
                "step": step + 1,
                "weight": weight,
                "prediction": prediction,
                "loss": loss,
                "gradient": weight_gradient,
            }
        )

        weight = weight - learning_rate * weight_gradient

    return weight, history


print("\n" + "=" * 65)
print("REUSABLE FUNCTION RESULT")
print("=" * 65)

trained_weight, training_history = train_one_weight(
    x=3,
    target=9,
    starting_weight=2,
    learning_rate=0.01,
    steps=10,
)

print("Trained weight:", round(trained_weight, 6))
print("Number of saved training steps:", len(training_history))
