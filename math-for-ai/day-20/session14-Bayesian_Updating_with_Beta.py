"""
DAY 20 — SESSION 14: BAYESIAN UPDATING WITH BETA
================================================

1. THE UPDATE RULE
------------------
Start with theta~Beta(alpha,beta). Observe S successes and F failures. The
posterior is:

    Beta(alpha+S, beta+F)

New successes add to alpha; new failures add to beta. This simple rule works
because Beta is conjugate to Bernoulli/binomial likelihoods: prior and posterior
remain in the same family.

2. BASKETBALL EXAMPLE
---------------------
Prior Beta(2,2) weakly favors an ability near 0.5. A player then scores 7 of 10:

    posterior = Beta(2+7, 2+3) = Beta(9,5)

Prior mean:

    2/(2+2) = 0.500

Posterior mean:

    9/(9+5) = 0.643

The center moved upward because successes exceeded failures. Strength grew from
4 to 14, so the distribution also narrowed. Bayesian learning changes both the
estimated location and our certainty.

3. SEQUENTIAL UPDATING
----------------------
Later the same player gets 4 successes and 1 failure. Today's posterior becomes
tomorrow's prior:

    Beta(9,5) -> Beta(9+4,5+1) = Beta(13,6)

New mean:

    13/19 = 0.684

This is the heart of online Bayesian learning: posterior after old evidence is
the prior before new evidence.

4. BATCH ORDER DOES NOT MATTER
------------------------------
Batch 1 has 7S,3F and batch 2 has 4S,1F. Combined data is 11S,4F:

    Beta(2+11,2+4) = Beta(13,6)

This matches sequential updating. Addition is commutative, so the same evidence
produces the same posterior whether processed together or in batches, provided
the model and independence assumptions remain valid.

5. PRIOR INFLUENCE AND DATA INFLUENCE
-------------------------------------
A strong prior changes slowly; a weak prior changes quickly. As observations
accumulate, a fixed prior becomes small relative to the likelihood. This is why
Bayesian estimates increasingly reflect data rather than prior preference.

6. AI APPLICATIONS
------------------
Beta updating can summarize accumulating clicks, recommendations, purchases,
defects, treatment outcomes, model-feedback approvals, and binary sensor events.
Only alpha and beta need to be retained rather than the whole event history.

7. ASSUMPTIONS AND WARNINGS
---------------------------
The events should represent the same underlying probability. If the website,
population, or environment changes, old and new data may not share one theta.
Observations should also be handled with an appropriate independence model.
More evidence increases confidence under assumptions; it cannot rescue biased
measurement or concept drift.

CORE MEMORY:

    prior Beta(alpha,beta)
      + S successes and F failures
      = posterior Beta(alpha+S,beta+F)
"""


def update_beta(alpha, beta, successes, failures):
    if min(alpha, beta) <= 0:
        raise ValueError("Beta parameters must be positive")
    if min(successes, failures) < 0:
        raise ValueError("Counts cannot be negative")
    return alpha + successes, beta + failures


def beta_mean(alpha, beta):
    return alpha / (alpha + beta)


if __name__ == "__main__":
    alpha, beta = 2, 2
    print(f"Prior Beta({alpha},{beta}), mean={beta_mean(alpha,beta):.3f}")
    alpha, beta = update_beta(alpha, beta, 7, 3)
    print(f"Batch 1 Beta({alpha},{beta}), mean={beta_mean(alpha,beta):.3f}")
    alpha, beta = update_beta(alpha, beta, 4, 1)
    print(f"Batch 2 Beta({alpha},{beta}), mean={beta_mean(alpha,beta):.3f}")
    assert (alpha, beta) == (13, 6)

