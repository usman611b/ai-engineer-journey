"""
LESSON 6 - SAMPLING FROM DISTRIBUTIONS
========================================================================

Core idea:

    A probability distribution describes what can happen and how likely each
    possibility is. Sampling converts that uncertainty into one actual outcome.

Run with:

    python 16_sampling_from_distributions.py


===============================================================================
1. DISTRIBUTION VERSUS SAMPLE
===============================================================================

Distribution:

    cat=0.70, dog=0.20, bird=0.10

One sample might be cat. The next could be dog. The distribution stays the same,
but random outcomes vary. Over many draws, frequencies approach probabilities.


===============================================================================
2. BERNOULLI SAMPLING
===============================================================================

Roadmap:

    def sample_bernoulli(p,n=1):
        return [1 if random.random()<p else 0 for _ in range(n)]

For p=0.8, split Uniform(0,1):

    0.0 -------------------------------- 0.8 -------- 1.0
               outcome 1                    outcome 0

If r=0.42, r<p, so return 1. If r=0.93, r is not below p, so return 0.
Ten draws need not contain exactly eight ones; long-run frequency approaches 0.8.


===============================================================================
3. CATEGORICAL SAMPLING
===============================================================================

Suppose:

    probs=[0.6,0.3,0.1]
    labels=[cat,dog,bird]

Build cumulative probabilities:

    first:  0.6
    second: 0.6+0.3=0.9
    third:  0.9+0.1=1.0

    cumulative=[0.6,0.9,1.0]

This makes regions:

    0.0 ---------------- 0.6 -------- 0.9 ---- 1.0
              cat              dog        bird

If r=0.72:

    0.72<=0.6? no
    0.72<=0.9? yes -> choose index 1 -> dog

If r=0.95, choose bird. Probability becomes interval length on a uniform random
number line.


===================================================================
4. ROADMAP CATEGORICAL CODE
===================================================================

    def sample_categorical(probs,n=1):
        cumulative=[]
        total=0
        for p in probs:
            total+=p
            cumulative.append(total)

        samples=[]
        for _ in range(n):
            r=random.random()
            for i,c in enumerate(cumulative):
                if r<=c:
                    samples.append(i)
                    break
        return samples

First loop builds region endpoints. Second loop draws r and finds the first
cumulative boundary containing it.


===============================================================================
5. GAUSSIAN SAMPLING WITH BOX-MULLER
===============================================================================

The roadmap may use the Box-Muller transform to turn two independent Uniform(0,1)
draws into a standard Normal sample:

    z=sqrt(-2*log(u1))*cos(2*pi*u2)

Then transform to desired mean and standard deviation:

    x=mu+sigma*z

Meaning:

    z        -> standard Normal, center 0 and spread 1
    sigma*z  -> change spread
    mu+...   -> move center

This is a beautiful example of using simple uniform randomness to sample a more
complex distribution. Python libraries already provide Gaussian sampling, but
the handwritten formula exposes the idea.


===============================================================================
6. SAMPLING VERSUS ARGMAX
===============================================================================

For A=0.45, B=0.35, C=0.20:

    argmax -> always A
    sampling -> perhaps A,B,A,C,A,B,... with A appearing most often

Argmax is deterministic. Sampling is stochastic and preserves diversity.


===============================================================================
7. LLM GENERATION
===============================================================================

    context -> token logits -> softmax distribution -> sample token
    -> append token -> new context -> repeat

Always using argmax can make text rigid or repetitive. Sampling allows different
valid continuations. Temperature, top-k, and top-p modify the distribution before
sampling; their advanced details are beyond this lesson's core roadmap.


===============================================================================
8. OTHER AI CONNECTIONS
===============================================================================

Diffusion models begin from sampled Gaussian noise and repeatedly denoise.
Dropout samples Bernoulli-like keep/drop masks. Data augmentation samples crop
positions, flips, angles, or brightness settings. Monte Carlo estimation uses
sample averages to approximate expectations that are difficult to calculate.


===============================================================================
9. RANDOM SEEDS AND REPRODUCIBILITY
===============================================================================

Python's random generator is pseudorandom. Setting the same seed reproduces the
same sequence, useful for debugging and lessons. A fixed seed does not make the
distribution non-random conceptually; it makes this particular experiment
repeatable. Security-sensitive randomness needs different tools.


===============================================================================
10. COMMON CONFUSIONS
===============================================================================

1. One sample need not be the most likely outcome.
2. Small samples need not match probabilities exactly.
3. Argmax and sampling answer different questions.
4. Cumulative probabilities create non-overlapping regions on [0,1].
5. Sampling does not change the distribution; it produces outcomes from it.

Mental model:

    mathematical uncertainty -> random draw -> one actual outcome
"""

import math
import random


def sample_bernoulli(p,n=1):
    if not 0<=p<=1 or n<1:
        raise ValueError("Use p in [0,1] and n>=1.")
    return [1 if random.random()<p else 0 for _ in range(n)]


def sample_categorical(probs,n=1):
    if any(p<0 for p in probs) or abs(sum(probs)-1)>1e-9 or n<1:
        raise ValueError("Use valid probabilities totaling 1 and n>=1.")
    cumulative=[]
    total=0
    for p in probs:
        total+=p
        cumulative.append(total)

    samples=[]
    for _ in range(n):
        r=random.random()
        for i,c in enumerate(cumulative):
            if r<=c:
                samples.append(i)
                break
    return samples


def sample_standard_normal_box_muller(n=1):
    samples=[]
    for _ in range(n):
        u1=random.random()
        u2=random.random()
        z=math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2)
        samples.append(z)
    return samples


def sample_normal(mu,sigma,n=1):
    if sigma<=0:
        raise ValueError("sigma must be positive.")
    return [mu+sigma*z for z in sample_standard_normal_box_muller(n)]


def demonstrate_bernoulli():
    print("\n"+"="*78)
    print("DEMO 1 - BERNOULLI SAMPLING")
    print("="*78)
    random.seed(16)
    ten=sample_bernoulli(0.8,10)
    many=sample_bernoulli(0.8,100_000)
    print("Ten outcomes:",ten)
    print("Long-run fraction of ones:",round(sum(many)/len(many),4),"theory=0.8")


def demonstrate_categorical_dry_run():
    print("\n"+"="*78)
    print("DEMO 2 - CATEGORICAL REGIONS")
    print("="*78)
    probs=[0.6,0.3,0.1]
    cumulative=[]; total=0
    for p in probs:
        total+=p; cumulative.append(total)
    print("probs=",probs)
    print("cumulative=",cumulative)
    for r in (0.22,0.81,0.55,0.97):
        for i,c in enumerate(cumulative):
            if r<=c:
                print(f"r={r} -> first boundary >=r is {c} -> index {i}")
                break


def demonstrate_categorical_frequencies():
    print("\n"+"="*78)
    print("DEMO 3 - MANY CATEGORICAL SAMPLES")
    print("="*78)
    random.seed(17)
    labels=["cat","dog","bird"]; probs=[0.6,0.3,0.1]
    samples=sample_categorical(probs,100_000)
    for i,label in enumerate(labels):
        print(f"{label}: observed={samples.count(i)/len(samples):.3f}, theory={probs[i]:.3f}")


def demonstrate_gaussian():
    print("\n"+"="*78)
    print("DEMO 4 - BOX-MULLER GAUSSIAN SAMPLES")
    print("="*78)
    random.seed(18)
    samples=sample_normal(10,2,100_000)
    mean=sum(samples)/len(samples)
    variance=sum((x-mean)**2 for x in samples)/len(samples)
    print("First five:",[round(x,3) for x in samples[:5]])
    print(f"Observed mean={mean:.3f}, target mu=10")
    print(f"Observed SD={variance**0.5:.3f}, target sigma=2")


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. What is the difference between a distribution and one sample?
2. Why does r<p correctly sample Bernoulli(p)?
3. Build cumulative probabilities for [0.5,0.3,0.2].
4. What class does r=0.72 select from those cumulative regions?
5. Why might an LLM sample instead of always using argmax?

Solutions:
1. A distribution lists likelihoods; a sample is one realized outcome.
2. The interval below p occupies fraction p of Uniform(0,1).
3. [0.5,0.8,1.0].
4. Index 1, because 0.5<0.72<=0.8.
5. Sampling permits varied valid continuations and avoids rigid determinism.
""")


def main():
    demonstrate_bernoulli(); demonstrate_categorical_dry_run()
    demonstrate_categorical_frequencies(); demonstrate_gaussian(); practice_questions()


if __name__=="__main__":
    main()
