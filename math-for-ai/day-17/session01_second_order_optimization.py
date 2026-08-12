"""
Lesson 4: Taylor Series and Smarter Optimization Methods
=========================================================

This file covers:
    1. Taylor series: a local approximation
    2. Newton's method: gradient + curvature
    3. L-BFGS: approximate curvature from a small memory
    4. Natural gradient: changes measured by their effect on predictions

Important learning goal
-----------------------
Understand the IDEA and recognize the formulas. You do not need to memorize
or write L-BFGS or natural-gradient code from scratch right now.

For practical deep learning, you will most often use Adam or AdamW through a
library such as PyTorch.
"""


# ---------------------------------------------------------------------------
# 1. TAYLOR SERIES: A SIMPLE MODEL NEAR THE CURRENT POINT
# ---------------------------------------------------------------------------
#
# A complicated function can be approximated near the current point x.
# Let h be a small move from x. Then:
#
#     f(x + h) ≈ f(x) + f'(x) * h + 1/2 * f''(x) * h**2
#
# Read it like this:
#     f(x)          -> current loss/value
#     f'(x) * h     -> effect of slope
#     1/2*f''(x)*h² -> effect of curvature (how bowl-shaped it is)
#
# "Local" means this model is trusted only near the current point. It is like
# looking at a few metres of a winding road: that small part can look straight
# even though the entire road is not straight.
#
# Why Taylor series matters in ML:
#     - It explains why gradients help us choose a direction.
#     - It explains why curvature/Hessians can improve the step size.
#     - Smooth loss functions are easier to optimize predictably.
#
# Approximation order:
#     0th order: value only              -> no direction information
#     1st order: slope                   -> gradient descent idea
#     2nd order: slope + curvature       -> Newton's method idea
#


def taylor_x_squared_at_5(h: float) -> float:
    """Second-order Taylor model of f(x)=x² around x=5.

    For x², this model is exact because x² is already a quadratic function.

    f(5) = 25, f'(5) = 10, f''(5) = 2
    model = 25 + 10h + 1/2 * 2 * h²
    """
    return 25 + 10 * h + h**2


# ---------------------------------------------------------------------------
# 2. NEWTON'S METHOD
# ---------------------------------------------------------------------------
#
# Problem it solves:
# Gradient descent knows only the slope. A steep direction may need a smaller
# step, while a flat direction may need a larger one. Newton also uses
# curvature, so it can choose a smarter-sized step.
#
# In one variable:
#
#     new_x = x - f'(x) / f''(x)
#                  gradient / curvature
#
# Why it can be fast:
# Newton makes a local quadratic model using Taylor series and moves to the
# lowest point of that model.
#
# Example f(x) = x² at x=5:
#     gradient  = 2x = 10
#     curvature = 2
#     new_x = 5 - 10/2 = 0
#
# It reaches the minimum in one step because x² is exactly quadratic.
#
# Example f(x) = x⁴:
#     gradient = 4x³
#     curvature = 12x²
#     new_x = x - (4x³)/(12x²) = 2x/3
#
# It gets closer to zero each time but does not reach zero in one step. Each
# step makes a NEW local quadratic model at the new point.
#
# In 2D or more dimensions, f'' becomes the Hessian matrix H:
#
#     new_point = old_point - inverse(H) @ gradient
#
# The @ means matrix multiplication.
#
# Example: f(x, y) = 10x² + y²
#     gradient = [20x, 2y]
#     Hessian  = [[20, 0],
#                 [ 0, 2]]
#
# At (4, 3), the Newton update is [4, 3], so:
#     (4, 3) - (4, 3) = (0, 0)
#
# The Hessian rescales the gradient:
#     steep direction -> large curvature -> divide more -> smaller update
#     flat direction  -> small curvature -> divide less -> larger update
#
# Why we usually do NOT use full Newton for neural networks:
#     - N parameters need an N by N Hessian.
#     - 1,000,000 parameters would mean about 1 trillion Hessian entries.
#     - Calculating and solving/inverting with that matrix is too expensive.
#     - Newton can also be unsafe when curvature is zero or negative.
#
# What we use instead in deep learning:
#     Adam or AdamW. They use cheap per-parameter adaptive scaling, not a full
#     Hessian. They are the normal practical default.


def newton_on_x_fourth(start_x: float, steps: int) -> list[tuple[int, float, float]]:
    """Run safe Newton steps on f(x)=x⁴ and return (step, x, loss)."""
    x = start_x
    history = []

    for step in range(1, steps + 1):
        gradient = 4 * x**3
        curvature = 12 * x**2

        # At x=0, both are zero and gradient/curvature would be 0/0.
        # Stop because we are already at the minimum.
        if abs(gradient) < 1e-8:
            break

        x = x - gradient / curvature
        history.append((step, x, x**4))

    return history


# ---------------------------------------------------------------------------
# 3. L-BFGS: LIMITED-MEMORY BFGS
# ---------------------------------------------------------------------------
#
# Problem it solves:
# Newton wants the full Hessian, which is too large for many parameters.
# L-BFGS tries to get some curvature benefit WITHOUT storing the full Hessian.
#
# Main idea:
# It remembers a small number of recent changes:
#
#     parameter change:  new_parameters - old_parameters
#     gradient change:   new_gradient - old_gradient
#
# From this history, it builds a cheap approximation to how curvature behaves.
# "Limited memory" means it keeps only a short recent history, not everything.
#
# Comparison:
#     Newton -> exact/full curvature information; very expensive
#     L-BFGS -> estimated curvature from recent history; much cheaper
#     Adam   -> adaptive scale per parameter; simple and common in deep learning
#
# When L-BFGS is useful:
#     - small or medium smooth optimization problems
#     - some classical machine-learning and scientific problems
#     - full-batch settings, where the gradient is stable
#
# Why it is NOT the normal default for deep neural networks:
#     - neural-network training commonly uses mini-batches
#     - mini-batch gradients are noisy
#     - L-BFGS's curvature estimate works best with more stable gradients
#     - Adam/AdamW is simpler and works well at very large scale
#
# You only need to remember:
#     L-BFGS = "Newton-like curvature estimate using a small memory of past
#               parameter and gradient changes."


# ---------------------------------------------------------------------------
# 4. NATURAL GRADIENT
# ---------------------------------------------------------------------------
#
# Problem it solves:
# Ordinary gradient descent measures distance by how far WEIGHTS move. But in a
# probability model, a tiny weight change can sometimes change predictions a
# lot, while a large weight change can barely change predictions.
#
# Natural gradient asks a more meaningful question:
#
#     "What parameter change improves loss while making a controlled change
#      in the model's probability predictions?"
#
# It uses the Fisher information matrix. This matrix measures how sensitive the
# model's probability distribution is to parameter changes.
#
# Formula idea:
#     natural_update = inverse(Fisher) @ gradient
#     new_parameters = old_parameters - learning_rate * natural_update
#
# Connection to Newton:
#     Newton uses the Hessian (curvature of the loss).
#     Natural gradient uses the Fisher matrix (geometry/sensitivity of the
#     probability model).
#
# When the idea appears:
#     - probability models
#     - reinforcement learning and policy optimization
#     - variational inference and some Bayesian ML
#
# Why we do NOT normally compute it exactly for big neural networks:
#     - The Fisher matrix can also be huge: N by N for N parameters.
#     - It is expensive to calculate and solve/invert.
#
# What is used instead:
#     - Adam/AdamW for most normal deep learning projects
#     - special approximations only in advanced research or specialized work
#
# You only need to remember:
#     Natural gradient = "move based on the effect on predictions, not only the
#     raw distance moved in weight space."


# ---------------------------------------------------------------------------
# SUMMARY: WHICH TOOL SOLVES WHICH PROBLEM?
# ---------------------------------------------------------------------------
#
# Gradient descent:
#     Uses: current gradient
#     Solves: basic downhill optimization
#     Limitation: one learning rate; no curvature information
#
# Newton:
#     Uses: gradient + exact Hessian
#     Solves: fast optimization on small, smooth problems
#     Limitation: full Hessian is too expensive for huge networks
#
# L-BFGS:
#     Uses: gradient + short history to estimate curvature
#     Solves: Newton-like optimization without the full Hessian
#     Limitation: less suitable for noisy mini-batch deep-learning training
#
# Natural gradient:
#     Uses: gradient + Fisher information matrix
#     Solves: updates that respect changes in probability predictions
#     Limitation: Fisher matrix is expensive for big models
#
# Adam / AdamW:
#     Uses: gradient direction memory + squared-gradient-size memory
#     Solves: practical, stable optimization for large neural networks
#     Why used most: cheap, scalable, and available in ML libraries


if __name__ == "__main__":
    print("Taylor model for x² around x=5, moving h=-5:")
    print("  predicted value:", taylor_x_squared_at_5(-5.0))

    print("\nNewton's method on f(x)=x**4 from x=6:")
    for step, x, loss in newton_on_x_fourth(6.0, 5):
        print(f"  step {step}: x={x:.4f}, loss={loss:.4f}")
