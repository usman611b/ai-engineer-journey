"""
LESSON 7.4 — WHY BAYES' FORMULA IS TRUE
========================================

Bayes is not a magic formula. The joint event "A and red" can be written in
two directions:

    P(A and red) = P(A)P(red | A)
    P(A and red) = P(red)P(A | red)

Because both describe the same overlap:

    P(A)P(red | A) = P(red)P(A | red)

Divide both sides by P(red):

    P(A | red) = P(red | A)P(A) / P(red)

The numerator is the route of interest: A selected and red observed. The
denominator is every route capable of producing red. Dividing asks: among all
red cases, what fraction came from A?

LAW OF TOTAL PROBABILITY
When A and B are mutually exclusive and cover all possibilities:

    P(red) = P(red|A)P(A) + P(red|B)P(B)

Thus the expanded binary formula is:

    P(A|red) = P(red|A)P(A) /
               [P(red|A)P(A) + P(red|B)P(B)]

WHY NORMALIZATION IS REQUIRED
Likelihood*prior produces an unnormalized joint score. The denominator rescales
all hypothesis scores so they sum to one and can be interpreted as posterior
probabilities.
"""


def bayes_binary(prior_h, likelihood_e_given_h, likelihood_e_given_not_h):
    prior_not_h = 1 - prior_h
    route_h = prior_h * likelihood_e_given_h
    route_not_h = prior_not_h * likelihood_e_given_not_h
    evidence = route_h + route_not_h
    return route_h / evidence


if __name__ == "__main__":
    answer = bayes_binary(0.5, 0.9, 0.2)
    print(f"P(A | red) = {answer:.4f} = {answer:.2%}")

