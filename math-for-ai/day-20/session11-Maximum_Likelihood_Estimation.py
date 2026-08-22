"""
LESSON 7.11 — MAXIMUM LIKELIHOOD ESTIMATION (MLE)
=================================================

PROBLEM MLE SOLVES
ML models contain unknown parameters: coin probability, regression weights,
word probabilities, Gaussian mean/variance, or neural-network weights. MLE
learns them from examples by choosing values that make the observed training
data most likely.

    theta_MLE = argmax_theta P(data | theta)

argmax returns the input theta producing the greatest likelihood; it does not
return the likelihood value itself.

COIN EXAMPLE
Seven heads and three tails have likelihood theta^7(1-theta)^3. This is
maximized at theta=7/10=0.7. In general:

    theta_MLE = heads / total tosses

NAIVE BAYES
If "free" appears in 80 of 100 spam emails, MLE estimates
P(free|spam)=80/100=0.8.

REGRESSION AND NEURAL NETWORKS
For linear regression with Gaussian noise, maximizing likelihood is equivalent
to minimizing squared error. For classification, maximizing likelihood of the
correct labels is equivalent to minimizing negative log-likelihood/cross-
entropy. Gradient descent is the search method; MLE defines the objective.

    MLE objective -> loss function -> gradient descent -> learned parameters

LIMITATION
MLE trusts observed data completely. One head in one toss gives theta=1, which
overstates certainty. With little/noisy data it may overfit or assign zero to
unseen outcomes. Priors, smoothing, or regularization can stabilize estimates.
"""

import math


def coin_likelihood(theta, heads, tails):
    return theta**heads * (1 - theta) ** tails


def coin_mle(heads, tails):
    return heads / (heads + tails)


if __name__ == "__main__":
    heads, tails = 7, 3
    estimate = coin_mle(heads, tails)
    print("MLE theta:", estimate)
    for candidate in (0.5, 0.6, 0.7, 0.8):
        value = coin_likelihood(candidate, heads, tails)
        print(f"theta={candidate:.1f}, likelihood={value:.8f}")
    assert math.isclose(estimate, 0.7)

