"""
LESSON 7.9 — ZERO PROBABILITY AND LAPLACE SMOOTHING
===================================================

PROBLEM
If P(meeting|spam)=0, multiplying it into a Naive Bayes score destroys all other
evidence: a*b*0=0. "Never observed" in a small dataset is not "impossible."

BERNOULLI LAPLACE SMOOTHING
For word present/absent, add one imaginary observation to both outcomes:

    P(word present | class) = (present_count + 1)/(class_count + 2)

Why +2? There are two possible states: present and absent. We add +1 to each,
so the total increases by two. This has nothing to do with having two classes.

With 0 of 3 spam emails containing "meeting":

    (0+1)/(3+2)=1/5=0.2

With 2 of 3 containing "free":

    (2+1)/(3+2)=3/5=0.6

Smoothing prevents exact zero and also pulls extreme estimates toward the
middle. It reserves a little probability for unseen possibilities and reduces
overconfidence from limited samples.

GENERAL ADDITIVE SMOOTHING
Using alpha instead of 1 gives:

    (count + alpha)/(total + alpha*K)

K is the number of possible outcomes/categories. Alpha controls smoothing
strength. Laplace smoothing specifically uses alpha=1.
"""


def smoothed_bernoulli(present_count, class_count, alpha=1.0):
    return (present_count + alpha) / (class_count + 2 * alpha)


if __name__ == "__main__":
    p_meeting_spam = smoothed_bernoulli(0, 3)
    p_free_spam = smoothed_bernoulli(2, 3)
    print("P(meeting|spam), smoothed =", p_meeting_spam)
    print("P(free|spam), smoothed    =", p_free_spam)
    assert p_meeting_spam > 0

