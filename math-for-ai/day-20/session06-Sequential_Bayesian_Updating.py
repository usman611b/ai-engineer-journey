"""
LESSON 7.6 — SEQUENTIAL UPDATING
================================

Bayesian learning can happen repeatedly:

    posterior after evidence 1 -> prior before evidence 2

For the rare-disease example, the first positive changes 0.1% to about 9.02%.
Use that posterior—not the original 0.1%—as the prior for a second positive.
With sensitivity 0.99 and false-positive rate 0.01, the second posterior is
about 90.74%.

WHY TWO POSITIVES ARE STRONGER
For a healthy person, one false positive has probability 0.01. If errors are
independent, two false positives have probability:

    0.01 * 0.01 = 0.0001 = 0.01% = 1 in 10,000

INDEPENDENCE ASSUMPTION
Independent means knowing the first error happened does not change the chance
of the second error. Two readings from the same faulty machine or contaminated
sample may share a systematic cause and are not truly independent. Multiplying
their probabilities as separate evidence would exaggerate confidence.

AI CONNECTION
Models often update as evidence arrives: sensor readings, user clicks, fraud
signals, or experimental results. Each posterior summarizes what has been
learned so far and becomes the starting belief for the next update.
"""


def update(prior, sensitivity=0.99, false_positive_rate=0.01):
    disease_positive = prior * sensitivity
    healthy_positive = (1 - prior) * false_positive_rate
    return disease_positive / (disease_positive + healthy_positive)


if __name__ == "__main__":
    prior = 0.001
    for test_number in (1, 2):
        prior = update(prior)
        print(f"After positive test {test_number}: {prior:.4%}")

