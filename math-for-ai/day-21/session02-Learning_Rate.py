"""
DAY 21 — SESSION 02: LEARNING RATE
==================================

1. DEFINITION AND PURPOSE
-------------------------
The learning rate (lr or eta) controls how strongly the optimizer responds to
a gradient:

    w_new = w_old - lr * gradient

The gradient provides direction and steepness. The learning rate converts that
information into an actual step size. It is a hyperparameter: training does not
normally learn it automatically; we choose or schedule it.

2. SAME GRADIENT, DIFFERENT STEP SIZES
--------------------------------------
Let w=5 and gradient=10.

    lr=0.01: w_new = 5 - 0.01(10) = 4.9   (safe but tiny)
    lr=0.10: w_new = 5 - 0.10(10) = 4.0   (useful progress)
    lr=0.90: w_new = 5 - 0.90(10) = -4.0  (crosses the minimum)

Crossing the minimum once is called overshooting, but it is not automatically
failure. With L(w)=w^2, loss still falls from 25 to 16 at w=-4. Failure occurs
when repeated overshooting moves farther away and loss grows.

3. TOO SMALL, SUITABLE, AND TOO LARGE
-------------------------------------
Too small:
    * updates are tiny;
    * loss may decrease, but training wastes time and compute.

Suitable:
    * loss generally decreases;
    * progress is fast enough while updates remain controlled.

Too large:
    * parameters bounce across a valley;
    * oscillations may grow;
    * loss may explode or become NaN (divergence).

4. EXACT ANALYSIS FOR L(w)=w^2
-------------------------------
Because gradient=2w:

    w_new = w - lr(2w)
          = (1 - 2lr)w

The multiplier (1-2lr) reveals the behavior:

* 0 < lr < 0.5: multiplier is between 0 and 1; approach zero from one side.
* lr = 0.5: multiplier is 0; reach zero in exactly one update.
* 0.5 < lr < 1: multiplier is between -1 and 0; cross sides but shrink.
* lr = 1: multiplier is -1; bounce 5,-5,5,-5 with constant loss.
* lr > 1: multiplier magnitude exceeds 1; oscillations grow and diverge.

Example with lr=1.1:

    5 -> -6 -> 7.2 -> -8.64 -> ...
    25 -> 36 -> 51.84 -> 74.6496 -> ...

This boundary belongs to this particular quadratic. Real neural-network losses
have different curvature in different directions, so there is no universal
perfect learning rate.

5. WHY STEEP CURVATURE REQUIRES CAUTION
---------------------------------------
Consider L(w)=100w^2. Its gradient is 200w, one hundred times steeper than the
gradient of w^2. An lr safe for w^2 may be far too large here. Neural networks
contain many directions with different curvature, making one fixed lr a
compromise.

6. PRACTICAL DIAGNOSIS
----------------------
Likely too large: loss jumps upward, oscillates violently, becomes infinity or
NaN, or gradients/weights explode.

Likely too small: loss decreases extremely slowly, training appears nearly
frozen despite nonzero gradients, or far too many epochs are required.

Common starting points—not guarantees—are Adam lr=0.001 and SGD+momentum
lr=0.01. Experiments, validation curves, and schedules are used to tune them.
"""


def quadratic_loss(weight):
    return weight ** 2


def run(start, learning_rate, steps=10):
    weight = float(start)
    history = []
    for step in range(steps + 1):
        history.append((step, weight, quadratic_loss(weight)))
        weight -= learning_rate * (2 * weight)
    return history


def compare_rates(rates=(0.01, 0.1, 0.5, 0.9, 1.0, 1.1)):
    for learning_rate in rates:
        history = run(5.0, learning_rate, steps=6)
        weights = " -> ".join(f"{w:.3f}" for _, w, _ in history)
        losses = " -> ".join(f"{value:.3f}" for _, _, value in history)
        print(f"\nlr={learning_rate}")
        print("weights:", weights)
        print("losses: ", losses)


if __name__ == "__main__":
    compare_rates()

