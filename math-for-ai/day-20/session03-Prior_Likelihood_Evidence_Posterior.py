"""
LESSON 7.3 — THE FOUR COMPONENTS OF BAYES
==========================================

HYPOTHESIS: Bag A was selected. EVIDENCE: a red ball was observed.

1. PRIOR, P(A)
   Belief before the new observation. Here P(A)=0.5. In spam filtering,
   P(spam) might be the historical fraction of incoming emails that are spam.

2. LIKELIHOOD, P(red | A)
   If A really were selected, how likely would this evidence be? Here it is
   0.9. A likelihood evaluates evidence under an assumed hypothesis; it is not
   yet the probability that the hypothesis is true.

3. EVIDENCE (MARGINAL LIKELIHOOD), P(red)
   Overall probability of seeing red through every possible explanation:
   P(red)=P(red|A)P(A)+P(red|B)P(B)=0.55. It normalizes competing routes.

4. POSTERIOR, P(A | red)
   Updated belief after observing red: 0.8182.

LIKELIHOOD RATIO
Evidence is informative when competing hypotheses predict it differently:

    P(red|A)/P(red|B) = 0.9/0.2 = 4.5

Red is 4.5 times as likely under A. If a symptom occurs in 80% of sick people
and 80% of healthy people, its likelihood ratio is 1. It cannot distinguish
the groups and should not change our odds.

MEMORY AID
Prior = before. Likelihood = evidence expected under hypothesis.
Evidence = all routes to observation. Posterior = after.
"""


def bayes_components():
    prior = 0.5
    likelihood = 0.9
    evidence = 0.9 * 0.5 + 0.2 * 0.5
    posterior = likelihood * prior / evidence
    return prior, likelihood, evidence, posterior


if __name__ == "__main__":
    names = ("prior", "likelihood", "evidence", "posterior")
    for name, value in zip(names, bayes_components()):
        print(f"{name:10s}: {value:.4f}")

