"""
DAY 20 — SESSION 13: BETA DISTRIBUTION AND UNCERTAINTY
======================================================

1. WHY A SINGLE ESTIMATE IS NOT ENOUGH
--------------------------------------
Player A scores 6 of 10 shots. Player B scores 600 of 1000. Both MLE estimates
are 0.60, but the evidence is not equally strong. Ten attempts allow substantial
luck; one thousand consistent attempts make values far from 0.60 implausible.
A point estimate reports location but hides confidence.

The Beta distribution represents our uncertainty about an unknown probability:

    theta ~ Beta(alpha, beta),       0 <= theta <= 1

It is useful for coin-head probability, click rate, conversion rate, scoring
ability, treatment success, defect probability, and any Bernoulli outcome.

2. OUTCOME UNCERTAINTY VS PARAMETER UNCERTAINTY
-----------------------------------------------
P(next shot succeeds | theta=0.60)=0.60 describes a future outcome assuming
theta is known. P(theta | data) asks which theta values are believable because
theta itself is unknown. Beta models this second kind of uncertainty.

3. INTUITION FOR ALPHA AND BETA
-------------------------------
alpha carries support associated with success; beta carries support associated
with failure. This count language is exact for Beta-Bernoulli updating but the
parameters are best understood as shape/evidence parameters, not always literal
historical observations.

The mean is:

    E[theta] = alpha/(alpha+beta)

The ratio controls location. The total alpha+beta controls concentration.

    Beta(6,4):       center 0.60, strength 10, wide
    Beta(60,40):     center 0.60, strength 100, narrower
    Beta(600,400):   center 0.60, strength 1000, very narrow

Same ratio gives the same center; more total evidence produces more confidence.

4. HOW BETA CREATES WIDE OR NARROW SHAPES
-----------------------------------------
Could a 40%-ability player score 6 of 10? Yes, luck can do that. Could a true
40%-ability player score 600 of 1000? That is extraordinarily unlikely. With
large evidence, Beta assigns little density to values far from the observed
ratio and concentrates around 0.60.

Variance measures spread:

    Var(theta) = alpha*beta / ((alpha+beta)^2*(alpha+beta+1))

Beta(6,4) variance is about 0.02182 and standard deviation about 0.148.
Beta(600,400) variance is about 0.000240 and standard deviation about 0.0155.
The second uncertainty is roughly ten times smaller in standard-deviation terms.

5. IMPORTANT BETA SHAPES
------------------------
Beta(1,1) is uniform: all theta values initially have equal density.
Beta(2,2) weakly favors values near 0.5.
Beta(100,100) strongly concentrates near 0.5.
Beta(8,2) favors high success probability; Beta(2,8) favors low probability.
If alpha or beta is below one, density may concentrate near a boundary; the
simple "hill around the mean" picture does not cover every possible Beta shape.

6. WHAT BETA DOES AND DOES NOT SAY
----------------------------------
A wide distribution means many theta values remain plausible, not that the data
is wrong. A narrow distribution means confidence under our model assumptions,
not absolute truth. Biased data or a wrong model can produce narrow confidence
around a wrong answer.

CORE MEMORY:

    alpha/(alpha+beta) -> center
    alpha+beta         -> evidence strength/concentration
    full Beta shape    -> uncertainty, not only one estimate
"""

import math


def beta_mean(alpha, beta):
    return alpha / (alpha + beta)


def beta_variance(alpha, beta):
    total = alpha + beta
    return alpha * beta / (total**2 * (total + 1))


if __name__ == "__main__":
    for alpha, beta in [(6, 4), (60, 40), (600, 400)]:
        mean = beta_mean(alpha, beta)
        variance = beta_variance(alpha, beta)
        std = math.sqrt(variance)
        print(
            f"Beta({alpha},{beta}): mean={mean:.3f}, "
            f"strength={alpha+beta}, std={std:.4f}"
        )
    assert beta_variance(600, 400) < beta_variance(6, 4)

