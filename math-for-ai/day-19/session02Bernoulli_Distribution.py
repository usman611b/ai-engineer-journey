"""
LESSON 6 — BERNOULLI DISTRIBUTION
=================================

HOW TO STUDY THIS FILE
----------------------
Study this lesson in order. Read the intuition, predict each example, follow the
hand calculation, and only then run the code:

    python 04_bernoulli_distribution.py

The code follows the simple Lesson 6 roadmap. It uses ordinary functions,
lists, loops, arithmetic, and Python's standard ``random`` module.


===============================================================================
1. WHAT PROBLEM DOES BERNOULLI SOLVE?
===============================================================================

Bernoulli is the simplest probability distribution. It is used when ONE
uncertain experiment has exactly TWO possible outcomes.

Examples:

    yes / no
    success / failure
    spam / not spam
    clicked / did not click
    fraud / not fraud
    cat / not cat
    customer leaves / customer stays

We usually encode the outcomes as:

    1 = the event we are interested in happened
    0 = the event did not happen

Therefore a Bernoulli random variable has only two possible values:

    X belongs to {0, 1}

"Success" is only a mathematical name for X=1. It does not have to mean
something good. If X=1 means fraud, fraud is called success only because it is
the event we chose to track.

Bernoulli describes ONE trial:

    Will this one email be spam?                -> Bernoulli
    Will this one user click the advertisement? -> Bernoulli

If we ask "How many of 100 emails are spam?", each email can be a Bernoulli
trial, but the total count leads to the Binomial distribution. Keep this basic
distinction in mind:

    one binary trial        -> Bernoulli
    successes in many trials -> Binomial


===============================================================================
2. THE ONE PARAMETER p
===============================================================================

The complete distribution is controlled by one number called p:

    p = probability that X equals 1

In symbols:

    P(X = 1) = p

There are only two outcomes, and total probability must be 1. Therefore:

    P(X = 0) = 1 - p

Example:

    p = 0.8

Then:

    P(X = 1) = 0.8
    P(X = 0) = 1 - 0.8 = 0.2

Check:

    0.8 + 0.2 = 1.0

We do not need a second independent parameter. Once p is known, 1-p is forced
by the rule that all probability must add to 1.

The valid range is:

    0 <= p <= 1

Meaning:

    p = 0   -> X is certainly 0
    p = 0.5 -> 0 and 1 are equally likely
    p = 1   -> X is certainly 1


===============================================================================
3. REAL INTUITION: A SPAM CLASSIFIER
===============================================================================

Suppose an email classifier says:

    Spam     = 0.90
    Not spam = 0.10

Define:

    X = 1 means spam
    X = 0 means not spam

Then the classifier is describing a Bernoulli distribution:

    P(X = 1) = 0.90
    P(X = 0) = 0.10

Bernoulli answers:

    For one uncertain yes/no event, how should total belief be divided between
    the two possible outcomes?

The actual label is still 0 or 1. The value 0.90 does not mean the email is
"90% of an email" or partly spam. It represents the model's uncertainty about
which binary label is correct.


===============================================================================
4. WHY BERNOULLI USES A PMF
===============================================================================

Bernoulli is discrete because we can list its values exactly: 0 and 1.

A Probability Mass Function (PMF) answers:

    What probability belongs to this exact discrete value?

For Bernoulli:

    PMF at 1 = p
    PMF at 0 = 1-p

The roadmap code is intentionally simple:

    def bernoulli_pmf(k, p):
        return p if k == 1 else (1 - p)

Read it as English:

    if k is 1:
        return p
    otherwise:
        return 1-p

Our runnable function adds basic validation so an invalid k or p produces a
helpful error. The probability idea remains exactly the roadmap idea.


===============================================================================
5. PMF HAND DRY-RUN
===============================================================================

Let p=0.8 and call:

    bernoulli_pmf(1, 0.8)

Line by line:

    Is k equal to 1? -> yes
    Return p          -> return 0.8

Now call:

    bernoulli_pmf(0, 0.8)

Line by line:

    Is k equal to 1? -> no
    Return 1-p        -> 1-0.8 -> return 0.2

The full PMF table is:

    k          0       1
    P(X=k)    0.2     0.8

The masses add to 1:

    0.2 + 0.8 = 1.0


===============================================================================
6. EXPECTED VALUE: WHY E[X] = p
===============================================================================

Expected value is a probability-weighted long-run average. For a discrete
random variable:

    E[X] = sum of (value * probability of that value)

Bernoulli has only 0 and 1:

    E[X] = 0*P(X=0) + 1*P(X=1)

Replace the probabilities:

    E[X] = 0*(1-p) + 1*p
         = 0 + p
         = p

For p=0.8:

    E[X] = 0*0.2 + 1*0.8
         = 0.8

But one Bernoulli outcome can never literally be 0.8. It is only 0 or 1. The
meaning appears when we repeat similar trials:

    1, 1, 0, 1, 1, 1, 0, 1, ...

For zero/one data:

    average = number of ones / number of trials

If roughly 80% of the outcomes are 1, their average approaches 0.8. Therefore
E[X]=p means that the long-run fraction of successes approaches p.


===============================================================================
7. WHY THE MEAN IS NOT ENOUGH
===============================================================================

Compare these datasets:

    A = [5, 5, 5, 5, 5]
    B = [1, 3, 5, 7, 9]

Both have mean 5. But A is perfectly stable and B is spread around 5.

This is why we also need variance:

    mean     -> Where is the center?
    variance -> How far do values spread around that center?


===============================================================================
8. BERNOULLI VARIANCE INTUITION
===============================================================================

Bernoulli variance is:

    Var(X) = p(1-p)

Do not memorize it before understanding it.

Case A: p=0.99

    P(1)=0.99 and P(0)=0.01
    Outcomes look like: 1, 1, 1, 1, 1, 0, 1, 1, ...

The result is random but very predictable. Variance is low:

    0.99*(1-0.99) = 0.0099

Case B: p=0.50

    P(1)=0.50 and P(0)=0.50
    Outcomes look like: 1, 0, 1, 1, 0, 0, 1, 0, ...

Either result can easily happen. Bernoulli variance is at its maximum:

    0.50*(1-0.50) = 0.25

Case C: p=0.01

The outcome is now almost always 0, so variance is low again:

    0.01*(1-0.01) = 0.0099

Mental model:

    p near 0 -> almost always 0 -> low variance
    p = 0.5  -> could go either way -> highest variance
    p near 1 -> almost always 1 -> low variance

For Bernoulli, variance gives useful uncertainty intuition. More precisely,
variance always means spread around the mean.


===============================================================================
9. DERIVING Var(X) = p(1-p), STEP BY STEP
===============================================================================

The general discrete variance formula says:

    variance = sum of probability * (value - mean)^2

For Bernoulli, the mean is p and the values are 0 and 1:

    Var(X) = P(X=0)*(0-p)^2 + P(X=1)*(1-p)^2

Replace the probabilities:

    Var(X) = (1-p)*(0-p)^2 + p*(1-p)^2
           = (1-p)*p^2 + p*(1-p)^2

Factor out p(1-p):

    Var(X) = p(1-p) * [p + (1-p)]

The bracket is 1, so:

    Var(X) = p(1-p)

Now calculate it by hand for p=0.8.

The mean is 0.8.

Outcome 0 contribution:

    distance from mean = 0-0.8 = -0.8
    squared distance   = (-0.8)^2 = 0.64
    probability        = 0.2
    contribution       = 0.2*0.64 = 0.128

Outcome 1 contribution:

    distance from mean = 1-0.8 = 0.2
    squared distance   = 0.2^2 = 0.04
    probability        = 0.8
    contribution       = 0.8*0.04 = 0.032

Add them:

    variance = 0.128 + 0.032 = 0.160

Check with the short formula:

    p(1-p) = 0.8*0.2 = 0.160


===============================================================================
10. SAMPLING — ROADMAP METHOD
===============================================================================

A distribution describes possible outcomes and their probabilities. Sampling
turns that description into actual outcomes.

Roadmap code:

    def sample_bernoulli(p, n=1):
        return [
            1 if random.random() < p else 0
            for _ in range(n)
        ]

``random.random()`` generates r between 0 and 1. With p=0.8, imagine:

    0.0 -------------------------------- 0.8 -------- 1.0
        return 1 across 80% of the line     return 0

Dry-run A:

    r=0.42
    0.42 < 0.80 is True
    return 1

Dry-run B:

    r=0.93
    0.93 < 0.80 is False
    return 0

Because 80% of the line lies below 0.8, repeated draws return roughly 80% ones.
Ten draws do not have to contain exactly eight ones. Probability describes
long-run behavior, not a guaranteed small-sample result.


===============================================================================
11. WHY BERNOULLI MATTERS IN AI
===============================================================================

A. Binary classification

    email -> neural network -> p=0.91 -> P(spam=1 | email)=0.91

Different inputs produce different values of p.

B. Sigmoid output

A binary model often produces a raw score and sigmoid converts it to a number
between 0 and 1. That number becomes Bernoulli parameter p. We do not need to
implement sigmoid here to understand this distribution.

C. Binary cross-entropy

The true label is 0 or 1. Binary cross-entropy measures how well the predicted
Bernoulli distribution explains that true label. Loss has its own lesson.

D. Dropout intuition

For every unit, a binary mask may be sampled during training:

    1 = keep the unit
    0 = drop the unit

That is a Bernoulli-like decision.

E. Data augmentation

"Flip this image or do not flip it" is another binary random decision.


===============================================================================
12. COMMON CONFUSIONS
===============================================================================

1. "p=0.8 means the outcome is 0.8."
   No. The outcome is 0 or 1. The value 0.8 is P(X=1) and the long-run mean.

2. "Success must be good."
   No. Success simply names the event encoded as 1.

3. "Bernoulli models the number of successes in 100 trials."
   No. One trial is Bernoulli; the repeated success count is Binomial-style.

4. "p=0.8 guarantees eight ones in ten trials."
   No. Small samples vary. The fraction approaches p over many trials.

5. "Variance is probability of an error."
   No. Variance measures spread around the mean. In Bernoulli it also gives a
   useful sense of how unpredictable the binary result is.


===============================================================================
13. FINAL MENTAL MODEL
===============================================================================

    ONE yes/no experiment
             |
             v
        X in {0,1}
             |
             v
    p = probability of X=1
    1-p = probability of X=0
             |
             v
    PMF gives probability of exact 0 or 1
             |
             v
    E[X]=p       -> long-run fraction of ones
    Var(X)=p(1-p)-> spread and predictability

One-sentence explanation:

    A Bernoulli distribution models one binary uncertain outcome, assigning
    probability p to X=1 and 1-p to X=0; in AI it represents binary predictions
    such as spam/not-spam, fraud/not-fraud, and click/no-click.
"""

import random


def bernoulli_pmf(k, p):
    """Return P(X=k) for a Bernoulli(p) random variable."""
    if k not in (0, 1):
        raise ValueError("A Bernoulli outcome k must be 0 or 1.")
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be between 0 and 1.")

    # This is the simple roadmap calculation.
    return p if k == 1 else (1 - p)


def bernoulli_expected_value(p):
    """Build E[X] from value * probability instead of only memorizing E[X]=p."""
    probability_of_zero = bernoulli_pmf(0, p)
    probability_of_one = bernoulli_pmf(1, p)

    return 0 * probability_of_zero + 1 * probability_of_one


def bernoulli_variance_from_definition(p):
    """Build variance from probability-weighted squared distances."""
    mean = bernoulli_expected_value(p)

    zero_contribution = bernoulli_pmf(0, p) * (0 - mean) ** 2
    one_contribution = bernoulli_pmf(1, p) * (1 - mean) ** 2

    return zero_contribution + one_contribution


def bernoulli_variance_short_formula(p):
    """Return the simplified Bernoulli variance p(1-p)."""
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be between 0 and 1.")
    return p * (1 - p)


def sample_bernoulli(p, n=1):
    """Draw n samples using the roadmap's random-number-line method."""
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be between 0 and 1.")
    if n < 1:
        raise ValueError("n must be at least 1.")

    return [
        1 if random.random() < p else 0
        for _ in range(n)
    ]


def demonstrate_pmf():
    print("\n" + "=" * 78)
    print("DEMO 1 - PMF")
    print("=" * 78)

    p = 0.8
    print("p =", p)
    print("P(X=1) = bernoulli_pmf(1, 0.8) =", bernoulli_pmf(1, p))
    print("P(X=0) = bernoulli_pmf(0, 0.8) =", round(bernoulli_pmf(0, p), 1))
    print("Total probability =", bernoulli_pmf(0, p) + bernoulli_pmf(1, p))


def demonstrate_expected_value():
    print("\n" + "=" * 78)
    print("DEMO 2 - EXPECTED VALUE")
    print("=" * 78)

    p = 0.8
    p_zero = bernoulli_pmf(0, p)
    p_one = bernoulli_pmf(1, p)
    print("E[X] = 0*P(X=0) + 1*P(X=1)")
    print(f"     = 0*{p_zero:.1f} + 1*{p_one:.1f}")
    print("     =", bernoulli_expected_value(p))
    print("Meaning: across many trials, about 80% are expected to be ones.")


def demonstrate_variance():
    print("\n" + "=" * 78)
    print("DEMO 3 - VARIANCE")
    print("=" * 78)

    p = 0.8
    mean = bernoulli_expected_value(p)
    zero_part = bernoulli_pmf(0, p) * (0 - mean) ** 2
    one_part = bernoulli_pmf(1, p) * (1 - mean) ** 2

    print("mean =", mean)
    print(f"zero contribution = 0.2 * (0 - 0.8)^2 = {zero_part:.3f}")
    print(f"one contribution  = 0.8 * (1 - 0.8)^2 = {one_part:.3f}")
    print(f"variance from definition = {zero_part:.3f} + {one_part:.3f}")
    print("                         =", round(bernoulli_variance_from_definition(p), 3))
    print("short formula p(1-p)     =", round(bernoulli_variance_short_formula(p), 3))

    print("\nHow uncertainty changes:")
    for example_p in (0.01, 0.25, 0.50, 0.75, 0.99):
        variance = bernoulli_variance_short_formula(example_p)
        print(f"p={example_p:>4.2f} -> variance={variance:.4f}")


def demonstrate_sampling():
    print("\n" + "=" * 78)
    print("DEMO 4 - SAMPLING")
    print("=" * 78)

    p = 0.8
    random.seed(6)  # makes the study output repeatable

    ten_samples = sample_bernoulli(p, 10)
    print("Ten samples:", ten_samples)
    print("Number of ones:", sum(ten_samples))
    print("A small sample does not have to contain exactly 80% ones.")

    many_samples = sample_bernoulli(p, 100_000)
    observed_fraction = sum(many_samples) / len(many_samples)
    print("\nAfter 100,000 samples:")
    print(f"Observed fraction of ones = {observed_fraction:.4f}")
    print(f"Theoretical probability p = {p:.4f}")


def demonstrate_ai_example():
    print("\n" + "=" * 78)
    print("DEMO 5 - BINARY AI PREDICTION")
    print("=" * 78)

    predicted_spam_probability = 0.91
    print("Model output p =", predicted_spam_probability)
    print("P(spam=1 | email) =", bernoulli_pmf(1, predicted_spam_probability))
    print("P(spam=0 | email) =", round(bernoulli_pmf(0, predicted_spam_probability), 2))
    print("Probabilities describe uncertainty; the class label remains 0 or 1.")


def practice_questions():
    print("\n" + "=" * 78)
    print("PRACTICE - ANSWER BEFORE READING THE SOLUTIONS")
    print("=" * 78)
    print("""
1. A click model has p=0.30. What are P(X=1) and P(X=0)?
2. For p=0.30, what is E[X], and what does it mean?
3. Which has more Bernoulli variance: p=0.50 or p=0.95? Why?
4. Is "number of spam emails among 100 emails" one Bernoulli variable?
5. If p=0.80, must every ten trials contain exactly eight ones?

Solutions:
1. P(X=1)=0.30 and P(X=0)=0.70.
2. E[X]=0.30. Across many similar trials, about 30% should be ones.
3. p=0.50. Either outcome is equally likely, so unpredictability is greatest.
4. No. Each email can be Bernoulli; the total count is Binomial-style.
5. No. p describes long-run probability, not a guaranteed small-sample count.
""")


def main():
    demonstrate_pmf()
    demonstrate_expected_value()
    demonstrate_variance()
    demonstrate_sampling()
    demonstrate_ai_example()
    practice_questions()


if __name__ == "__main__":
    main()
