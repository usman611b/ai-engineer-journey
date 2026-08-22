"""
LESSON 7.1 — BAYESIAN THINKING: LEARNING FROM EVIDENCE
=======================================================

CORE QUESTION
Bayesian thinking asks: after observing new evidence, how should our belief
change? Here, "belief" is not emotion. It is a probability based on the
information currently available.

    belief before evidence + new evidence -> belief after evidence
    prior                  + evidence     -> posterior

BAG EXAMPLE
Bag A contains 9 red and 1 blue ball. Bag B contains 2 red and 8 blue balls.
The hidden bag is initially chosen fairly, so P(A)=P(B)=0.5. Before seeing a
ball, neither explanation is preferred.

If we observe red, A becomes more believable because red is common under A.
It is not certain: B can also produce red. Evidence changes confidence; it
usually does not create absolute proof.

FREQUENCY INTUITION
Imagine 100 repetitions. A is selected about 50 times and produces about
50*0.9=45 red observations. B is selected about 50 times and produces about
50*0.2=10 red observations. Of the 55 red observations, 45 came from A:

    P(A | red) = 45 / 55 = 0.8182

The symbol | means "given that". P(A | red) reads: probability that A was
selected, given that red was observed.

WHY AI NEEDS THIS
AI sees uncertain clues: a word suggests spam, pixels suggest a cat, symptoms
suggest disease. A clue can support a class without guaranteeing it. Bayesian
reasoning supplies a disciplined way to update confidence.

COMMON MISTAKE
"Red is common in A" does not mean "red proves A." Always compare every
possible explanation that could produce the evidence.
"""


def frequency_update(prior_a=0.5, prior_b=0.5):
    red_from_a = prior_a * 0.9
    red_from_b = prior_b * 0.2
    return red_from_a / (red_from_a + red_from_b)


if __name__ == "__main__":
    posterior_a = frequency_update()
    print(f"Prior P(A): 50.00%")
    print(f"Posterior P(A | red): {posterior_a:.2%}")
    assert round(posterior_a, 4) == 0.8182

