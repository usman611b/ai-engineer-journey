"""
LESSON 6 - NORMAL / GAUSSIAN DISTRIBUTION
==========================================

Core intuition:

    Values near the average are common; values far from the average become
    increasingly rare.

Run with:

    python 08_normal_gaussian_distribution.py


===============================================================================
1. THE BELL CURVE
===============================================================================-

Many measurements cluster around a center. Human heights, repeated measurement
errors, and aggregated noise often behave approximately like:

                      /\
                    /    \
                  /        \
    ______________/          \______________
                         mu

The curve is symmetric. The center has the greatest density, and density falls
as we move farther away in either direction.

Normal and Gaussian are two names for the same distribution.


===============================================================================
2. MEAN mu CONTROLS LOCATION
===============================================================================

The Greek letter mu is the mean:

    mu = center of the bell

Changing mu moves the entire curve without changing its shape:

    mu=0  -> centered at 0
    mu=10 -> centered at 10

Question answered by mu: Where is the distribution centered?


===============================================================================
3. STANDARD DEVIATION sigma CONTROLS SPREAD
===============================================================================

Sigma is standard deviation:

    small sigma -> values tightly concentrated near mu; narrow/tall bell
    large sigma -> values spread farther from mu; wide/short bell

Question answered by sigma: How spread out are values around the center?

Variance is sigma squared:

    Var(X) = sigma^2

Why does a wider bell become shorter? Every PDF must keep total area equal to 1.
Spreading the same probability over more width requires a lower height.


===============================================================================
4. PDF HEIGHT VERSUS PROBABILITY
===============================================================================

Gaussian is continuous. Therefore:

    f(0) may be about 0.3989

does not mean:

    P(X=0)=0.3989

At one exact point, probability is zero. Probability is area across a range:

    P(a <= X <= b) = integral from a to b of f(x) dx

The PDF tells us where probability is concentrated. The integral collects the
density across an interval and produces actual probability.


===============================================================================
5. THE FORMULA, EXPLAINED RATHER THAN MEMORIZED
===============================================================================

    f(x) = [1/(sigma*sqrt(2*pi))]
           * exp(-0.5 * ((x-mu)/sigma)^2)

Read the important middle part:

    x-mu            -> distance from the center
    (x-mu)/sigma    -> distance measured in standard deviations (z-score)
    square it       -> left and right distances behave equally
    multiply -0.5   -> make farther distances negative
    exponentiate    -> density falls rapidly with distance

The coefficient 1/(sigma*sqrt(2*pi)) gives the correct height so total area is 1.

The formula implements:

    close to mu -> high density
    far from mu -> low density


===============================================================================
6. HAND DRY-RUN FOR THE STANDARD NORMAL
===============================================================================

Standard Normal means:

    mu=0, sigma=1

At x=0:

    z=(0-0)/1=0
    exponent=-0.5*0^2=0
    e^0=1
    coefficient=1/sqrt(2*pi)=0.3989
    density=0.3989

At x=1:

    z=(1-0)/1=1
    exponent=-0.5*1^2=-0.5
    density=0.3989*e^-0.5, approximately 0.2420

At x=5:

    z=5
    exponent=-0.5*25=-12.5
    e^-12.5 is tiny, so density is extremely small.


===============================================================================
7. Z-SCORES
===============================================================================

    z = (x-mu)/sigma

z tells how many standard deviations x lies from the mean.

Example: test scores have mu=100, sigma=15, and x=130:

    z=(130-100)/15=30/15=2

The score is two standard deviations above the mean. Standardization lets us
compare positions across distributions with different units and scales.


===============================================================================
8. THE 68-95-99.7 RULE
===============================================================================

For a normal distribution, approximately:

    mu +/- 1 sigma contains 68%
    mu +/- 2 sigma contains 95%
    mu +/- 3 sigma contains 99.7%

Example: heights approximately Normal(mu=170 cm, sigma=5 cm):

    about 68% lie from 165 to 175 cm
    about 95% lie from 160 to 180 cm
    about 99.7% lie from 155 to 185 cm

The intuition matters more than memorizing decimals: most values lie near the
center, and extremely distant values are rare.


===============================================================================
9. WHY GAUSSIANS APPEAR OFTEN
===============================================================================

A quantity may be affected by many small influences:

    genetics, nutrition, sleep, environment, measurement noise, ...

Some push upward and others downward. When many small independent effects add,
the final value often clusters near an average. This connects to the Central
Limit Theorem, which receives its own detailed lesson.

Not every bell-looking dataset is exactly Gaussian, and real data may be skewed,
heavy-tailed, multimodal, or bounded. Always treat Normal as a model assumption.


===============================================================================
10. AI CONNECTIONS
===============================================================================

Noise:

    noise sampled from Normal(0,1)

Most changes are near zero; very large changes are rare.

Weight initialization:

    weights may be sampled near zero from a carefully scaled Normal distribution

Modern initialization selects variance based on layer size; it is not enough to
choose any Gaussian blindly.

Diffusion models:

    image -> add Gaussian noise repeatedly -> nearly pure noise
    learned reverse process -> remove noise repeatedly -> generated image

Gaussian assumptions also appear in uncertainty models and measurement errors.


===============================================================================
11. GAUSSIAN VERSUS UNIFORM
===============================================================================

Uniform:

    flat density; no preferred location inside [a,b]

Gaussian:

    highest density near mu; smoothly decreasing density farther away; unbounded

Both are continuous PDFs, but they make very different assumptions.


===============================================================================
12. COMMON CONFUSIONS
===============================================================================

1. PDF height is not exact-point probability.
2. sigma is standard deviation; variance is sigma^2.
3. Larger sigma spreads the same total area and lowers the peak.
4. Normal distributions are symmetric; not all real data are Normal.
5. A z-score is a relative distance, not a probability.
6. The 68-95-99.7 rule applies specifically to Normal distributions.

Mental model: mu chooses the center; sigma chooses the width; distance from mu
determines how quickly density falls.
"""

import math
import random


def normal_pdf(x, mu, sigma):
    """Return Gaussian density at x using the Lesson 6 roadmap formula."""
    if sigma <= 0:
        raise ValueError("sigma must be positive.")
    coeff = 1.0 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coeff * math.exp(exponent)


def z_score(x, mu, sigma):
    if sigma <= 0:
        raise ValueError("sigma must be positive.")
    return (x-mu)/sigma


def normal_cdf(x, mu, sigma):
    """Return area to the left using Python's error function."""
    return 0.5 * (1 + math.erf((x-mu)/(sigma*math.sqrt(2))))


def interval_probability(left, right, mu, sigma):
    return normal_cdf(right,mu,sigma)-normal_cdf(left,mu,sigma)


def demonstrate_formula():
    print("\n" + "=" * 78)
    print("DEMO 1 - STANDARD NORMAL PDF")
    print("=" * 78)
    for x in (0,1,2,3,5):
        print(f"x={x}: z={z_score(x,0,1):.1f}, density={normal_pdf(x,0,1):.6f}")


def demonstrate_z_score():
    print("\n" + "=" * 78)
    print("DEMO 2 - Z-SCORE")
    print("=" * 78)
    print("mu=100, sigma=15, x=130")
    print("z=(130-100)/15 =", z_score(130,100,15))
    print("Interpretation: two standard deviations above the mean.")


def demonstrate_68_95_997():
    print("\n" + "=" * 78)
    print("DEMO 3 - AREA AROUND THE MEAN")
    print("=" * 78)
    for n in (1,2,3):
        area=interval_probability(-n,n,0,1)
        print(f"Within +/-{n} sigma: {area:.3%}")


def demonstrate_sampling():
    print("\n" + "=" * 78)
    print("DEMO 4 - SAMPLED VALUES CLUSTER NEAR mu")
    print("=" * 78)
    random.seed(8)
    samples=[random.gauss(10,2) for _ in range(100_000)]
    mean=sum(samples)/len(samples)
    variance=sum((x-mean)**2 for x in samples)/len(samples)
    print("First five samples:",[round(x,3) for x in samples[:5]])
    print(f"Observed mean={mean:.3f}; expected mu=10")
    print(f"Observed SD={math.sqrt(variance):.3f}; expected sigma=2")


def practice_questions():
    print("\n" + "=" * 78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("=" * 78)
    print("""
1. What do mu and sigma control?
2. If variance is 25, what is sigma?
3. Does normal_pdf(0,0,1)=0.3989 mean P(X=0)=39.89%?
4. For mu=50, sigma=5, what is the z-score of x=60?
5. About what percent lies within two sigma of the mean?

Solutions:
1. mu controls center; sigma controls spread.
2. sigma=sqrt(25)=5.
3. No. It is density; exact-point probability is zero.
4. z=(60-50)/5=2.
5. Approximately 95% for a Normal distribution.
""")


def main():
    demonstrate_formula()
    demonstrate_z_score()
    demonstrate_68_95_997()
    demonstrate_sampling()
    practice_questions()


if __name__ == "__main__":
    main()
