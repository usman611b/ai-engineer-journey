"""
LESSON 7.8 — HOW NAIVE BAYES LEARNS FROM TRAINING DATA
======================================================

Training emails:
    spam: "free prize", "free winner", "prize winner"
    ham:  "team meeting", "project meeting", "free meeting"

CLASS PRIORS
Three of six emails are spam, so P(spam)=3/6=0.5. The same holds for ham.

BERNOULLI WORD LIKELIHOODS
This version asks whether a word is present, not how many times it occurs.
"free" occurs in two of three spam documents:

    P(free|spam)=2/3

It occurs in one of three ham documents:

    P(free|ham)=1/3

This is an MLE count: matching class documents divided by all documents in the
class. In Multinomial Naive Bayes, repeated word tokens are counted instead;
the model choice changes the denominator and interpretation.

TRAINING VERSUS PREDICTION
Training estimates priors and likelihoods from labeled examples. Prediction
combines those learned values for a new email and chooses the largest posterior
score.

LIMIT OF SMALL DATA
"meeting" occurs in zero spam examples, which gives 0/3. That does not prove it
can never appear in spam. It reveals uncertainty caused by limited training
data and motivates smoothing.
"""


def bernoulli_likelihood(word, documents):
    present = sum(word in document.split() for document in documents)
    return present / len(documents)


if __name__ == "__main__":
    spam = ["free prize", "free winner", "prize winner"]
    ham = ["team meeting", "project meeting", "free meeting"]
    for word in ("free", "meeting"):
        print(f"P({word}|spam) = {bernoulli_likelihood(word, spam):.3f}")
        print(f"P({word}|ham)  = {bernoulli_likelihood(word, ham):.3f}")

