"""
LESSON 6 - CATEGORICAL DISTRIBUTION
===================================

HOW TO STUDY THIS FILE
----------------------
Read this file from top to bottom before running it. Try to calculate every
example yourself, then run:

    python 05_categorical_distribution.py

This lesson follows the original roadmap code:

    def categorical_pmf(k, probs):
        return probs[k]

The code is simple because the important work is understanding what the list of
probabilities means.


===============================================================================
1. START FROM WHAT WE ALREADY KNOW: BERNOULLI
===============================================================================

Bernoulli models one uncertain choice with only two outcomes:

    spam / not spam
    yes / no
    1 / 0

It needs one probability p:

    P(X=1) = p
    P(X=0) = 1-p

But many AI problems have more than two possible answers:

    cat / dog / bird
    red / green / blue
    happy / sad / angry / neutral
    token 0 / token 1 / ... / token 49,999

Bernoulli cannot directly represent all these choices with one p.

This is the problem solved by the Categorical distribution.

Core intuition:

    A Categorical distribution models ONE uncertain choice from MANY discrete
    categories.


===============================================================================
2. ONE OUTCOME FROM MANY OPTIONS
===============================================================================

Suppose an image classifier sees one image. Its possible classes are:

    cat
    dog
    bird

Define the random variable:

    X belongs to {cat, dog, bird}

The model might assign:

    P(X=cat)  = 0.70
    P(X=dog)  = 0.20
    P(X=bird) = 0.10

These probabilities form one Categorical distribution.

Why?

    - The outcomes are discrete: cat, dog, or bird.
    - There are more than two outcomes.
    - Exactly one category is the outcome of this trial.
    - Every category has a probability.
    - The probabilities add to 1.

Check:

    0.70 + 0.20 + 0.10 = 1.00

The final outcome could be cat, dog, or bird. The distribution describes the
uncertainty before that outcome is selected or observed.


===============================================================================
3. THE PROBABILITY VECTOR
===============================================================================

Bernoulli uses one parameter p because the other probability must be 1-p.

Categorical uses a list (or vector) of probabilities:

    probs = [p_0, p_1, p_2, ..., p_(K-1)]

Here K means the number of categories.

For cat, dog, bird:

    labels = ["cat", "dog", "bird"]
    probs  = [ 0.70,  0.20,  0.10]

The positions connect labels to probabilities:

    index 0 -> cat  -> probability 0.70
    index 1 -> dog  -> probability 0.20
    index 2 -> bird -> probability 0.10

This alignment is essential. The number 0.20 has no class meaning by itself.
It means "dog probability" only because dog is at the same index.

Rules for a valid probability vector:

    1. Every p_i must be between 0 and 1.
    2. No probability can be negative.
    3. All probabilities must add to 1.

In symbols:

    0 <= p_i <= 1
    sum of all p_i = 1

Intuition: imagine exactly 100 probability coins:

    cat  receives 70 coins
    dog  receives 20 coins
    bird receives 10 coins

All 100 coins must be distributed among the available possibilities.


===============================================================================
4. WHY CATEGORICAL USES A PMF
===============================================================================

The possible outcomes are discrete. We can list them or assign each one an
integer index. Therefore Categorical uses a Probability Mass Function (PMF).

The PMF asks:

    What probability mass belongs to category k?

If categories are represented by indices, the rule is:

    P(X=k) = p_k

That simply means:

    probability of category k = probability stored at position k

The roadmap code is:

    def categorical_pmf(k, probs):
        return probs[k]

It is short because the distribution is already stored in ``probs``. The PMF
only looks up the requested category's probability.


===============================================================================
5. HAND DRY-RUN OF THE ROADMAP CODE
===============================================================================

Let:

    labels = ["cat", "dog", "bird"]
    probs  = [0.7, 0.2, 0.1]

Example A:

    categorical_pmf(0, probs)

Dry-run:

    k = 0
    probs[k] = probs[0]
    probs[0] = 0.7

Therefore:

    P(X=cat) = 0.7

Example B:

    categorical_pmf(2, probs)

Dry-run:

    k = 2
    probs[k] = probs[2]
    probs[2] = 0.1

Therefore:

    P(X=bird) = 0.1

Example C:

    categorical_pmf(1, probs)

Dry-run:

    k = 1
    probs[1] = 0.2

Therefore:

    P(X=dog) = 0.2

Complete PMF table:

    k       label       P(X=k)
    0       cat          0.70
    1       dog          0.20
    2       bird         0.10


===============================================================================
6. WHY DO THE PROBABILITIES HAVE TO SUM TO 1?
===============================================================================

The list represents all possible outcomes. One of those outcomes must contain
the result, so total belief across them must be 100%:

    P(cat or dog or bird) = 1

Because these categories are mutually exclusive for one single-label trial,
their probability masses add:

    P(cat) + P(dog) + P(bird) = 1

Valid:

    [0.60, 0.30, 0.10] -> total 1.00

Invalid:

    [0.60, 0.30, 0.40] -> total 1.30

That invalid vector claims to distribute 130% belief.

Also invalid:

    [0.80, 0.40, -0.20]

It happens to sum to 1, but negative probability has no valid meaning here.


===============================================================================
7. CATEGORICAL DESCRIBES ONE DRAW
===============================================================================

This distinction is important.

Categorical describes ONE multi-class trial:

    What class is this one image?
    What is the next one token?
    Which one action will the agent choose?

If we repeat the same Categorical experiment many times and count how often
each class appears, that leads to the Multinomial distribution.

Relationship map:

    one binary trial          -> Bernoulli
    many binary trials        -> Binomial
    one multi-category trial  -> Categorical
    many multi-category trials-> Multinomial

You do not need Multinomial code now. This map only prevents the distributions
from becoming mixed together in your mind.


===============================================================================
8. BERNOULLI VS CATEGORICAL
===============================================================================

Bernoulli:

    number of outcomes: 2
    example: spam / not spam
    parameter: one number p
    probabilities: [1-p, p]
    one trial

Categorical:

    number of outcomes: 2 or more, usually discussed for many classes
    example: cat / dog / bird
    parameters: list [p_0, p_1, ..., p_(K-1)]
    probabilities add to 1
    one trial

A Bernoulli distribution can be viewed as the special two-class case, while
Categorical is the general one-of-many idea.


===============================================================================
9. ONE-HOT ENCODING IS NOT THE DISTRIBUTION
===============================================================================

Suppose the observed correct class is dog.

Using label order:

    [cat, dog, bird]

the one-hot target is:

    [0, 1, 0]

This means dog is the observed class. It is a target representation.

The model's predicted Categorical distribution might be:

    [0.20, 0.70, 0.10]

These two vectors play different roles:

    [0, 1, 0]       -> which class was actually observed
    [0.2, 0.7, 0.1] -> model's uncertainty over possible classes

Later, cross-entropy compares the target with the predicted distribution.


===============================================================================
10. AI CONNECTION: IMAGE CLASSIFICATION
===============================================================================

An image classifier follows this conceptual flow:

    image
      |
      v
    neural network
      |
      v
    raw scores called logits
      |
      v
    softmax
      |
      v
    [0.70, 0.20, 0.10]
      |
      v
    Categorical distribution over cat/dog/bird

The output says how the model divides its belief among the possible classes.

Important: a softmax value of 0.70 is the model's assigned probability mass. It
does not guarantee that the model is perfectly calibrated or objectively 70%
certain. Models can be confidently wrong.


===============================================================================
11. AI CONNECTION: LANGUAGE MODELS
===============================================================================

An LLM must choose one next token from a vocabulary that may contain tens of
thousands of tokens.

Given the context:

    "The capital of France is"

the model may produce probabilities such as:

    P("Paris")  = 0.72
    P("Lyon")   = 0.05
    P("London") = 0.02
    ... probabilities for every other token ...

This is a Categorical distribution over the vocabulary.

Conceptual generation loop:

    current text
        -> model produces next-token Categorical distribution
        -> select/sample one token
        -> append token to text
        -> repeat

The separate sampling lesson explains how one actual token is drawn from these
probabilities. For now, the key idea is that the probability list itself is a
Categorical distribution.


===============================================================================
12. WHY SOFTMAX IS THE BRIDGE
===============================================================================

A neural network may output raw scores:

    cat  = 2.4
    dog  = 1.2
    bird = -0.3

These are logits, not probabilities:

    - one score is negative
    - the values do not add to 1

Softmax transforms them into something like:

    cat  = 0.73
    dog  = 0.22
    bird = 0.05

Now every value is nonnegative and the total is 1. The result is a valid
Categorical distribution.

Do not jump ahead and memorize softmax here. Its own lesson will build it by
hand. Just remember:

    raw model scores -> softmax -> Categorical probabilities


===============================================================================
13. PROBABILITY, ARGMAX, AND SAMPLING ARE DIFFERENT
===============================================================================

Suppose:

    cat  = 0.60
    dog  = 0.30
    bird = 0.10

The distribution is the full list of beliefs.

Argmax chooses the largest probability:

    cat

Sampling draws randomly according to the probabilities, so cat appears most
often, dog sometimes, and bird rarely.

These answer different questions:

    distribution -> How likely is each possibility?
    argmax        -> Which possibility has the greatest probability?
    sampling      -> Draw one outcome while respecting the probabilities.

Sampling gets its own detailed roadmap file later.


===============================================================================
14. COMMON CONFUSIONS
===============================================================================

1. "Categorical means the probabilities themselves are categories."
   No. Categories are outcomes; probabilities describe belief in them.

2. "The largest class must have probability 1."
   No. The model may prefer cat at 0.60 while keeping uncertainty for dog/bird.

3. "Categorical describes many draws."
   No. It describes one draw. Repeated category counts are Multinomial-style.

4. "The indexes are the real category meanings."
   No. Index 0 means cat only because we defined labels[0] as cat.

5. "Any list that sums to 1 is valid."
   No. Every entry must also be nonnegative.

6. "One-hot target and predicted distribution are the same."
   No. One-hot records an observed class; predicted probabilities express model
   uncertainty.

7. "Categorical is only for exactly three classes."
   No. It can represent any finite number K of discrete categories.


===============================================================================
15. FINAL MENTAL MODEL
===============================================================================

    ONE uncertain choice
            |
            v
    MANY discrete categories
            |
            v
    [p_0, p_1, ..., p_(K-1)]
            |
            v
    each p_i >= 0 and all sum to 1
            |
            v
    PMF(k) returns p_k

In AI:

    neural network -> logits -> softmax -> Categorical distribution

One-sentence explanation:

    A Categorical distribution models one uncertain choice among multiple
    discrete outcomes, assigning each category a nonnegative probability so
    that all probabilities sum to one; image-class probabilities and LLM
    next-token probabilities are important AI examples.
"""


def validate_probabilities(probs):
    """Check the two basic rules for a Categorical probability vector."""
    if len(probs) == 0:
        raise ValueError("The probability list cannot be empty.")

    for probability in probs:
        if probability < 0 or probability > 1:
            raise ValueError("Each probability must be between 0 and 1.")

    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("Categorical probabilities must add to 1.")


def categorical_pmf(k, probs):
    """Return P(X=k) using the Lesson 6 roadmap's list lookup."""
    validate_probabilities(probs)

    if k < 0 or k >= len(probs):
        raise ValueError("Category index k is outside the probability list.")

    # The central roadmap line:
    return probs[k]


def category_probability(label, labels, probs):
    """Connect a readable label to its index and then use the roadmap PMF."""
    if len(labels) != len(probs):
        raise ValueError("Every label needs exactly one probability.")
    if label not in labels:
        raise ValueError("The requested label is not in labels.")

    k = labels.index(label)
    return categorical_pmf(k, probs)


def one_hot(category_index, number_of_categories):
    """Represent one observed category using one 1 and all other entries 0."""
    if category_index < 0 or category_index >= number_of_categories:
        raise ValueError("Category index is outside the valid range.")

    return [
        1 if i == category_index else 0
        for i in range(number_of_categories)
    ]


def argmax_index(probs):
    """Return the index with the largest probability, written without libraries."""
    validate_probabilities(probs)

    largest_index = 0

    for i in range(1, len(probs)):
        if probs[i] > probs[largest_index]:
            largest_index = i

    return largest_index


def demonstrate_probability_vector():
    print("\n" + "=" * 78)
    print("DEMO 1 - THE PROBABILITY VECTOR")
    print("=" * 78)

    labels = ["cat", "dog", "bird"]
    probs = [0.7, 0.2, 0.1]

    print("labels =", labels)
    print("probs  =", probs)
    print("total  =", sum(probs))
    print("total  =", round(sum(probs), 10))

    for i in range(len(labels)):
        print(f"index {i} connects {labels[i]!r} to probability {probs[i]}")


def demonstrate_pmf_dry_run():
    print("\n" + "=" * 78)
    print("DEMO 2 - ROADMAP PMF DRY-RUN")
    print("=" * 78)

    labels = ["cat", "dog", "bird"]
    probs = [0.7, 0.2, 0.1]

    for k in range(len(probs)):
        print(f"k={k}: probs[{k}]={categorical_pmf(k, probs)} -> P({labels[k]})")

    print("\nDirect example:")
    print("categorical_pmf(2, [0.7, 0.2, 0.1])")
    print("-> return probs[2]")
    print("-> return", categorical_pmf(2, probs))
    print("-> P(bird)=0.1")


def demonstrate_label_lookup():
    print("\n" + "=" * 78)
    print("DEMO 3 - CONNECT LABELS TO INDEXES")
    print("=" * 78)

    labels = ["cat", "dog", "bird"]
    probs = [0.7, 0.2, 0.1]

    for label in labels:
        probability = category_probability(label, labels, probs)
        print(f"P(X={label}) = {probability}")


def demonstrate_one_hot():
    print("\n" + "=" * 78)
    print("DEMO 4 - TARGET VS PREDICTED DISTRIBUTION")
    print("=" * 78)

    labels = ["cat", "dog", "bird"]
    correct_index = 1
    predicted_probs = [0.2, 0.7, 0.1]

    print("Label order:            ", labels)
    print("Observed target (dog):  ", one_hot(correct_index, len(labels)))
    print("Predicted probabilities:", predicted_probs)
    print("The target identifies truth; probabilities represent model uncertainty.")


def demonstrate_argmax():
    print("\n" + "=" * 78)
    print("DEMO 5 - DISTRIBUTION VS ARGMAX")
    print("=" * 78)

    labels = ["cat", "dog", "bird"]
    probs = [0.6, 0.3, 0.1]
    best_index = argmax_index(probs)

    print("Full Categorical distribution:", dict(zip(labels, probs)))
    print("Largest probability index:", best_index)
    print("Argmax class:", labels[best_index])
    print("Argmax selects one class; it does not replace the full distribution.")


def practice_questions():
    print("\n" + "=" * 78)
    print("PRACTICE - ANSWER BEFORE READING THE SOLUTIONS")
    print("=" * 78)
    print("""
1. Is [0.5, 0.3, 0.2] a valid Categorical probability vector? Why?
2. Is [0.8, 0.4, -0.2] valid even though it sums to 1? Why not?
3. With labels [red, green, blue] and probs [0.1, 0.6, 0.3], what is PMF(1)?
4. Is predicting one next LLM token Bernoulli or Categorical?
5. What is the difference between [0,1,0] and [0.2,0.7,0.1]?
6. Does Categorical describe one draw or counts from many draws?
7. What turns neural-network logits into Categorical probabilities?

Solutions:
1. Yes. Every value is nonnegative and the total is 1.
2. No. A probability cannot be negative.
3. PMF(1)=0.6, which is the probability of green.
4. Categorical: one token is chosen from many vocabulary options.
5. [0,1,0] is a one-hot observed target; the other is predicted uncertainty.
6. One draw. Repeated category counts lead to Multinomial-style modeling.
7. Softmax. Its detailed calculation is taught in a later file.
""")


def main():
    demonstrate_probability_vector()
    demonstrate_pmf_dry_run()
    demonstrate_label_lookup()
    demonstrate_one_hot()
    demonstrate_argmax()
    practice_questions()


if __name__ == "__main__":
    main()