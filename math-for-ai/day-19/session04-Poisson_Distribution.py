"""
LESSON 6 - POISSON DISTRIBUTION
===============================

STUDY ORDER
-----------
Read the question Poisson answers, understand lambda, calculate one probability
by hand, then read the roadmap code. Run with:

    python 06_poisson_distribution.py


===============================================================================
1. WHAT QUESTION DOES POISSON ANSWER?
===============================================================================

Bernoulli asks:    Did one event happen? (0 or 1)
Categorical asks:  Which one category happened?
Poisson asks:      How many times did an event happen in a fixed interval?

Examples:

    How many API requests arrive in one second?
    How many customers enter a store in ten minutes?
    How many errors occur in one hour?
    How many emails arrive in one day?

Define:

    X = number of events in the interval

Possible values are:

    X belongs to {0, 1, 2, 3, ...}

These values are countable, so Poisson is discrete and uses a PMF.


===============================================================================
2. THE PARAMETER lambda
===============================================================================

The Greek letter lambda is written ``lam`` in our Python code.

    lambda = expected average number of events per chosen interval

If a server receives 3 requests per second on average:

    lambda = 3 for a one-second interval

This does not mean exactly three requests arrive every second. Observations may
look like:

    2, 5, 3, 1, 4, 3, 6, ...

Across many equal intervals, their average tends toward 3.

The interval matters. If the average is 3 per second, then over ten seconds the
corresponding expected count is 30, assuming the rate stays constant.


===============================================================================
3. THE PMF AND WHAT ITS PARTS MEAN
===============================================================================

For count k and rate lambda:

    P(X=k) = (lambda^k * e^(-lambda)) / k!

Do not memorize it blindly. Read its purpose:

    Given the usual average rate lambda, how believable is exactly k events?

Pieces:

    lambda^k  -> combines the expected activity with the requested count
    e^-lambda -> exponential decrease needed by the probability model
    k!        -> factorial normalization for the many possible event orderings

Factorial means:

    0! = 1
    1! = 1
    3! = 3*2*1 = 6
    5! = 5*4*3*2*1 = 120


===============================================================================
4. COMPLETE HAND CALCULATION
===============================================================================

Suppose a support desk averages 2 tickets per hour:

    lambda = 2

Question: what is the probability of exactly 3 tickets next hour?

    k = 3

Substitute:

    P(X=3) = (2^3 * e^-2) / 3!

Calculate each part:

    2^3 = 8
    e^-2 is approximately 0.1353
    3! = 3*2*1 = 6

Combine:

    P(X=3) = (8 * 0.1353) / 6
           = 1.0824 / 6
           = 0.1804

Interpretation: about an 18.04% chance of exactly three tickets, under this
Poisson model.


===============================================================================
5. SHAPE, MEAN, AND VARIANCE
===============================================================================

The largest probabilities usually occur near lambda.

    lambda=1  -> likely counts are near 0, 1, 2
    lambda=10 -> likely counts move near 8, 9, 10, 11, 12

For Poisson:

    E[X] = lambda
    Var(X) = lambda

The first equality matches the definition of lambda. The second is a special
property: as the expected count increases, absolute count variation also grows.

This equality is also a warning. Real count data can have variance much larger
than its mean (overdispersion), which tells us simple Poisson may not fit well.


===============================================================================
6. WHEN POISSON IS A REASONABLE MODEL
===============================================================================

The basic assumptions are approximately:

    - We count events in a fixed time, space, or opportunity interval.
    - Events happen roughly independently.
    - The average rate is reasonably stable inside the interval.
    - Simultaneous events in an infinitely tiny interval are negligible.

Do not use Poisson automatically for every count. A changing rate, events that
trigger other events, or strong overdispersion can violate its assumptions.


===============================================================================
7. AI/ENGINEERING CONNECTIONS
===============================================================================

Anomaly detection:

    normal server errors per hour: lambda=2
    observed this hour: 15

If P(X=15) is extremely small, the count may deserve investigation.

Count prediction:

    customer features -> neural network -> predicted lambda=2.7

The model does not claim the customer makes exactly 2.7 purchases. Counts are
integers. It says the expected count is 2.7 and Poisson turns that rate into a
distribution over 0, 1, 2, 3, ... purchases.

Other examples include click counts, failures, requests, purchases, messages,
and occurrences of a word or event.


===============================================================================
8. ROADMAP CODE DRY-RUN
===============================================================================

Roadmap:

    def poisson_pmf(k, lam):
        return (lam ** k) * math.exp(-lam) / factorial(k)

For poisson_pmf(3, 2):

    lam ** k          -> 2 ** 3 -> 8
    math.exp(-lam)    -> e^-2   -> 0.1353
    factorial(k)      -> 3!     -> 6
    8*0.1353/6        -> 0.1804


===============================================================================
9. COMMON CONFUSIONS
===============================================================================

1. lambda is not the count guaranteed in every interval; it is the average.
2. Poisson counts occurrences, while Bernoulli describes one yes/no trial.
3. The output of the PMF is a probability; lambda itself need not be an integer.
4. k must be a nonnegative integer because it is an observed event count.
5. A count dataset is not automatically Poisson; assumptions still matter.

Mental model:

    average event rate lambda
              -> Poisson PMF
              -> probability of each possible count k
"""

import math


def factorial(n):
    """Calculate n! using the beginner roadmap loop."""
    if n < 0 or int(n) != n:
        raise ValueError("Factorial requires a nonnegative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def poisson_pmf(k, lam):
    """Return P(X=k) for a Poisson distribution with average rate lam."""
    if k < 0 or int(k) != k:
        raise ValueError("k must be a nonnegative integer count.")
    if lam <= 0:
        raise ValueError("lambda must be positive.")
    return (lam ** k) * math.exp(-lam) / factorial(k)


def demonstrate_factorial():
    print("\n" + "=" * 78)
    print("DEMO 1 - FACTORIAL")
    print("=" * 78)
    for n in range(6):
        print(f"{n}! = {factorial(n)}")


def demonstrate_hand_example():
    print("\n" + "=" * 78)
    print("DEMO 2 - EXACTLY 3 EVENTS WHEN LAMBDA=2")
    print("=" * 78)
    k, lam = 3, 2
    power = lam ** k
    decay = math.exp(-lam)
    normalization = factorial(k)
    print(f"lambda^k = {lam}^{k} = {power}")
    print(f"e^(-lambda) = e^-{lam} = {decay:.4f}")
    print(f"k! = {k}! = {normalization}")
    print(f"P(X=3) = {power}*{decay:.4f}/{normalization}")
    print(f"P(X=3) = {poisson_pmf(k, lam):.4f} = 18.04% approximately")


def demonstrate_distribution():
    print("\n" + "=" * 78)
    print("DEMO 3 - PROBABILITIES ACROSS COUNTS")
    print("=" * 78)
    lam = 3
    total_shown = 0
    for k in range(11):
        probability = poisson_pmf(k, lam)
        total_shown += probability
        print(f"k={k:>2}: P(X=k)={probability:.5f} {'#' * round(probability * 80)}")
    print(f"Probability shown for k=0..10: {total_shown:.6f}")
    print("The tiny remaining tail lies above 10.")


def practice_questions():
    print("\n" + "=" * 78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("=" * 78)
    print("""
1. What does lambda=4 requests/minute mean?
2. Can k be 2.5? Why?
3. What are the Poisson mean and variance when lambda=4?
4. Is "did one request arrive?" naturally Poisson or Bernoulli?
5. Name two assumptions that can make Poisson reasonable.

Solutions:
1. The expected average is four requests in each one-minute interval.
2. No. k is an event count and must be a nonnegative integer.
3. Mean=4 and variance=4.
4. Bernoulli is the direct yes/no model; Poisson models the number of arrivals.
5. Rough independence and a reasonably stable average rate (among others).
""")


def main():
    demonstrate_factorial()
    demonstrate_hand_example()
    demonstrate_distribution()
    practice_questions()


if __name__ == "__main__":
    main()
