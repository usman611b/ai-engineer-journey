"""
LESSON 7.12 — MAXIMUM A POSTERIORI (MAP)
=========================================

WHY MAP EXISTS
MLE may be extreme with small datasets. MAP combines observed data with prior
knowledge and chooses the single parameter value having the highest posterior:

    theta_MAP = argmax_theta P(theta | data)
              = argmax_theta P(data | theta)P(theta)

P(data) is omitted in argmax because it is constant while candidate theta
values are compared.

INTUITION
Prior: parameter values believed plausible before current data.
Likelihood: how well each value explains current data.
Posterior: updated plausibility after combining both.
MAP chooses the peak/mode of that posterior.

IMAGINARY-COUNT INTUITION
A fair-coin prior can behave like earlier balanced evidence. We used two prior
heads and two prior tails only as an example of prior strength—not a universal
rule. One and one would be a weaker balanced prior; 100 and 100 would be much
stronger. Larger prior counts resist movement from a small amount of new data.

For 800 real heads and 200 tails plus prior 2H,2T, combined counts are 802H and
202T, total 1004. The quantity 802/1004 is the POSTERIOR MEAN under the
corresponding Beta-count interpretation, not the exact MAP. The earlier phrase
"MAP-like" deliberately described intuition; precise formulas differ.

BETA PRIOR PRECISION
If theta ~ Beta(alpha,beta) and data has H heads and T tails, posterior is:

    Beta(alpha+H, beta+T)

Posterior mean:
    (alpha+H)/(alpha+beta+H+T)

Exact MAP when updated parameters are both >1:
    (alpha+H-1)/(alpha+beta+H+T-2)

Example Beta(2,2), H=7,T=3:
    MLE = 7/10 = 0.700
    posterior = Beta(9,5)
    posterior mean = 9/14 = 0.643
    MAP = (9-1)/(9+5-2) = 8/12 = 0.667

WHY MLE AND MAP CONVERGE
As data becomes huge, the likelihood overwhelms a fixed prior, so their
estimates become similar.

REGULARIZATION CONNECTION
MAP with a Gaussian prior favoring small weights corresponds to L2
regularization; a Laplace prior corresponds to L1. Data loss asks the model to
fit observations, while the prior penalty discourages implausible parameters.

SHORTEST SUMMARY
MLE: fit observed data. MAP: fit observed data while respecting a prior.
"""


def beta_posterior(alpha, beta, heads, tails):
    return alpha + heads, beta + tails


def beta_mean(alpha, beta):
    return alpha / (alpha + beta)


def beta_map(alpha, beta):
    if alpha <= 1 or beta <= 1:
        raise ValueError("This simple interior-mode formula requires alpha,beta > 1")
    return (alpha - 1) / (alpha + beta - 2)


if __name__ == "__main__":
    posterior_alpha, posterior_beta = beta_posterior(2, 2, 7, 3)
    mle = 7 / 10
    mean = beta_mean(posterior_alpha, posterior_beta)
    map_estimate = beta_map(posterior_alpha, posterior_beta)
    print(f"Posterior: Beta({posterior_alpha}, {posterior_beta})")
    print(f"MLE:            {mle:.3f}")
    print(f"Posterior mean: {mean:.3f}")
    print(f"MAP:            {map_estimate:.3f}")
