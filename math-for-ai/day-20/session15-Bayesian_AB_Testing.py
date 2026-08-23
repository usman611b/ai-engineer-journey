"""
DAY 20 — SESSION 15: BAYESIAN A/B TESTING
=========================================

1. THE DECISION PROBLEM
-----------------------
A/B testing compares two versions: webpage designs, button labels, recommenders,
email subjects, or model variants. Each visitor sees one version. A conversion
is success and no conversion is failure.

Let theta_A and theta_B be unknown true conversion probabilities. We want more
than observed percentages; we want uncertainty-aware questions such as:

    P(theta_B > theta_A | data)

This means our posterior probability that B's underlying rate exceeds A's.

2. WORKED EXAMPLE
-----------------
A receives 20 clicks and 80 non-clicks. B receives 30 clicks and 70 non-clicks.
MLE rates are 20% and 30%, but random variation remains possible.

With equal Beta(1,1) priors:

    theta_A | data ~ Beta(21,81)
    theta_B | data ~ Beta(31,71)

Posterior means are 21/102=20.6% and 31/102=30.4%. B looks better, but comparing
means alone does not measure uncertainty in the difference.

3. WHY SAMPLE SIZE MATTERS
--------------------------
2/10 versus 3/10 and 2000/10000 versus 3000/10000 both show 20% versus 30%.
The small experiment has wide distributions with considerable overlap. The
large experiment has narrow distributions and much less overlap.

    difference in observed rates != confidence in the difference

4. MONTE CARLO COMPARISON
-------------------------
Repeatedly sample one plausible theta_A from A's posterior and one theta_B from
B's posterior. Count how often theta_B>theta_A. If B wins 93,000 of 100,000
simulated worlds, estimate P(theta_B>theta_A)=93%.

This 93% is NOT B's conversion rate. B's rate might be near 30%; 93% describes
confidence that B's underlying rate is larger than A's.

5. PRACTICAL SIGNIFICANCE
-------------------------
"B is probably better" is not the entire decision. Also ask:

* How large is the expected lift theta_B-theta_A?
* What is P(theta_B-theta_A > a worthwhile threshold)?
* What is the expected cost of choosing the wrong version?
* Does the benefit justify deployment cost or risk?

A 0.1% lift may be valuable at enormous scale and irrelevant on a tiny site.

6. VALIDITY WARNINGS
--------------------
Randomly assign comparable users; do not route strong users mainly to B. Avoid
changing the experiment midway in ways the model ignores. Account for season,
novelty, repeated users, bots, and changing traffic. A confident posterior from
biased experimental design is confidently wrong.

CORE MEMORY:

    update a Beta posterior for each variant
    compare full distributions, not only averages
    interpret P(B>A) as confidence in superiority, not B's conversion rate
"""


def update_variant(prior_alpha, prior_beta, conversions, non_conversions):
    return prior_alpha + conversions, prior_beta + non_conversions


if __name__ == "__main__":
    a = update_variant(1, 1, 20, 80)
    b = update_variant(1, 1, 30, 70)
    mean_a = a[0] / sum(a)
    mean_b = b[0] / sum(b)
    print(f"A posterior Beta{a}, mean={mean_a:.3%}")
    print(f"B posterior Beta{b}, mean={mean_b:.3%}")

