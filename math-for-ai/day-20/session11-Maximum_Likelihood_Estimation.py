"""
DAY 20 — SESSION 11: MAXIMUM LIKELIHOOD ESTIMATION (MLE)
========================================================

Read this as a complete conceptual lesson, then run the demonstrations.

1. THE PROBLEM MLE SOLVES
-------------------------
Every ML model contains unknown adjustable numbers called parameters:

* Coin model: probability of heads, theta
* Naive Bayes: word probabilities under spam and ham
* Linear regression: weights and bias
* Gaussian model: mean and variance
* Neural network: all weights and biases

Before training, the model does not know their correct values. MLE gives a
logical learning rule:

    Choose parameter values that make the data we actually observed
    most likely to occur.

In symbols:

    theta_MLE = argmax_theta P(data | theta)

Meaning:

1. Keep the observed data fixed.
2. Try possible parameter values.
3. Ask how well each value explains the fixed data.
4. Select the value giving the greatest likelihood.

"argmax" returns the INPUT producing the maximum output. We want the best
theta, not merely the largest likelihood number.


2. COIN EXAMPLE — INTUITION FIRST
---------------------------------
Let theta=P(heads). We toss an unknown coin 10 times and observe 7 heads and 3
tails. Compare possible coins:

* theta=0.2 normally produces mostly tails, so 7 heads are a poor fit.
* theta=0.5 can produce 7 heads, but approximately 5 are expected.
* theta=0.7 expects approximately 7 heads, so it fits well.
* theta=0.95 expects nearly all heads, so 3 tails are a poor fit.

MLE chooses theta=0.7:

    theta_MLE = heads / total = 7/10 = 0.7

This is not a magic formula. The observed frequency 0.7 is the parameter that
best matches what happened.


3. PROBABILITY VERSUS LIKELIHOOD
--------------------------------
They may use the same expression but hold different things fixed.

Probability viewpoint:

    theta is fixed; possible data varies.
    "If theta=0.7, what results might occur?"

Likelihood viewpoint:

    observed data is fixed; candidate theta varies.
    "Given 7 heads and 3 tails, which theta explains them best?"

Likelihood is NOT P(theta is true). It is a compatibility score between a
candidate parameter and the observations.


4. COIN LIKELIHOOD CALCULATION
------------------------------
For independent tosses, one fixed sequence with 7 heads and 3 tails has:

    L(theta) = theta**7 * (1-theta)**3

Examples:

    L(0.5) = 0.5**7 * 0.5**3 = 0.0009765625
    L(0.7) = 0.7**7 * 0.3**3 = about 0.00222357

The sequence is more compatible with theta=0.7. Comparing every theta between
0 and 1 gives a peak at 0.7. If we count every possible ordering, a combination
factor appears, but it is constant across candidate theta values and therefore
does not change the maximizing theta.


5. WHY ML USES MLE
-------------------
MLE converts examples into usable model parameters:

    training examples
        -> calculate their probability under model parameters
        -> find parameters giving the observations high probability
        -> use learned parameters to predict new examples

It supplies a consistent meaning of "best parameters": those that best explain
the training observations.


6. NAIVE BAYES EXAMPLE
----------------------
Suppose "free" occurs in 80 of 100 labeled spam emails. The model needs:

    P(free | spam)

MLE estimates:

    P(free | spam)_MLE = 80/100 = 0.8

Raw emails became a learned parameter for future classification. Similarly, if
"meeting" occurs in 30 of 100 ham emails:

    P(meeting | ham)_MLE = 30/100 = 0.3


7. LINEAR REGRESSION CONNECTION
-------------------------------
A linear model predicts y_hat=w*x+b. Its unknown parameters are w and b. A
common assumption is:

    y = w*x + b + Gaussian noise

Gaussian noise makes predictions close to observed targets more probable than
distant predictions. Under this assumption, maximizing likelihood is
equivalent to minimizing:

    sum((y-y_hat)**2)

Therefore squared-error training is not arbitrary: it is MLE under a Gaussian-
noise assumption. Different probability assumptions can create different loss
functions.


8. CLASSIFICATION AND NEURAL NETWORKS
-------------------------------------
Suppose a training image has the label "cat."

* Weights A give P(cat|image)=0.10: they explain the label poorly.
* Weights B give P(cat|image)=0.95: they explain the label well.

MLE prefers parameters assigning high probability to all correct training
labels. Dataset likelihood multiplies example probabilities. Products become
extremely small, so we use logs:

    log L(theta) = sum(log P(correct_label_i | input_i, theta))

Log preserves order, so maximizing log-likelihood gives the same winner.
Software minimizes losses, so we negate it:

    NLL = -sum(log P(correct label))

For ordinary classification, this is cross-entropy loss.


9. MLE, LOSS, AND GRADIENT DESCENT ARE DIFFERENT
------------------------------------------------
* MLE defines the goal: make observed data likely.
* NLL/cross-entropy measures current failure numerically.
* Gradient descent searches for parameters that reduce that failure.

    MLE principle -> loss -> gradients -> parameter updates

MLE says where we want to go. Loss is the navigation score. Gradient descent
is the movement method.


10. MLE'S MAIN WEAKNESS
-----------------------
MLE uses only observed data. With abundant representative data this is strong;
with tiny data it can be extremely confident.

One coin toss produces heads:

    theta_MLE = 1/1 = 1.0

It assigns P(heads)=100% and P(tails)=0%. This fits the only observation but
does not prove tails is impossible. Similarly, a word absent from three spam
emails gets MLE probability zero even though future spam may contain it.

Other limitations:

* can overfit small or noisy datasets;
* inherits incorrect assumptions in the chosen probability model;
* gives a point estimate and alone does not express parameter uncertainty;
* cannot repair biased, unrepresentative training data merely by having more of
  the same bias.


11. WHEN MLE IS USEFUL
----------------------
MLE is especially useful when sufficient reliable data exists, a sensible
probabilistic model is available, and no meaningful prior knowledge is needed.
With large representative datasets, observed evidence stabilizes estimates.


12. FINAL MENTAL MODEL
----------------------
MLE asks:

    "Which parameter value best explains what I observed?"

Its strength is direct learning from data. Its weakness is trusting limited
data too completely. MAP addresses that weakness by combining likelihood with
a prior.
"""

import math


def coin_likelihood(theta, heads, tails):
    """Likelihood of one fixed heads/tails sequence under candidate theta."""
    if not 0 <= theta <= 1:
        raise ValueError("theta must be between 0 and 1")
    return theta**heads * (1-theta)**tails


def coin_mle(heads, tails):
    """MLE for a Bernoulli coin probability."""
    total = heads + tails
    if total == 0:
        raise ValueError("MLE requires observations")
    return heads / total


def negative_log_likelihood(correct_label_probabilities):
    """NLL is smaller when correct labels receive high probability."""
    return -sum(math.log(p) for p in correct_label_probabilities)


if __name__ == "__main__":
    print("="*65)
    print("DEMO 1: Candidate coins for 7 heads and 3 tails")
    print("="*65)
    heads, tails = 7, 3
    for candidate in (0.2, 0.5, 0.7, 0.9):
        value = coin_likelihood(candidate, heads, tails)
        print(f"theta={candidate:.1f} -> likelihood={value:.10f}")

    estimate = coin_mle(heads, tails)
    print(f"\nMLE = {heads}/{heads+tails} = {estimate:.1f}")

    print("\n"+"="*65)
    print("DEMO 2: Small-data weakness")
    print("="*65)
    print(f"One head, zero tails -> MLE = {coin_mle(1, 0):.1f}")
    print("This fits the observation but does not prove tails is impossible.")

    print("\n"+"="*65)
    print("DEMO 3: Negative log-likelihood")
    print("="*65)
    good = negative_log_likelihood([0.95, 0.90, 0.92])
    poor = negative_log_likelihood([0.20, 0.30, 0.10])
    print(f"Good model NLL: {good:.4f} (smaller)")
    print(f"Poor model NLL: {poor:.4f} (larger)")

    assert math.isclose(estimate, 0.7)
    assert good < poor
