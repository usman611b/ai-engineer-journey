"""
LESSON 6 - CROSS-ENTROPY AND NEGATIVE LOG-LIKELIHOOD
=====================================================

Core intuition:

    Cross-entropy asks how much probability the model assigned to the truth.
    High probability on truth gives small loss; low probability gives large loss.

Run with:

    python 15_cross_entropy_negative_log_likelihood.py


===============================================================================
1. ONE CLASSIFICATION EXAMPLE
===============================================================================

True class: cat

Model prediction:

    cat=0.90, dog=0.07, bird=0.03

Correct probability is 0.90. Loss:

    -log(0.90)=0.105 approximately

Small loss: the model strongly believed the correct answer.

Worse prediction:

    cat=0.10, dog=0.80, bird=0.10

    -log(0.10)=2.303

Much larger loss because only 10% belief went to truth.


===============================================================================
2. WHY NEGATIVE LOG?
===============================================================================

    P(correct)=0.99  -> -log=0.010
    P(correct)=0.50  -> -log=0.693
    P(correct)=0.10  -> -log=2.303
    P(correct)=0.001 -> -log=6.908

Log makes tiny probabilities strongly costly. The negative sign turns negative
log probabilities into a nonnegative loss to minimize.

Why not simply 1-P(correct)? It does not distinguish strongly enough between
being wrong and extremely confidently wrong. Negative log grows without bound
as correct probability approaches zero.


===============================================================================
3. FULL CROSS-ENTROPY FORMULA
===============================================================================

For true distribution y and predicted probabilities p:

    cross_entropy = -sum_i y_i*log(p_i)

If cat is true, one-hot target is:

    y=[1,0,0]

For p=[0.9,0.07,0.03]:

    -[1*log(0.9)+0*log(0.07)+0*log(0.03)]
    =-log(0.9)

Zero terms disappear. For ordinary single-label classification, cross-entropy
reduces to negative log probability of the correct class.


===============================================================================
4. WHAT IS NEGATIVE LOG-LIKELIHOOD?
===============================================================================

Likelihood asks how much probability the model gave the observed answer. If the
observed class is cat and P(cat)=0.9, its likelihood is 0.9.

    negative log-likelihood = -log(likelihood of observed answer)

For one-hot single-label classification, categorical cross-entropy and NLL give
the same per-example result.

Minimizing -log P(correct) is equivalent to maximizing P(correct), so training
adjusts model parameters to make observed data more likely.


===============================================================================
5. FROM LOGITS TO LOSS: ROADMAP PIPELINE
===============================================================================

    def cross_entropy_loss(logits,target_index):
        log_probs=log_softmax(logits)
        return -log_probs[target_index]

For logits [2.0,1.0,0.1]:

    log-softmax approximately [-0.417,-1.417,-2.317]

If cat is target index 0:

    choose log_probs[0] = -0.417
    negate = 0.417 loss

Full pipeline:

    network -> logits -> log-softmax -> correct class log probability
    -> negative -> loss -> backpropagation -> parameter update


===============================================================================
6. CORRECT ARGMAX IS NOT THE WHOLE STORY
===============================================================================

Both models predict cat:

    Model A: cat=0.51, dog=0.49
    Model B: cat=0.99, dog=0.01

But B gets much lower loss because it assigned much more belief to truth.
Cross-entropy trains probability quality, not only whether argmax happens to win.


===============================================================================
7. LANGUAGE MODEL CONNECTION
===============================================================================

For each token position, an LLM asks:

    How much probability did I assign to the actual next token?

Token loss:

    -log P(correct next token | previous tokens)

Losses are summed/averaged across token positions and training examples. This is
how probability becomes a learning signal for language modeling.


===============================================================================
8. WHY FRAMEWORKS EXPECT RAW LOGITS
===============================================================================

PyTorch CrossEntropyLoss conceptually combines stable log-softmax and NLL. You
usually pass raw logits and integer target indexes; manually applying softmax
first is unnecessary and can reduce numerical stability.


===============================================================================
9. COMMON CONFUSIONS
===============================================================================

1. Cross-entropy loss is low when truth gets high probability.
2. Target index selects the correct class; it is not a predicted probability.
3. For one-hot classification, CE reduces to NLL of the correct class.
4. Do not take log(0); stable code works from logits via log-softmax.
5. Loss measures the prediction during training; backprop computes how weights
   contributed and gradient descent updates them.

Mental model:

    probability on truth -> negative log -> useful training penalty
"""

import math


def log_softmax(logits):
    maximum=max(logits)
    shifted=[z-maximum for z in logits]
    log_sum_exp=maximum+math.log(sum(math.exp(z) for z in shifted))
    return [z-log_sum_exp for z in logits]


def cross_entropy_loss(logits,target_index):
    if target_index < 0 or target_index >= len(logits):
        raise ValueError("target index is outside logits.")
    log_probs=log_softmax(logits)
    return -log_probs[target_index]


def cross_entropy_from_probabilities(target,probs):
    if len(target)!=len(probs):
        raise ValueError("target and probs must align.")
    if any(p <= 0 for p in probs):
        raise ValueError("predicted probabilities must be positive for log.")
    return -sum(y*math.log(p) for y,p in zip(target,probs))


def demonstrate_probability_loss():
    print("\n"+"="*78)
    print("DEMO 1 - CORRECT PROBABILITY CONTROLS LOSS")
    print("="*78)
    for p in (0.99,0.9,0.5,0.1,0.001):
        print(f"P(correct)={p:>5} -> -log(p)={-math.log(p):.4f}")


def demonstrate_roadmap():
    print("\n"+"="*78)
    print("DEMO 2 - LOGITS TO CROSS-ENTROPY")
    print("="*78)
    logits=[2.0,1.0,0.1]; target_index=0
    logs=log_softmax(logits)
    probs=[math.exp(x) for x in logs]
    print("logits=",logits)
    print("log probabilities=",[round(x,3) for x in logs])
    print("probabilities=",[round(x,3) for x in probs])
    print("target index=0 -> correct log probability=",round(logs[0],3))
    print("loss=-correct log probability=",round(cross_entropy_loss(logits,0),3))
    print("one-hot formula check=",round(cross_entropy_from_probabilities([1,0,0],probs),3))


def demonstrate_confidence():
    print("\n"+"="*78)
    print("DEMO 3 - SAME TARGET, DIFFERENT LOGITS")
    print("="*78)
    cases={"strong correct":[4,0,0],"uncertain":[1,0.9,0.8],"strong wrong":[0,4,0]}
    for name,logits in cases.items():
        print(f"{name:>14}: logits={logits}, target-0 loss={cross_entropy_loss(logits,0):.4f}")


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. Why does P(correct)=0.99 give tiny loss?
2. Why place a negative sign before log probability?
3. Why does one-hot CE select only the correct class term?
4. How are CE and NLL related in ordinary single-label classification?
5. Should raw logits or manually softmaxed values go to framework CE loss?

Solutions:
1. log(0.99) is close to zero, so its negative is tiny.
2. Log probabilities are nonpositive; the sign creates a loss to minimize.
3. Every incorrect-class target entry is zero, so those products disappear.
4. They become the same negative log probability of the observed class.
5. Raw logits; the stable loss combines log-softmax and NLL internally.
""")


def main():
    demonstrate_probability_loss(); demonstrate_roadmap(); demonstrate_confidence()
    practice_questions()


if __name__=="__main__":
    main()
