"""
LESSON 6 - SOFTMAX FROM SCRATCH
===============================

Core intuition:

    A neural network produces raw scores. Softmax turns those scores into a
    valid Categorical probability distribution.

Run with:

    python 13_softmax.py


===============================================================================
1. LOGITS ARE NOT PROBABILITIES
===============================================================================

Suppose a classifier outputs:

    cat=2.0, dog=1.0, bird=0.1

These are logits: raw unnormalized scores. They may be negative, larger than 1,
and do not sum to 1. Higher logit means stronger relative model preference, but
the number itself is not yet a probability.


===============================================================================
2. THE SOFTMAX FORMULA IN TWO IDEAS
===============================================================================

    softmax(z_i)=exp(z_i)/sum_j exp(z_j)

Do not memorize first. Think:

    1. exp turns arbitrary scores into positive strengths and amplifies gaps.
    2. divide each strength by their total to make shares that sum to 1.

Exponentiation preserves ordering: if z_a>z_b, then exp(z_a)>exp(z_b).


===============================================================================
3. COMPLETE HAND CALCULATION
===============================================================================

Logits:

    [2.0,1.0,0.1]

Naive exponentials:

    e^2.0=7.389
    e^1.0=2.718
    e^0.1=1.105

Total:

    7.389+2.718+1.105=11.212

Normalize:

    cat =7.389/11.212=0.659
    dog =2.718/11.212=0.242
    bird=1.105/11.212=0.099

Result:

    [0.659,0.242,0.099]

All values are positive and sum to 1. We now have a Categorical distribution.


===============================================================================
4. WHY EXPONENTIAL?
===============================================================================

For logits [3,2,1]:

    e^3=20.1, e^2=7.4, e^1=2.7

Exp keeps rank but makes the strongest score stand out. It also makes every
strength positive. Dividing by the sum turns each one into its fraction of total
model preference.


===============================================================================
5. NUMERICAL STABILITY: SUBTRACT THE MAXIMUM
===============================================================================

For [1000,1001,1002], directly calculating e^1002 can overflow.

Subtract the largest logit from every score:

    max=1002
    shifted=[1000-1002,1001-1002,1002-1002]
           =[-2,-1,0]

Now:

    e^-2=0.135, e^-1=0.368, e^0=1

Safe values.

Why is the answer unchanged?

    exp(z_i-c)/sum exp(z_j-c)

Every numerator/denominator contains the same factor exp(-c), which cancels.
Softmax depends on relative differences, not the absolute location of logits.


===============================================================================
6. ROADMAP CODE LINE BY LINE
===============================================================================

    def softmax(logits):
        max_logit=max(logits)
        shifted=[z-max_logit for z in logits]
        exps=[math.exp(z) for z in shifted]
        total=sum(exps)
        return [e/total for e in exps]

Flow:

    raw logits -> max shift -> exponentiate -> positive strengths
    -> divide by total -> probabilities

Dry-run for [2,1,0.1]:

    max=2
    shifted=[0,-1,-1.9]
    exps=[1,0.368,0.150]
    total=1.518
    result=[0.659,0.242,0.099]


===============================================================================
7. RELATIVE DIFFERENCES MATTER
===============================================================================

Adding 100 to every logit does not change softmax:

    softmax([2,1,0.1]) = softmax([102,101,100.1])

But multiplying logits changes their gaps and therefore changes how sharp the
distribution is. This leads to temperature later in sampling.


===============================================================================
8. AI CONNECTIONS
===============================================================================

Image classification:

    image -> network -> class logits -> softmax -> class probabilities

Language model:

    context -> transformer -> one logit per vocabulary token -> softmax
    -> next-token Categorical distribution

Softmax output is a mathematical probability distribution, but a model can be
overconfident. A value 0.99 is the model's assigned probability mass, not a
guarantee of real-world calibration.


===============================================================================
9. COMMON CONFUSIONS
===============================================================================

1. Logits are scores, not probabilities.
2. Softmax is across competing classes, not independently applied per class.
3. Subtracting the max does not change the result.
4. Exp amplifies differences; normalization makes the total 1.
5. Softmax probabilities need not be perfectly calibrated real-world confidence.
6. Do not round intermediate values aggressively; rounding can make totals drift.

Mental model:

    logits -> safe shift -> exp -> positive strengths -> shares of total -> probs
"""

import math


def softmax(logits):
    if len(logits)==0:
        raise ValueError("logits cannot be empty.")
    max_logit=max(logits)
    shifted=[z-max_logit for z in logits]
    exps=[math.exp(z) for z in shifted]
    total=sum(exps)
    return [e/total for e in exps]


def demonstrate_dry_run():
    print("\n"+"="*78)
    print("DEMO 1 - COMPLETE ROADMAP DRY-RUN")
    print("="*78)
    logits=[2.0,1.0,0.1]
    maximum=max(logits)
    shifted=[z-maximum for z in logits]
    exps=[math.exp(z) for z in shifted]
    total=sum(exps)
    probs=softmax(logits)
    print("logits=",logits)
    print("max=",maximum)
    print("shifted=",shifted)
    print("exps=",[round(e,3) for e in exps])
    print("total=",round(total,3))
    print("probabilities=",[round(p,3) for p in probs])
    print("unrounded sum=",sum(probs))


def demonstrate_large_logits():
    print("\n"+"="*78)
    print("DEMO 2 - STABILITY WITH HUGE LOGITS")
    print("="*78)
    logits=[1000,1001,1002]
    print("logits=",logits)
    print("shifted=",[z-max(logits) for z in logits])
    print("softmax=",[round(p,3) for p in softmax(logits)])


def demonstrate_shift_invariance():
    print("\n"+"="*78)
    print("DEMO 3 - ADDING A CONSTANT CHANGES NOTHING")
    print("="*78)
    original=[2,1,0.1]; moved=[z+100 for z in original]
    print("original:",softmax(original))
    print("plus 100:",softmax(moved))


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. Why are logits not probabilities?
2. What two jobs do exp and normalization perform?
3. Why subtract max(logits)?
4. Does adding the same constant change softmax?
5. What AI distribution does softmax produce?

Solutions:
1. They are unrestricted scores and need not be positive or total 1.
2. Exp creates positive relative strengths; normalization makes shares total 1.
3. To prevent exponential overflow while preserving relative differences.
4. No.
5. A Categorical distribution over classes or tokens.
""")


def main():
    demonstrate_dry_run(); demonstrate_large_logits(); demonstrate_shift_invariance()
    practice_questions()


if __name__=="__main__":
    main()
