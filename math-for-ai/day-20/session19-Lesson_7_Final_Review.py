"""
DAY 20 — SESSION 19: LESSON 7 FINAL REVIEW
==========================================

COMPLETE CONCEPTUAL FLOW
------------------------
Bayes updates beliefs using evidence. Prior is belief before evidence;
likelihood asks how expected evidence is under a hypothesis; evidence totals
all routes to the observation; posterior is belief after evidence.

    posterior = likelihood*prior/evidence

MLE estimates unknown parameters using observed data only. MAP adds a prior and
selects the posterior mode. A full posterior retains uncertainty rather than
compressing belief to one point.

Beta represents uncertainty about a success probability. Its ratio controls
center and alpha+beta controls concentration. After successes and failures:

    Beta(alpha,beta) -> Beta(alpha+successes,beta+failures)

In A/B testing, update one posterior per variant and estimate P(theta_B>theta_A)
by repeated posterior sampling. This is confidence that B's underlying rate is
higher, not B's conversion rate.

PRACTICE ANSWERS EXPLAINED
--------------------------
Factory Bayes example: A makes 60% with 2% defects; B makes 40% with 5%.
Defective routes are 0.012 and 0.020; total 0.032; therefore P(B|defect)=
0.020/0.032=0.625. B produces fewer products but most observed defects.

Beta update: Beta(3,3)+12 successes+8 failures = Beta(15,11); posterior mean
15/26=0.5769.

Bernoulli Laplace smoothing: a word present in 0 of 8 spam documents gets
(0+1)/(8+2)=0.1, preventing a zero score.

For Beta(10,6), posterior mean=10/16=0.625 and MAP=9/14=0.6429. Mean averages
the posterior; MAP chooses its highest point.

If B wins 91,000 of 100,000 posterior simulations, P(B>A) is estimated at 91%.
That does not mean B converts 91% of users.

FINAL MEMORY MAP
----------------
MLE: best fit to data only.
MAP: most believable point after prior+data.
Posterior mean: average parameter under posterior.
Beta: complete uncertainty about an unknown probability.
Bayesian update: old posterior becomes new prior.
A/B testing: compare uncertain rates, then consider practical lift and cost.
"""

import random


def bayes_binary(prior_h, likelihood_e_h, likelihood_e_not_h):
    route_h = prior_h * likelihood_e_h
    route_not_h = (1 - prior_h) * likelihood_e_not_h
    return route_h / (route_h + route_not_h)


def update_beta(alpha, beta, successes, failures):
    return alpha + successes, beta + failures


def beta_mean(alpha, beta):
    return alpha / (alpha + beta)


def beta_map(alpha, beta):
    return (alpha - 1) / (alpha + beta - 2)


def probability_b_better(a, b, simulations=50_000, seed=42):
    random.seed(seed)
    wins = sum(
        random.betavariate(*b) > random.betavariate(*a)
        for _ in range(simulations)
    )
    return wins / simulations


if __name__ == "__main__":
    factory_answer = bayes_binary(0.40, 0.05, 0.02)
    print(f"Factory P(B|defect): {factory_answer:.3%}")

    posterior = update_beta(3, 3, 12, 8)
    print(f"Updated Beta: Beta{posterior}, mean={beta_mean(*posterior):.3%}")

    example = (10, 6)
    print(f"Beta{example} mean={beta_mean(*example):.3f}")
    print(f"Beta{example} MAP={beta_map(*example):.3f}")

    a = update_beta(1, 1, 20, 80)
    b = update_beta(1, 1, 30, 70)
    print(f"Estimated P(B>A): {probability_b_better(a,b):.2%}")
