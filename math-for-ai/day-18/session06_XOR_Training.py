"""
LESSON 5 — PART 10
XOR + TRAINING LOOP

============================================================
WHAT IS XOR?
============================================================

XOR means EXCLUSIVE OR.

Rule:

    output 1 when inputs are DIFFERENT
    output 0 when inputs are the SAME

Truth table:

    A B | XOR
    0 0 | 0
    0 1 | 1
    1 0 | 1
    1 1 | 0

============================================================
WHY DOES OUR LESSON USE -1/+1?
============================================================

Normal XOR targets are:

    [0,1,1,0]

But our output activation is tanh, whose range is approximately:

    [-1,+1]

So we encode:

    class 0 -> -1
    class 1 -> +1

Therefore:

    [0,0] -> -1
    [0,1] -> +1
    [1,0] -> +1
    [1,1] -> -1

These are GIVEN TARGETS.

The MLP does not invent them.

============================================================
WHY XOR IS A GOOD TEST
============================================================

XOR is not linearly separable.

The positive and negative examples sit diagonally opposite each other.

A single straight-line decision boundary cannot solve it.

Therefore XOR demonstrates why we need:

    hidden layer + nonlinear activation

============================================================
WHAT THE MLP ACTUALLY LEARNS
============================================================

The model does NOT hard-code:

    if inputs are different -> +1

Instead, it starts with random weights.

Then it repeatedly adjusts them until:

    model([0,0]) ≈ -1
    model([0,1]) ≈ +1
    model([1,0]) ≈ +1
    model([1,1]) ≈ -1

The learned function behaves like XOR.

============================================================
TRAINING LOOP
============================================================

Core training cycle:

    FORWARD
      ↓
    LOSS
      ↓
    ZERO OLD GRADIENTS
      ↓
    BACKWARD
      ↓
    UPDATE PARAMETERS
      ↓
    REPEAT

============================================================
LOSS
============================================================

We use squared error:

    loss = (prediction - target)^2

If prediction is close to target:
    loss small

If prediction is far:
    loss large

Example target=1:

    prediction=0.5
    loss=(0.5-1)^2=0.25

    prediction=-0.5
    loss=(-0.5-1)^2=2.25

============================================================
WHY ZERO GRADIENTS?
============================================================

Our engine uses += when accumulating gradients.

Therefore gradients persist unless we clear them.

Before each new backward pass:

    p.grad = 0.0

This is conceptually like:

    optimizer.zero_grad()

in PyTorch.

============================================================
WHAT DOES loss.backward() DO?
============================================================

It asks:

    How does the loss depend on EVERY parameter?

For each parameter p:

    p.grad = dLoss/dp

Positive gradient:
    increasing p would increase loss locally

Negative gradient:
    increasing p would decrease loss locally

============================================================
GRADIENT DESCENT
============================================================

Update rule:

    p_new = p_old - learning_rate * p.grad

We move OPPOSITE the gradient because the gradient points toward increasing loss.

Example:

    p=5
    grad=2
    lr=0.1

    new p = 5 - 0.1*2 = 4.8

If grad=-2:

    new p = 5 - 0.1*(-2)
          = 5.2

============================================================
WHY REPEAT MANY STEPS?
============================================================

One update usually only improves the model slightly.

Repeated updates gradually reduce loss.

This is training.
"""

print("XOR theoretical notes file.")
print("See autodiff.py for the complete runnable training implementation.")
