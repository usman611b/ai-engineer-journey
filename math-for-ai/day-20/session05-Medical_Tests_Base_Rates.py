"""
LESSON 7.5 — MEDICAL TESTS AND THE BASE-RATE EFFECT
===================================================

Suppose disease prevalence is 1/1000=0.001, sensitivity is 0.99, and the
false-positive rate is 0.01. A positive result is observed.

NATURAL-FREQUENCY VIEW (100,000 PEOPLE)
100 are sick; the test finds 99 true positives. 99,900 are healthy; 1% gives
999 false positives. Among 1,098 total positives, only 99 are sick:

    P(disease | positive) = 99/1098 = about 9.02%

Why not 99%? Sensitivity is P(+|D), not P(D|+). The disease's prior/base rate
is tiny. A small error applied to a huge healthy group creates many errors.

FORMULA VIEW
    numerator = P(+|D)P(D)
    evidence  = P(+|D)P(D) + P(+|not D)P(not D)

COMPLEMENT RULE
Disease and no disease are mutually exclusive and exhaustive, so:

    P(not D) = 1 - P(D)

If P(D)=0.09, the remaining probability is P(not D)=0.91. We subtract from 1
because the total probability of all possible cases is 1 (100%).

INTERPRETATION
The test is not useless. It updates risk from 0.1% to about 9%, roughly a
90-fold increase. But evidence must be interpreted alongside the base rate.
This lesson applies to anomaly detection, fraud detection, and rare-event ML.

This file is educational, not personal medical advice.
"""


def positive_predictive_value(prevalence, sensitivity, false_positive_rate):
    true_positive_route = prevalence * sensitivity
    false_positive_route = (1 - prevalence) * false_positive_rate
    return true_positive_route / (true_positive_route + false_positive_route)


if __name__ == "__main__":
    result = positive_predictive_value(0.001, 0.99, 0.01)
    print(f"P(disease | positive) = {result:.4%}")

