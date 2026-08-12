"""
Lesson 4: Integrals in Machine Learning
=======================================

Main goal
---------
Understand the idea. You do NOT need to solve difficult integrals by hand
right now.

    derivative -> how fast something changes at one point
    integral   -> total accumulated amount over a range

In machine learning, integrals appear mostly in continuous probability and
expected values. During normal model training, we usually use averages over
data batches as a practical approximation instead of calculating an integral.
"""


# ---------------------------------------------------------------------------
# 1. WHAT AN INTEGRAL MEANS
# ---------------------------------------------------------------------------
#
# An integral adds many tiny pieces together.
#
# Picture the area under a curve. Split the curve into many thin rectangles:
#
#     area ≈ height_1 * tiny_width
#          + height_2 * tiny_width
#          + height_3 * tiny_width
#          + ...
#
# More, thinner rectangles give a better approximation. This is the basic
# intuition behind an integral.
#
# In symbols:
#
#     integral from a to b of f(x) dx
#
# means: add the tiny values of f(x) from x=a to x=b.


def numerical_area_under_line(a: float, b: float, rectangles: int) -> float:
    """Approximate the area under f(x)=x from a to b using rectangles.

    The exact area from 0 to 1 is 0.5. Using more rectangles gets closer to
    0.5. This is an illustration of the integral idea, not ML training code.
    """
    width = (b - a) / rectangles
    area = 0.0

    for index in range(rectangles):
        # Use the midpoint of each thin rectangle for a better approximation.
        x = a + (index + 0.5) * width
        height = x  # f(x) = x
        area += height * width

    return area


# ---------------------------------------------------------------------------
# 2. INTEGRALS AND CONTINUOUS PROBABILITY
# ---------------------------------------------------------------------------
#
# A continuous random variable can take infinitely many values. Examples:
#     height, temperature, time, weight
#
# A probability density function (PDF), written p(x), is a curve describing
# where values are more or less common.
#
# Important difference:
#     p(170) is the HEIGHT of the density curve at 170.
#     It is NOT the probability of exactly 170.000000... cm.
#
# For a continuous variable, probability comes from an AREA over a range:
#
#     P(a < X < b) = integral from a to b of p(x) dx
#
# Example:
#     Area under a height-density curve from 160 cm to 180 cm
#     = probability that a randomly chosen height lies in that range.
#
# Every valid PDF has total area 1:
#
#     integral from -infinity to infinity of p(x) dx = 1
#
# That represents 100% of all possible outcomes.


# ---------------------------------------------------------------------------
# 3. DISCRETE PROBABILITY FIRST: EASY EXPECTED VALUE
# ---------------------------------------------------------------------------
#
# Before continuous probability, use a small discrete example.
#
#     score       probability
#       1             0.2
#       2             0.5
#       3             0.3
#
# Expected value means probability-weighted average:
#
#     E[score] = 1(0.2) + 2(0.5) + 3(0.3) = 2.1
#
# Outcomes that happen more often have more influence on the average.


def discrete_expected_value(values: list[float], probabilities: list[float]) -> float:
    """Return the probability-weighted average of discrete outcomes."""
    if len(values) != len(probabilities):
        raise ValueError("values and probabilities must have the same length")

    return sum(value * probability for value, probability in zip(values, probabilities))


# ---------------------------------------------------------------------------
# 4. EXPECTED VALUE FOR CONTINUOUS DATA
# ---------------------------------------------------------------------------
#
# For continuous data, the same weighted-average idea uses an integral:
#
#     E[f(X)] = integral of f(x) * p(x) dx
#
# Read it as:
#     possible result f(x) * how likely x is
#     added across every possible x
#
# ML connection:
#
#     expected loss = average loss over the whole real data distribution
#
# This is the ideal goal. But we do not know every possible future image,
# sentence, customer, or medical record. We only have a dataset.
#
# So training uses an empirical (data-based) estimate:
#
#     average batch loss = sum of losses in batch / number of examples
#
# Adam or gradient descent reduces this average loss.


def average_loss(losses: list[float]) -> float:
    """Return the batch average: a practical estimate of expected loss."""
    if not losses:
        raise ValueError("losses cannot be empty")

    return sum(losses) / len(losses)


# ---------------------------------------------------------------------------
# 5. OTHER PLACES INTEGRALS APPEAR IN ML (RECOGNIZE THE IDEA ONLY)
# ---------------------------------------------------------------------------
#
# KL divergence:
#     Measures how different two probability distributions are.
#     Used in VAEs, knowledge distillation, and some reinforcement learning.
#
#     KL(p || q) = integral of p(x) * log(p(x) / q(x)) dx
#
# Bayesian inference:
#     Uses integrals to add over all possible parameter values.
#     These integrals are often too hard to calculate exactly, so advanced
#     methods use approximations such as sampling or variational inference.
#
# You only need the high-level message for now:
#     Integrals let probability models combine information across a continuous
#     range of possible values.


# ---------------------------------------------------------------------------
# KEY TAKEAWAYS
# ---------------------------------------------------------------------------
#
# 1. An integral is continuous adding / accumulated area.
# 2. For continuous probability, area over a range is probability.
# 3. A PDF's total area is 1.
# 4. Expected value is a probability-weighted average.
# 5. Expected loss is the ideal average loss over all real-world data.
# 6. Training batches use a normal average as an estimate of expected loss.
# 7. You will use batch-average losses often; you will rarely hand-calculate
#    integrals in ordinary deep-learning projects.


if __name__ == "__main__":
    print("Area under f(x)=x from 0 to 1:")
    for rectangles in (1, 10, 100):
        area = numerical_area_under_line(0.0, 1.0, rectangles)
        print(f"  {rectangles:3d} rectangles -> {area:.4f}")
    print("  exact answer         -> 0.5000")

    scores = [1.0, 2.0, 3.0]
    probabilities = [0.2, 0.5, 0.3]
    print("\nExpected score:", discrete_expected_value(scores, probabilities))

    batch_losses = [0.2, 0.7, 0.1, 0.4]
    print("Average batch loss:", average_loss(batch_losses))
