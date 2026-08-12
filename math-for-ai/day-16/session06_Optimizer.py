"""
Lesson 4: Optimizers after ordinary Gradient Descent
====================================================

Topics in this file:
    1. Momentum
    2. RMSProp
    3. Adam (Momentum + RMSProp)

These are study notes. Run this file to see small examples.

We will minimize f(x) = x**2.
The minimum is at x = 0, where loss = 0.
For this function:

    loss = x**2
    gradient = 2 * x

The gradient says which way is uphill. To reduce loss, we move in the
opposite direction of the gradient.
"""

import math


def loss_function(x: float) -> float:
    """Return f(x) = x**2."""
    return x**2


def gradient_function(x: float) -> float:
    """Return the derivative / gradient of x**2, which is 2x."""
    return 2 * x


# ---------------------------------------------------------------------------
# 1. ORDINARY GRADIENT DESCENT: the starting point for comparison
# ---------------------------------------------------------------------------
#
# Rule:
#     x = x - learning_rate * gradient
#
# Problem:
# Ordinary gradient descent only sees the CURRENT gradient. It does not
# remember its earlier moves. On a long, narrow valley it may zig-zag:
# left, right, left, right ... and make slow progress toward the bottom.


def ordinary_gradient_descent(
    x: float, learning_rate: float, steps: int
) -> list[tuple[int, float, float]]:
    """Minimize x**2 with ordinary gradient descent.

    Returns tuples in this order:
        (step_number, x_after_update, loss_after_update)
    """
    history = []

    for step in range(1, steps + 1):
        gradient = gradient_function(x)
        x = x - learning_rate * gradient
        history.append((step, x, loss_function(x)))

    return history


# ---------------------------------------------------------------------------
# 2. MOMENTUM
# ---------------------------------------------------------------------------
#
# Intuition:
# Think about rolling a ball down a hill. It remembers some of its previous
# movement. If gradients keep pointing in roughly the same direction,
# momentum builds up speed. If gradients flip left/right, the old movement
# partly cancels the new movement, which reduces zig-zagging.
#
# We keep a variable named velocity. It is a signed number:
#     negative velocity -> x moves left / becomes smaller
#     positive velocity -> x moves right / becomes larger
#
# Rules:
#     velocity = momentum * old_velocity - learning_rate * gradient
#     x = x + velocity
#
# We ADD velocity because the minus sign is already inside the velocity rule.
# Do not subtract it again.
#
# Common setting:
#     momentum = 0.9
#
# First example: x=5, learning_rate=0.1, velocity=0
#     gradient = 2*5 = 10
#     velocity = 0.9*0 - 0.1*10 = -1
#     x = 5 + (-1) = 4
#
# Second step:
#     gradient = 2*4 = 8
#     velocity = 0.9*(-1) - 0.1*8 = -1.7
#     x = 4 + (-1.7) = 2.3
#
# Momentum can overshoot the bottom. That is normal: when x becomes negative,
# the gradient becomes negative and future updates slow/reverse the velocity.
# Loss never becomes negative here, because x**2 is always >= 0.


def momentum_gradient_descent(
    x: float, learning_rate: float, momentum: float, steps: int
) -> list[tuple[int, float, float, float]]:
    """Minimize x**2 using momentum.

    Each returned tuple is:
        (step_number, x_after_update, velocity, loss_after_update)
    """
    velocity = 0.0  # No past movement at the beginning.
    history = []

    for step in range(1, steps + 1):
        gradient = gradient_function(x)

        # Mix old movement with the new downhill push.
        velocity = momentum * velocity - learning_rate * gradient
        x = x + velocity

        history.append((step, x, velocity, loss_function(x)))

    return history


# ---------------------------------------------------------------------------
# 3. RMSPROP
# ---------------------------------------------------------------------------
#
# Why it exists:
# In a 2D or neural-network problem, different parameters can have very
# different gradient sizes. One direction may be steep and another flat.
# A single learning rate is not ideal for both.
#
# RMSProp remembers the RECENT SIZE of gradients for every parameter.
# It keeps a variable s (sometimes written v):
#
#     s = decay * old_s + (1 - decay) * gradient**2
#
# gradient**2 is used because size should not have a direction:
#     (+10)**2 = 100
#     (-10)**2 = 100
# Without the square, positive and negative gradients could cancel even when
# both were large.
#
# Update:
#     x = x - learning_rate * gradient / (sqrt(s) + epsilon)
#
# sqrt(s) is important. s stores a SQUARED size, so sqrt brings it back to
# the normal gradient scale. epsilon is a tiny number that prevents division
# by zero when s is zero.
#
# Effect:
#     large recent gradients -> large s -> larger denominator -> smaller step
#     small recent gradients -> small s -> smaller denominator -> relatively
#                               larger step
#
# Example with s=0, gradient=10, decay=.9:
#     s = .9*0 + .1*(10**2) = 10
#     step size = .1*10 / sqrt(10) ~= .316
#
# Note: RMSProp does NOT store direction memory. It uses the current gradient
# for direction. It only adapts the step size.


def rmsprop_gradient_descent(
    x: float,
    learning_rate: float,
    decay: float,
    steps: int,
    epsilon: float = 1e-8,
) -> list[tuple[int, float, float, float]]:
    """Minimize x**2 using RMSProp.

    Each returned tuple is:
        (step_number, x_after_update, s, loss_after_update)
    """
    s = 0.0  # Squared-gradient-size memory.
    history = []

    for step in range(1, steps + 1):
        gradient = gradient_function(x)

        # Remember recent gradient sizes, without direction.
        s = decay * s + (1 - decay) * gradient**2

        # Current gradient gives direction; sqrt(s) scales the step safely.
        x = x - learning_rate * gradient / (math.sqrt(s) + epsilon)
        history.append((step, x, s, loss_function(x)))

    return history


# ---------------------------------------------------------------------------
# 4. ADAM: Adaptive Moment Estimation
# ---------------------------------------------------------------------------
#
# Adam combines the best ideas above:
#
#     m = direction memory (like Momentum)
#     v = squared-gradient-size memory (like RMSProp)
#
# Raw memory rules:
#     m = beta1 * old_m + (1 - beta1) * gradient
#     v = beta2 * old_v + (1 - beta2) * gradient**2
#
# m must keep its sign:
#     m < 0 means a negative-direction push
#     m > 0 means a positive-direction push
# We do NOT take sqrt(m): m may be negative, and squaring it would lose the
# direction.
#
# v is always >= 0 because it stores gradient**2. We DO use sqrt(v), because
# v measures a squared size.
#
# Common settings:
#     beta1 = 0.9     # direction-memory amount
#     beta2 = 0.999   # size-memory amount
#     epsilon = 1e-8  # division-by-zero safety
#
# Bias correction:
# At the beginning m and v start at 0. Their first values are artificially
# too small because they are mixed with that starting zero.
#
# For gradient = 10 at step 1:
#     m = .9*0 + .1*10 = 1       (but the gradient was 10)
#     v = .999*0 + .001*100 = .1 (but gradient**2 was 100)
#
# Correct them:
#     m_corrected = m / (1 - beta1**step)
#     v_corrected = v / (1 - beta2**step)
#
# At step 1:
#     m_corrected = 1 / (1 - .9) = 10
#     v_corrected = .1 / (1 - .999) = 100
#
# Final Adam update:
#     x = x - learning_rate * m_corrected / (sqrt(v_corrected) + epsilon)
#
# At the FIRST step in this example, x moves about 0.1, not 0.316:
#     .1 * 10 / sqrt(100) = .1
# Bias correction is the reason.


def adam_gradient_descent(
    x: float,
    learning_rate: float,
    beta1: float,
    beta2: float,
    steps: int,
    epsilon: float = 1e-8,
) -> list[tuple[int, float, float, float, float]]:
    """Minimize x**2 using Adam.

    Each returned tuple is:
        (step_number, x_after_update, m, v, loss_after_update)
    """
    m = 0.0  # Signed direction memory.
    v = 0.0  # Non-negative squared-size memory.
    history = []

    # Start at 1 because bias correction divides by (1 - beta**step).
    # At step 0, (1 - beta**0) is zero, so that would divide by zero.
    for step in range(1, steps + 1):
        gradient = gradient_function(x)

        # 1. Update the two memories.
        m = beta1 * m + (1 - beta1) * gradient
        v = beta2 * v + (1 - beta2) * gradient**2

        # 2. Remove the early "started at zero" bias.
        m_corrected = m / (1 - beta1**step)
        v_corrected = v / (1 - beta2**step)

        # 3. Take a step using direction from m and safe scale from sqrt(v).
        x = x - learning_rate * m_corrected / (
            math.sqrt(v_corrected) + epsilon
        )

        history.append((step, x, m, v, loss_function(x)))

    return history


def print_examples() -> None:
    """Run all three optimizer examples and print simple results."""
    print("Ordinary gradient descent (start=5, lr=0.1):")
    for step, x, loss in ordinary_gradient_descent(5.0, 0.1, 5):
        print(f"  step {step}: x={x:.4f}, loss={loss:.4f}")

    print("\nMomentum (start=5, lr=0.1, momentum=0.9):")
    for step, x, velocity, loss in momentum_gradient_descent(5.0, 0.1, 0.9, 5):
        print(
            f"  step {step}: x={x:.4f}, velocity={velocity:.4f}, "
            f"loss={loss:.4f}"
        )

    print("\nRMSProp (start=5, lr=0.1, decay=0.9):")
    for step, x, s, loss in rmsprop_gradient_descent(5.0, 0.1, 0.9, 5):
        print(f"  step {step}: x={x:.4f}, s={s:.4f}, loss={loss:.4f}")

    print("\nAdam (start=5, lr=0.1, beta1=0.9, beta2=0.999):")
    for step, x, m, v, loss in adam_gradient_descent(5.0, 0.1, 0.9, 0.999, 5):
        print(
            f"  step {step}: x={x:.4f}, m={m:.4f}, v={v:.4f}, "
            f"loss={loss:.4f}"
        )


if __name__ == "__main__":
    print_examples()


# ---------------------------------------------------------------------------
# KEY TAKEAWAYS
# ---------------------------------------------------------------------------
#
# 1. Gradient descent uses only the current gradient.
# 2. Momentum remembers previous movement / direction and can reduce zig-zags.
# 3. RMSProp remembers squared gradient size for each parameter and adapts
#    the effective step size.
# 4. Adam has BOTH memories:
#       m -> direction memory
#       v -> size memory
# 5. Adam's bias correction matters most at early steps because m and v
#    started at zero.
# 6. In real ML code, a library such as PyTorch calculates gradients and
#    applies Adam. Learning these formulas lets you understand what it does.
#
# COMMON MISTAKES
#
# - Momentum: writing x = x - velocity. Wrong with the convention used here;
#   velocity already contains the minus-gradient direction. Use x = x + velocity.
# - RMSProp / Adam: forgetting gradient**2 in s or v.
# - Adam: using sqrt(m). m must keep direction and can be negative.
# - Adam: forgetting bias correction at the beginning.
# - Adam: beginning steps at 0; this makes (1 - beta**step) equal zero.
# - Thinking loss is negative when x is negative. For x**2, loss is always
#   non-negative; only x, gradient, m, or velocity may be negative.
