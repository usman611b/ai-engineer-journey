"""
LESSON 6 - LOG PROBABILITIES
=============================

Core intuition:

    Multiplying many small probabilities creates unusably tiny numbers. Logs
    turn multiplication into addition while preserving which result is likelier.

Run with:

    python 12_log_probabilities.py


===============================================================================
1. SEQUENCE PROBABILITIES MULTIPLY
===============================================================================

Suppose an LLM assigns:

    P("I")=0.1
    P("love" | "I")=0.05
    P("AI" | "I love")=0.02

The sequence probability is:

    0.1*0.05*0.02 = 0.0001

For 100 or 1000 tokens, multiplying values smaller than 1 repeatedly creates a
number so tiny that floating-point arithmetic may round it to 0. This is called
numerical underflow. Mathematically the probability is positive; the computer
can no longer represent it in its ordinary number format.


===============================================================================
2. WHY PRODUCTS SHRINK
===============================================================================

    0.1*0.1=0.01
    0.01*0.1=0.001
    0.001*0.1=0.0001

Each multiplication by a number between 0 and 1 makes the result smaller.


===============================================================================
3. THE LOG TRICK
===============================================================================

The key rule is:

    log(a*b)=log(a)+log(b)

Therefore:

    log(0.1*0.05*0.02)
    =log(0.1)+log(0.05)+log(0.02)
    approximately -2.303 + -2.996 + -3.912
    = -9.210

-9.210 is easy for a computer to represent. We changed the representation, not
the underlying ordering of sequence likelihoods.


===============================================================================
4. WHY LOG PROBABILITIES ARE NEGATIVE
===============================================================================

Natural log values:

    log(1)=0
    log(0.9)=-0.105
    log(0.5)=-0.693
    log(0.1)=-2.303
    log(0.01)=-4.605

For 0<p<=1:

    more likely -> log probability closer to 0
    less likely -> more negative log probability

Log is strictly increasing. If P(A)>P(B), then log P(A)>log P(B). Therefore the
most probable candidate is also the candidate with the greatest (least negative)
log probability.


===============================================================================
5. LLM SEQUENCE FORMULA IN WORDS
===============================================================================

Conceptually:

    P(x1,...,xn) = product over t of P(xt | earlier tokens)

In log space:

    log P(x1,...,xn) = sum over t of log P(xt | earlier tokens)

So an LLM can add token log probabilities instead of multiplying tiny token
probabilities.


===============================================================================
6. CONNECTION TO LOSS
===============================================================================

For the correct answer:

    P(correct)=0.9  -> -log(0.9)=0.105, small loss
    P(correct)=0.01 -> -log(0.01)=4.605, large loss

The minus sign turns negative log probability into a positive quantity we can
minimize. This becomes negative log-likelihood and cross-entropy later.


===============================================================================
7. LOG OF ZERO AND NUMERICAL CARE
===============================================================================

log(0) is negative infinity, not an ordinary finite number. Our beginner code
rejects probabilities <=0. Stable model code usually works directly from logits
using log-softmax so tiny probabilities do not first round to zero.


===============================================================================
8. COMMON CONFUSIONS
===============================================================================

1. A more negative log probability is less likely, not more likely.
2. Adding raw probabilities is not equivalent to multiplying them; add their logs.
3. Logs do not change probability ranking because log is increasing.
4. Percentages do not solve underflow; the logarithm's product-to-sum rule does.
5. Exponentiating a very negative total can underflow again; comparison can stay
   entirely in log space.

Mental flow:

    many tiny probabilities -> product underflows
    take logs -> add manageable negative values -> stable comparison/training
"""

import math


def sequence_probability(probabilities):
    result=1.0
    for probability in probabilities:
        result*=probability
    return result


def sequence_log_probability(probabilities):
    total=0.0
    for probability in probabilities:
        if probability <= 0 or probability > 1:
            raise ValueError("Every probability must be in (0,1].")
        total+=math.log(probability)
    return total


def demonstrate_short_sequence():
    print("\n"+"="*78)
    print("DEMO 1 - SHORT LLM SEQUENCE")
    print("="*78)
    probs=[0.1,0.05,0.02]
    logs=[math.log(p) for p in probs]
    print("probabilities:",probs)
    print("product:",sequence_probability(probs))
    print("individual logs:",[round(x,3) for x in logs])
    print("sum of logs:",round(sequence_log_probability(probs),3))
    print("exp(sum of logs):",round(math.exp(sequence_log_probability(probs)),7))


def demonstrate_underflow():
    print("\n"+"="*78)
    print("DEMO 2 - UNDERFLOW")
    print("="*78)
    probs=[0.01]*500
    print("Direct product of 500 probabilities 0.01:",sequence_probability(probs))
    print("Log probability:",sequence_log_probability(probs))
    print("The log value remains usable even though direct multiplication became 0.")


def demonstrate_ranking():
    print("\n"+"="*78)
    print("DEMO 3 - RANKING IS PRESERVED")
    print("="*78)
    candidates={"A":[0.8,0.7,0.6],"B":[0.9,0.5,0.5]}
    for name,probs in candidates.items():
        print(name,"probability=",sequence_probability(probs),"log probability=",round(sequence_log_probability(probs),4))
    print("The larger probability also has the larger/less-negative log probability.")


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. Why do sequence probabilities become tiny?
2. What log rule makes computation easier?
3. Which is more likely: log probability -2 or -8?
4. What is log(1)? What happens at log(0)?
5. Why are logs important for LLMs?

Solutions:
1. They multiply many factors between 0 and 1.
2. log(a*b)=log(a)+log(b).
3. -2, because it is larger and closer to zero.
4. log(1)=0; log(0) tends to negative infinity.
5. Long token-sequence products underflow, while summed logs remain manageable.
""")


def main():
    demonstrate_short_sequence(); demonstrate_underflow(); demonstrate_ranking()
    practice_questions()


if __name__=="__main__":
    main()
