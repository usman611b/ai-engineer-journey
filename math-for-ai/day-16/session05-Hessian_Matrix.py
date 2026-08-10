"""
LESSON 4 — HESSIAN MATRIX AND CURVATURE
========================================

These are detailed notes for everything learned about second derivatives, the
Hessian matrix, minima, maxima, saddle points, eigenvalues, and learning-rate
behavior on different-shaped loss surfaces.


1. WHY DO WE NEED THE HESSIAN?
------------------------------

Gradient descent uses the gradient to decide which direction reduces the loss:

    parameters_new = parameters_old - learning_rate * gradient

But a gradient of zero only means that the surface is flat at the current point.
It does NOT prove that the point is a minimum.

A flat point can be:

    * A local minimum: bottom of a bowl.
    * A local maximum: top of a hill.
    * A saddle point: upward in some directions and downward in others.

The Hessian measures CURVATURE. It helps us identify the shape of a flat point.


2. SECOND DERIVATIVE: THE ONE-VARIABLE IDEA
--------------------------------------------

For a one-variable function:

    f(x) = x^2

First derivative:

    f'(x) = 2x

Second derivative:

    f''(x) = 2

The first derivative describes slope.
The second derivative describes how the slope changes, or how the graph curves.

At a critical point where f'(x) = 0:

    f''(x) > 0  -> curves upward -> local minimum
    f''(x) < 0  -> curves downward -> local maximum
    f''(x) = 0  -> inconclusive; investigate further

Example: f(x) = x^2

    f'(0) = 0
    f''(0) = 2 > 0

So x = 0 is a minimum.

Example: f(x) = -x^2

    f'(0) = 0
    f''(0) = -2 < 0

So x = 0 is a maximum.

Example: f(x) = x^3

    f'(0) = 0
    f''(0) = 0

The second-derivative test is inconclusive. x=0 is neither a minimum nor a
maximum; it is a flat inflection point.


3. THE HESSIAN: SECOND DERIVATIVES FOR TWO VARIABLES
----------------------------------------------------

For a function f(x, y), the gradient contains the first partial derivatives:

    gradient = [df/dx, df/dy]

The Hessian contains every second partial derivative:

                 [ d2f/dx2    d2f/dxdy ]
    Hessian =    [                       ]
                 [ d2f/dydx   d2f/dy2  ]

We commonly write these entries as:

    fxx = d2f/dx2   (differentiate twice with respect to x)
    fyy = d2f/dy2   (differentiate twice with respect to y)
    fxy = d2f/dxdy  (differentiate first with x and then y)
    fyx = d2f/dydx  (differentiate first with y and then x)

For smooth functions, fxy and fyx are usually equal.


4. EXAMPLE: f(x, y) = x^2 + y^2 (BOWL / MINIMUM)
--------------------------------------------------

First partial derivatives:

    fx = 2x
    fy = 2y

Set the gradient to zero:

    2x = 0  -> x = 0
    2y = 0  -> y = 0

Critical point: (0, 0)

Second partial derivatives:

    fxx = 2
    fyy = 2
    fxy = 0
    fyx = 0

Hessian:

    H = [2  0]
        [0  2]

The surface curves upward in both x and y directions, so (0,0) is a bowl-shaped
minimum. It is also the global minimum because x^2 + y^2 can never be negative.


5. EXAMPLE: f(x, y) = -x^2 - y^2 (MAXIMUM)
------------------------------------------------

First partial derivatives:

    fx = -2x
    fy = -2y

Critical point: (0, 0)

Second partial derivatives:

    fxx = -2
    fyy = -2
    fxy = 0

Hessian:

    H = [-2   0]
        [ 0  -2]

The surface curves downward in every direction: an upside-down bowl.
Therefore, (0,0) is a local maximum.


6. EXAMPLE: f(x, y) = x^2 - y^2 (SADDLE POINT)
------------------------------------------------

First partial derivatives:

    fx = 2x
    fy = -2y

Critical point: (0, 0)

Second partial derivatives:

    fxx = 2
    fyy = -2
    fxy = 0

Hessian:

    H = [2   0]
        [0  -2]

At (0,0), the surface goes up in the x direction:

    f(x, 0) = x^2

but goes down in the y direction:

    f(0, y) = -y^2

So (0,0) is neither a minimum nor a maximum. It is a saddle point.

AI connection:
    A saddle point can have gradient = 0 even though some directions still lower
    the loss. Gradient = 0 is therefore not enough to prove training reached a
    minimum.


7. MIXED PARTIALS: f(x, y) = x^2 + 3xy + y^2
------------------------------------------------

First partial derivatives:

    fx = 2x + 3y
    fy = 3x + 2y

Second partial derivatives:

    fxx = 2
    fyy = 2
    fxy = 3
    fyx = 3

Hessian:

    H = [2  3]
        [3  2]

What does the 3xy term mean?

Without the mixed term, for f(x,y) = x^2 + y^2:

    fx = 2x

The x slope depends only on x. Changing y does not alter the x slope.

With the mixed term 3xy:

    fx = 2x + 3y

Now y changes the x slope.

At x=1:

    If y=0: fx = 2(1) + 3(0) = 2
    If y=2: fx = 2(1) + 3(2) = 8

The same x has a different x slope because y changed. The variables are coupled
or connected. The mixed partial fxy=3 measures this connection strength.

At the critical point (0,0), this surface is a saddle point. We prove this using
the determinant test next.


8. THE 2D HESSIAN DETERMINANT TEST
----------------------------------

At a critical point, calculate:

    D = fxx * fyy - (fxy)^2

Then classify the point:

    D > 0 and fxx > 0 -> local minimum
    D > 0 and fxx < 0 -> local maximum
    D < 0             -> saddle point
    D = 0             -> inconclusive

Example: x^2 + y^2

    fxx=2, fyy=2, fxy=0
    D = 2*2 - 0^2 = 4

    D > 0 and fxx > 0 -> local minimum

Example: -x^2 - y^2

    fxx=-2, fyy=-2, fxy=0
    D = (-2)(-2) - 0^2 = 4

    D > 0 and fxx < 0 -> local maximum

Example: x^2 - y^2

    fxx=2, fyy=-2, fxy=0
    D = 2(-2) - 0^2 = -4

    D < 0 -> saddle point

Example: x^2 + 3xy + y^2

    fxx=2, fyy=2, fxy=3
    D = 2*2 - 3^2 = 4 - 9 = -5

    D < 0 -> saddle point


9. HESSIAN EIGENVALUES
----------------------

Eigenvalues of the Hessian describe curvature in the most important directions
of the surface.

    All eigenvalues positive -> curves upward in every direction -> minimum
    All eigenvalues negative -> curves downward in every direction -> maximum
    Mixed signs              -> up in some directions, down in others -> saddle

Examples:

    H = [2 0]       eigenvalues:  2,  2  -> minimum
        [0 2]

    H = [-2  0]     eigenvalues: -2, -2  -> maximum
        [ 0 -2]

    H = [2  0]      eigenvalues:  2, -2  -> saddle
        [0 -2]

The determinant test is especially convenient for a 2D function. Eigenvalues
generalize the same idea to neural networks with many parameters.


10. HESSIAN, CURVATURE, AND LEARNING RATE
-----------------------------------------

Consider:

    f(x, y) = 10x^2 + y^2

Gradient:

    fx = 20x
    fy = 2y

Hessian:

    H = [20  0]
        [ 0  2]

The x direction is much steeper than the y direction.

Start at x=4, y=3, with learning_rate=0.1:

    x_new = 4 - 0.1(20*4) = -4
    y_new = 3 - 0.1(2*3) = 2.4

x jumps from 4 to -4, crossing the minimum. On later steps it keeps bouncing:

    4 -> -4 -> 4 -> -4 -> ...

But y moves smoothly toward zero:

    3 -> 2.4 -> 1.92 -> ...

This shows why the same learning rate can be too large for a steep direction but
fine for a flatter direction.

With learning_rate=0.05:

    x_new = 4 - 0.05(80) = 0

The x coordinate reaches zero in one step. In real ML surfaces, different
curvatures make choosing one learning rate difficult. This motivates optimizers
such as Momentum and Adam.


11. KEY TAKEAWAYS
-----------------

* The gradient tells a local uphill/downhill direction.
* The Hessian tells local curvature/shape.
* Gradient = 0 does not guarantee a minimum.
* The Hessian distinguishes minima, maxima, and saddle points.
* A mixed term like 3xy means one variable changes the other variable's slope.
* For a 2D critical point, use D = fxx*fyy - fxy^2.
* Hessian eigenvalues give the same curvature story in higher dimensions.
* Different curvature in different directions makes learning-rate selection hard.


12. COMMON MISTAKES
-------------------

* Calling every gradient-zero point a minimum.
* Forgetting to solve gradient = 0 before using the determinant test.
* Forgetting the square in (fxy)^2.
* Thinking fxy means multiply f, x, and y. It means a mixed second derivative.
* Differentiating y when taking an x partial derivative, or vice versa.
* Mixing up maximum/minimum: if D>0, fxx decides the result.
* Assuming D=0 means saddle point; it means the test is inconclusive.


RUNNABLE PYTHON EXAMPLES
========================
Run this file to see the Hessian test and learning-rate behavior.
"""


# =============================================================================
# EXAMPLE 1: REUSABLE HESSIAN CLASSIFIER
# =============================================================================


def classify_critical_point(fxx, fyy, fxy):
    """Classify a 2D critical point from its second partial derivatives."""
    # Determinant of the 2D Hessian.
    determinant = fxx * fyy - fxy**2

    if determinant > 0 and fxx > 0:
        return determinant, "local minimum"
    elif determinant > 0 and fxx < 0:
        return determinant, "local maximum"
    elif determinant < 0:
        return determinant, "saddle point"
    else:
        return determinant, "inconclusive"


print("=" * 65)
print("EXAMPLE 1: Hessian determinant test")
print("=" * 65)

# Each tuple has: name, fxx, fyy, fxy.
examples = [
    ("x^2 + y^2", 2, 2, 0),
    ("-x^2 - y^2", -2, -2, 0),
    ("x^2 - y^2", 2, -2, 0),
    ("x^2 + 3xy + y^2", 2, 2, 3),
]

for name, fxx, fyy, fxy in examples:
    determinant, result = classify_critical_point(fxx, fyy, fxy)

    print("\nFunction:", name)
    print("Hessian: [[", fxx, ",", fxy, "], [", fxy, ",", fyy, "]]", sep="")
    print("D:", determinant)
    print("Classification:", result)


# =============================================================================
# EXAMPLE 2: THE MIXED TERM CHANGES THE X SLOPE
# =============================================================================

print("\n" + "=" * 65)
print("EXAMPLE 2: The 3xy connection term")
print("=" * 65)

x = 1

for y in (0, 2):
    # For f(x,y)=x^2+3xy+y^2, fx=2x+3y.
    x_slope = 2 * x + 3 * y
    print("x =", x, "y =", y, "-> x slope =", x_slope)

print("Changing y changed the slope in the x direction.")


# =============================================================================
# EXAMPLE 3: CURVATURE AFFECTS LEARNING RATE
# =============================================================================


def loss(x, y):
    """Return f(x,y) = 10x^2 + y^2."""
    return 10 * x**2 + y**2


def gradient(x, y):
    """Return the gradient [20x, 2y] for f(x,y) = 10x^2 + y^2."""
    x_gradient = 20 * x
    y_gradient = 2 * y
    return x_gradient, y_gradient


def run_gradient_descent(learning_rate, steps):
    """Show gradient descent on a surface steep in x and flatter in y."""
    x = 4.0
    y = 3.0

    print("\nLearning rate:", learning_rate)
    for step in range(steps):
        x_gradient, y_gradient = gradient(x, y)

        x = x - learning_rate * x_gradient
        y = y - learning_rate * y_gradient

        print(
            "Step:", step + 1,
            "Point:", (round(x, 4), round(y, 4)),
            "Loss:", round(loss(x, y), 4),
        )


print("\n" + "=" * 65)
print("EXAMPLE 3: Same function, different learning rates")
print("=" * 65)

# lr=0.1 makes x oscillate between 4 and -4.
run_gradient_descent(learning_rate=0.1, steps=4)

# lr=0.05 reaches x=0 immediately, then y decreases toward zero.
run_gradient_descent(learning_rate=0.05, steps=4)



#========================================================================
def hessian_2d(f, x, y, h=1e-5):
    fxx = (f(x + h, y) - 2 * f(x, y) + f(x - h, y)) / (h ** 2)
    fyy = (f(x, y + h) - 2 * f(x, y) + f(x, y - h)) / (h ** 2)
    fxy = (f(x + h, y + h) - f(x + h, y - h) - f(x - h, y + h) + f(x - h, y - h)) / (4 * h ** 2)
    return [[fxx, fxy], [fxy, fyy]]

def saddle(x, y):
    return x ** 2 - y ** 2

def bowl(x, y):
    return x ** 2 + y ** 2

H_saddle = hessian_2d(saddle, 0.0, 0.0)
H_bowl = hessian_2d(bowl, 0.0, 0.0)
print(f"Saddle Hessian: {H_saddle}")  # [[2, 0], [0, -2]] -- mixed signs
print(f"Bowl Hessian:   {H_bowl}")    # [[2, 0], [0, 2]]  -- both positive


#===========================================================================




# =============================================================================
# EXAMPLE 4: OPTIONAL NUMPY EIGENVALUE CHECK
# =============================================================================

# The following is optional. It uses NumPy, a common numerical Python library.
# Uncomment it later when you are comfortable with imports and arrays.
#
# import numpy as np
#
# hessian = np.array([[2, 3], [3, 2]])
# eigenvalues = np.linalg.eigvals(hessian)
# print("Eigenvalues:", eigenvalues)  # One positive and one negative -> saddle
