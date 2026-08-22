"""
LESSON 7.10 — NUMERICAL UNDERFLOW AND LOG PROBABILITIES
=======================================================

Naive Bayes may multiply hundreds of probabilities smaller than one. Products
shrink rapidly: 0.01**200 = 10**-400. Standard floating-point numbers cannot
represent arbitrarily tiny values, so a nonzero mathematical value may become
computer value 0.0. This is numerical underflow.

If spam=10^-400 and ham=10^-450, spam should win, but both may be stored as
zero. The comparison is lost.

LOG-SPACE SOLUTION
The logarithm converts products into sums:

    log(a*b*c) = log(a)+log(b)+log(c)

Instead of multiplying probabilities, calculate:

    log_score(class) = log P(class) + sum(log P(word|class))

Logs preserve ordering: if a>b>0, log(a)>log(b). Scores become negative because
log(p)<0 when 0<p<1, but the larger score (closer to zero) still wins.

Example:
    spam score = 0.4*0.7*0.6 = 0.168
    log score  = -0.916-0.357-0.511 = about -1.784

The representation changes; the prediction does not. Laplace smoothing is also
important because log(0) is undefined.

ML CONNECTION
Cross-entropy and negative log-likelihood use the same log idea. Log-space is a
general numerical-stability technique, not a special trick limited to Bayes.
"""

import math


def log_score(prior, likelihoods):
    return math.log(prior) + sum(math.log(p) for p in likelihoods)


if __name__ == "__main__":
    spam = log_score(0.4, [0.7, 0.6])
    ham = log_score(0.6, [0.1, 0.05])
    print(f"spam log-score: {spam:.4f}")
    print(f"ham log-score:  {ham:.4f}")
    print("Prediction:", "spam" if spam > ham else "ham")

