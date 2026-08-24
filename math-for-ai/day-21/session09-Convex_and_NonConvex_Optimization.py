"""
DAY 21 — SESSION 09: CONVEX AND NON-CONVEX OPTIMIZATION
=======================================================

LEARNING GOALS
--------------
This lesson develops the geometry behind optimization. It explains what convex
and non-convex mean, why convex problems are easier to reason about, and why
neural-network training is still possible even though its loss is non-convex.

1. THE BOWL INTUITION
---------------------
The simplest convex loss is:

    f(x) = x^2

It has one bowl-shaped valley and one minimum at x=0. From either side, the
negative gradient points toward the same answer.

A common non-convex example is:

    f(x) = (x^2 - 1)^2

It has two minima, at x=-1 and x=1, with a hill between them. Which minimum an
optimizer reaches can depend on initialization and update dynamics.

2. THE FORMAL CONVEXITY CONDITION
---------------------------------
Take any two inputs x1 and x2. Connect the graph points with a straight line.
A function f is convex when the function lies at or below that line:

    f(lambda*x1 + (1-lambda)*x2)
        <= lambda*f(x1) + (1-lambda)*f(x2)

for every lambda between 0 and 1.

lambda=0 selects x2, lambda=1 selects x1, and lambda=0.5 selects their
midpoint. This inequality says the bowl does not contain a hidden hump above
the chord.

Example for f(x)=x^2, x1=-2, x2=4, lambda=0.5:

    midpoint input = 0.5(-2) + 0.5(4) = 1
    f(midpoint) = 1^2 = 1
    midpoint of endpoint losses = 0.5(4) + 0.5(16) = 10

Since 1 <= 10, this particular check satisfies convexity. One check does not
prove global convexity, but a violation is enough to prove non-convexity.

3. WHY CONVEXITY IS VALUABLE
----------------------------
For a convex function, every local minimum is also a global minimum. There is
no smaller hidden valley elsewhere. Under appropriate assumptions about the
function and learning rate, gradient methods can reliably approach a global
solution.

Careful wording matters: convexity alone does not mean every arbitrary learning
rate converges. An enormous learning rate can still diverge. Nondifferentiable
convex functions may require subgradients. The practical benefit is the absence
of misleading local minima, not magical protection from poor optimization.

4. STRICT AND STRONG CONVEXITY
------------------------------
Strict convexity means the chord inequality is strict for distinct points and
0<lambda<1. It normally gives at most one minimizer.

Strong convexity adds a guaranteed amount of upward curvature. A strongly
convex bowl cannot become arbitrarily flat. Strong convexity allows stronger
convergence guarantees, but a full proof is beyond what an AI engineer needs
at this stage.

5. DERIVATIVE AND CURVATURE INTUITION
-------------------------------------
For a differentiable one-dimensional convex function, the slope never
decreases as x increases. If the second derivative exists, a useful test is:

    f''(x) >= 0 everywhere  -> convex

Examples:

    f(x)=x^2       -> f''(x)=2     -> convex
    f(x)=x^4       -> f''(x)=12x^2 -> convex, although flat at x=0
    f(x)=x^3       -> f''(x)=6x    -> changes sign, not globally convex

For many variables, the analogous object is the Hessian matrix. A
positive-semidefinite Hessian everywhere indicates convexity. We only need the
intuition here: convex curvature bends upward in every direction.

6. NON-CONVEX LANDSCAPES
------------------------
A non-convex loss may contain:

* several local minima;
* saddle points;
* flat plateaus;
* sharp walls and gentle directions;
* curved valleys;
* barriers between low-loss regions.

The word non-convex does not mean impossible. It means the simple one-bowl
guarantees no longer apply.

7. WHY NEURAL NETWORK LOSSES ARE NON-CONVEX
-------------------------------------------
Neural networks compose many layers and nonlinear activations. Parameters
interact multiplicatively and through nonlinear functions. Hidden units can
also be permuted: two different parameter vectors may represent essentially
the same function. These properties create an enormous, complicated landscape.

Despite this, modern networks train successfully because:

* high-dimensional spaces contain many useful low-loss solutions;
* mini-batch noise perturbs the path;
* momentum carries motion through difficult regions;
* adaptive optimizers handle unequal gradient scales;
* initialization, normalization, residual connections, and schedules improve
  optimization geometry.

8. LOCAL AND GLOBAL MINIMA
--------------------------
A local minimum is lower than all sufficiently nearby points. A global minimum
is lower than every point in the entire domain.

In a convex function, a local minimum is global. In a non-convex function, a
local minimum can be higher than another distant valley.

For large neural networks, exact global optimality is usually not the training
goal. We want a parameter region with low training loss and good validation or
test performance. A slightly higher training minimum can generalize better.

9. WHAT AN OPTIMIZER CAN AND CANNOT KNOW
----------------------------------------
A first-order optimizer sees local gradients, not a complete map of the loss
landscape. It does not know whether a nearby-looking bottom is global. It takes
steps based on current and possibly historical gradient information.

This is why initialization and the optimizer path matter in non-convex
problems: different starts can reveal different local information.
"""


def convex_quadratic(x):
    """A one-bowl convex function with global minimum f(0)=0."""
    return x ** 2


def convex_quadratic_gradient(x):
    return 2 * x


def double_well(x):
    """A non-convex function with global minima at x=-1 and x=1."""
    return (x ** 2 - 1) ** 2


def double_well_gradient(x):
    return 4 * x * (x ** 2 - 1)


def chord_gap(function, x1, x2, weight):
    """
    Return right_side-left_side from the convexity inequality.

    A negative result is a definite convexity violation for this test triple.
    A non-negative result only says this one test passed; it does not prove the
    function is convex everywhere.
    """
    if not 0 <= weight <= 1:
        raise ValueError("weight must be between 0 and 1")
    mixed_x = weight * x1 + (1 - weight) * x2
    left_side = function(mixed_x)
    right_side = weight * function(x1) + (1 - weight) * function(x2)
    return right_side - left_side


def gradient_descent_1d(function, gradient, start, lr, steps):
    """Return a transparent optimization history for a scalar function."""
    x = float(start)
    history = []
    for step in range(steps + 1):
        history.append((step, x, function(x)))
        if step < steps:
            x = x - lr * gradient(x)
    return history


def compare_starting_points():
    print("Convex f(x)=x^2 from two starts")
    for start in (-2.0, 2.0):
        history = gradient_descent_1d(
            convex_quadratic,
            convex_quadratic_gradient,
            start,
            lr=0.1,
            steps=30,
        )
        _, final_x, final_loss = history[-1]
        print(f"start={start:+.1f} -> x={final_x:+.6f}, loss={final_loss:.8f}")

    print("\nNon-convex double well from two starts")
    for start in (-0.2, 0.2):
        history = gradient_descent_1d(
            double_well,
            double_well_gradient,
            start,
            lr=0.05,
            steps=50,
        )
        _, final_x, final_loss = history[-1]
        print(f"start={start:+.1f} -> x={final_x:+.6f}, loss={final_loss:.8f}")


def demonstrate_convexity_checks():
    quadratic_gap = chord_gap(convex_quadratic, -2, 4, 0.5)
    # For the double well, f(-1)=f(1)=0 but f(0)=1. The midpoint lies above
    # the chord, so right-left is -1: a direct non-convexity certificate.
    double_well_gap = chord_gap(double_well, -1, 1, 0.5)
    print("\nConvexity inequality examples")
    print(f"quadratic chord gap:  {quadratic_gap:+.3f} (passes this check)")
    print(f"double-well gap:      {double_well_gap:+.3f} (negative = violation)")


if __name__ == "__main__":
    assert chord_gap(convex_quadratic, -2, 4, 0.5) == 9.0
    assert chord_gap(double_well, -1, 1, 0.5) == -1.0
    compare_starting_points()
    demonstrate_convexity_checks()

