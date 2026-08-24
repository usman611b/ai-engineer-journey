"""
DAY 21 — SESSION 10: SADDLE POINTS AND PLATEAUS
===============================================

LEARNING GOALS
--------------
This file explains why gradient=0 does not automatically mean minimum, how a
saddle behaves in different directions, why an exact saddle differs from a
near-saddle region, and what momentum or mini-batch noise can contribute.

1. STATIONARY OR CRITICAL POINT
-------------------------------
A differentiable function has a stationary point where its gradient is zero:

    gradient f(theta) = 0

This tells us that all first-order slopes are zero at that exact point. It does
not identify the type of point. A stationary point may be:

* a local minimum;
* a local maximum;
* a saddle point;
* part of a flat region.

2. THE STANDARD SADDLE
----------------------
Consider:

    f(x,y) = x^2 - y^2

Its gradient is:

    df/dx = 2x
    df/dy = -2y

At (0,0), both partial derivatives are zero. But inspect two directions.

Along the x-axis, set y=0:

    f(x,0)=x^2 >= 0

The origin behaves like a minimum in the x direction.

Along the y-axis, set x=0:

    f(0,y)=-y^2 <= 0

The origin behaves like a maximum in the y direction. It is therefore neither
a complete minimum nor a complete maximum: it is a saddle.

3. GRADIENT DESCENT NEAR THE SADDLE
-----------------------------------
With learning rate lr:

    x_new = x - lr*(2x)  = (1-2lr)x
    y_new = y - lr*(-2y) = (1+2lr)y

For 0<lr<0.5, x shrinks toward zero while the magnitude of y grows away from
zero. Thus a point near the saddle has a downhill direction that lets gradient
descent escape.

Example x=0.1, y=0.1, lr=0.1:

    gradient = [0.2,-0.2]
    new point = [0.08,0.12]
    old loss  = 0
    new loss  = 0.08^2 - 0.12^2 = -0.008

4. EXACT SADDLE VERSUS NEAR SADDLE
----------------------------------
At the exact origin, vanilla gradient descent sees [0,0] and makes no update.
Deterministic momentum and Adam also cannot create movement from nothing when:

* the point is exactly the saddle;
* every current gradient is exactly zero;
* all optimizer state begins at zero;
* there is no noise or numerical perturbation.

Momentum can move through the exact point when it already has velocity from
earlier updates. For example, with previous velocity [0.2,-0.1], beta=0.9,
zero current gradient, and lr=0.1:

    new velocity = [0.18,-0.09]
    new point = [-0.018,0.009]

The movement comes from stored velocity, not from the zero gradient.

5. WHY EXACT SADDLES ARE LESS COMMON IN PRACTICE
-------------------------------------------------
Real neural-network training normally includes perturbations:

* random initialization rarely selects an exact critical coordinate;
* mini-batches give noisy estimates of the full-dataset gradient;
* previous optimizer velocity may remain nonzero;
* floating-point arithmetic breaks perfect mathematical symmetry.

These do not guarantee escape from every difficult region, but they make
remaining forever at one exact idealized saddle unlikely.

6. PLATEAUS AND SADDLE-LIKE REGIONS
-----------------------------------
The practical problem is often not one exact zero-gradient point. It is a large
region where gradients are extremely small in many directions:

    gradient approximately 0

Then:

    update = learning_rate * gradient

is tiny, so training appears stuck. Such regions are often called plateaus.
Momentum can carry some existing motion through them, while mini-batch noise
can provide perturbations. A learning rate that decayed too early can make a
plateau even harder to cross.

7. CURVATURE AND THE HESSIAN INTUITION
--------------------------------------
The Hessian records second derivatives, describing local curvature. At a
smooth local minimum, curvature is non-negative in every direction. At a
saddle, some directions curve upward and some curve downward.

For f(x,y)=x^2-y^2, the Hessian is:

    [[ 2,  0],
     [ 0, -2]]

The positive 2 matches the upward x direction. The negative -2 matches the
downward y direction. You do not need to compute Hessians during ordinary
first-order training; this explains the geometry.

8. WHY SADDLES MATTER IN HIGH DIMENSIONS
----------------------------------------
A network may have millions of parameter directions. A true local minimum must
have no immediate downhill direction. A saddle needs only a mixture: upward
curvature in some directions and downward curvature in at least one other.
With many directions, mixed curvature is common.

9. IMPORTANT LIMITATION
-----------------------
Saying mini-batch noise or momentum helps escape saddles is not the same as
saying it always escapes quickly. Escape depends on curvature, learning rate,
noise scale, optimizer state, and how close the path is to an exact critical
point.
"""


def saddle_loss(params):
    x, y = params
    return x ** 2 - y ** 2


def saddle_gradient(params):
    x, y = params
    return [2 * x, -2 * y]


def gradient_descent_step(params, grads, lr):
    return [p - lr * g for p, g in zip(params, grads)]


class Momentum:
    """Roadmap momentum convention: velocity=beta*velocity+gradient."""

    def __init__(self, lr=0.1, beta=0.9, initial_velocity=None):
        self.lr = lr
        self.beta = beta
        self.velocity = None if initial_velocity is None else list(initial_velocity)

    def step(self, params, grads):
        if self.velocity is None:
            self.velocity = [0.0] * len(params)
        if len(params) != len(grads) or len(params) != len(self.velocity):
            raise ValueError("params, grads, and velocity must have equal lengths")

        self.velocity = [
            self.beta * velocity + gradient
            for velocity, gradient in zip(self.velocity, grads)
        ]
        return [
            parameter - self.lr * velocity
            for parameter, velocity in zip(params, self.velocity)
        ]


def run_vanilla_near_saddle(start=(0.1, 0.1), lr=0.1, steps=5):
    params = list(start)
    print("Vanilla GD near the saddle")
    for step in range(steps + 1):
        print(
            f"step={step} x={params[0]:+.6f} y={params[1]:+.6f} "
            f"loss={saddle_loss(params):+.8f}"
        )
        if step < steps:
            grads = saddle_gradient(params)
            params = gradient_descent_step(params, grads, lr)
    return params


def compare_exact_saddle_cases():
    exact = [0.0, 0.0]
    zero_grads = saddle_gradient(exact)

    no_history = Momentum(lr=0.1, beta=0.9)
    still_exact = no_history.step(exact, zero_grads)

    stored_history = Momentum(
        lr=0.1,
        beta=0.9,
        initial_velocity=[0.2, -0.1],
    )
    moved = stored_history.step(exact, zero_grads)

    print("\nExact saddle comparison")
    print("zero gradient + zero velocity:  ", still_exact)
    print("zero gradient + stored velocity:", moved)
    return still_exact, moved


if __name__ == "__main__":
    assert saddle_gradient([0.0, 0.0]) == [0.0, -0.0]
    first = gradient_descent_step([0.1, 0.1], [0.2, -0.2], 0.1)
    assert all(abs(a - b) < 1e-12 for a, b in zip(first, [0.08, 0.12]))

    run_vanilla_near_saddle()
    still, moved = compare_exact_saddle_cases()
    assert still == [0.0, 0.0]
    assert abs(moved[0] + 0.018) < 1e-12
    assert abs(moved[1] - 0.009) < 1e-12

