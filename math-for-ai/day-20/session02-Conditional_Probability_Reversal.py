"""
LESSON 7.2 — CONDITIONAL PROBABILITY REVERSAL
==============================================

These questions look similar but point in opposite directions:

    P(blue | B): If B was selected, how likely is blue?
    P(B | blue): If blue was observed, how likely was B selected?

For Bag B, P(blue | B)=8/10=0.8. But P(B | blue) is not automatically 0.8.
We must compare blue observations from both bags and include how often each bag
was selected. With equal priors:

    blue from A = 0.5*0.1 = 0.05
    blue from B = 0.5*0.8 = 0.40
    P(B | blue) = 0.40/(0.05+0.40) = 0.8889

CAUSE-TO-EFFECT VERSUS EFFECT-TO-CAUSE
P(evidence | hypothesis) asks how expected the evidence is if a hypothesis is
true. P(hypothesis | evidence) uses observed evidence to reason backward about
its cause. Bayes converts the first direction into the second.

MEDICAL WARNING
P(positive | disease)=0.99 (sensitivity) does not imply
P(disease | positive)=0.99. Healthy people may also test positive, and the
disease may be rare.

WHY THIS MATTERS IN ML
A word may be common in spam without every email containing that word being
spam. Classification requires comparing competing classes, not reversing a
conditional probability by intuition.
"""


def posterior_b_given_blue(prior_a=0.5, prior_b=0.5):
    b_and_blue = prior_b * 0.8
    all_blue = prior_a * 0.1 + b_and_blue
    return b_and_blue / all_blue


if __name__ == "__main__":
    print("P(blue | B) =", 0.8)
    print("P(B | blue) =", round(posterior_b_given_blue(), 4))
    print("They are different questions and different values.")

