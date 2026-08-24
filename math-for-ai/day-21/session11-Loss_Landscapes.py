"""
DAY 21 — SESSION 11: LOSS LANDSCAPES
====================================

LEARNING GOALS
--------------
This file explains what a loss landscape represents, how dimensionality is
counted, what an optimization path means, how researchers form a two-direction
slice, and why that slice is useful but incomplete.

1. ONE PARAMETER: A CURVE
-------------------------
Suppose a model contains one parameter w and loss:

    L(w)=w^2

The horizontal axis is w and the vertical axis is L. Every graph point has the
form (w,L(w)). Training is a sequence of locations on this curve:

    w0 -> w1 -> w2 -> ...

2. TWO PARAMETERS: A SURFACE
----------------------------
For:

    L(w1,w2)=w1^2+w2^2

we use one axis for w1, one for w2, and a height for loss. One point such as:

    (w1,w2,L)=(2,3,13)

means the complete two-parameter model [2,3] produces loss 13.

An axis is one direction. A point is one complete parameter configuration and
its associated loss. Confusing a point with an axis loses the central idea.

3. MANY PARAMETERS
------------------
Let a model have n parameters:

    w = [w1,w2,...,wn]

Parameter space has n dimensions. The graph of scalar loss over that space is
often described as an n+1 dimensional landscape because loss supplies the
height:

    [w1,w2,...,wn,L(w)]

Thus 500 parameters form a 500-dimensional parameter space, or 501 dimensions
when representing all parameter coordinates plus loss height.

For a million-parameter network, humans cannot directly visualize the full
object. The mathematics still exists even though our visual system cannot draw
it.

4. EVERY LOCATION IS A COMPLETE MODEL
-------------------------------------
Changing one coordinate changes one weight. Changing the whole vector creates
a new parameter configuration. The architecture and code may be identical,
but different parameter vectors usually make different predictions and losses.

Training produces a trajectory:

    w_0 -> w_1 -> w_2 -> ... -> w_T

The optimizer selects each movement using gradients and its internal state.
The history list in our code is a discrete record of this trajectory.

5. FEATURES OF A LANDSCAPE
--------------------------
A non-convex landscape may include high-loss hills, low-loss valleys, local
minima, saddle points, plateaus, sharp walls, and narrow curved paths. These
are geometric metaphors for how loss changes under parameter perturbations.

Gradient: local uphill direction.
Negative gradient: local downhill direction.
Learning rate: scale of the movement.
Optimizer: rule that converts gradient information into a path.
Schedule: rule that changes overall step scale through time.

6. TWO-DIRECTION SLICES
-----------------------
Choose a reference parameter vector w and two direction vectors d1 and d2.
Evaluate:

    L(w + alpha*d1 + beta*d2)

for many alpha and beta values. alpha and beta become the two horizontal axes,
and loss becomes height. The resulting surface is a two-dimensional slice
through the high-dimensional parameter space.

Direction vectors are not individual weights. Each direction may change every
weight simultaneously. For example:

    w  = [1,2,3]
    d1 = [1,0,0]
    d2 = [0,1,1]

alpha changes the first coordinate; beta changes the second and third together.

7. WHAT A SLICE DOES NOT SHOW
-----------------------------
A two-direction slice is not the complete neural-network landscape. Different
direction choices can reveal different geometry. A valley visible in one slice
may look flat in another; a downhill direction may lie outside the selected
plane.

Therefore, landscape plots are diagnostic views, not perfect maps. Researchers
must state how directions were chosen and how parameter scales were handled.

8. CONTOUR VIEW VERSUS SURFACE VIEW
-----------------------------------
A surface plot uses height for loss. A contour plot looks from above and draws
curves connecting equal-loss points. Closely spaced contours indicate rapid
change; widely spaced contours indicate gentle change. Optimization paths are
often easier to overlay on contour plots.

9. PARAMETERIZATION WARNING
---------------------------
Neural networks can sometimes represent the same function using differently
scaled parameters. A landscape may appear sharper after reparameterization even
when predictions are unchanged. Geometry in raw parameter coordinates must be
interpreted carefully.

10. WHY SAVE HISTORY?
---------------------
Final loss tells us where an optimizer ended. History tells us how it arrived:
whether it oscillated, stalled, overshot, or moved smoothly. Comparing only the
final point can hide important differences in efficiency and stability.
"""


def dot(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have equal lengths")
    return sum(a * b for a, b in zip(left, right))


def add_scaled(base, direction1, alpha, direction2, beta):
    """Return w + alpha*d1 + beta*d2."""
    if not (len(base) == len(direction1) == len(direction2)):
        raise ValueError("all vectors must have equal lengths")
    return [
        w + alpha * d1 + beta * d2
        for w, d1, d2 in zip(base, direction1, direction2)
    ]


def high_dimensional_quadratic(params):
    """Simple loss L(w)=sum(w_i^2), valid for any parameter count."""
    return dot(params, params)


def landscape_slice(loss_function, center, direction1, direction2, values):
    """Evaluate a square alpha-beta grid and return explicit records."""
    records = []
    for alpha in values:
        for beta in values:
            params = add_scaled(center, direction1, alpha, direction2, beta)
            records.append(
                {
                    "alpha": alpha,
                    "beta": beta,
                    "params": params,
                    "loss": loss_function(params),
                }
            )
    return records


def gradient_of_quadratic(params):
    return [2 * value for value in params]


def optimize_quadratic(start, lr=0.1, steps=5):
    """Save the complete parameter-space path for a simple loss."""
    params = list(start)
    history = []
    for step in range(steps + 1):
        history.append(
            {
                "step": step,
                "params": params[:],
                "loss": high_dimensional_quadratic(params),
            }
        )
        if step < steps:
            grads = gradient_of_quadratic(params)
            params = [p - lr * g for p, g in zip(params, grads)]
    return history


def print_slice_example():
    center = [1.0, 2.0, 3.0]
    direction1 = [1.0, 0.0, 0.0]
    direction2 = [0.0, 1.0, 1.0]
    values = [-1.0, 0.0, 1.0]

    print("Two-direction slice through a 3-parameter loss")
    print("center:", center)
    for record in landscape_slice(
        high_dimensional_quadratic,
        center,
        direction1,
        direction2,
        values,
    ):
        print(
            f"alpha={record['alpha']:+.1f} beta={record['beta']:+.1f} "
            f"params={record['params']} loss={record['loss']:.2f}"
        )


def print_trajectory_example():
    print("\nOptimization trajectory in 3D parameter space")
    for record in optimize_quadratic([2.0, -1.0, 3.0], lr=0.1, steps=5):
        print(
            f"step={record['step']} params={record['params']} "
            f"loss={record['loss']:.6f}"
        )


if __name__ == "__main__":
    point = add_scaled(
        [1.0, 2.0, 3.0],
        [1.0, 0.0, 0.0],
        2.0,
        [0.0, 1.0, 1.0],
        -1.0,
    )
    assert point == [3.0, 1.0, 2.0]
    assert high_dimensional_quadratic([2.0, 3.0]) == 13.0
    print_slice_example()
    print_trajectory_example()

