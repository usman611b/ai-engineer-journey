"""
LESSON 6 - EXPECTED VALUE, VARIANCE, AND STANDARD DEVIATION
===========================================================

Core mental model:

    Expected value     -> Where does the random process average out?
    Variance           -> How spread out are values around that center?
    Standard deviation -> Spread expressed in the original units

Run with:

    python 09_expected_value_variance.py


===============================================================================
1. EXPECTED VALUE IS A WEIGHTED AVERAGE
===============================================================================

An ordinary average gives each observation equal weight. Expected value gives
each possible value weight equal to its probability.

For a discrete random variable:

    E[X] = sum of value * probability

Roadmap code:

    def expected_value(values, probabilities):
        return sum(v*p for v,p in zip(values, probabilities))

Read it in words:

    multiply each value by how likely it is, then add the contributions

Expected value is the long-run average across many repetitions. It does not
have to be one of the possible outcomes.


===============================================================================
2. FAIR-DIE HAND CALCULATION
===============================================================================

For a fair die:

    values        = [1, 2, 3, 4, 5, 6]
    probabilities = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

Calculate:

    E[X] = 1*(1/6)+2*(1/6)+3*(1/6)+4*(1/6)+5*(1/6)+6*(1/6)
         = (1+2+3+4+5+6)/6
         = 21/6
         = 3.5

A die cannot roll 3.5. The meaning is that many rolls average toward 3.5.


===============================================================================
3. WHY MEAN ALONE IS NOT ENOUGH
===============================================================================

    A = [5,5,5,5,5]
    B = [1,3,5,7,9]

Both have mean 5. A has no spread; B has large spread. Variance separates them.


===============================================================================
4. VARIANCE STEP BY STEP
===============================================================================

For a discrete distribution:

    Var(X) = sum of probability * (value - mean)^2

Why each operation exists:

    value-mean -> distance from the center
    square      -> negative/positive distances do not cancel
    probability -> likely values count more than unlikely values
    sum         -> combine all contributions into one spread measure

Roadmap:

    def variance(values, probabilities):
        mu = expected_value(values, probabilities)
        return sum(p*(v-mu)**2 for v,p in zip(values,probabilities))


===============================================================================
5. FAIR-DIE VARIANCE BY HAND
===============================================================================

Mean is 3.5. Deviations and squares:

    value   deviation   squared deviation
      1       -2.5            6.25
      2       -1.5            2.25
      3       -0.5            0.25
      4        0.5            0.25
      5        1.5            2.25
      6        2.5            6.25

Every value has probability 1/6:

    Var(X)=(6.25+2.25+0.25+0.25+2.25+6.25)/6
          =17.5/6
          =2.9167 approximately


===============================================================================
6. WHY STANDARD DEVIATION?
===============================================================================

Variance uses squared units. If X is measured in centimeters, variance is in
square centimeters. Standard deviation takes the square root:

    SD(X) = sqrt(Var(X))

For the die:

    SD=sqrt(2.9167)=1.708 approximately

Standard deviation is easier to interpret because it uses X's original units.


===============================================================================
7. A SECOND VARIANCE FORMULA
===============================================================================

Algebra also gives:

    Var(X) = E[X^2] - E[X]^2

Meaning:

    average of squared values minus square of average

It gives the same answer, but the first definition better exposes the intuition
of squared distance from the mean.


===============================================================================
8. TRANSFORMING A RANDOM VARIABLE
===============================================================================

For Y=aX+b:

    E[Y] = aE[X]+b
    Var(Y) = a^2 Var(X)

Adding b shifts every value equally, so spread does not change. Multiplying by a
stretches all distances by a, and squared distances grow by a^2.

If die X has mean 3.5 and variance 2.9167, and Y=2X+10:

    E[Y]=2*3.5+10=17
    Var(Y)=2^2*2.9167=11.6668


===============================================================================
9. AI CONNECTIONS
===============================================================================

Model losses:

    Model A: 0.29,0.31,0.30,0.28,0.32
    Model B: 0.01,0.70,0.05,0.65,0.09

The means may be similar, but B is much less consistent and has higher variance.

Gradient variance:

Different mini-batches produce different gradients. Low variance gives more
consistent updates; high variance makes training noisy. Batch size affects this.

Expected loss means average performance under the data distribution. Variance
adds information about consistency that the average alone hides.


===============================================================================
10. COMMON CONFUSIONS
===============================================================================

1. Expected value need not be a possible outcome.
2. Variance is not average absolute distance; it uses squared distance.
3. Standard deviation is not variance; it is the square root of variance.
4. Same mean does not imply same distribution or spread.
5. Variance is always nonnegative because squared distances are nonnegative.
6. High variance is not always bad; its meaning depends on the task.

Final flow:

    find center -> measure distances -> square -> probability-weight -> add
"""

import math
import random


def validate_distribution(values, probabilities):
    if len(values) == 0 or len(values) != len(probabilities):
        raise ValueError("Values and probabilities must be aligned and nonempty.")
    if any(p < 0 for p in probabilities):
        raise ValueError("Probabilities cannot be negative.")
    if abs(sum(probabilities)-1) > 1e-9:
        raise ValueError("Probabilities must add to 1.")


def expected_value(values, probabilities):
    validate_distribution(values, probabilities)
    return sum(v*p for v,p in zip(values,probabilities))


def variance(values, probabilities):
    validate_distribution(values, probabilities)
    mu=expected_value(values,probabilities)
    return sum(p*(v-mu)**2 for v,p in zip(values,probabilities))


def standard_deviation(values, probabilities):
    return math.sqrt(variance(values,probabilities))


def variance_second_formula(values, probabilities):
    mean=expected_value(values,probabilities)
    expected_square=sum((v**2)*p for v,p in zip(values,probabilities))
    return expected_square-mean**2


def demonstrate_die_mean():
    print("\n"+"="*78)
    print("DEMO 1 - FAIR-DIE EXPECTED VALUE")
    print("="*78)
    values=list(range(1,7)); probabilities=[1/6]*6
    contributions=[v*p for v,p in zip(values,probabilities)]
    for v,p,c in zip(values,probabilities,contributions):
        print(f"{v} * {p:.4f} = {c:.4f}")
    print("Add contributions -> E[X] =",expected_value(values,probabilities))


def demonstrate_die_variance():
    print("\n"+"="*78)
    print("DEMO 2 - FAIR-DIE VARIANCE")
    print("="*78)
    values=list(range(1,7)); probabilities=[1/6]*6
    mu=expected_value(values,probabilities)
    for v,p in zip(values,probabilities):
        print(f"v={v}: deviation={v-mu:>4.1f}, square={(v-mu)**2:.2f}, weighted={p*(v-mu)**2:.4f}")
    print(f"Variance={variance(values,probabilities):.4f}")
    print(f"Standard deviation={standard_deviation(values,probabilities):.4f}")
    print(f"Second formula check={variance_second_formula(values,probabilities):.4f}")


def demonstrate_simulation():
    print("\n"+"="*78)
    print("DEMO 3 - LONG-RUN AVERAGE")
    print("="*78)
    random.seed(9)
    for n in (10,100,100_000):
        rolls=[random.randint(1,6) for _ in range(n)]
        mean=sum(rolls)/n
        var=sum((x-mean)**2 for x in rolls)/n
        print(f"n={n:>7}: observed mean={mean:.4f}, variance={var:.4f}")
    print("Theory: mean=3.5, variance=2.9167")


def demonstrate_transformation():
    print("\n"+"="*78)
    print("DEMO 4 - Y=2X+10")
    print("="*78)
    x=list(range(1,7)); probs=[1/6]*6
    y=[2*v+10 for v in x]
    print("X values:",x,"Y values:",y)
    print("E[Y] actual=",expected_value(y,probs),"predicted=",2*expected_value(x,probs)+10)
    print("Var[Y] actual=",variance(y,probs),"predicted=",4*variance(x,probs))


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. Can E[die]=3.5 even though a die cannot show 3.5?
2. Why do we square deviations in variance?
3. What extra information does variance give beyond mean?
4. If Var(X)=9, what is SD(X)?
5. If Y=3X+5, how do mean and variance transform?

Solutions:
1. Yes. Expected value is the long-run probability-weighted average.
2. To prevent sign cancellation and measure magnitude of spread.
3. It measures how widely values move around the center.
4. SD=sqrt(9)=3.
5. E[Y]=3E[X]+5 and Var(Y)=9Var(X).
""")


def main():
    demonstrate_die_mean()
    demonstrate_die_variance()
    demonstrate_simulation()
    demonstrate_transformation()
    practice_questions()


if __name__=="__main__":
    main()
