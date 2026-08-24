"""
DAY 21 — SESSION 12: SHARP AND FLAT MINIMA
==========================================

LEARNING GOALS
--------------
This lesson explains sensitivity around a minimum, the curvature intuition
behind sharpness and flatness, the connection to robustness and generalization,
and the important reasons that flatness is not a universal guarantee.

1. A MINIMUM IS A REGION, NOT ONLY A NUMBER
--------------------------------------------
An optimizer returns parameter values. To understand the quality of the
solution, we can ask two separate questions:

1. How low is the loss at the selected point?
2. How quickly does loss increase when parameters move slightly nearby?

Two models can have the same minimum training loss but very different answers
to the second question.

2. SHARP MINIMUM
----------------
A sharp minimum is a narrow low-loss region. Small parameter perturbations can
increase loss substantially. In a one-dimensional picture it resembles a deep,
narrow valley with steep walls.

Example centered at w=1:

    L_sharp(w) = 100*(w-1)^2

At w=1, loss is zero. At w=1.1:

    L_sharp(1.1) = 100*(0.1)^2 = 1

A parameter movement of only 0.1 creates loss 1.

3. FLAT MINIMUM
---------------
A flat minimum is a wide region where many nearby parameters keep similarly
low loss:

    L_flat(w) = 0.1*(w-1)^2

At w=1.1:

    L_flat(1.1) = 0.1*(0.1)^2 = 0.001

The same perturbation produces a loss 1,000 times smaller than in the sharp
example.

4. CURVATURE INTUITION
----------------------
The second derivative measures one-dimensional curvature:

    d^2/dw^2 [a*(w-1)^2] = 2a

For the examples:

    sharp curvature = 200
    flat curvature  = 0.2

Large positive curvature means the slope changes rapidly near the bottom.
Small positive curvature means the bottom changes gently.

For many parameters, curvature differs by direction. A minimum can be sharp in
one direction and flat in another. The Hessian's eigenvalues summarize those
principal curvature directions: large positive eigenvalues indicate sharp
directions; small eigenvalues indicate flat directions.

5. PERTURBATION TEST
--------------------
A practical thought experiment is:

    choose trained parameters w;
    add a small perturbation delta;
    compare L(w+delta) with L(w).

If many small perturbations cause large loss increases, the region is
sensitive. If loss remains similar for many perturbations, it is robust in
those tested directions.

One or two perturbations are not a proof about every high-dimensional
direction. The scale and direction of perturbations must be stated.

6. WHY FLATNESS MAY RELATE TO GENERALIZATION
---------------------------------------------
Training data is only a sample from the real data-generating process. A model
that works only at one extremely precise parameter configuration may be more
sensitive to data noise, sampling changes, quantization, or parameter noise.

A wide low-loss region contains many nearby parameter configurations with
similar training performance. This supports the intuition:

    flat region -> parameter robustness -> possibly better generalization

This is an association and useful mental model, not an absolute theorem.

7. TRAINING LOSS IS NOT TEST PERFORMANCE
----------------------------------------
Model A may achieve training loss 0.001 but test loss 0.8. Model B may achieve
training loss 0.01 but test loss 0.2. Optimization minimizes the chosen
training objective, while the real goal is performance on unseen data.

The lowest training point is therefore not automatically the best model.
Validation data, regularization, architecture, and data quality remain crucial.

8. MINI-BATCH NOISE AND VALLEY WIDTH
------------------------------------
Mini-batch gradients fluctuate because every batch contains different samples.
Noisy updates can push an optimizer out of a very narrow region. A wider region
can tolerate the same perturbation without a large loss increase.

This provides one intuition for why SGD or SGD with momentum sometimes reaches
broader solutions and stronger final test accuracy than Adam, even when Adam
reduces training loss faster. It is not guaranteed for every task.

9. PARAMETERIZATION WARNING
---------------------------
The same neural-network function can sometimes be represented by differently
scaled parameters. Rescaling one layer and inversely rescaling another may
preserve predictions while changing raw-coordinate curvature.

Consequently, a minimum may look sharp in one parameterization and flatter in
another. Meaningful sharpness comparisons should consider parameter scale and
function behavior, not only a visually narrow raw-weight plot.

10. FLAT DOES NOT MEAN ZERO GRADIENT EVERYWHERE
-----------------------------------------------
At the exact bottom of a smooth minimum, the gradient can be zero. In a broad
nearby region, gradients may be small but nonzero. Flat means loss changes
slowly; it does not require a mathematically constant loss over a whole area.

11. SHARPNESS AND LEARNING RATE
-------------------------------
Steep walls produce rapidly changing gradients. A large learning rate can jump
from one wall to the other, causing oscillation. A smaller late-stage learning
rate helps settle. Momentum can smooth consistent progress, while a schedule
can reduce update scale near the end.

12. CAREFUL CONCLUSION
----------------------
Use this statement:

    Flatness is often associated with robustness and good generalization, but
    flatness alone does not guarantee generalization.

Avoid this overstatement:

    Every flat minimum generalizes well and every sharp minimum generalizes
    poorly.
"""


def quadratic_minimum(weight, center=1.0, curvature_scale=1.0):
    """L(w)=a*(w-center)^2; the second derivative is 2a."""
    if curvature_scale < 0:
        raise ValueError("curvature_scale must be non-negative for a minimum")
    return curvature_scale * (weight - center) ** 2


def sharp_loss(weight):
    return quadratic_minimum(weight, center=1.0, curvature_scale=100.0)


def flat_loss(weight):
    return quadratic_minimum(weight, center=1.0, curvature_scale=0.1)


def perturbation_report(function, center, perturbations):
    base_loss = function(center)
    return [
        {
            "delta": delta,
            "weight": center + delta,
            "loss": function(center + delta),
            "increase": function(center + delta) - base_loss,
        }
        for delta in perturbations
    ]


def anisotropic_two_parameter_loss(params):
    """Sharp in x, flat in y: one minimum can mix both geometries."""
    x, y = params
    return 100 * (x - 1) ** 2 + 0.1 * (y - 1) ** 2


def compare_same_perturbations():
    perturbations = [-0.2, -0.1, -0.01, 0.0, 0.01, 0.1, 0.2]
    print("Perturbations around w=1")
    print("delta      sharp loss      flat loss      sharp/flat")
    for delta in perturbations:
        sharp = sharp_loss(1.0 + delta)
        flat = flat_loss(1.0 + delta)
        ratio = 0.0 if flat == 0 else sharp / flat
        print(f"{delta:+.2f}    {sharp:12.6f}   {flat:12.6f}   {ratio:10.1f}")


def compare_directions():
    center = [1.0, 1.0]
    x_perturbed = [1.1, 1.0]
    y_perturbed = [1.0, 1.1]
    print("\nOne 2D minimum, different directional curvature")
    print("center loss:       ", anisotropic_two_parameter_loss(center))
    print("x perturbation loss:", anisotropic_two_parameter_loss(x_perturbed))
    print("y perturbation loss:", anisotropic_two_parameter_loss(y_perturbed))


if __name__ == "__main__":
    assert sharp_loss(1.0) == 0.0
    assert flat_loss(1.0) == 0.0
    assert abs(sharp_loss(1.1) - 1.0) < 1e-12
    assert abs(flat_loss(1.1) - 0.001) < 1e-12
    assert abs(anisotropic_two_parameter_loss([1.1, 1.0]) - 1.0) < 1e-12

    compare_same_perturbations()
    compare_directions()

