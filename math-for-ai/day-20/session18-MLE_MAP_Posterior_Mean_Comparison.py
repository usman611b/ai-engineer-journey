"""
DAY 20 — SESSION 18: MLE, MAP, AND POSTERIOR MEAN
=================================================

These three estimates summarize different information.

MLE uses data only:

    successes/(successes+failures)

MAP uses prior and data, then chooses the posterior's highest point. For a Beta
posterior with alpha>1 and beta>1:

    (alpha-1)/(alpha+beta-2)

Posterior mean also uses prior and data but averages all theta values according
to posterior density:

    alpha/(alpha+beta)

For prior Beta(2,2) and data 7 successes,3 failures:

    posterior Beta(9,5)
    MLE            = 7/10  = 0.700
    MAP            = 8/12  = 0.667
    posterior mean = 9/14  = 0.643

Mountain intuition: full posterior is the entire mountain, MAP is its highest
point, and posterior mean is its balance point. MLE is the peak produced by the
likelihood without multiplying by the prior.

With huge data, MLE and MAP usually become close because the fixed prior is
small relative to accumulated likelihood evidence. A uniform prior also makes
MAP and MLE share the same winner.

Boundary warning: when updated alpha or beta is <=1, the Beta mode may lie on a
boundary and the simple interior MAP formula should not be used blindly.
"""


def mle(successes, failures):
    total = successes + failures
    if total == 0:
        raise ValueError("MLE requires observations")
    return successes / total


def posterior_parameters(prior_alpha, prior_beta, successes, failures):
    return prior_alpha + successes, prior_beta + failures


def posterior_mean(alpha, beta):
    return alpha / (alpha + beta)


def map_estimate(alpha, beta):
    if alpha <= 1 or beta <= 1:
        raise ValueError("Interior Beta MAP formula requires alpha,beta > 1")
    return (alpha - 1) / (alpha + beta - 2)


def compare(prior_alpha, prior_beta, successes, failures):
    alpha, beta = posterior_parameters(
        prior_alpha, prior_beta, successes, failures
    )
    return {
        "posterior": (alpha, beta),
        "mle": mle(successes, failures),
        "map": map_estimate(alpha, beta),
        "posterior_mean": posterior_mean(alpha, beta),
    }


if __name__ == "__main__":
    result = compare(2, 2, 7, 3)
    print(f"Posterior: Beta{result['posterior']}")
    print(f"MLE:            {result['mle']:.3f}")
    print(f"MAP:            {result['map']:.3f}")
    print(f"Posterior mean: {result['posterior_mean']:.3f}")

