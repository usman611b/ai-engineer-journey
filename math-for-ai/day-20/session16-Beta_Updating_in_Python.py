"""
DAY 20 — SESSION 16: BETA UPDATING IN PYTHON
=============================================

This implementation turns the theory into small reusable functions.

update_beta(alpha,beta,successes,failures) returns the posterior parameters.
For update_beta(2,2,7,3), Python performs:

    new_alpha = 2+7 = 9
    new_beta  = 2+3 = 5
    return (9,5)

Tuple unpacking assigns both returned values:

    alpha, beta = (9,5)

beta_mean then calculates 9/(9+5)=0.643. A second update with 4 successes and
1 failure enters using alpha=9,beta=5 and returns 13,6. This demonstrates that
the stored posterior becomes the starting prior for new evidence.

The BetaBelief class below packages parameters with validation, mean, variance,
standard deviation, and update behavior. It is not required for understanding
Bayes; it simply organizes state cleanly for a real program.
"""

from dataclasses import dataclass
import math


def update_beta(alpha, beta, successes, failures):
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")
    if successes < 0 or failures < 0:
        raise ValueError("observation counts cannot be negative")
    return alpha + successes, beta + failures


def beta_mean(alpha, beta):
    return alpha / (alpha + beta)


@dataclass
class BetaBelief:
    alpha: float
    beta: float

    def __post_init__(self):
        if self.alpha <= 0 or self.beta <= 0:
            raise ValueError("Beta parameters must be positive")

    @property
    def strength(self):
        return self.alpha + self.beta

    @property
    def mean(self):
        return self.alpha / self.strength

    @property
    def variance(self):
        return self.alpha * self.beta / (
            self.strength**2 * (self.strength + 1)
        )

    @property
    def standard_deviation(self):
        return math.sqrt(self.variance)

    def update(self, successes, failures):
        if successes < 0 or failures < 0:
            raise ValueError("Counts cannot be negative")
        self.alpha += successes
        self.beta += failures

    def describe(self, label):
        print(
            f"{label}: Beta({self.alpha:g},{self.beta:g}), "
            f"mean={self.mean:.3%}, strength={self.strength:g}, "
            f"std={self.standard_deviation:.4f}"
        )


if __name__ == "__main__":
    belief = BetaBelief(2, 2)
    belief.describe("Prior")
    belief.update(7, 3)
    belief.describe("After batch 1")
    belief.update(4, 1)
    belief.describe("After batch 2")
    assert (belief.alpha, belief.beta) == (13, 6)

