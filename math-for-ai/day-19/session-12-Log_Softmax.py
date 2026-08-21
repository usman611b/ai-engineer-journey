"""
LESSON 6 - LOG-SOFTMAX FROM SCRATCH
===================================

Core intuition:

    Softmax gives probabilities. Log-softmax gives the same information as log
    probabilities, computed directly and safely from logits.

Run with:

    python 14_log_softmax.py


===============================================================================
1. FROM SOFTMAX TO LOG-SOFTMAX
===============================================================================

For logits [2.0,1.0,0.1], softmax is approximately:

    [0.659,0.242,0.099]

Take logs:

    [log(0.659),log(0.242),log(0.099)]
    approximately [-0.417,-1.417,-2.317]

Higher probability corresponds to log probability closer to zero.


===============================================================================
2. WHY NOT CALCULATE log(softmax(logits)) NAIVELY?
===============================================================================

An extremely small softmax probability may round to 0. Then log(0) is not a
finite usable number. Instead, derive log probabilities directly from logits.


===============================================================================
3. DERIVE THE FORMULA STEP BY STEP
===============================================================================

Softmax:

    p_i=exp(z_i)/sum_j exp(z_j)

Take log:

    log(p_i)=log(exp(z_i)/sum_j exp(z_j))

Use log(a/b)=log(a)-log(b):

    log(p_i)=log(exp(z_i))-log(sum_j exp(z_j))

Because log(exp(z_i))=z_i:

    log(p_i)=z_i-log(sum_j exp(z_j))

The second part is called log-sum-exp. It is the common normalization term
subtracted from every logit.


===============================================================================
4. STABLE LOG-SUM-EXP
===============================================================================

Direct exp(1000) overflows. Let m=max(logits):

    log_sum_exp = m + log(sum exp(z-m))

Subtracting m makes the largest exponent exp(0)=1 and all others <=1. Adding m
outside restores the correct mathematical value.


===============================================================================
5. COMPLETE ROADMAP DRY-RUN
===============================================================================

For logits [2.0,1.0,0.1]:

    max_logit=2.0
    shifted=[0,-1,-1.9]
    exp(shifted)=[1,0.368,0.150]
    sum=1.518
    log(sum)=0.417
    log_sum_exp=2.0+0.417=2.417

Subtract from original logits:

    2.0-2.417=-0.417
    1.0-2.417=-1.417
    0.1-2.417=-2.317

Result:

    [-0.417,-1.417,-2.317]

Exponentiating these returns the softmax probabilities.


===============================================================================
6. WHY TRAINING USES THIS
===============================================================================

Cross-entropy for one correct class selects its log probability and negates it:

    logits -> log-softmax -> choose correct log probability -> negative -> loss

Frameworks combine these operations for stability. That is why classification
loss usually expects raw logits, not manually softmaxed probabilities.


===============================================================================
7. COMMON CONFUSIONS
===============================================================================

1. Negative log probabilities are normal; probabilities are at most 1.
2. A value closer to 0 represents higher probability.
3. Log-softmax is not a different distribution; it is the same distribution in
   log space.
4. The stable formula does not change the mathematical result.
5. Sum of log probabilities is not 1; exponentials of them sum to 1.

Mental model:

    raw scores -> stable common normalizer -> log probabilities -> stable loss
"""

import math


def log_softmax(logits):
    if len(logits)==0:
        raise ValueError("logits cannot be empty.")
    max_logit=max(logits)
    shifted=[z-max_logit for z in logits]
    log_sum_exp=max_logit+math.log(sum(math.exp(z) for z in shifted))
    return [z-log_sum_exp for z in logits]


def softmax_for_check(logits):
    return [math.exp(value) for value in log_softmax(logits)]


def demonstrate_dry_run():
    print("\n"+"="*78)
    print("DEMO 1 - COMPLETE LOG-SOFTMAX DRY-RUN")
    print("="*78)
    logits=[2.0,1.0,0.1]
    maximum=max(logits)
    shifted=[z-maximum for z in logits]
    exp_sum=sum(math.exp(z) for z in shifted)
    log_sum_exp=maximum+math.log(exp_sum)
    print("logits=",logits)
    print("max=",maximum)
    print("shifted=",shifted)
    print("sum(exp(shifted))=",round(exp_sum,3))
    print("log_sum_exp=",round(log_sum_exp,3))
    print("log probabilities=",[round(x,3) for x in log_softmax(logits)])


def demonstrate_recovery():
    print("\n"+"="*78)
    print("DEMO 2 - SAME INFORMATION AS SOFTMAX")
    print("="*78)
    logs=log_softmax([2,1,0.1])
    probs=[math.exp(x) for x in logs]
    print("log probs:",[round(x,3) for x in logs])
    print("exp(log probs):",[round(x,3) for x in probs])
    print("unrounded probability sum:",sum(probs))


def demonstrate_extreme_logits():
    print("\n"+"="*78)
    print("DEMO 3 - EXTREME LOGITS REMAIN FINITE")
    print("="*78)
    logits=[1000,0,-1000]
    print("logits:",logits)
    print("log-softmax:",log_softmax(logits))


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. What does log-softmax output?
2. Why not always compute log(softmax(logits)) separately?
3. What is the formula z_i-log-sum-exp doing?
4. Which represents higher probability: -0.2 or -5?
5. What happens when log-softmax outputs are exponentiated?

Solutions:
1. Log probabilities for a Categorical distribution.
2. Tiny softmax values may round to zero before log is applied.
3. It subtracts one common normalization term from every raw score.
4. -0.2, because it is closer to zero.
5. They become ordinary softmax probabilities that sum to 1.
""")


def main():
    demonstrate_dry_run(); demonstrate_recovery(); demonstrate_extreme_logits()
    practice_questions()


if __name__=="__main__":
    main()
