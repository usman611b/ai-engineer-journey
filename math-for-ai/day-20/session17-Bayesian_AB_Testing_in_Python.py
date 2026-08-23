"""
DAY 20 — SESSION 17: BAYESIAN A/B TESTING IN PYTHON
===================================================

random.betavariate(alpha,beta) draws one possible true rate from a Beta
posterior. One draw is one plausible world, not a prediction or final estimate.

Monte Carlo procedure:

1. Draw theta_A from A's posterior.
2. Draw theta_B from B's posterior.
3. Record whether B>A.
4. Repeat many times.
5. B wins / simulations estimates P(theta_B>theta_A).

With only five simulations, sampling noise is large. With 100,000, the estimate
is much more stable. random.seed makes the pseudo-random sequence reproducible;
it does not change the mathematical distributions.

We also calculate expected lift B-A and the probability that lift exceeds a
practically meaningful threshold. This separates "probably better" from
"better by enough to matter."
"""

import random


def posterior(prior_alpha, prior_beta, successes, failures):
    return prior_alpha + successes, prior_beta + failures


def compare_variants(
    posterior_a,
    posterior_b,
    simulations=100_000,
    minimum_useful_lift=0.0,
    seed=42,
):
    if simulations <= 0:
        raise ValueError("simulations must be positive")
    random.seed(seed)
    b_wins = 0
    useful_wins = 0
    total_lift = 0.0

    for _ in range(simulations):
        theta_a = random.betavariate(*posterior_a)
        theta_b = random.betavariate(*posterior_b)
        lift = theta_b - theta_a
        total_lift += lift
        if lift > 0:
            b_wins += 1
        if lift > minimum_useful_lift:
            useful_wins += 1

    return {
        "probability_b_better": b_wins / simulations,
        "probability_useful_lift": useful_wins / simulations,
        "expected_absolute_lift": total_lift / simulations,
    }


if __name__ == "__main__":
    a = posterior(1, 1, successes=20, failures=80)
    b = posterior(1, 1, successes=30, failures=70)
    result = compare_variants(a, b, minimum_useful_lift=0.05)
    print(f"A posterior: Beta{a}")
    print(f"B posterior: Beta{b}")
    print(f"P(B>A): {result['probability_b_better']:.2%}")
    print(f"P(B-A>5 points): {result['probability_useful_lift']:.2%}")
    print(f"Expected absolute lift: {result['expected_absolute_lift']:.2%}")

