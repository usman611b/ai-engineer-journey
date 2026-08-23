"""
DAY 20 — SESSION 12: MAXIMUM A POSTERIORI ESTIMATION (MAP)
==========================================================

This lesson builds MAP naturally from MLE's weakness.

1. WHY MAP IS NEEDED
--------------------
MLE chooses the parameter that best fits observed data, but tiny datasets can
produce unrealistic certainty.

A new basketball player takes one shot and scores. MLE uses only that data:

    scoring_probability_MLE = 1 success / 1 attempt = 1.0

It estimates 100% ability. This perfectly fits the one observation, but one
shot is weak evidence and does not prove the player never misses.

MAP combines:

    what seemed reasonable before the data (prior)
                      +
    how well parameters explain the data (likelihood)
                      ->
    what is reasonable after the data (posterior)

It then chooses the single parameter value at the posterior's highest point.


2. SIMPLE DEFINITION
--------------------
MAP means Maximum A Posteriori:

    theta_MAP = argmax_theta P(theta | data)

It asks:

    "After combining prior knowledge with observations, which parameter value
     is now the most believable?"

Bayes gives:

    P(theta | data) = P(data | theta)P(theta) / P(data)

* P(theta): prior over parameter values
* P(data|theta): likelihood
* P(theta|data): posterior
* P(data): normalizing evidence

When comparing theta values, P(data) is constant because data is fixed:

    theta_MAP = argmax_theta [P(data|theta)P(theta)]

So MAP seeks a parameter that explains the data well AND was reasonably
plausible beforehand.


3. BASKETBALL INTUITION
-----------------------
Represent weak previous knowledge as count-like evidence:

    5 prior successful shots, 5 prior missed shots

The initial center is 5/(5+5)=0.5. Now the player scores one real shot:

    successes = 5+1 = 6
    failures  = 5+0 = 5
    total     = 11

A posterior-mean-style estimate becomes:

    6/11 = about 0.545

Our belief rises from 50% to 54.5%. Bayesian reasoning does not ignore the
successful shot. It says one success should increase belief, but should not
create certainty.

PRECISION: this count ratio is the posterior mean for a corresponding Beta
model. It provides excellent intuition, but is not always the exact MAP mode.
The exact formulas appear later.


4. COIN EXAMPLE: TWO REASONING STYLES
-------------------------------------
An unknown coin is tossed once and produces heads.

MLE:

    "1 head in 1 toss means theta=1 best fits observed data."

MAP:

    "Ordinary coins are not normally guaranteed-head coins. The head moves my
     estimate upward, but one observation cannot justify theta=1."

MAP balances two forces:

* likelihood pulls toward the observed frequency;
* prior pulls toward previously plausible parameter values.

Their relative influence depends on data amount and prior strength.


5. WHAT A PRIOR REALLY IS
-------------------------
A prior is a distribution over parameter values before the current dataset.
For a coin it may say values near 0.5 are initially more plausible than 0 or 1.

A prior can come from:

* earlier experiments or historical datasets;
* scientific/domain knowledge;
* related tasks or populations;
* a weak mathematical preference preventing extreme estimates.

It is not automatically correct. A bad or excessively strong prior can bias
results, so important applications should state priors clearly and check how
conclusions change under reasonable alternative priors.


6. PRIOR STRENGTH: COUNT INTUITION
----------------------------------
Balanced count-like evidence visualizes prior strength:

* 1 success + 1 failure: weak belief around 0.5
* 5 successes + 5 failures: stronger belief around 0.5
* 100 successes + 100 failures: very strong belief around 0.5

After one real success:

    weak:     (1+1)/(1+1+1) = 2/3 = 0.667
    stronger: (5+1)/(5+5+1) = 6/11 = 0.545

The stronger prior moves less because one sample is small compared with its
previous/prior evidence. These are an intuition for Beta prior strength, not a
rule that every MAP model literally inserts fake observations.


7. SMALL DATA VERSUS LARGE DATA
-------------------------------
With one head:

    MLE = 1.0
    MAP with a balanced prior = below 1.0

With 800 heads and 200 tails:

    MLE = 800/1000 = 0.8

A modest fair-coin prior only pulls slightly toward 0.5. One thousand real
observations overwhelm a few units of prior evidence.

    little data    -> prior has visible influence
    abundant data -> likelihood/data dominates

MAP does not stubbornly ignore evidence. Strong evidence gradually overrules a
reasonable fixed prior.


8. BETA PRIOR: PRECISE COIN MODEL
---------------------------------
The Beta distribution represents uncertainty about a probability theta:

    theta ~ Beta(alpha, beta), where 0 <= theta <= 1

Intuitively:

* alpha carries support associated with successes;
* beta carries support associated with failures;
* their relative sizes control the center;
* alpha+beta controls concentration/strength.

After H successes and T failures:

    prior:     Beta(alpha, beta)
    posterior: Beta(alpha+H, beta+T)

The posterior stays in the Beta family; this is conjugate updating.


9. MLE, POSTERIOR MEAN, AND MAP DIFFER
--------------------------------------
Suppose prior=Beta(2,2), then observe 7 heads and 3 tails:

    posterior = Beta(2+7, 2+3) = Beta(9,5)

MLE uses only observations:

    MLE = 7/10 = 0.700

Posterior mean averages theta under the posterior:

    mean = 9/(9+5) = 9/14 = about 0.643

MAP selects the posterior peak. When both posterior parameters exceed 1:

    MAP = (alpha_posterior-1) /
          (alpha_posterior+beta_posterior-2)

For Beta(9,5):

    MAP = (9-1)/(9+5-2) = 8/12 = about 0.667

Comparison:

    MLE            = 0.700: data-only best fit
    MAP            = 0.667: most probable posterior point
    posterior mean = 0.643: average posterior value

They are related but answer different questions.


10. WHY DID EARLIER EXAMPLES ADD 2 AND 4?
------------------------------------------
With intuitive prior counts of 2 heads and 2 tails plus 800 real heads and 200
real tails:

    heads = 800+2 = 802
    tails = 200+2 = 202
    total = 1000+2+2 = 1004

We add 2 to the numerator because it counts heads only. We add 4 to the
denominator because it counts both prior heads and prior tails.

The number 2 was only an example of strength. We could use 1 and 1 for a weaker
prior or 100 and 100 for a stronger prior. MAP does not universally add 2.
Also, the direct combined-count ratio is a Beta posterior mean; exact Beta MAP
uses the minus-one mode formula above.


11. MAP IN MACHINE LEARNING
---------------------------
MAP is useful when data is limited, meaningful earlier knowledge exists, or we
want to prevent extreme/implausible parameters.

Spam example: if a word appears zero times in three spam emails, MLE gives zero
probability. A prior or smoothing assumption preserves a small nonzero chance
because absence from tiny data does not prove impossibility.


12. MAP AND REGULARIZATION
--------------------------
Large weights may fit noise. MAP can use a prior saying small weights are more
plausible. Starting from maximizing likelihood*prior, negative logs give:

    minimize negative_log_likelihood + negative_log_prior

The first term fits data. The second discourages parameters conflicting with
the prior.

* Gaussian prior centered at zero -> L2 regularization
* Laplace prior centered at zero  -> L1 regularization

Thus regularization has a Bayesian/MAP interpretation, not merely an arbitrary
penalty.


13. RELATIONSHIP BETWEEN MLE AND MAP
------------------------------------

    MLE = argmax P(data|theta)
    MAP = argmax P(data|theta)P(theta)

If the prior is uniform, every candidate gets the same multiplier, so MAP and
MLE have the same winner. They also become similar with huge datasets because
likelihood dominates a fixed prior.


14. COMMON MISUNDERSTANDINGS
----------------------------
"MAP ignores data." False: it uses the entire likelihood plus a prior.

"The prior is always correct." False: poor priors can bias results.

"MAP always adds one or two." False: those are special count examples.

"MAP gives all uncertainty." False: full Bayesian inference retains the whole
posterior; MAP compresses it into one peak value.

"MAP is always better." False: it helps only when its prior is appropriate.


15. FINAL MENTAL MODEL
----------------------
MLE asks:

    "Which parameter best explains observed data alone?"

MAP asks:

    "Which parameter is most believable after combining prior knowledge with
     how well it explains observed data?"

One scored shot:

    MLE -> 100%, because that best fits the only observation
    MAP -> raises the estimate, but prevents unjustified certainty

The prior matters most with little data. Evidence dominates as data grows.
"""

import math


def coin_mle(successes, failures):
    """Data-only Bernoulli estimate."""
    total = successes+failures
    if total == 0:
        raise ValueError("MLE requires observations")
    return successes/total


def beta_posterior(alpha, beta, successes, failures):
    """Update Beta prior with success/failure observations."""
    if alpha <= 0 or beta <= 0:
        raise ValueError("Beta parameters must be positive")
    return alpha+successes, beta+failures


def beta_posterior_mean(alpha, beta):
    return alpha/(alpha+beta)


def beta_map(alpha, beta):
    """Interior Beta mode; requires both parameters greater than one."""
    if alpha <= 1 or beta <= 1:
        raise ValueError("Interior MAP formula requires alpha,beta > 1")
    return (alpha-1)/(alpha+beta-2)


if __name__ == "__main__":
    print("="*70)
    print("DEMO 1: One successful basketball shot")
    print("="*70)
    one_mle = coin_mle(1, 0)
    a1, b1 = beta_posterior(5, 5, 1, 0)
    print(f"MLE (data only):       {one_mle:.3f}")
    print(f"Posterior:             Beta({a1}, {b1})")
    print(f"Posterior mean:        {beta_posterior_mean(a1,b1):.3f}")
    print(f"MAP (posterior mode):  {beta_map(a1,b1):.3f}")

    print("\n"+"="*70)
    print("DEMO 2: Beta(2,2) prior, 7 heads and 3 tails")
    print("="*70)
    a2, b2 = beta_posterior(2, 2, 7, 3)
    mle = coin_mle(7, 3)
    mean = beta_posterior_mean(a2, b2)
    map_estimate = beta_map(a2, b2)
    print(f"Posterior:       Beta({a2}, {b2})")
    print(f"MLE:             {mle:.3f}")
    print(f"MAP:             {map_estimate:.3f}")
    print(f"Posterior mean:  {mean:.3f}")

    print("\n"+"="*70)
    print("DEMO 3: Abundant data makes MLE and MAP similar")
    print("="*70)
    a3, b3 = beta_posterior(2, 2, 800, 200)
    large_mle = coin_mle(800, 200)
    large_map = beta_map(a3, b3)
    print(f"MLE:                 {large_mle:.6f}")
    print(f"MAP:                 {large_map:.6f}")
    print(f"Absolute difference: {abs(large_mle-large_map):.6f}")

    assert math.isclose(mle, 0.7)
    assert math.isclose(map_estimate, 8/12)
    assert abs(large_mle-large_map) < 0.001
