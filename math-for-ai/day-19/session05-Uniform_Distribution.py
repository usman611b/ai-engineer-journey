"""
LESSON 6 - UNIFORM DISTRIBUTION
===============================

Core idea:

    Uniform means there is no preferred outcome or location inside the allowed
    set/range.

Run this file with:

    python 07_uniform_distribution.py


===============================================================================
1. DISCRETE UNIFORM
===============================================================================

A fair die has outcomes {1,2,3,4,5,6}. Every exact outcome is equally likely:

    P(X=k) = 1/6

This is discrete, so it uses a PMF. Four equally likely choices would each have
probability 1/4. In general, n equally likely discrete outcomes each get 1/n.


===============================================================================
2. CONTINUOUS UNIFORM
===============================================================================

Now pick a real number between a and b. There are infinitely many possible
values, so we use a PDF (probability density function).

The density is flat:

    f(x) = 1/(b-a), when a <= x <= b
    f(x) = 0,       outside the interval

For Uniform(0,10):

    density = 1/(10-0) = 0.1

Picture:

    density
      0.1 |------------------------------
          |                              |
        0 +------------------------------
          0                             10

Every equally wide region has equal probability.


===============================================================================
3. WHY IS THE HEIGHT 1/(b-a)?
===============================================================================

A valid PDF must have total area 1. The uniform PDF is a rectangle:

    width  = b-a
    height = f(x)
    area   = width*height

Require area=1:

    (b-a)*f(x) = 1
    f(x) = 1/(b-a)

The formula is simply the rectangle height that makes total probability 100%.


===============================================================================
4. PDF HEIGHT IS NOT POINT PROBABILITY
===============================================================================

For Uniform(0,10):

    f(3) = 0.1

This does NOT mean P(X=3)=0.1. For a continuous variable:

    P(X=3) = 0

Probability needs width. It is area under the PDF over an interval:

    probability = density * interval width

As interval width shrinks to zero, probability also shrinks to zero.


===============================================================================
5. HAND CALCULATION WITH AN INTEGRAL
===============================================================================

Let X be Uniform(0,10). Find P(2 <= X <= 5).

Density is 0.1. The desired interval has width:

    5-2 = 3

Area:

    P(2 <= X <= 5) = integral from 2 to 5 of 0.1 dx
                    = width*height
                    = 3*0.1
                    = 0.3

So the probability is 30%.

Equivalent shortcut for a uniform distribution:

    probability = desired interval length / total interval length
                = (5-2)/(10-0)
                = 3/10
                = 0.3

A wider interval contains more probability because density is equal everywhere.


===============================================================================
6. MEAN AND VARIANCE INTUITION
===============================================================================

For continuous Uniform(a,b):

    mean = (a+b)/2

This is the midpoint, which makes sense because the distribution is symmetric.

    variance = (b-a)^2/12

The width b-a controls spread. Moving the whole interval without changing its
width changes the mean but not the variance.

For Uniform(0,10):

    mean = (0+10)/2 = 5
    variance = (10-0)^2/12 = 100/12 = 8.333...


===============================================================================
7. AI CONNECTIONS
===============================================================================

Random initialization:

    weight sampled uniformly from [-0.1, 0.1]

Every location in that range has equal density. Random initialization helps
break symmetry between neurons. Modern Xavier/He methods carefully choose the
scale, but may still use a uniform distribution.

Data augmentation:

    angle sampled from Uniform(-10 degrees, +10 degrees)

There is no preferred angle inside the allowed range. Crop positions,
brightness amounts, and other augmentation settings can use the same idea.

Uniform(0,1) also acts as the starting random-number line for sampling from
Bernoulli and Categorical distributions.


===============================================================================
8. ROADMAP CODE AND DRY-RUN
===============================================================================

Roadmap:

    def uniform_pdf(x, a, b):
        if a <= x <= b:
            return 1.0/(b-a)
        return 0.0

For uniform_pdf(3,0,10):

    Is 0 <= 3 <= 10? yes
    return 1/(10-0)
    return 0.1

For uniform_pdf(15,0,10):

    Is 0 <= 15 <= 10? no
    return 0.0


===============================================================================
9. COMMON CONFUSIONS
===============================================================================

1. Discrete uniform gives mass to exact outcomes; continuous uniform gives
   density and interval areas.
2. f(3)=0.1 does not mean P(X=3)=0.1 for a continuous variable.
3. Uniform does not mean "random with no rules"; it is a specific equal-density
   assumption over a defined range.
4. Outside [a,b], density is zero.
5. The endpoints do not change continuous interval probability because single
   points have probability zero.

Mental model: a perfectly flat layer of probability sand between two walls.
"""

import random


def uniform_pdf(x, a, b):
    """Return the continuous Uniform(a,b) density at x."""
    if a >= b:
        raise ValueError("a must be smaller than b.")
    if a <= x <= b:
        return 1.0 / (b - a)
    return 0.0


def uniform_interval_probability(left, right, a, b):
    """Calculate interval area using overlap width * uniform height."""
    if a >= b or left > right:
        raise ValueError("Use ordered valid intervals.")
    overlap_left = max(left, a)
    overlap_right = min(right, b)
    overlap_width = max(0.0, overlap_right - overlap_left)
    return overlap_width * (1.0 / (b - a))


def demonstrate_pdf():
    print("\n" + "=" * 78)
    print("DEMO 1 - ROADMAP PDF")
    print("=" * 78)
    for x in (-1, 0, 3, 10, 15):
        print(f"uniform_pdf({x}, 0, 10) = {uniform_pdf(x, 0, 10)}")


def demonstrate_area():
    print("\n" + "=" * 78)
    print("DEMO 2 - PROBABILITY IS AREA")
    print("=" * 78)
    a, b, left, right = 0, 10, 2, 5
    density = uniform_pdf(3, a, b)
    width = right-left
    print(f"density = 1/({b}-{a}) = {density}")
    print(f"desired width = {right}-{left} = {width}")
    print(f"area = {width}*{density} = {uniform_interval_probability(left,right,a,b)}")


def demonstrate_sampling():
    print("\n" + "=" * 78)
    print("DEMO 3 - SAMPLES HAVE NO PREFERRED LOCATION")
    print("=" * 78)
    random.seed(7)
    samples = [random.uniform(0, 10) for _ in range(100_000)]
    observed_mean = sum(samples)/len(samples)
    print("First five samples:", [round(x,3) for x in samples[:5]])
    print(f"Observed mean={observed_mean:.3f}; theoretical midpoint=5.000")
    print("Fraction in [2,5]:", round(sum(2 <= x <= 5 for x in samples)/len(samples),3))
    print("Theoretical P([2,5])=0.300")


def practice_questions():
    print("\n" + "=" * 78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("=" * 78)
    print("""
1. What is the density of Uniform(2,6)?
2. For Uniform(0,10), what is P(4<=X<=8)?
3. Does f(3)=0.1 mean P(X=3)=0.1?
4. Why does a wider uniform distribution have a lower PDF height?
5. Give one AI use of a uniform distribution.

Solutions:
1. 1/(6-2)=0.25.
2. Desired width 4 / total width 10 = 0.4.
3. No. Exact-point probability is zero; 0.1 is density.
4. Total area must stay 1, so increasing width requires decreasing height.
5. Random initialization or uniformly sampled augmentation settings.....
""")


def main():
    demonstrate_pdf()
    demonstrate_area()
    demonstrate_sampling()
    practice_questions()


if __name__ == "__main__":
    main()
