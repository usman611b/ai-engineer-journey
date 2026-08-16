"""
Lesson 06 - Probability, Part 1
================================

This is a standalone study file. Read it from top to bottom, then run it:

    python lesson_06_probability_part1.py

The printed demonstrations reinforce these ideas:

1. Probability intuition
2. Sample spaces and events
3. Conditional probability and independence
4. Random variables
5. Discrete versus continuous random variables
6. PMF versus PDF

Only Python's standard library is used.

BIG PICTURE
-----------
Probability is a language for reasoning when we are uncertain. In AI/ML, we
rarely know everything with certainty: an image may be a cat with probability
0.9, a future word may have several plausible choices, and observed data may
contain noise. Probability lets us represent and update that uncertainty.
"""

from collections import Counter
from math import pi, sqrt, exp
from random import Random


SEPARATOR = "\n" + "=" * 78


def heading(title: str) -> None:
    """Print a clear separator when the demonstrations are run."""
    print(SEPARATOR)
    print(title)
    print("=" * 78)


# =============================================================================
# 1. PROBABILITY INTUITION
# =============================================================================

# A probability is a number from 0 to 1:
#
#     0   means impossible
#     1   means certain
#     0.5 means a 50% chance
#
# For equally likely outcomes:
#
#              number of favorable outcomes
#     P(event) = ----------------------------
#                total number of outcomes
#
# Example: a fair die has six equally likely results. Two results (2 and 4)
# are even and below 5, so that event has probability 2/6 = 1/3.
#
# Two useful interpretations:
#
# - Theoretical probability: what a mathematical model says should happen.
# - Experimental probability: the fraction observed after repeated trials.
#
# The experimental fraction usually approaches the theoretical probability
# as the number of trials grows. It does not have to match exactly in a small
# experiment. This is the intuition behind the law of large numbers.


def probability_from_counts(favorable: int, total: int) -> float:
    """Return favorable / total, with basic validation."""
    if total <= 0:
        raise ValueError("total must be positive")
    if not 0 <= favorable <= total:
        raise ValueError("favorable must be between 0 and total")
    return favorable / total


def demo_probability_intuition(rng: Random) -> None:
    heading("1. Probability intuition")
    theoretical = 1 / 6
    print(f"Theoretical P(rolling a 6) = {theoretical:.4f}")

    for number_of_rolls in (10, 100, 10_000):
        rolls = [rng.randint(1, 6) for _ in range(number_of_rolls)]
        experimental = rolls.count(6) / number_of_rolls
        print(
            f"After {number_of_rolls:>6,} rolls: observed fraction of sixes "
            f"= {experimental:.4f}"
        )


# AI/ML CONNECTION:
# A classifier may output {"cat": 0.80, "dog": 0.15, "bird": 0.05}.
# These numbers express uncertainty and add to 1. A well-calibrated model that
# says "80%" many times should be correct roughly 80% of those times.


# =============================================================================
# 2. SAMPLE SPACES AND EVENTS
# =============================================================================

# An experiment is a process with an uncertain result, such as rolling a die.
#
# The sample space, often written Omega, is the set of ALL possible basic
# outcomes. For a die:
#
#     Omega = {1, 2, 3, 4, 5, 6}
#
# An event is any subset of the sample space. For example:
#
#     E = "roll an even number" = {2, 4, 6}
#
# The event happens whenever the observed outcome belongs to its set.
#
# Set operations give probability words a precise meaning:
#
#     A or B  -> union, A | B
#     A and B -> intersection, A & B
#     not A   -> complement, Omega - A


def event_probability(event: set, sample_space: set) -> float:
    """Probability of an event when all sample-space outcomes are equally likely."""
    if not event <= sample_space:
        raise ValueError("event must be a subset of the sample space")
    return len(event) / len(sample_space)


def demo_sample_space_and_events() -> None:
    heading("2. Sample spaces and events")
    omega = {1, 2, 3, 4, 5, 6}
    even = {2, 4, 6}
    greater_than_three = {4, 5, 6}

    print("Die sample space Omega:", sorted(omega))
    print("A = even:", sorted(even))
    print("B = greater than 3:", sorted(greater_than_three))
    print(f"P(A)       = {event_probability(even, omega):.3f}")
    print(f"P(A and B) = {event_probability(even & greater_than_three, omega):.3f}")
    print(f"P(A or B)  = {event_probability(even | greater_than_three, omega):.3f}")
    print(f"P(not A)   = {event_probability(omega - even, omega):.3f}")


# AI/ML CONNECTION:
# For a classifier with sample space {cat, dog, bird}, the event "not a bird"
# is {cat, dog}. If P(cat)=0.70 and P(dog)=0.20, then P(not bird)=0.90.


# =============================================================================
# 3. CONDITIONAL PROBABILITY AND INDEPENDENCE
# =============================================================================

# Conditional probability asks:
#
#     "What is the probability of A now that I know B happened?"
#
# It is written P(A | B), read "probability of A given B":
#
#                  P(A and B)
#     P(A | B) = --------------       when P(B) > 0
#                      P(B)
#
# Intuition: knowledge of B shrinks our world from the whole sample space to B.
# We then ask what fraction of that smaller world also belongs to A.
#
# Example with a die:
#     A = even = {2, 4, 6}
#     B = greater than 3 = {4, 5, 6}
#
# After learning B, only {4, 5, 6} remain possible. Two of those values, 4 and
# 6, are even. Therefore P(A | B) = 2/3.
#
# INDEPENDENCE
# Two events A and B are independent when learning that one happened does not
# change the probability of the other:
#
#     P(A | B) = P(A)
#
# Equivalently:
#
#     P(A and B) = P(A) * P(B)
#
# Important: "independent" does NOT mean "cannot happen together." Mutually
# exclusive non-impossible events are actually dependent: if one happens, we
# know the other did not happen.


def conditional_probability(a: set, given_b: set) -> float:
    """Compute P(A | B) for equally likely outcomes represented by sets."""
    if not given_b:
        raise ValueError("cannot condition on an impossible/empty event")
    return len(a & given_b) / len(given_b)


def demo_conditional_probability() -> None:
    heading("3. Conditional probability and independence")
    omega = {1, 2, 3, 4, 5, 6}
    even = {2, 4, 6}
    above_three = {4, 5, 6}
    print(f"P(even) = {event_probability(even, omega):.3f}")
    print(f"P(even | above 3) = {conditional_probability(even, above_three):.3f}")
    print("Knowledge changed the probability, so these events are dependent.")

    # Two fair coin flips: the first flip does not affect the second.
    coin_space = {"HH", "HT", "TH", "TT"}
    first_heads = {"HH", "HT"}
    second_heads = {"HH", "TH"}
    p_first = event_probability(first_heads, coin_space)
    p_first_given_second = conditional_probability(first_heads, second_heads)
    print(f"\nP(first is H) = {p_first:.3f}")
    print(f"P(first is H | second is H) = {p_first_given_second:.3f}")
    print("The probability did not change: the two flips are independent.")


# AI/ML CONNECTION:
# Spam detection uses conditional information. P(spam) is a prior belief;
# P(spam | email contains "free prize") is an updated belief after evidence.
# Many useful models make simplifying independence assumptions. Naive Bayes,
# for example, assumes features are conditionally independent given the class.


# =============================================================================
# 4. RANDOM VARIABLES
# =============================================================================

# A random variable is a rule that converts each outcome of an uncertain
# experiment into a number. Despite its name, it is a function/mapping.
#
# Example: flip two coins and let X = number of heads.
#
#     outcome HH -> X = 2
#     outcome HT -> X = 1
#     outcome TH -> X = 1
#     outcome TT -> X = 0
#
# Notice that different outcomes can produce the same random-variable value.
# The original outcome and the number assigned to it are not the same thing.


def number_of_heads(two_flip_outcome: str) -> int:
    """Random variable X: map a two-coin outcome to its number of heads."""
    return two_flip_outcome.count("H")


def demo_random_variable() -> None:
    heading("4. Random variables")
    outcomes = ["HH", "HT", "TH", "TT"]
    for outcome in outcomes:
        print(f"Outcome {outcome} -> X = number of heads = {number_of_heads(outcome)}")


# AI/ML CONNECTION:
# Random variables can represent a class label, token ID, pixel intensity,
# prediction error, training loss, or a model's uncertain future output.


# =============================================================================
# 5. DISCRETE VERSUS CONTINUOUS RANDOM VARIABLES
# =============================================================================

# DISCRETE random variables have separate, countable possible values.
# Examples: die result, number of emails, token ID, class label encoding.
# Possible die values are 1, 2, ..., 6; a normal die cannot produce 2.713.
#
# CONTINUOUS random variables can take any value in an interval (in the model).
# Examples: time, height, temperature, speed, audio amplitude.
# Between 170 cm and 171 cm are infinitely many theoretical values.
#
# A computer stores finite-precision measurements, but we often model physical
# quantities as continuous because that model is useful.


def demo_discrete_vs_continuous(rng: Random) -> None:
    heading("5. Discrete versus continuous")
    die_samples = [rng.randint(1, 6) for _ in range(8)]
    temperature_samples = [rng.uniform(20.0, 25.0) for _ in range(8)]
    print("Discrete die samples:       ", die_samples)
    print("Continuous temperature model:", [round(x, 4) for x in temperature_samples])


# =============================================================
# 6. PMF VERSUS PDF
# =============================================================

# PMF - Probability Mass Function
# --------------------------------
# A PMF belongs to a DISCRETE random variable. It assigns an actual probability
# to every possible individual value:
#
#     p(x) = P(X = x)
#
# A valid PMF obeys:
#
#     p(x) >= 0 for every x
#     sum of p(x) over all possible x = 1
#
# For X = number of heads in two fair flips:
#
#     P(X=0) = 1/4
#     P(X=1) = 2/4
#     P(X=2) = 1/4
#
# The middle value is more likely because two outcomes, HT and TH, map to it.


def build_heads_pmf() -> dict[int, float]:
    """Construct the PMF for the number of heads in two fair coin flips."""
    outcomes = ["HH", "HT", "TH", "TT"]
    counts = Counter(number_of_heads(outcome) for outcome in outcomes)
    return {x: count / len(outcomes) for x, count in sorted(counts.items())}


# PDF - Probability Density Function
# -----------------------------------
# A PDF belongs to a CONTINUOUS random variable. Its height is a DENSITY, not
# the probability of one exact value. Probability is AREA under the PDF:
#
#     P(a <= X <= b) = area under f(x) from a to b
#
# A valid PDF obeys:
#
#     f(x) >= 0
#     total area under the curve = 1
#
# For a truly continuous variable:
#
#     P(X = exactly one particular value) = 0
#
# This does not mean the value is impossible. It means one point has zero width
# and therefore zero area. Intervals have probability; isolated points do not.
# Also, a PDF height can be greater than 1 as long as the total area is 1.
#
# Simple example: X is uniform from 0 to 10. The PDF has constant height 0.1.
#
#     P(2 <= X <= 5) = width * height = (5 - 2) * 0.1 = 0.3


def uniform_pdf(x: float, low: float = 0.0, high: float = 10.0) -> float:
    """PDF height for a uniform distribution on [low, high]."""
    if high <= low:
        raise ValueError("high must be greater than low")
    return 1 / (high - low) if low <= x <= high else 0.0


def uniform_interval_probability(a: float, b: float,
                                 low: float = 0.0, high: float = 10.0) -> float:
    """Area/probability where [a,b] overlaps a uniform [low,high] model."""
    overlap_width = max(0.0, min(b, high) - max(a, low))
    return overlap_width / (high - low)


def normal_pdf(x: float, mean: float = 0.0, std: float = 1.0) -> float:
    """Return the normal-distribution density at x (a height, not point probability)."""
    if std <= 0:
        raise ValueError("std must be positive")
    z = (x - mean) / std
    return exp(-0.5 * z * z) / (std * sqrt(2 * pi))


def demo_pmf_vs_pdf(rng: Random) -> None:
    heading("6. PMF versus PDF")
    pmf = build_heads_pmf()
    print("PMF for X = number of heads in two flips:")
    for x, probability in pmf.items():
        print(f"  P(X = {x}) = {probability:.2f}")
    print(f"  PMF total = {sum(pmf.values()):.2f}")

    print("\nPDF for X uniform on [0, 10]:")
    print(f"  density f(3) = {uniform_pdf(3):.2f} (density, not P(X=3))")
    interval_p = uniform_interval_probability(2, 5)
    print(f"  P(2 <= X <= 5) = area = {interval_p:.2f}")
    print("  P(X = exactly 3) = 0.00 in the continuous mathematical model")

    # Simulation approximates an interval probability. We use a seeded random
    # generator, so results are reproducible when studying/debugging.
    samples = [rng.uniform(0, 10) for _ in range(100_000)]
    estimated = sum(2 <= x <= 5 for x in samples) / len(samples)
    print(f"  Simulation estimate from 100,000 samples = {estimated:.4f}")

    print("\nStandard normal PDF heights (bell-curve shape):")
    for x in (-2, -1, 0, 1, 2):
        print(f"  f({x:>2}) = {normal_pdf(x):.4f}")


# AI/ML CONNECTIONS:
# - A softmax classifier gives a discrete distribution over classes: PMF-like.
# - A language model gives a discrete distribution over its next token.
# - A regression model may predict a normal distribution over a continuous
#   target; its likelihood is evaluated using density.
# - Generative models often sample continuous latent variables from a normal
#   distribution and turn them into images, audio, or other outputs.
# - Negative log-likelihood trains models to put more mass/density on observed
#   data. For continuous data we optimize density values, not point probability.


# ==============================================================
# QUICK MEMORY GUIDE
# ==============================================================

# Sample space: all basic outcomes.
# Event: a set of outcomes we care about.
# Conditional probability: probability after restricting to known evidence.
# Independence: knowing one event does not change the other's probability.
# Random variable: maps uncertain outcomes to numerical values.
# Discrete: separate/countable values -> use a PMF -> probabilities are heights.
# Continuous: values along intervals -> use a PDF -> probabilities are areas.
#
# The shortest PMF/PDF reminder:
#
#     PMF: add probability masses at individual values.
#     PDF: integrate density over an interval (find area).


def main() -> None:
    """Run all small demonstrations in lesson order."""
    rng = Random(42)  # Reproducible demonstrations.
    print(__doc__)
    demo_probability_intuition(rng)
    demo_sample_space_and_events()
    demo_conditional_probability()
    demo_random_variable()
    demo_discrete_vs_continuous(rng)
    demo_pmf_vs_pdf(rng)
    heading("End of Lesson 06, Part 1")
    print("Try changing an event, sample size, or interval and run the file again.")


if __name__ == "__main__":
    main()
