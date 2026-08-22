"""
LESSON 7.7 — NAIVE BAYES FOR CLASSIFICATION
============================================

GOAL
Given the words "free prize," compare P(spam|words) with P(ham|words). Ham means
legitimate email.

Assume P(spam)=0.4 and P(ham)=0.6. Learned word likelihoods are:

    P(free|spam)=0.7,  P(prize|spam)=0.6
    P(free|ham)=0.1,   P(prize|ham)=0.05

UNNORMALIZED CLASS SCORES
    spam score = 0.4*0.7*0.6  = 0.168
    ham score  = 0.6*0.1*0.05 = 0.003

Normalize by their sum, 0.171:
    P(spam|words)=0.168/0.171=98.25%

WHY "NAIVE"?
Given the class, it treats features as conditionally independent:

    P(free, prize | spam)
      approximately P(free|spam)P(prize|spam)

Real words are related, so the assumption is simplified. Yet it reduces an
otherwise difficult joint probability to easy counts and multiplications and
often works well for text baselines.

IMPORTANT
"Free" does not guarantee spam. The classifier compares how all evidence fits
every class while including class priors.
"""


def normalize(scores):
    total = sum(scores.values())
    return {label: score / total for label, score in scores.items()}


if __name__ == "__main__":
    scores = {
        "spam": 0.4 * 0.7 * 0.6,
        "ham": 0.6 * 0.1 * 0.05,
    }
    probabilities = normalize(scores)
    print("Raw scores:", scores)
    print("Posteriors:", {k: f"{v:.2%}" for k, v in probabilities.items()})
    print("Prediction:", max(probabilities, key=probabilities.get))

